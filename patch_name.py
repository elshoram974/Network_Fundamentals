import os

old_footer = """<footer style="text-align: center; padding: 20px; margin-top: 40px; font-weight: bold; border-top: 1px solid var(--line); direction: ltr;">
  <a href="https://wa.me/201553668845" target="_blank" style="text-decoration: none; color: var(--accent); font-family: 'IBM Plex Sans', sans-serif;">
    By Mohammed El Shora - +201553668845
  </a>
</footer>"""

new_footer = """<footer style="text-align: center; padding: 20px; margin-top: 40px; font-weight: bold; border-top: 1px solid var(--line);">
  <a href="https://wa.me/201553668845" target="_blank" style="text-decoration: none; color: var(--accent); font-family: 'IBM Plex Sans', sans-serif; display: inline-flex; align-items: center; gap: 8px; justify-content: center;" dir="ltr">
    <span class="en">By Mohammed El Shora</span>
    <span class="ar" style="direction:rtl">بواسطة محمد الشوره</span>
    <span dir="ltr">- 📞 +201553668845</span>
  </a>
</footer>"""

old_meta = "كورس CCNA 200-301 م. محمد الشورى"
new_meta = "كورس CCNA 200-301 م. محمد الشوره"

for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r') as file:
            content = file.read()
        
        patched = False
        if old_footer in content:
            content = content.replace(old_footer, new_footer)
            patched = True
            
        if old_meta in content:
            content = content.replace(old_meta, new_meta)
            patched = True
            
        if patched:
            with open(f, 'w') as file:
                file.write(content)
            print(f"Patched {f}")
