import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import arabic_reshaper
from bidi.algorithm import get_display

def fix_arabic(text):
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)

all_books = []
print(fix_arabic("🚀 جاري بدء سحب البيانات بدقة وفصل الأعمدة... يرجى الانتظار..."))

for page in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            # استخدام lxml أو html.parser مع ترميز utf-8 صريح
            soup = BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')
            books = soup.find_all('article', class_='product_pod')
            
            for book in books:
                title = book.h3.a['title'] if book.h3.a else "No Title"
                price_tag = book.find('p', class_='price_color')
                raw_price = price_tag.text if price_tag else "0"
                
                # تنظيف حاسم وجذري لكل الرموز الغريبة (Â و £) عشان يتبقى الرقم فقط
                clean_price_str = raw_price.replace('£', '').replace('Â', '').strip()
                clean_price = float(clean_price_str)
                
                # هنا بنأكد إنهم هينزلوا كـ Dictionary فيه مفتاحين منفصلين تماماً كعواميد
                all_books.append({
                    'Book Title': title,
                    'Price (£)': clean_price
                })
                
            print(fix_arabic(f"✅ تم سحب وتنسيق الصفحة {page} بنجاح..."))
            time.sleep(0.1)
        else:
            break
    except Exception as e:
        print(f"Error: {e}")
        break

if all_books:
    # تحويل الداتا لـ DataFrame وفصلها التلقائي لعواميد
    df = pd.DataFrame(all_books)
    
    # حفظ الملف مع تحديد الـ engine لمنع أي لخبطة حروف في الإكسل
    df.to_excel('analyzed_books_portfolio.xlsx', index=False, engine='openpyxl')
    
    # التحليلات
    total_books = len(df)
    avg_price = df['Price (£)'].mean()
    max_price = df['Price (£)'].max()
    min_price = df['Price (£)'].min()

    
    expensive_book = df[df['Price (£)'] == max_price]['Book Title'].iloc[0]
    cheapest_book = df[df['Price (£)'] == min_price]['Book Title'].iloc[0]
    
    print("\n" + "="*60)
    print(fix_arabic("🎯 التقرير الذكي المُنظف (Data Insights Report) 🎯"))
    print("="*60)
    print(fix_arabic(f"🔹 إجمالي عدد الكتب: {total_books} كتاب"))
    print(fix_arabic(f"🔹 متوسط السعر: {avg_price:.2f} £"))
    print(f"{fix_arabic('🔹 أغلى كتاب:')} {max_price:.2f} £ -> ({expensive_book})")
    print(f"{fix_arabic('🔹 أرخص كتاب:')} {min_price:.2f} £ -> ({cheapest_book})")
    print("="*60)
    print(fix_arabic("💾 تم الحفظ المظبوط بنجاح في: analyzed_books_portfolio.xlsx"))