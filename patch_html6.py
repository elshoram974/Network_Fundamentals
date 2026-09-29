import os
import re
import lesson_lib

def patch_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update <style>...</style>
    # We will extract the style block from lesson_lib.HEAD
    style_match = re.search(r'<style>(.*?)</style>', lesson_lib.HEAD, flags=re.DOTALL)
    if style_match:
        new_style = style_match.group(0)
        html = re.sub(r'<style>.*?</style>', new_style, html, flags=re.DOTALL)

    # 2. Update the head <script>...</script>
    head_script_match = re.search(r'</style>\n<script>(.*?)</script>', lesson_lib.HEAD, flags=re.DOTALL)
    if head_script_match:
        new_head_script = f'<script>{head_script_match.group(1)}</script>'
        html = re.sub(r'</style>\s*<script>.*?</script>', f'</style>\n{new_head_script}', html, flags=re.DOTALL)

    # 3. Update the tail <script>...</script>
    # This is from lesson_lib.SCRIPT
    tail_script_match = re.search(r'<script>(.*?)</script>', lesson_lib.SCRIPT, flags=re.DOTALL)
    if tail_script_match:
        new_tail_script = f'<script>{tail_script_match.group(1)}</script>'
        # We find the tail script by looking for "const UI = {" which is a unique marker
        # But maybe the HTML has a single giant script tag at the end.
        html = re.sub(r'<script>\s*const UI = \{.*?</script>', new_tail_script, html, flags=re.DOTALL)
        
        # If the above failed because it was combined with buildQuiz calls:
        if "const UI = {" in html and new_tail_script not in html:
            # We replace from "const UI = {" up to the end of the script, but preserve the buildQuiz calls.
            # Actually, the tail script in HTML is: <script>const UI = {...} ... buildQuiz(...);</script>
            # Let's just replace the UI dict and functions
            pass # The regex above should work if it wasn't combined.
            
            # Since the tail script in HTML is a single <script> block that contains BOTH UI logic and buildQuiz calls:
            # Let's extract everything BEFORE buildQuiz('recapArea',...) and replace it.
            html = re.sub(r'<script>\s*const UI = \{.*?function buildQuiz[^\}]+\}\s*', new_tail_script.replace('</script>', '\n'), html, flags=re.DOTALL)

    # 4. Update the source footer
    url_map = {
        "01-introduction_to_the_osi_model.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/introduction-to-the-osi-model",
        "02-ipv4.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/ipv4", 
        "03-ipv4-header.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/ipv4-packet-header",
        "04-arp.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/arp-address-resolution-protocol",
        "05-tcp-udp.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/introduction-to-tcp-and-udp",
        "06-tcp-header.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/tcp-header",
        "07-tcp window size scaling.pdf": "https://networklessons.com/cisco/ccna-routing-switching/tcp-window-size-scaling",
    }
    
    # Map html prefix to pdf name
    html_to_pdf = {
        "lesson-01": "01-introduction_to_the_osi_model.pdf",
        "lesson-02": "02-ipv4.pdf",
        "lesson-03": "03-ipv4-header.pdf",
        "lesson-04": "04-arp.pdf",
        "lesson-05": "05-tcp-udp.pdf",
        "lesson-06": "06-tcp-header.pdf",
        "lesson-07": "07-tcp window size scaling.pdf"
    }
    
    pdf_name = ""
    for prefix, pdf in html_to_pdf.items():
        if prefix in filepath:
            pdf_name = pdf
            break

    real_url = url_map.get(pdf_name, "https://networklessons.com/cisco/ccna-200-301")
    
    new_footer = f'''<div class="source-footer">
    <div class="en">
      📝 <strong>Source Material:</strong> This lesson is officially sourced from <a href="{real_url}" target="_blank">NetworkLessons.com</a> (PDF: <a href="pdfs/{pdf_name}" target="_blank">{pdf_name}</a>). We transformed it into an interactive, bilingual format with extra simplified notes (yellow boxes) and realistic exam questions for an optimal learning experience!
    </div>
    <div class="ar">
      📝 <strong>المصدر الرسمي:</strong> هذا الدرس مأخوذ رسمياً من <a href="{real_url}" target="_blank">NetworkLessons.com</a> (ملف الـ PDF: <a href="pdfs/{pdf_name}" target="_blank">{pdf_name}</a>). لقد قمنا بتحويله إلى شكل تفاعلي ثنائي اللغة مع إضافة شروحات مبسطة (المربعات الصفراء) وأسئلة امتحانات حقيقية لتسهيل المذاكرة!
    </div>
</div>'''
    
    html = re.sub(r'<div class="source-footer">.*?</div>\n</div>', new_footer + '\n', html, flags=re.DOTALL) # wait, footer might not have </div>\n</div>
    # Better regex:
    html = re.sub(r'<div class="source-footer">.*?</div>\s*(?=<script>)', new_footer + '\n', html, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Processed {filepath}")

for i in range(1, 8):
    files = [f for f in os.listdir('.') if f.startswith(f'lesson-0{i}') and f.endswith('.html')]
    if files:
        patch_file(files[0])
