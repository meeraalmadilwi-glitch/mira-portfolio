import re, json

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# CSS for gold card
gold_css = """
/* Gold project styles */
.gold-card{position:relative;border:1px solid rgba(234,179,8,.3);background:radial-gradient(ellipse at 85% 0%,rgba(234,179,8,.09),transparent 65%),var(--card-bg)}
.gold-badge{display:inline-flex;align-items:center;gap:6px;padding:3px 14px;border-radius:999px;font-size:12px;font-weight:700;color:#eab308;background:rgba(234,179,8,.12);border:1px solid rgba(234,179,8,.35)}
.gold-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:14px}
@media(max-width:700px){.gold-grid{grid-template-columns:repeat(2,1fr)}}
.gold-mini{background:var(--card-solid);border:1px solid var(--line);border-radius:10px;padding:10px 12px;text-align:center}
.gold-mini em{display:block;font-style:normal;font-size:12px;color:var(--mut)}
.gold-mini b{display:block;font-size:17px;color:#eab308;margin:2px 0}
.gold-mini span{display:block;font-size:11px;color:var(--ink-subtle)}
"""

# Insert gold_css before </style>
if '.gold-card' not in content:
    content = content.replace('</style>', gold_css + '\n</style>', 1)

# Update nav: replace <a href="#baseera">بصيرة</a> with <a href="#projects">المشاريع</a>
content = content.replace('<nav><a href="#about">من أنا</a><a href="#journey">رحلتي</a><a href="#baseera">بصيرة</a><a href="#ask">اسألني</a><a href="#certs">الشهادات</a></nav>',
                          '<nav><a href="#about">من أنا</a><a href="#journey">رحلتي</a><a href="#projects">المشاريع</a><a href="#ask">اسألني</a><a href="#certs">الشهادات</a></nav>')

# Update skills strip in hero to include Angular and Tailwind CSS
content = content.replace('<div class="strip"><span>Flutter</span><span>Django</span><span>Python</span><span>Java</span><span>Visual Basic</span><span>HTML</span><span>Excel</span><span>VS Code</span></div>',
                          '<div class="strip"><span>Flutter</span><span>Angular</span><span>Tailwind CSS</span><span>Django</span><span>Python</span><span>Java</span><span>Visual Basic</span><span>HTML</span><span>Excel</span><span>VS Code</span></div>')

# Update skills chips in journey
content = content.replace('<span class="chip">Flutter</span><span class="chip">Django</span><span class="chip">Python</span><span class="chip">Java</span></div>',
                          '<span class="chip">Flutter</span><span class="chip">Angular</span><span class="chip">Tailwind CSS</span><span class="chip">Django</span><span class="chip">Python</span><span class="chip">Java</span></div>')

