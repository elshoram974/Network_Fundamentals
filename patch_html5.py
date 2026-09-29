import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update document.documentElement.dir in IIFE
    if "document.documentElement.dir = savedLang === 'ar' ? 'rtl' : 'ltr';" not in html:
        html = html.replace(
            "document.documentElement.lang = savedLang;",
            "document.documentElement.lang = savedLang;\n  document.documentElement.dir = savedLang === 'ar' ? 'rtl' : 'ltr';"
        )

    # 2. Update document.documentElement.dir in setGlobalLang
    if "document.documentElement.dir = (l === 'ar') ? 'rtl' : 'ltr';" not in html:
        html = html.replace(
            "document.documentElement.classList.remove('lang-en', 'lang-ar');",
            "document.documentElement.dir = (l === 'ar') ? 'rtl' : 'ltr';\n  document.documentElement.classList.remove('lang-en', 'lang-ar');"
        )
        
    # In case previous patch didn't add it perfectly because the string was slightly different in lesson-01:
    if "document.documentElement.dir =" not in html:
        # Fallback regex for setGlobalLang
        html = re.sub(
            r"(function setGlobalLang\(l\){\s*)(document\.body)", 
            r"\1document.documentElement.dir = (l === 'ar') ? 'rtl' : 'ltr';\n  \2", 
            html
        )

    # 3. Update the Brand to use the lesson title
    # First, extract the title
    title_match = re.search(r'<h1>(.*?)</h1>', html)
    if title_match:
        title = title_match.group(1).strip()
        # Remove any inner HTML from title like span class="en" etc.
        # Actually wait, the <h1> in our files is just <h1>Title</h1>
        # Let's clean it just in case
        title = re.sub(r'<[^>]+>', '', title)
        
        old_brand_en_ar = r'<span class="en">CCNA Study Notes</span><span class="ar">مذكرات CCNA</span>'
        new_brand_title = f'<span class="lesson-title">{title}</span>'
        html = re.sub(old_brand_en_ar, new_brand_title, html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Processed {filepath}")

for i in range(1, 8):
    files = [f for f in os.listdir('.') if f.startswith(f'lesson-0{i}') and f.endswith('.html')]
    if files:
        process_file(files[0])
