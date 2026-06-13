# Book Data Scraper & Analyzer

أداة برمجية لسحب بيانات الكتب من موقع [books.toscrape.com]، تنظيفها، وإجراء تحليل إحصائي عليها.
A tool to scrape, clean, and analyze book data from [books.toscrape.com].

## 🛠 التقنيات المستخدمة (Tech Stack)
- **Python**: لغة البرمجة الأساسية.
- **BeautifulSoup4**: لسحب وتحليل بيانات الـ HTML.
- **Pandas**: لمعالجة البيانات وتصديرها لملفات Excel.
- **Arabic-Reshaper & Bidi**: لعرض النصوص العربية بشكل صحيح في الـ Terminal.

## 📊 مميزات المشروع (Features)
- **سحب ذكي:** سحب البيانات من 50 صفحة تلقائياً.
- **تنظيف البيانات:** معالجة النصوص وحذف الرموز غير المرغوب فيها من الأسعار.
- **تحليل إحصائي:** استخراج المتوسط، وأغلى وأرخص كتاب.
- **تصدير النتائج:** حفظ البيانات النهائية في ملف `analyzed_books_portfolio.xlsx`.

## 🚀 كيف تستخدم البرنامج (Getting Started)
1. قم بتثبيت المكتبات المطلوبة:
   `pip install -r requirements.txt`
2. قم بتشغيل الكود:
   `books-scraper-analyzer`