# Build the new Projects & Baseera & Gold Dashboard section
old_section_pattern = r'<section id="baseera">.*?</section>'
new_section = '''<section id="projects">
<div id="baseera" style="position:relative;top:-90px;height:0;visibility:hidden" aria-hidden="true"></div>
<span class="tag">◈ المشاريع والابتكارات</span><h2>مشاريعي وابتكاراتي التقنية</h2>
<p class="sub">من تأسيس الشركات الناشئة وتطبيقات الويب الحديثة إلى منصات ذكاء الأعمال.</p>

<!-- Project 1: Baseera Startup -->
<div style="text-align:start;margin-bottom:12px">
<span class="tag" style="margin-bottom:8px">◈ شركتنا الناشئة</span>
<h3 style="font-size:22px;margin:0 0 6px">بصيرة — حلول وخدمات تقنية ذكية</h3>
<p class="sub" style="margin:0 0 16px;text-align:start">من مسابقة «هندسها بالذكاء الاصطناعي 2026» إلى شركة بثلاث خدمات تقنية متقدمة.</p>
</div>
<div class="g g3">
<div class="c"><h3>رصد</h3><p>تابع مشروعك بوضوح.</p><div class="vz"><div class="bar" style="width:90%"></div><div class="bar" style="width:62%"></div><div class="bar" style="width:76%"></div></div></div>
<div class="c"><h3>بناء التطبيقات</h3><p>جوال ومواقع.</p><div class="vz"><div class="rw on">Flutter</div><div class="rw">Django</div><div class="rw">Web</div></div></div>
<div class="c"><h3>مساعد واتساب ذكي</h3><p>يخدم عملاءك على واتساب.</p><div class="vz"><div class="bb u">مرحباً، أبي أحجز موعد</div><div class="bb">أهلاً بك! وش اليوم المناسب لك؟</div></div></div>
</div>
<h3 style="margin:36px 0 16px;font-size:20px;text-align:start">فريق بصيرة</h3>
<div class="g g3">
<div class="c t"><h3>CIO</h3><p>قيادة المشروع</p><b>ميرة المديلوي</b></div>
<div class="c t"><h3>الذكاء الاصطناعي والباك إند</h3><p>حل متعدد الوكلاء</p><b>سارة الحربي</b></div>
<div class="c t"><h3>UI/UX</h3><p>تصميم الواجهات</p><b>فوز المديلوي</b></div>
</div>

<!-- Project 2: Oman Gold Price Dashboard -->
<div class="g" style="margin-top:28px">
<div class="c gold-card">
<div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:12px">
  <div>
    <span class="gold-badge">✦ مجان للمبرمجين · تطبيق عملي</span>
    <h3 style="font-size:22px;margin:8px 0 4px">لوحة أسعار الذهب في عُمان — Oman Gold Price Dashboard</h3>
    <p style="font-size:15px;max-width:44em">تطبيق ويب من صفحة واحدة (SPA) لمتابعة أسعار الذهب في سلطنة عُمان بالريال العُماني لحظياً، مبني بـ Angular وTailwind CSS بواجهة عربية RTL ودعم كامل للوضع الداكن والفاتح.</p>
  </div>
  <div style="display:flex;gap:6px;flex-wrap:wrap">
    <span class="pill" style="border-color:rgba(234,179,8,.4);color:#eab308">Angular</span>
    <span class="pill">Tailwind CSS</span>
    <span class="pill">TypeScript</span>
    <span class="pill">SSR & Docker</span>
  </div>
</div>

<div class="vz" style="min-height:auto;padding:18px;margin-top:18px">
  <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px;font-size:13px;color:var(--ink-subtle);border-bottom:1px solid var(--line);padding-bottom:12px;margin-bottom:14px">
    <span>📍 السوق: <b>سلطنة عُمان</b></span>
    <span>💰 العملة: <b>الريال العُماني (ر.ع)</b></span>
    <span>⚖️ الوحدة: <b>جرام</b></span>
    <span>⚡ التحديث: <b>مباشر (بيانات تجريبية)</b></span>
  </div>

  <div class="gold-grid">
    <div class="gold-mini"><em>عيار 24</em><b>28.45 ر.ع</b><span>نقاء 99.9%</span></div>
    <div class="gold-mini"><em>عيار 22</em><b>26.08 ر.ع</b><span>نقاء 91.6%</span></div>
    <div class="gold-mini"><em>عيار 21</em><b>24.89 ر.ع</b><span>نقاء 87.5%</span></div>
    <div class="gold-mini"><em>عيار 18</em><b>21.34 ر.ع</b><span>نقاء 75.0%</span></div>
  </div>

  <div style="margin-top:16px;background:var(--card-solid);border:1px solid var(--line);border-radius:12px;padding:12px 16px">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
      <span style="font-size:13px;font-weight:700;color:var(--ink)">مؤشر حركة الأسعار (آخر 30 يوماً - SVG Polyline)</span>
      <span style="font-size:12px;color:#22c55e;font-weight:700">+3.8% ↑ نمو مستمر</span>
    </div>
    <svg viewBox="0 0 500 60" style="width:100%;height:48px;overflow:visible" preserveAspectRatio="none">
      <defs>
        <linearGradient id="goldGrad" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#eab308" stop-opacity="0.3"/>
          <stop offset="100%" stop-color="#eab308" stop-opacity="0"/>
        </linearGradient>
      </defs>
      <polygon fill="url(#goldGrad)" points="0,55 30,50 65,52 100,45 140,48 180,38 220,40 260,32 300,35 340,26 380,28 420,18 460,15 500,8 500,60 0,60"/>
      <polyline fill="none" stroke="#eab308" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" points="0,55 30,50 65,52 100,45 140,48 180,38 220,40 260,32 300,35 340,26 380,28 420,18 460,15 500,8"/>
      <circle cx="500" cy="8" r="4" fill="#eab308"/>
    </svg>
  </div>
</div>

<div class="mods">
  <div><b>الهيدر والواجهة الرئيسية</b>شريط تنقل ثابت، شارة «بيانات تجريبية»، مسار تنقل (Breadcrumbs)، وزر تبديل الوضع الداكن/الفاتح.</div>
  <div><b>أسعار اليوم اللحظية</b>4 بطاقات تفاعلية لعيارات (18، 21، 22، 24) تعرض السعر والعملة والوحدة والنقاء بدقة.</div>
  <div><b>حاسبة الذهب التقديرية</b>حاسبة ذكية لاختيار العيار وإدخال الوزن بالجرام مع تحقق فوري وحالة فارغة تفاعلية.</div>
  <div><b>رسم بياني لـ 30 يوماً</b>خط SVG Polyline مع تبديل العيارات وإحصائيات لأعلى/أقل/آخر سعر ومقارنة التغير.</div>
  <div><b>جدول سجل الأسعار</b>جدول تاريخي متجاوب لـ 30 يوماً لكافة العيارات بألوان صفوف متناوبة وتمرير أفقي سلس.</div>
  <div><b>معمارية المكونات النظيفة</b>بنية Angular مجزأة ومستقلة: header, gold-price-card, gold-calculator, chart, price-history.</div>
  <div><b>خدمات قابلة للتوسع</b>GoldService لقراءة ومعالجة البيانات وجاهزية ربط API، وThemeService لإدارة الوضع الداكن.</div>
  <div><b>جاهزية النشر والحاويات</b>دعم كامل لـ SSR وDocker، وملف README تفصيلي بالخطوات واختبارات معيارية مدمجة.</div>
</div>

<div class="chips" style="justify-content:flex-start;margin-top:16px">
  <span class="chip">Angular</span>
  <span class="chip">TypeScript</span>
  <span class="chip">Tailwind CSS</span>
  <span class="chip">SSR</span>
  <span class="chip">Docker</span>
  <span class="chip">SPA</span>
  <span class="chip">RTL</span>
  <span class="chip">Component-Driven</span>
</div>
</div>
</div>

<!-- Project 3: MADA Analytics -->
<div class="g" style="margin-top:20px"><div class="c"><h3>مدى — MADA Analytics</h3><p>منصة ذكاء أعمال بـ Django/Python. دوري: تصميم الموقع.</p><div class="mods"><div><b>محرك الفرص</b>اكتشاف الفرص الاستثمارية والتجارية من البيانات</div><div><b>التقييم والاحتساب</b>إعطاء نقاط وأوزان لترتيب الخيارات</div><div><b>المحاكاة</b>سيناريوهات افتراضية لتوقع نتائج القرارات</div><div><b>التنبؤ</b>نماذج للتنبؤ بالاتجاهات ومؤشرات الأداء</div><div><b>السوق والمنافسة</b>مراقبة السوق وتحليل المنافسين</div><div><b>الجودة والموقع</b>فحص جودة البيانات وتحليلات جغرافية</div><div><b>إدارة الأدلة</b>دلائل مدعومة بالبيانات للنتائج والمقترحات</div><div><b>الوكلاء الأذكياء</b>أتمتة جلب البيانات والتحليل والتفاعل</div></div><div class="chips" style="justify-content:flex-start"><span class="chip">Django</span><span class="chip">Python</span><span class="chip">SQLite</span></div></div></div>
</section>'''

