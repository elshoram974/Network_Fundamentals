import os

js_append = """
document.addEventListener("DOMContentLoaded", () => {
  const savedLang = localStorage.getItem('ccna-lang') || 'en';
  const btnEn = document.getElementById('btnEn');
  const btnAr = document.getElementById('btnAr');
  if(btnEn && btnAr) {
    btnEn.classList.toggle('active', savedLang==='en');
    btnAr.classList.toggle('active', savedLang==='ar');
  }
});
"""

for f in os.listdir('.'):
    if f.endswith('.html') and f != 'index.html':
        with open(f, 'r') as file:
            content = file.read()
        
        if "btnEn.classList.toggle('active'" not in content.split("</body>")[0].split("<script>")[-1]:
            content = content.replace("</script>\n</body>", js_append + "</script>\n</body>")
            with open(f, 'w') as file:
                file.write(content)
            print(f"Patched {f}")

with open('lesson_lib.py', 'r') as file:
    content = file.read()
if "btnEn.classList.toggle('active'" not in content:
    content = content.replace("</script>\n'''", js_append + "</script>\n'''")
    with open('lesson_lib.py', 'w') as file:
        file.write(content)
    print("Patched lesson_lib.py")

with open('build_exam.py', 'r') as file:
    content = file.read()
if "btnEn.classList.toggle('active'" not in content:
    content = content.replace("</script>\n'''", js_append + "</script>\n'''")
    with open('build_exam.py', 'w') as file:
        file.write(content)
    print("Patched build_exam.py")
