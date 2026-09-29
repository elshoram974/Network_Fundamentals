import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

footer_html = """
<footer style="text-align: center; padding: 20px; margin-top: 40px; font-weight: bold; border-top: 1px solid var(--line); direction: ltr;">
  <a href="https://wa.me/201553668845" target="_blank" style="text-decoration: none; color: var(--accent); font-family: 'IBM Plex Sans', sans-serif;">
    By Mohammed El Shora - +201553668845
  </a>
</footer>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Extract Title
    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1) if title_match else "CCNA 200-301 Course"
    
    # Check if already patched
    if '<meta property="og:title"' in content and 'By Mohammed El Shora' in content:
        print(f"Skipping {file}, already patched.")
        continue

    # 2. Inject Meta tags right after <title> if not exists
    if '<meta property="og:title"' not in content:
        desc = f"شرح تفصيلي لـ {title} - كورس CCNA 200-301 م. محمد الشورى"
        meta_tags = f"""<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">"""
        content = re.sub(r'(<title>.*?</title>)', r'\1\n' + meta_tags, content)

    # 3. Inject footer just before </body>
    if 'By Mohammed El Shora' not in content:
        content = content.replace('</body>', footer_html + '\n</body>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Patched {file}")