content = re.sub(old_section_pattern, new_section, content, flags=re.DOTALL)

# Add new translations to EN dictionary
new_translations = {
    "المشاريع": "Projects",
    "◈ المشاريع والابتكارات": "◈ Projects & Innovations",
    "مشاريعي وابتكاراتي التقنية": "My Technical Projects & Innovations",
    "من تأسيس الشركات الناشئة وتطبيقات الويب الحديثة إلى منصات ذكاء الأعمال.": "From founding startups and modern web apps to business intelligence platforms.",
    "بصيرة — حلول وخدمات تقنية ذكية": "Baseera — Smart Tech Solutions & Services",
    "من مسابقة «هندسها بالذكاء الاصطناعي 2026» إلى شركة بثلاث خدمات تقنية متقدمة.": "From the Engineer It with AI 2026 competition to a company with three advanced tech services.",
    "لوحة أسعار الذهب في عُمان — Oman Gold Price Dashboard": "Oman Gold Price Dashboard",
    "تطبيق ويب من صفحة واحدة (SPA) لمتابعة أسعار الذهب في سلطنة عُمان بالريال العُماني لحظياً، مبني بـ Angular وTailwind CSS بواجهة عربية RTL ودعم كامل للوضع الداكن والفاتح.": "A single-page web application (SPA) for real-time tracking of Oman gold prices (in OMR/g), built with Angular & Tailwind CSS featuring RTL Arabic layout and full dark/light mode support.",
    "✦ مجان للمبرمجين · تطبيق عملي": "✦ Majan for Programmers · Practical Project",
    "السوق: سلطنة عُمان": "Market: Sultanate of Oman",
    "العملة: الريال العُماني (ر.ع)": "Currency: Omani Rial (OMR)",
    "الوحدة: جرام": "Unit: Gram",
    "التحديث: مباشر (بيانات تجريبية)": "Update: Live (Demo Data)",
    "سلطنة عُمان": "Sultanate of Oman",
    "الريال العُماني (ر.ع)": "Omani Rial (OMR)",
    "جرام": "Gram",
    "مباشر (بيانات تجريبية)": "Live (Demo Data)",
    "عيار 24": "24 Karat",
    "عيار 22": "22 Karat",
    "عيار 21": "21 Karat",
    "عيار 18": "18 Karat",
    "نقاء 99.9%": "99.9% purity",
    "نقاء 91.6%": "91.6% purity",
    "نقاء 87.5%": "87.5% purity",
    "نقاء 75.0%": "75.0% purity",
    "28.45 ر.ع": "28.45 OMR",
    "26.08 ر.ع": "26.08 OMR",
    "24.89 ر.ع": "24.89 OMR",
    "21.34 ر.ع": "21.34 OMR",
    "مؤشر حركة الأسعار (آخر 30 يوماً - SVG Polyline)": "Price Trend Indicator (Last 30 Days - SVG Polyline)",
    "+3.8% ↑ نمو مستمر": "+3.8% ↑ Steady Growth",
    "الهيدر والواجهة الرئيسية": "Header & Hero Interface",
    "شريط تنقل ثابت، شارة «بيانات تجريبية»، مسار تنقل (Breadcrumbs)، وزر تبديل الوضع الداكن/الفاتح.": "Fixed navbar, demo data badge, breadcrumb trail, and dark/light mode switcher.",
    "أسعار اليوم اللحظية": "Today's Live Prices",
    "4 بطاقات تفاعلية لعيارات (18، 21، 22، 24) تعرض السعر والعملة والوحدة والنقاء بدقة.": "4 interactive karat cards (18, 21, 22, 24) displaying price, currency, unit, and purity.",
    "حاسبة الذهب التقديرية": "Estimated Gold Calculator",
    "حاسبة ذكية لاختيار العيار وإدخال الوزن بالجرام مع تحقق فوري وحالة فارغة تفاعلية.": "Smart calculator to choose karat and input weight in grams with instant validation.",
    "رسم بياني لـ 30 يوماً": "30-Day Trend Chart",
    "خط SVG Polyline مع تبديل العيارات وإحصائيات لأعلى/أقل/آخر سعر ومقارنة التغير.": "SVG Polyline chart with karat switching and min/max/current price statistics.",
    "جدول سجل الأسعار": "Price History Table",
    "جدول تاريخي متجاوب لـ 30 يوماً لكافة العيارات بألوان صفوف متناوبة وتمرير أفقي سلس.": "Responsive 30-day price history table with alternating rows and smooth scrolling.",
    "معمارية المكونات النظيفة": "Clean Component Architecture",
    "بنية Angular مجزأة ومستقلة: header, gold-price-card, gold-calculator, chart, price-history.": "Modular Angular structure: header, gold-price-card, gold-calculator, chart, price-history.",
    "خدمات قابلة للتوسع": "Extensible Services",
    "GoldService لقراءة ومعالجة البيانات وجاهزية ربط API، وThemeService لإدارة الوضع الداكن.": "GoldService for data handling and API readiness, and ThemeService for theme switching.",
    "جاهزية النشر والحاويات": "Deployment & Containerization",
    "دعم كامل لـ SSR وDocker، وملف README تفصيلي بالخطوات واختبارات معيارية مدمجة.": "Full SSR and Docker support with detailed README instructions and unit tests."
}

