import re, json

# --- Update index.html ---
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_mada_block = r'<!-- Project 3: MADA Analytics -->.*?</div></div></div>'
new_mada_block = """<!-- Project 3: MADA Analytics -->
<div class="g" style="margin-top:28px">
<div class="c">
<div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:12px;margin-bottom:16px">
  <div>
    <span class="tag" style="background:rgba(59,130,246,.1);color:#3b82f6;border-color:rgba(59,130,246,.3);margin-bottom:8px;padding-top:4px">◈ ذكاء الأعمال · منصة ويب</span>
    <h3 style="font-size:22px;margin:0 0 4px">مدى (MADA) — منصة اكتشاف الفرص التجارية في عُمان</h3>
    <p style="font-size:15px;max-width:48em;color:var(--ink-subtle)">منصة ويب تساعد رواد الأعمال والمستثمرين على تقييم الفرص التجارية في سلطنة عُمان. تقوم بتقييم الفرصة من 100 بناءً على قطاع العمل والولاية باستخدام محرك تقييم بمعادلة ثابتة (الطلب، الموقع، المنافسة، النمو، فجوة السوق، وملاءمة المستخدم) وإصدار تقرير مفصل.</p>
  </div>
  <div style="display:flex;gap:6px;flex-wrap:wrap">
    <span class="pill">Django</span>
    <span class="pill">Python</span>
    <span class="pill">SQLite</span>
    <span class="pill">Bootstrap</span>
  </div>
</div>
<div class="mods">
  <div><b>محرك التقييم والمحاكاة</b>معادلة ثابتة من 6 أبعاد لتقييم الفرصة، مع محاكي «ماذا لو» لسيناريوهات الأعمال.</div>
  <div><b>النزاهة والشفافية</b>يعرض «بيانات غير كافية» بدل اختلاق الأرقام، ويربط كل رقم بمصدره الرسمي أو التجريبي.</div>
  <div><b>نطاق واسع وخريطة تفاعلية</b>يغطي 11 محافظة و63 ولاية و12 قطاعًا مع خريطة تفاعلية وتقارير قابلة للطباعة.</div>
  <div><b>نظام حسابات وصلاحيات</b>بيانات معزولة لكل مستخدم، مع لوحة إدارة للموظفين وسجل يرصد الزيارات ومحاولات الدخول.</div>
</div>
<div class="chips" style="justify-content:flex-start;margin-top:16px">
  <span class="chip">HTML/CSS/JS</span>
  <span class="chip">RTL & LTR</span>
  <span class="chip">Dark Mode</span>
  <span class="chip">Auth System</span>
  <span class="chip">Admin Panel</span>
</div>
</div>
</div>"""

content = re.sub(old_mada_block, new_mada_block, content, flags=re.DOTALL)

new_translations = {
    "◈ ذكاء الأعمال · منصة ويب": "◈ Business Intelligence · Web Platform",
    "مدى (MADA) — منصة اكتشاف الفرص التجارية في عُمان": "MADA — Business Opportunity Discovery Platform for Oman",
    "منصة ويب تساعد رواد الأعمال والمستثمرين على تقييم الفرص التجارية في سلطنة عُمان. تقوم بتقييم الفرصة من 100 بناءً على قطاع العمل والولاية باستخدام محرك تقييم بمعادلة ثابتة (الطلب، الموقع، المنافسة، النمو، فجوة السوق، وملاءمة المستخدم) وإصدار تقرير مفصل.": "A web platform that scores business opportunities in Oman out of 100 by sector and wilayat, using a fixed six-factor model (demand, location fit, competition, growth, market gap, user fit) and generating detailed reports.",
    "محرك التقييم والمحاكاة": "Evaluation Engine & Simulator",
    "معادلة ثابتة من 6 أبعاد لتقييم الفرصة، مع محاكي «ماذا لو» لسيناريوهات الأعمال.": "A fixed 6-dimension formula for scoring, with a 'what-if' simulator for business scenarios.",
    "النزاهة والشفافية": "Integrity & Transparency",
    "يعرض «بيانات غير كافية» بدل اختلاق الأرقام، ويربط كل رقم بمصدره الرسمي أو التجريبي.": "Displays 'insufficient data' instead of estimating, linking figures to their official or demo sources.",
    "نطاق واسع وخريطة تفاعلية": "Broad Scope & Interactive Map",
    "يغطي 11 محافظة و63 ولاية و12 قطاعًا مع خريطة تفاعلية وتقارير قابلة للطباعة.": "Covers 11 governorates, 63 wilayats, and 12 sectors with an interactive map and printable reports.",
    "نظام حسابات وصلاحيات": "Auth & Permissions System",
    "بيانات معزولة لكل مستخدم، مع لوحة إدارة للموظفين وسجل يرصد الزيارات ومحاولات الدخول.": "Per-user data isolation, a staff admin panel, and an activity log for visits and logins."
}

