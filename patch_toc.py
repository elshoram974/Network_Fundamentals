import os

js_old = """const tocLinks=[...document.querySelectorAll('.toc a')];
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
    if f.endswith('.html'):
        with open(f, 'r') as file:
            content = file.read()
        if js_old in content:
            content = content.replace(js_old, js_new)
            with open(f, 'w') as file:
                file.write(content)
            print(f"Patched {f}")
        else:
            print(f"Not found in {f}")

# Also update lesson_lib.py
with open('lesson_lib.py', 'r') as file:
    content = file.read()
if js_old in content:
    content = content.replace(js_old, js_new)
    with open('lesson_lib.py', 'w') as file:
        file.write(content)
    print("Patched lesson_lib.py")

# Also update build_exam.py
with open('build_exam.py', 'r') as file:
    content = file.read()
if js_old in content:
    content = content.replace(js_old, js_new)
    with open('build_exam.py', 'w') as file:
        file.write(content)
    print("Patched build_exam.py")