# Update EN in index.html
en_match = re.search(r'var EN\s*=\s*(\{.*?\});', content, re.DOTALL)
if en_match:
    old_en_json = en_match.group(1)
    en_dict = json.loads(old_en_json)
    en_dict.update(new_translations)
    new_en_json = json.dumps(en_dict, ensure_ascii=False)
    content = content[:en_match.start(1)] + new_en_json + content[en_match.end(1):]

# Update Q questions to include the Gold project
gold_q_ar = ["ما هي تفاصيل مشروع لوحة أسعار الذهب؟", "تطبيق ويب (SPA) طورته ميرة بـ Angular وTailwind CSS لمتابعة أسعار الذهب في سلطنة عُمان، يتضمن حاسبة ذكية ورسماً بيانياً لـ 30 يوماً وسجل أسعار متجاوباً، وهو التطبيق العملي من مبادرة «مجان للمبرمجين»."]
gold_q_en = ["What are the details of the Gold Price Dashboard?", "An Angular & Tailwind CSS SPA web app developed by Mira to track Oman gold prices, featuring a smart calculator, 30-day SVG chart, and responsive history table, built for 'Majan for Programmers'."]

# Update "ما هي أبرز مشاريع ميرة؟" answer
content = content.replace('"أبرزها بصيرة، الشركة الناشئة اللي تؤسسها ميرة مع سارة الحربي وفوز المديلوي. ميرة هي الـ CIO فيها، وبدأت الفكرة في مسابقة هندسها بالذكاء الاصطناعي 2026. ولها كذلك مشروع مدى للتحليلات."',
                          '"أبرز مشاريع ميرة: شركة بصيرة الناشئة (تطبيقات ومساعد ذكي)، ولوحة أسعار الذهب في عُمان (تطبيق ويب بـ Angular وTailwind CSS)، ومنصة مدى للتحليلات (بـ Django وPython)."')

content = content.replace('"The main one is Baseera, the startup Mira is founding with Sara Al Harbi and Fawz Al Madilwi. Mira is its CIO, and the idea began in the Engineer It with AI 2026 competition. She also worked on MADA Analytics."',
                          '"Mira\'s key projects: Baseera startup (apps & AI assistant), the Oman Gold Price Dashboard (Angular & Tailwind CSS SPA), and MADA Analytics (Django & Python BI platform)."')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html successfully!')