en_match = re.search(r'var EN\s*=\s*(\{.*?\});', content, re.DOTALL)
if en_match:
    old_en_json = en_match.group(1)
    en_dict = json.loads(old_en_json)
    en_dict.update(new_translations)
    new_en_json = json.dumps(en_dict, ensure_ascii=False)
    content = content[:en_match.start(1)] + new_en_json + content[en_match.end(1):]

# Keep "منصة مدى للتحليلات (MADA Analytics)" in Q since they are part of Q.ar / Q.en
content = content.replace("ومنصة مدى للتحليلات (بـ Django وPython).", "ومنصة مدى (MADA) لاكتشاف الفرص التجارية بـ Django وPython.")
content = content.replace("and MADA Analytics (Django & Python BI platform).", "and MADA Analytics (Django & Python business opportunity platform).")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# --- Update local-ai-server.py ---
with open('local-ai-server.py', 'r', encoding='utf-8') as f:
    server_content = f.read()

old_sys_mada = r'"Other project: MADA Analytics, a business intelligence platform for companies, Django/Python, .*?"Mira role: website design\. "'
new_sys_mada = '"Other project: MADA Analytics (مدى), a bilingual (Arabic RTL/English) web platform built with Python, Django, SQLite, and Bootstrap for discovering and scoring business opportunities in Oman. Users get an opportunity score (out of 100) based on a fixed 6-dimension formula (demand, location fit, competition, growth, market gap, user fit). It emphasizes data integrity (returns \'insufficient data\' instead of inventing numbers, separates official data like NCSI from demo data), covers 11 governorates and 63 wilayats, and includes an interactive map, what-if simulator, printable reports, and full user authentication with a staff admin panel and activity log. No machine learning is used (it is a fixed formula). "'

server_content = re.sub(old_sys_mada, new_sys_mada, server_content, flags=re.DOTALL)

old_responder_mada = r'    # 6\. MADA Analytics / مشروع مدى\s+if has\("مدي", "تحليلات", "mada", "analytics", "بيزنس انتلجنس"\):\s+if is_ar:\s+return "منصة «مدى للتحليلات» \(MADA Analytics\) هي منصة ذكاء أعمال للشركات لدعم القرارات المبنية على البيانات، مبنية بـ Django وPython بمعمارية خدمات منفصلة\. دور ميرة فيها كان تصميم الموقع وواجهات المنصة\."\s+return "MADA Analytics is a business intelligence platform built with Python & Django on a microservices-inspired architecture with an admin panel\. Mira\'s role in the project was designing the website interface\."'

new_responder_mada = """    # 6. MADA Analytics / مشروع مدى
    if has("مدي", "mada", "فرص تجاريه", "analytics", "بيزنس", "business"):
        if is_ar:
            return "منصة «مدى» (MADA) هي منصة ويب لاكتشاف الفرص التجارية في عُمان وتقييمها من 100 بمعادلة ثابتة (الطلب، الموقع، المنافسة، وغيرها). مبنية بـ Django وPython، وتتميز بالشفافية (تفصل البيانات الرسمية عن التجريبية)، وبها نظام حسابات متكامل وخريطة تفاعلية للمحافظات."
        return "MADA is a web platform for discovering and scoring business opportunities in Oman out of 100 using a fixed multi-factor formula. Built with Django and Python, it features an interactive map, strict data integrity rules, and a complete user authentication system with an admin panel."""

server_content = re.sub(old_responder_mada, new_responder_mada, server_content, flags=re.DOTALL)

# Also update the projects summary in responder
server_content = server_content.replace('3. منصة «مدى للتحليلات» (MADA Analytics) لذكاء الأعمال بـ Django وPython.', '3. منصة «مدى» (MADA) لاكتشاف الفرص التجارية بـ Django وPython.')
server_content = server_content.replace('3. MADA Analytics (BI platform for data-driven business decisions).', '3. MADA Analytics (business opportunity discovery platform in Django/Python).')

with open('local-ai-server.py', 'w', encoding='utf-8') as f:
    f.write(server_content)

print("Updated MADA successfully in both files!")
