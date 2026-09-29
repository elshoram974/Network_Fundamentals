import os
import re

from lesson_lib import HEAD

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix literal \n in the script section that causes Syntax Error
    html = html.replace('\\nbuildQuiz', '\nbuildQuiz')
    html = html.replace(']);\\n', ']);\n')
    html = html.replace('</script>\\n', '</script>\n')
    html = html.replace('</body>\\n', '</body>\n')
    html = html.replace('</html>\\n', '</html>\n')
    
    # Also replace \n anywhere else in the script tag
    html = html.replace('<script>\\n', '<script>\n')

    # Update brand to use الفهرس
    old_brand = r'<div class="brand">\s*<a href="index.html">Index</a>\s*<span class="en">CCNA Study Notes</span><span class="ar">مذكرات CCNA</span>\s*</div>'
    new_brand = '''<div class="brand">
    <a href="index.html">الفهرس</a>
    <span class="en">CCNA Study Notes</span><span class="ar">مذكرات CCNA</span>
  </div>'''
    html = re.sub(old_brand, new_brand, html)

    # Make sure we didn't miss it if it still has old old brand
    old_old_brand = r'<div class="brand"><span class="dot"></span>\s*<span class="en">CCNA 200-301 Study</span><span class="ar">مذاكرة CCNA 200-301</span>\s*<span class="lesson-tag">— Network Fundamentals</span></div>'
    html = re.sub(old_old_brand, new_brand, html)

    # Fix Footer to use Cisco.com instead of NetworkLessons.com
    html = html.replace('NetworkLessons.com', 'Cisco.com')

    # Fix Previous link for Lesson 1
    if 'lesson-01' in filepath:
        html = html.replace('<a class="prev" href="#"><span class="k"><span class="en">Previous Lesson</span><span class="ar">الدرس السابق</span></span><strong>— none —</strong></a>', '<a class="prev" href="index.html"><span class="k"><span class="en">Index</span><span class="ar">الرئيسية</span></span><strong>الفهرس</strong></a>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Processed {filepath}")

for i in range(1, 8):
    files = [f for f in os.listdir('.') if f.startswith(f'lesson-0{i}') and f.endswith('.html')]
    if files:
        process_file(files[0])
