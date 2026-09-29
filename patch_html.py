import os
import re

# We will read HEAD from lesson_lib.py to get the new style.
from lesson_lib import HEAD

# But HEAD has {NUM} and {TITLE} which we need to extract from each file.
def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Fix the HEAD/CSS
    # Extract Title and Lesson Number
    title_match = re.search(r'<title>Lesson (\d+) — (.*?) \| CCNA', html)
    if title_match:
        num = title_match.group(1)
        title = title_match.group(2)
        
        # Calculate progress percent based on some logic or just extract it
        pct_match = re.search(r'width:\s*(\d+)%;?', html)
        pct = pct_match.group(1) if pct_match else "10"

        # Reconstruct HEAD
        new_head = HEAD.replace('{NUM}', num).replace('{TITLE}', title).replace('{PCT}', pct)
        
        # We need to replace everything from <!DOCTYPE html> down to <div class="controls"> inclusive?
        # Actually, let's just replace from <!DOCTYPE html> down to </style>
        # Wait, the new HEAD in lesson_lib includes the <body> tag and topbar.
        # Let's extract from lesson_lib.py HEAD everything up to </style>
        head_style_end = new_head.find('</style>') + 8
        new_head_only = new_head[:head_style_end]

        old_head_end = html.find('</style>') + 8
        if old_head_end > 7 and '<style>' in html:
            # Replace old head with new head
            html = new_head_only + html[old_head_end:]
        
        # Also need to replace the langswitch with controls if it exists
        old_langswitch = '''<div class="langswitch">
    <button id="btnEn" class="active" onclick="setGlobalLang('en')">EN</button>
    <button id="btnAr" onclick="setGlobalLang('ar')">AR</button>
  </div>'''
        new_controls = '''<div class="controls">
    <button class="theme-btn" onclick="toggleTheme()">🌓</button>
    <div class="langswitch">
      <button id="btnEn" class="active" onclick="setGlobalLang('en')">EN</button>
      <button id="btnAr" onclick="setGlobalLang('ar')">AR</button>
    </div>
  </div>'''
        if old_langswitch in html:
            html = html.replace(old_langswitch, new_controls)
        
        # Also update brand
        old_brand = r'<div class="brand"><span class="dot"></span>\s*<span class="en">CCNA 200-301 Study</span><span class="ar">مذاكرة CCNA 200-301</span>\s*<span class="lesson-tag">— Network Fundamentals</span></div>'
        new_brand = '''<div class="brand">
    <a href="index.html">Index</a>
    <span class="en">CCNA Study Notes</span><span class="ar">مذكرات CCNA</span>
  </div>'''
        html = re.sub(old_brand, new_brand, html)

    # 2. Fix the Footer to make it clickable
    # Look for "Source: pdf_name.pdf — "
    def footer_repl(m):
        pdf_name = m.group(1)
        rest = m.group(2)
        # Check if it's already a link
        if '<a href' in pdf_name:
            return m.group(0) # don't touch
        return f'<div class="source-footer">\n    Source: <a href="pdfs/{pdf_name}" target="_blank">{pdf_name}</a> — {rest}\n</div>'
    
    html = re.sub(r'<div class="source-footer">\s*Source:\s*([^\s]+)\s*—\s*(.*?)\s*</div>', footer_repl, html, flags=re.DOTALL)
    
    # Also if the footer is using the old <p>Reference material:</p> format
    def footer_repl2(m):
        pdf_name = m.group(1)
        return f'<div class="source-footer">\n    Source: <a href="pdfs/{pdf_name}" target="_blank">{pdf_name}</a> — NetworkLessons.com (CCNA 200-301, Unit 2) · Yellow boxes = extra explanations outside the source, alternate ways to picture the idea, not for memorization as exam-source facts · Diagrams are lightweight self-drawn boxes, not reproductions of the PDF\'s images.\n</div>'
    
    html = re.sub(r'<div class="source-footer">\s*<p>[^<]*<a href="pdfs/([^"]+)"[^>]*>.*?</div>', footer_repl2, html, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Processed {filepath}")

for i in range(1, 8):
    files = [f for f in os.listdir('.') if f.startswith(f'lesson-0{i}') and f.endswith('.html')]
    if files:
        process_file(files[0])
