import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update brand to include both languages
    old_brand = r'<div class="brand">\s*<a href="index.html">الفهرس</a>\s*<span class="en">CCNA Study Notes</span><span class="ar">مذكرات CCNA</span>\s*</div>'
    new_brand = '''<div class="brand">
    <a href="index.html"><span class="en">Index</span><span class="ar">الفهرس</span></a>
    <span class="en">CCNA Study Notes</span><span class="ar">مذكرات CCNA</span>
  </div>'''
    html = re.sub(old_brand, new_brand, html)
    
    # 1b. Catch cases where it was still Index
    old_brand2 = r'<div class="brand">\s*<a href="index.html">Index</a>\s*<span class="en">CCNA Study Notes</span><span class="ar">مذكرات CCNA</span>\s*</div>'
    html = re.sub(old_brand2, new_brand, html)

    # 2. Add document.documentElement.dir = l === 'ar' ? 'rtl' : 'ltr'; to setGlobalLang
    if "document.documentElement.dir =" not in html:
        html = html.replace("document.documentElement.classList.remove('lang-en', 'lang-ar');", 
                            "document.documentElement.dir = (l === 'ar') ? 'rtl' : 'ltr';\n  document.documentElement.classList.remove('lang-en', 'lang-ar');")

    # 3. Add Recap and Quiz to the TOC
    # The TOC looks like: <nav class="toc"><div class="toc-title"><span class="en">Contents</span><span class="ar">المحتويات</span></div><a href="#...
    # We want to insert Recap at the beginning, and Quiz at the end.
    if '<a href="#recap">' not in html:
        toc_title_end = html.find('</div>', html.find('<div class="toc-title">')) + 6
        recap_link = '<a href="#recap"><span class="en">Recap Quiz</span><span class="ar">اختبار المراجعة</span></a>'
        if html.find('<nav class="toc">') != -1:
            html = html[:toc_title_end] + recap_link + html[toc_title_end:]
    
    if '<a href="#quiz">' not in html:
        toc_end = html.find('</nav>')
        quiz_link = '<a href="#quiz"><span class="en">Lesson Quiz</span><span class="ar">اختبار الدرس</span></a>'
        if toc_end != -1:
            html = html[:toc_end] + quiz_link + html[toc_end:]

    # 4. Remove inline styles from fb-diagram divs that have dark background hardcoded
    # Look for <div style="background:#0a0a0a;... or <div style="background: #0a0a0a;... inside fb-diagram
    # Or just replace the specific hardcoded style string in lesson 7
    hardcoded_style = 'style="background:#0a0a0a; color:#f0f0f0; font-family:monospace; padding:20px; border-radius:8px; line-height:1.2; overflow-x:auto;"'
    hardcoded_style2 = "style='background:#0a0a0a; color:#f0f0f0; font-family:monospace; padding:20px; border-radius:8px; line-height:1.2; overflow-x:auto;'"
    html = html.replace(hardcoded_style, '')
    html = html.replace(hardcoded_style2, '')
    
    # Another variant: style="height:150px; position:relative; border-left:2px solid var(--line); border-bottom:2px solid var(--line); padding:10px; margin:20px 0;"
    # Let's keep that one because it uses CSS vars and is structural, not colors that conflict with theme.

    # Also add the CSS for .img-fallback .fb-diagram > div
    if '.img-fallback .fb-diagram > div {' not in html:
        css_inject = '''
.img-fallback .fb-diagram > div { background: var(--panel2); color: var(--text); padding: 20px; border-radius: 8px; font-family: 'IBM Plex Mono', monospace; overflow-x: auto; text-align: left; direction: ltr; }
'''
        html = html.replace('</style>', css_inject + '</style>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Processed {filepath}")

for i in range(1, 8):
    files = [f for f in os.listdir('.') if f.startswith(f'lesson-0{i}') and f.endswith('.html')]
    if files:
        process_file(files[0])
