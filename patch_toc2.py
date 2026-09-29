import os
import re

pattern = re.compile(r"const tocLinks=\[\.\.\.document\.querySelectorAll\('\.toc a'\)\], secs=tocLinks\.map\(a=>document\.querySelector\(a\.getAttribute\('href'\)\)\);\nwindow\.addEventListener\('scroll',\(\)=>\{let i=0;secs\.forEach\(\(s,k\)=>\{if\(s&&s\.getBoundingClientRect\(\)\.top<\d+\)i=k\}\);tocLinks\.forEach\(a=>a\.classList\.remove\('active'\)\);tocLinks\[i\]&&tocLinks\[i\]\.classList\.add\('active'\);\};\);")

js_new = """const tocLinks=[...document.querySelectorAll('.toc a')];
const secs=tocLinks.map(a=>document.querySelector(a.getAttribute('href'))).filter(Boolean);
function updateToc(){
  let i = -1;
  secs.forEach((s,k)=>{ if(s.getBoundingClientRect().top < 200) i = k; });
  if(i === -1 && secs.length > 0) i = 0;
  if(window.innerHeight + window.scrollY >= document.body.offsetHeight - 50) i = secs.length - 1;
  tocLinks.forEach(a=>a.classList.remove('active'));
  if(tocLinks[i]) tocLinks[i].classList.add('active');
}
window.addEventListener('scroll', updateToc, {passive: true});
updateToc();"""

for f in os.listdir('.'):
    if f.endswith('.html') and f != 'index.html':
        with open(f, 'r') as file:
            content = file.read()
        if pattern.search(content):
            content = pattern.sub(js_new, content)
            with open(f, 'w') as file:
                file.write(content)
            print(f"Patched {f}")
        else:
            print(f"Not found in {f}")

# Also check build_exam.py and lesson_lib.py
for f in ['build_exam.py', 'lesson_lib.py']:
    with open(f, 'r') as file:
        content = file.read()
    if pattern.search(content):
        content = pattern.sub(js_new, content)
        with open(f, 'w') as file:
            file.write(content)
        print(f"Patched {f}")
