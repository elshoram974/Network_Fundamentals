import os
import re

url_map = {
    "01-introduction_to_the_osi_model.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/introduction-to-the-osi-model",
    "02-ipv4.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/ipv4", 
    "03-ipv4-header.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/ipv4-packet-header",
    "04-arp.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/arp-address-resolution-protocol",
    "05-tcp-udp.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/introduction-to-tcp-and-udp",
    "06-tcp-header.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/tcp-header",
    "07-tcp window size scaling.pdf": "https://networklessons.com/cisco/ccna-routing-switching/tcp-window-size-scaling",
}

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the source_pdf in this file
    match = re.search(r'Source: <a href="pdfs/([^"]+)"', html)
    if not match:
        match = re.search(r'Source Material: <a href="[^"]+" target="_blank">NetworkLessons\.com</a>', html)
        if not match:
            # Maybe already replaced?
            print(f"Skipping {filepath}, no match.")
            return
    
    # We want to replace the whole source-footer div contents
    old_footer_pattern = r'<div class="source-footer">.*?</div>'
    
    pdf_name = ""
    for k in url_map.keys():
        if k.split('.pdf')[0] in filepath: # heuristic to find which lesson it is
            pdf_name = k
            break
            
    if not pdf_name and 'lesson-07' in filepath:
        pdf_name = "07-tcp window size scaling.pdf"

    real_url = url_map.get(pdf_name, "https://networklessons.com/cisco/ccna-200-301")
    
    new_footer = f'''<div class="source-footer">
    <div class="en">
      📝 <strong>Source Material:</strong> This lesson is officially sourced from <a href="{real_url}" target="_blank">NetworkLessons.com</a>. We transformed it into an interactive, bilingual format with extra simplified notes (yellow boxes) and realistic exam questions for an optimal learning experience!
    </div>
    <div class="ar">
      📝 <strong>المصدر الرسمي:</strong> هذا الدرس مأخوذ رسمياً من <a href="{real_url}" target="_blank">NetworkLessons.com</a>. لقد قمنا بتحويله إلى شكل تفاعلي ثنائي اللغة مع إضافة شروحات مبسطة (المربعات الصفراء) وأسئلة امتحانات حقيقية لتسهيل المذاكرة!
    </div>
</div>'''
    
    # Replace
    html = re.sub(old_footer_pattern, new_footer, html, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Processed {filepath}")

for i in range(1, 8):
    files = [f for f in os.listdir('.') if f.startswith(f'lesson-0{i}') and f.endswith('.html')]
    if files:
        process_file(files[0])
