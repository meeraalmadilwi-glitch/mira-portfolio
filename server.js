// Web server for Render: serves index.html and proxies the smart assistant to Gemini.
// The key lives only in the GEMINI_API_KEY environment variable (Render > Environment).
// Optional: MODEL (tried first), then the fallback models below.
const http = require("http");
const fs = require("fs");
const path = require("path");

const PORT = process.env.PORT || 3000;
const MODELS = [process.env.MODEL, "gemini-3.1-flash-lite", "gemini-flash-latest", "gemini-3.8-flash"].filter(Boolean);

// Reuse the system prompt from the Cloudflare worker file so there is one source of truth.
function loadSystemPrompt() {
  const src = fs.readFileSync(path.join(__dirname, "ai-proxy", "worker-gemini.js"), "utf8");
  const m = src.match(/const SYS = ("(?:[^"\\]|\\.)*");/);
  return JSON.parse(m[1]);
}
const SYS = loadSystemPrompt();

// Simple per-IP limit so nobody can drain the API quota: 15 requests per minute.
const hits = new Map();
function limited(ip) {
  const now = Date.now();
  const arr = (hits.get(ip) || []).filter((t) => now - t < 60000);
  arr.push(now);
  hits.set(ip, arr);
  return arr.length > 15;
}
setInterval(() => hits.clear(), 10 * 60000).unref();

function send(res, status, body, type = "application/json; charset=utf-8") {
  res.writeHead(status, { "Content-Type": type, "Cache-Control": "no-store" });
  res.end(typeof body === "string" ? body : JSON.stringify(body));
}

async function askGemini(msgs) {
  for (const model of MODELS) {
    try {
      const r = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`, {
        method: "POST",
        headers: { "Content-Type": "application/json", "x-goog-api-key": process.env.GEMINI_API_KEY },
        body: JSON.stringify({
          systemInstruction: { parts: [{ text: SYS }] },
          contents: msgs,
          generationConfig: { maxOutputTokens: 800, temperature: 0.4 },
        }),
      });
      if (!r.ok) { console.error("gemini", model, r.status); continue; }
      const d = await r.json();
      const text = ((d.candidates && d.candidates[0] && d.candidates[0].content && d.candidates[0].content.parts) || [])
        .map((p) => p.text || "").join("").trim();
      if (text) return text;
    } catch (e) { console.error("gemini", model, e.message); }
  }
  return null;
}

function readBody(req) {
  return new Promise((resolve, reject) => {
    let data = "";
    req.on("data", (c) => { data += c; if (data.length > 20000) { req.destroy(); reject(new Error("big")); } });
    req.on("end", () => resolve(data));
    req.on("error", reject);
  });
}

const server = http.createServer(async (req, res) => {
  const url = req.url.split("?")[0];

  if (req.method === "POST" && url === "/api/chat") {
    if (!process.env.GEMINI_API_KEY) return send(res, 503, { error: "no key" });
    if (limited(req.headers["x-forwarded-for"] || req.socket.remoteAddress)) return send(res, 429, { error: "slow down" });
    let body;
    try { body = JSON.parse(await readBody(req)); } catch { return send(res, 400, { error: "bad json" }); }
    const msgs = (Array.isArray(body.messages) ? body.messages : [])
      .slice(-8)
      .filter((m) => m && typeof m.content === "string")
      .map((m) => ({ role: m.role === "assistant" ? "model" : "user", parts: [{ text: m.content.slice(0, 600) }] }));
    while (msgs.length && msgs[0].role !== "user") msgs.shift();
    if (!msgs.length || msgs[msgs.length - 1].role !== "user") return send(res, 400, { error: "bad input" });
    const text = await askGemini(msgs);
    return text ? send(res, 200, { text }) : send(res, 502, { error: "upstream" });
  }

  if (req.method === "GET" && (url === "/" || url === "/index.html")) {
    return fs.readFile(path.join(__dirname, "index.html"), (err, html) =>
      err ? send(res, 500, "error", "text/plain") : send(res, 200, html, "text/html; charset=utf-8"));
  }
  if (url === "/healthz") return send(res, 200, "ok", "text/plain");

  // Everything else (.env, python files, versions/...) is intentionally not served.
  send(res, 404, "Not found", "text/plain");
});

server.listen(PORT, () => console.log("Mira portfolio listening on " + PORT));
