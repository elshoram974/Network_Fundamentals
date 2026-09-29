import os
import re
from lesson_lib import HEAD, SCRIPT, bi

def patch_file(filename):
    with open(filename, 'r', encoding='utf8') as f:
        html = f.read()

    # 1. Replace <style> block
    new_style = re.search(r'<style>.*?</style>', HEAD, flags=re.DOTALL).group(0)
    html = re.sub(r'<style>.*?</style>', new_style, html, flags=re.DOTALL)

    # 2. Extract the buildQuiz(...) calls at the end
    # The end of the file looks like:
    # function buildQuiz(id, items){ ... }
    # 
    # buildQuiz('recapArea', [...]);
    # buildQuiz('quizArea', [...]);
    # </script>
    
    quiz_calls_match = re.search(r'(buildQuiz\([\s\S]*?)</script>', html)
    if quiz_calls_match:
        quiz_calls = quiz_calls_match.group(1).strip()
    else:
        quiz_calls = ""
        print(f"Warning: No buildQuiz calls found in {filename}")

    # 3. Replace the entire <script> ... </script> block at the end with SCRIPT + quiz_calls
    # Wait, there are multiple <script> blocks (e.g. one in HEAD).
    # We want to replace the LAST <script> block.
    # We can just split by "<script>" and take the last one.
    parts = html.rsplit('<script>', 1)
    if len(parts) == 2:
        new_tail = SCRIPT.replace('</script>', '\n' + quiz_calls + '\n</script>')
        # SCRIPT includes "<script>", so we just append it to parts[0]
        # But wait, parts[1] contains everything up to the end of the file.
        # So we need to remove the old script content from parts[1]
        after_script = parts[1].split('</script>', 1)[1]
        html = parts[0] + new_tail + after_script

    # 4. Update the Footer URLs
    url_map = {
        "01-introduction_to_the_osi_model.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/introduction-to-the-osi-model",
        "02-ipv4.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/ipv4", 
        "03-ipv4-header.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/ipv4-packet-header",
        "04-arp.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/arp-address-resolution-protocol",
        "05-tcp-udp.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/introduction-to-tcp-and-udp",
        "06-tcp-header.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/tcp-header",
        "07-tcp window size scaling.pdf": "https://networklessons.com/cisco/ccna-routing-switching/tcp-window-size-scaling",
    }
    
    # Extract the source_pdf from the existing HTML (it's in the footer)
    pdf_match = re.search(r'pdfs/([^"]+\.pdf)', html)
    if pdf_match:
        source_pdf = pdf_match.group(1)
        real_url = url_map.get(source_pdf, "https://networklessons.com/cisco/ccna-200-301")
        
        # Replace the source-footer div completely
        new_footer = f'''<div class="source-footer">
    <div class="en">
      📝 <strong>Source Material:</strong> This lesson is officially sourced from <a href="{real_url}" target="_blank">NetworkLessons.com</a> (PDF: <a href="pdfs/{source_pdf}" target="_blank">{source_pdf}</a>). We transformed it into an interactive, bilingual format with extra simplified notes (yellow boxes) and realistic exam questions for an optimal learning experience!
    </div>
    <div class="ar">
      📝 <strong>المصدر الرسمي:</strong> هذا الدرس مأخوذ رسمياً من <a href="{real_url}" target="_blank">NetworkLessons.com</a> (ملف الـ PDF: <a href="pdfs/{source_pdf}" target="_blank">{source_pdf}</a>). لقد قمنا بتحويله إلى شكل تفاعلي ثنائي اللغة مع إضافة شروحات مبسطة (المربعات الصفراء) وأسئلة امتحانات حقيقية لتسهيل المذاكرة!
    </div>
</div>'''
        html = re.sub(r'<div class="source-footer">.*?</div>\s*</div>', new_footer, html, flags=re.DOTALL)
        # Wait, the regex `.*?</div>\s*</div>` might match too much. Let's be careful.
    
    with open(filename, 'w', encoding='utf8') as f:
        f.write(html)
    print(f"Processed {filename}")

for i in range(1, 8):
    filename = f"lesson-0{i}"
    # find the actual file
    for f in os.listdir('.'):
        if f.startswith(filename) and f.endswith('.html'):
            patch_file(f)
