ميرة المديلوي | Portfolio
============================

التشغيل محلياً | Run locally
- افتحي index.html بالمتصفح مباشرة (دبل كلك). | Just double-click index.html.
- بدون إنترنت يشتغل كل شي، بس الخط (Tajawal) يرجع لخط النظام.
- زر EN / AR يبدّل اللغة.

المساعد الذكي | AI assistant
- بدون إعداد: يعرض 4 أسئلة جاهزة بإجابات ثابتة.
- للمساعد الحقيقي: انشري واحد من ملفات ai-proxy كـ Cloudflare Worker:
    worker-gemini.js  -> Secret: GEMINI_API_KEY      (مفتاح مجاني من aistudio.google.com/apikey)
    worker-claude.js  -> Secret: ANTHROPIC_API_KEY   (من platform.claude.com، برصيد مدفوع)
- انسخي رابط الـ Worker وضعيه في index.html مكان PASTE_WORKER_URL_HERE (قرب آخر السكربت).
- لا تضعي المفتاح داخل index.html أبداً.

أين أعدّل | Where to edit
- المعلومات الشخصية: أسماء الفريق والنصوص داخل index.html.
- الترجمة الإنجليزية: القاموس EN في آخر سكربت.
- نصوص المساعد (SYS): داخل ملف الـ Worker.

versions/ فيها النسخ القديمة للمرجع.
