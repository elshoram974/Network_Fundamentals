# Shared builder for CCNA study lessons — keeps every lesson visually/behaviourally identical.
import re

def T(term, tip):
    return f'<span class="term">{term}<span class="tip">{tip}</span></span>'

def bi(en, ar):
    return f'<span class="en">{en}</span><span class="ar">{ar}</span>'

def bl(en, ar):
    return f'<div class="para-block"><div class="en">{en}</div><div class="ar">{ar}</div><button class="tr-btn" onclick="toggleParaLang(this)"></button></div>'

def h2(i, en, ar):
    return f'<section id="{i}"><h2>{bi(en, ar)}</h2>'

def src(inner):
    return f'<div class="src"><div class="src-label">{bi("SOURCE MATERIAL", "النص الأصلي من المرجع")}</div>{inner}</div>'

def extra(en, ar):
    """Yellow box — explicitly anything NOT in the source PDF: alt explanations, analogies, real-world/exam notes."""
    return f'<div class="extra"><div class="lab">{bi("AUTHOR NOTE", "ملاحظة إضافية للتوضيح")}</div>{bl(en, ar)}</div>'

def img(url, alt, cap_en, cap_ar, fb, alt2='', backup_diagram=''):
    a = f' data-alt="{alt2}"' if alt2 else ''
    bd = f'<div class="fb-diagram">{backup_diagram}</div>' if backup_diagram else ''
    return (f'<figure class="img-card"><img src="{url}"{a} alt="{alt}" loading="lazy" onerror="imgFail(this)">'
            f'<div class="img-fallback"><div class="fb-desc">🖼️ {fb}</div>{bd}</div>'
            f'<figcaption>{bi(cap_en, cap_ar)}</figcaption></figure>')

def cli(x):
    return f'<div class="cli">{x}</div>'

def diagram(inner, cap_en='', cap_ar=''):
    cap = f'<div class="cap">{bi(cap_en, cap_ar)}</div>' if cap_en else ''
    return f'<div class="diagram">{inner}{cap}</div>'

def osi_stack():
    layers = [(7,'Application','تطبيقات'),(6,'Presentation','تمثيل البيانات'),(5,'Session','الجلسة'),
              (4,'Transport','النقل'),(3,'Network','الشبكة'),(2,'Data Link','ربط البيانات'),(1,'Physical','فيزيائية')]
    rows = ''.join(f'<div class="layer L{n}"><span><span class="num">{n}</span>{en}</span><span>{ar}</span></div>' for n,en,ar in layers)
    return f'<div class="osi-stack">{rows}</div>'

def stack_h(items):
    colors = ['#e07be0','#6d8dff','#3ee6d6','#38d17a','#f5c451']
    segs = ''.join(f'<div class="seg" style="background:{colors[i%len(colors)]};flex:{flex}">{label}</div>' for i,(label,flex) in enumerate(items))
    return f'<div class="stack-h">{segs}</div>'

HEAD = '''<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Lesson {NUM} — {TITLE} | CCNA 200-301 Study</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&family=Tajawal:wght@400;500;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
/* Premium UI Theme */
:root {
  --bg: #ffffff;
  --panel: #ffffff;
  --panel2: #f8fafc;
  --line: #e2e8f0;
  --text: #0f172a;
  --muted: #64748b;
  --accent: #2563eb;
  --accent-hover: #1d4ed8;
  --accent2: #f59e0b;
  --warn: #eab308;
  --good: #10b981;
  --bad: #ef4444;
  --radius: 8px;
  --maxw: 740px;
  --font-head: 'Lora', 'Tajawal', serif;
  --font-body: 'IBM Plex Sans', 'Tajawal', sans-serif;
  --cli-bg: #f8fafc;
  --cli-text: #0f172a;
  --cli-border: #cbd5e1;
}
:root[data-theme="dark"] {
  --bg: #0f172a;
  --panel: #1e293b;
  --panel2: #0f172a;
  --line: #334155;
  --text: #f8fafc;
  --muted: #94a3b8;
  --accent: #3b82f6;
  --accent-hover: #60a5fa;
  --accent2: #fbbf24;
  --warn: #eab308;
  --good: #34d399;
  --bad: #f87171;
  --cli-bg: #020617;
  --cli-text: #cbd5e1;
  --cli-border: #1e293b;
}
*{box-sizing:border-box;min-width:0}
html{scroll-behavior:smooth;scroll-padding-top:75px}
body{margin:0;background:var(--bg);color:var(--text);font-family:var(--font-body);line-height:1.8;font-size:1.05rem;padding-bottom:100px;transition:background-color 0.2s, color 0.2s}
code,.mono{font-family:'IBM Plex Mono',monospace;font-size:0.9em;background:var(--panel2);padding:2px 6px;border-radius:3px;color:var(--accent2)}
img{max-width:100%;height:auto;display:block;margin:0 auto}
p,li,td,th{overflow-wrap:break-word;word-break:break-word;color:var(--text)}

body.lang-en .ar{display:none!important}
body.lang-ar .en{display:none!important}
body.lang-en .flip .en{display:none!important}
body.lang-en .flip .ar{display:block!important}
body.lang-ar .flip .ar{display:none!important}
body.lang-ar .flip .en{display:block!important}
.ar{direction:rtl;text-align:start}
span.ar{direction:rtl;unicode-bidi:isolate}
ul.ar,ol.ar{padding-inline-start:0;padding-inline-end:22px}

.topbar{position:sticky;top:0;z-index:50;background:rgba(255,255,255,0.85);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid var(--line);padding:16px 24px;display:flex;align-items:center;justify-content:space-between;gap:14px;flex-wrap:wrap;transition:background 0.2s}
:root[data-theme="dark"] .topbar{background:rgba(15,23,42,0.85)}
.brand{display:flex;align-items:center;gap:12px;font-family:var(--font-head);font-weight:600;font-size:1.15rem;letter-spacing:-0.01em}
.brand a{text-decoration:none;color:var(--text);border:1px solid var(--line);padding:4px 10px;border-radius:6px;font-size:0.9rem;font-family:var(--font-body);transition:all 0.2s}
.brand a:hover{background:var(--panel2);border-color:var(--muted)}
.lesson-tag{color:var(--muted);font-family:var(--font-body);font-size:0.9rem;text-transform:uppercase;letter-spacing:0.05em}

.progress-wrap{flex:1;min-width:120px;max-width:200px;height:4px;background:var(--line);overflow:hidden}
.progress-bar{height:100%;width:{PCT}%;background:var(--accent)}

.controls{display:flex;align-items:center;gap:16px}
.theme-btn{background:transparent;border:1px solid var(--line);border-radius:4px;padding:6px 12px;cursor:pointer;font-size:1rem;color:var(--text)}
.theme-btn:hover{background:var(--panel2)}
.langswitch{display:flex;border:1px solid var(--line);border-radius:4px;overflow:hidden}
.langswitch button{border:none;background:transparent;color:var(--muted);font-weight:600;padding:6px 16px;cursor:pointer;font-size:0.85rem;font-family:var(--font-body)}
.langswitch button.active{background:var(--panel2);color:var(--text)}

.shell{max-width:1080px;margin:40px auto 0;padding:0 24px;display:grid;grid-template-columns:1fr;gap:60px}
@media(min-width:1020px){.shell{grid-template-columns:220px minmax(0,var(--maxw))}.toc{display:block!important}}
.toc{display:none;position:sticky;top:100px;align-self:start;font-size:0.9rem;font-family:var(--font-body)}
.toc a{display:block;color:var(--muted);text-decoration:none;padding:8px 0;border-inline-start:2px solid transparent;padding-inline-start:16px;margin-bottom:4px;transition:0.1s}
.toc a:hover,.toc a.active{color:var(--text);border-inline-start-color:var(--accent)}
.toc-title{color:var(--text);font-weight:600;font-size:0.8rem;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:16px;padding-inline-start:16px}

.hero{padding:20px 0 40px;border-bottom:1px solid var(--line);margin-bottom:40px}
.hero h1{font-family:var(--font-head);font-size:2.8rem;line-height:1.2;margin:0 0 16px;letter-spacing:-0.02em}
.hero .sub{color:var(--muted);font-size:1.15rem;max-width:90%}
.chip{display:inline-flex;align-items:center;background:var(--panel2);padding:4px 12px;font-size:0.85rem;color:var(--text);margin-bottom:24px;font-family:var(--font-body);letter-spacing:0.02em}

main{min-width:0}
section{margin:60px 0;scroll-margin-top:75px}
h2{font-family:var(--font-head);font-size:1.8rem;margin-bottom:24px;color:var(--accent)}
h3{font-family:var(--font-head);font-size:1.3rem;margin:32px 0 16px}
p{margin:0 0 20px;max-width:70ch}
ul,ol{padding-inline-start:24px;margin:0 0 24px;max-width:70ch}
li{margin-bottom:10px}
.badge{display:inline-block;border:1px solid var(--line);color:var(--text);font-size:0.75rem;text-transform:uppercase;letter-spacing:0.05em;padding:4px 10px;margin-bottom:16px}

.para-block{margin-bottom:24px}
.tr-btn{display:inline-flex;align-items:center;margin-top:8px;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.05em;color:var(--accent);background:rgba(37,99,235,0.05);border:1px solid rgba(37,99,235,0.2);padding:6px 14px;border-radius:20px;cursor:pointer;font-weight:600;transition:all 0.2s;font-family:var(--font-body)}
.tr-btn:hover{background:var(--accent);color:#fff;border-color:var(--accent);transform:translateY(-1px)}

.term{border-bottom:1px dashed var(--accent);cursor:help;position:relative;color:var(--text);font-weight:600}
.term .tip{visibility:hidden;opacity:0;position:absolute;bottom:140%;inset-inline-start:0;background:var(--text);color:var(--bg);padding:8px 14px;font-size:0.9rem;z-index:20;transition:opacity .15s;font-family:var(--font-body);direction:rtl;text-align:start;width:max-content;max-width:min(280px,70vw);font-weight:400}
.term:hover .tip,.term.tap .tip{visibility:visible;opacity:1}

/* Editorial styling for source materials */
.src{margin:32px 0;padding:0 0 0 24px;border-inline-start:3px solid var(--accent);background:transparent}
.src-label{font-size:0.75rem;font-weight:600;color:var(--accent);text-transform:uppercase;letter-spacing:0.05em;margin-bottom:16px}

/* Distinct styling for extra notes */
.extra{margin:40px 0;padding:32px;background:var(--panel2);border-top:2px solid var(--warn)}
.extra .lab{color:var(--warn);font-weight:600;font-size:0.8rem;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:16px}

.cli{background:var(--cli-bg);color:var(--cli-text);border:1px solid var(--cli-border);border-radius:8px;padding:20px;overflow-x:auto;margin:24px 0;direction:ltr;text-align:start;white-space:pre;font-family:'IBM Plex Mono',monospace;font-size:0.9rem;line-height:1.6;box-shadow:inset 0 2px 4px rgba(0,0,0,0.02)}
.cli b{color:var(--accent)}

.table-wrap{overflow-x:auto;margin:32px 0}
table{width:100%;border-collapse:collapse;font-size:0.95rem;min-width:500px;text-align:start}
th,td{border-bottom:1px solid var(--line);padding:14px 16px;text-align:start}
th{font-weight:600;color:var(--muted);text-transform:uppercase;font-size:0.8rem;letter-spacing:0.05em}
.mono-cell{font-family:'IBM Plex Mono',monospace;direction:ltr;text-align:start}

.img-card{margin:40px 0}
.img-card img{border:1px solid var(--line);border-radius:4px}
.img-card figcaption{font-size:0.9rem;color:var(--muted);text-align:center;margin-top:16px;font-style:italic}
.img-fallback{display:none;padding:32px 24px;background:var(--panel2);border:1px solid var(--line);text-align:center}
.img-fallback .fb-desc{color:var(--muted);margin-bottom:16px}
.img-fallback .fb-diagram > div { background: var(--panel2); color: var(--text); padding: 20px; border-radius: 8px; font-family: 'IBM Plex Mono', monospace; overflow-x: auto; text-align: start; direction: ltr; }

.quiz-intro{color:var(--muted);font-size:0.95rem;margin-bottom:24px}
.q-card{background:var(--panel);border:1px solid var(--line);padding:32px;margin-bottom:24px;border-radius:12px;box-shadow:0 4px 6px -1px rgba(0,0,0,0.05),0 2px 4px -1px rgba(0,0,0,0.03);transition:all 0.2s}
.q-card:hover{box-shadow:0 10px 15px -3px rgba(0,0,0,0.05),0 4px 6px -2px rgba(0,0,0,0.03)}
.q-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:16px}
.q-num{color:var(--muted);font-size:0.85rem;text-transform:uppercase;letter-spacing:0.05em;font-weight:600}
.q-text{font-weight:500;margin-bottom:24px;font-size:1.15rem;font-family:var(--font-head)}
.q-card[data-lang=ar] .q-text,.q-card[data-lang=ar] .explain,.q-card[data-lang=ar] .opt span{direction:rtl;text-align:start}
.opt{display:flex;align-items:flex-start;gap:12px;padding:12px 16px;border:1px solid var(--line);margin-bottom:8px;cursor:pointer;border-radius:4px;transition:0.1s}
.opt:hover{border-color:var(--text)}
.opt input{margin-top:6px;accent-color:var(--accent)}
.opt.correct{border-color:var(--good);background:rgba(5,150,105,.05)}
.opt.wrong{border-color:var(--bad);background:rgba(220,38,38,.05)}
.opt.disabled{pointer-events:none;opacity:0.8}
.q-actions{display:flex;gap:12px;margin-top:24px}
.btn{background:var(--accent);color:#fff;border:none;padding:10px 20px;font-weight:600;cursor:pointer;font-size:0.95rem;border-radius:6px;font-family:var(--font-body);transition:all 0.2s;box-shadow:0 2px 4px rgba(37,99,235,0.2)}
.btn:hover{background:var(--accent-hover);transform:translateY(-1px);box-shadow:0 4px 6px rgba(37,99,235,0.3)}
.btn.secondary{background:transparent;border:1px solid var(--line);color:var(--text);box-shadow:none}
.btn.secondary:hover{background:var(--panel2);border-color:var(--muted);transform:translateY(0)}
.btn.tiny{padding:6px 12px;font-size:0.8rem;border-radius:4px}
.btn:disabled{opacity:0.3;cursor:not-allowed}
.explain{display:none;margin-top:24px;padding:20px;background:var(--panel2);border-inline-start:3px solid var(--accent);font-size:0.95rem}
.explain.show{display:block}
.q-result{font-size:0.95rem;font-weight:600;margin-top:16px}
.q-result.ok{color:var(--good)}.q-result.no{color:var(--bad)}

.lesson-nav{max-width:1080px;margin:80px auto 0;padding:32px 24px;display:flex;justify-content:space-between;border-top:1px solid var(--line);gap:24px}
.lesson-nav a{color:var(--text);text-decoration:none;border:1px solid var(--line);padding:20px;flex:1;display:flex;flex-direction:column;gap:8px;border-radius:var(--radius);transition:0.1s}
.lesson-nav a:hover{border-color:var(--text)}
.lesson-nav a .k{color:var(--muted);font-size:0.8rem;text-transform:uppercase;letter-spacing:0.05em}
.lesson-nav a strong{font-size:1.1rem;font-family:var(--font-head)}
.lesson-nav a.next{text-align:end;align-items:flex-end}

.source-footer{max-width:1080px;margin:0 auto 40px;padding:0 24px;color:var(--muted);font-size:0.85rem}
.source-footer a{color:var(--text);text-decoration:underline;text-underline-offset:4px}

/* CSS Diagrams Minimalist */
.diagram{border:1px solid var(--line);padding:32px;margin:32px 0}
.diagram .cap{text-align:center;color:var(--muted);font-size:0.85rem;margin-top:24px;font-style:italic}
.osi-stack{display:flex;flex-direction:column;gap:4px;max-width:400px;margin:0 auto}
.osi-stack .layer{display:flex;align-items:center;justify-content:space-between;padding:12px 20px;background:var(--panel2);font-weight:500;color:var(--text);border:1px solid var(--line)}
.osi-stack .layer span.num{opacity:0.5;font-size:0.85rem;margin-inline-end:12px}
.stack-h{display:flex;gap:4px;direction:ltr;flex-wrap:wrap}
.stack-h .seg{flex:1;min-width:100px;text-align:center;padding:16px 10px;background:var(--panel2);border:1px solid var(--line);color:var(--text);font-family:'IBM Plex Mono',monospace;font-size:0.85rem}
.ip32{display:flex;gap:4px;direction:ltr}
.ip32 .oct{flex:1;text-align:center;padding:16px 8px;background:var(--panel2);border:1px solid var(--line);font-family:'IBM Plex Mono',monospace}
.ip32 .lbl{font-size:0.75rem;opacity:0.7;display:block;margin-top:8px}
.bits-row{display:flex;direction:ltr;gap:4px;margin:12px 0;font-family:'IBM Plex Mono',monospace;font-size:0.85rem}
.bits-row .bit{flex:1;text-align:center;background:var(--panel2);border:1px solid var(--line);padding:8px 4px}
.class-bar{display:flex;direction:ltr;margin:12px 0;font-family:'IBM Plex Mono',monospace;font-size:0.85rem}
.class-bar div{padding:12px 8px;text-align:center;border:1px solid var(--line)}
.cb-net{background:var(--panel2);color:var(--text)}
.cb-host{background:transparent;color:var(--muted)}
.hdr-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:4px;direction:ltr}
.hdr-grid .f{background:var(--panel2);border:1px solid var(--line);padding:12px 8px;text-align:center;font-size:0.8rem;color:var(--text)}
.hdr-grid .f b{display:block;font-size:0.85rem;color:var(--text);margin-bottom:4px;font-family:'IBM Plex Mono',monospace}
.hdr-grid .span2{grid-column:span 2}.hdr-grid .span4{grid-column:span 4}
</style>
<script>
(function(){
  const savedTheme = localStorage.getItem('ccna-theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);
  const savedLang = localStorage.getItem('ccna-lang') || 'en';
  document.documentElement.lang = savedLang;
  document.documentElement.dir = savedLang === 'ar' ? 'rtl' : 'ltr';
  document.documentElement.classList.add('lang-'+savedLang);
})();
function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
  document.documentElement.setAttribute('data-theme', current);
  localStorage.setItem('ccna-theme', current);
}
</script>
</head>
<body class="lang-en">

<div class="topbar">
  <div class="brand">
    <a href="index.html"><span class="en">Index</span><span class="ar">الفهرس</span></a>
    <span class="lesson-title">{TITLE}</span>
  </div>
  <div class="controls">
    <button id="btnTheme" onclick="toggleTheme()" class="theme-btn" title="Toggle Light/Dark Mode">Theme</button>
    <div class="langswitch">
      <button id="btnEn" class="active" onclick="setGlobalLang('en')">EN</button>
      <button id="btnAr" onclick="setGlobalLang('ar')">AR</button>
    </div>
  </div>
</div>
'''

SCRIPT = '''
<script>
const UI = {
  en:{tr:'🌐 Translate to Arabic', trBack:'🌐 Show English', check:'Check answer', reveal:'Reveal answer', q:'Question', ok:'Correct', no:'Incorrect', qlang:'🌐 العربية'},
  ar:{tr:'🌐 ترجمة للعربية', trBack:'🌐 عرض الإنجليزية', check:'تحقق من الإجابة', reveal:'إظهار الإجابة', q:'سؤال', ok:'إجابة صحيحة', no:'إجابة خاطئة', qlang:'🌐 English'}
};
const curLang = () => document.body.classList.contains('lang-ar') ? 'ar' : 'en';
function arShown(pb){ return (curLang()==='ar') !== pb.classList.contains('flip'); }
function updBtn(pb){
  const b = pb.querySelector(':scope > .tr-btn'); if(!b) return;
  if(curLang()==='en') {
    b.textContent = arShown(pb) ? UI.en.trBack : UI.en.tr;
  } else {
    b.textContent = arShown(pb) ? UI.ar.trBack : UI.ar.tr;
  }
}
function toggleParaLang(btn){ const pb = btn.closest('.para-block'); pb.classList.toggle('flip'); updBtn(pb); }
function setGlobalLang(l){
  document.documentElement.dir = (l === 'ar') ? 'rtl' : 'ltr';
  document.body.classList.remove('lang-en', 'lang-ar');
  document.body.classList.add('lang-'+l);
  document.documentElement.lang = l;
  document.documentElement.classList.remove('lang-en', 'lang-ar');
  document.documentElement.classList.add('lang-'+l);
  document.getElementById('btnEn').classList.toggle('active', l==='en');
  document.getElementById('btnAr').classList.toggle('active', l==='ar');
  document.querySelectorAll('.para-block').forEach(pb=>{ pb.classList.remove('flip'); updBtn(pb); });
  document.querySelectorAll('.q-card').forEach(c=>applyQuizLang(c, l));
  localStorage.setItem('ccna-lang', l);
}

document.addEventListener("DOMContentLoaded", () => {
  const savedLang = localStorage.getItem('ccna-lang') || 'en';
  setGlobalLang(savedLang);
});

function imgFail(img){
  if(img.dataset.alt && !img.dataset.tried){ img.dataset.tried='1'; img.src=img.dataset.alt; return; }
  img.style.display='none';
  const f=img.parentElement.querySelector('.img-fallback'); if(f) f.style.display='block';
}
document.querySelectorAll('.para-block').forEach(updBtn);
document.querySelectorAll('.term').forEach(t=>t.addEventListener('click',e=>{e.stopPropagation();document.querySelectorAll('.term.tap').forEach(o=>{if(o!==t)o.classList.remove('tap')});t.classList.toggle('tap');}));
document.addEventListener('click',()=>document.querySelectorAll('.term.tap').forEach(o=>o.classList.remove('tap')));
const tocLinks=[...document.querySelectorAll('.toc a')], secs=tocLinks.map(a=>document.querySelector(a.getAttribute('href')));
window.addEventListener('scroll',()=>{let i=0;secs.forEach((s,k)=>{if(s&&s.getBoundingClientRect().top<150)i=k});tocLinks.forEach(a=>a.classList.remove('active'));tocLinks[i]&&tocLinks[i].classList.add('active');});

function applyQuizLang(card, l){
  const it=card._item, Tx=UI[l];
  card.dataset.lang=l;
  card.querySelector('.q-text').textContent=it.q[l];
  card.querySelectorAll('.opt span').forEach((s,i)=>s.textContent=it.opts[i][l]);
  card.querySelector('.explain').textContent=it.explain[l];
  card.querySelector('.q-num').textContent=Tx.q+' '+card._n+' / '+card._total;
  card.querySelector('.check').textContent=Tx.check;
  card.querySelector('.reveal').textContent=Tx.reveal;
  card.querySelector('.qlang').textContent=Tx.qlang;
  const r=card.querySelector('.q-result'); if(card._state) r.textContent = card._state==='ok'?Tx.ok:Tx.no;
}
function buildQuiz(id, items){
  const area=document.getElementById(id);
  if(!area) return;
  items.forEach((it,qi)=>{
    const card=document.createElement('div'); card.className='q-card'; card._item=it; card._n=qi+1; card._total=items.length;
    card.innerHTML=`<div class="q-top"><div class="q-num"></div><button class="btn secondary tiny qlang"></button></div>
      <div class="q-text"></div><div class="opts"></div>
      <div class="q-actions"><button class="btn check" disabled></button><button class="btn secondary reveal"></button></div>
      <div class="q-result"></div><div class="explain"></div>`;
    const ow=card.querySelector('.opts');
    it.opts.forEach((o,oi)=>{const lb=document.createElement('label');lb.className='opt';lb.innerHTML=`<input type="radio" name="${id}-${qi}" value="${oi}"><span></span>`;ow.appendChild(lb);});
    area.appendChild(card);
    applyQuizLang(card, curLang());
    card.querySelector('.qlang').onclick=()=>applyQuizLang(card, card.dataset.lang==='en'?'ar':'en');
    const chk=card.querySelector('.check'), rev=card.querySelector('.reveal'), ex=card.querySelector('.explain'), labs=card.querySelectorAll('.opt'), res=card.querySelector('.q-result');
    card.querySelectorAll('input').forEach(r=>r.onchange=()=>chk.disabled=false);
    chk.onclick=()=>{const c=card.querySelector('input:checked'); if(!c) return; const ci=+c.value;
      labs.forEach((l,i)=>{l.classList.add('disabled'); if(i===it.correct) l.classList.add('correct'); else if(i===ci) l.classList.add('wrong');});
      card._state = ci===it.correct?'ok':'no'; res.className='q-result '+card._state; res.textContent=UI[card.dataset.lang][card._state];
      ex.classList.add('show'); chk.disabled=true;};
    rev.onclick=()=>{labs.forEach((l,i)=>{l.classList.add('disabled'); if(i===it.correct) l.classList.add('correct');}); ex.classList.add('show');};
  });
}
</script>
'''

def Q(q, qa, opts, c, e, ea):
    o = ','.join('{en:%r,ar:%r}' % (a, b) for a, b in opts)
    return '{q:{en:%r,ar:%r},opts:[%s],correct:%d,explain:{en:%r,ar:%r}}' % (q, qa, o, c, e, ea)

def build(num, pct, title, sub, chip_en, chip_ar, toc_items, body_sections,
          prev_href, prev_label, next_href, next_label, source_pdf, extra_footnote, recap_items, quiz_items, out_path):
    head = HEAD.replace('{NUM}', str(num)).replace('{PCT}', str(pct)).replace('{TITLE}', str(title))
    hero = f'''<div class="hero"><div class="chip">{bi(chip_en, chip_ar)}</div>
<h1>{title}</h1><div class="sub">{bi(sub[0], sub[1])}</div></div>'''
    my_toc = [('recap', 'Recap Quiz', 'اختبار المراجعة')] + list(toc_items) + [('quiz', 'Lesson Quiz', 'اختبار الدرس')]
    toc = ''.join(f'<a href="#{i}">{bi(e,a)}</a>' for i,e,a in my_toc)
    recap_sec = f'<section id="recap"><span class="badge">{bi(f"Recap", "مراجعة سريعة")}</span><h2>{bi("Quick recap quiz","اختبار مراجعة سريع")}</h2><div id="recapArea"></div></section>'
    quiz_sec = f'<section id="quiz"><h2>{bi("Lesson quiz","اختبار الدرس")}</h2><p class="quiz-intro">{bi("Select an answer and check. You can toggle language for each question individually.","اختر إجابة وتحقق. يمكنك تبديل اللغة لكل سؤال على حدة.")}</p><div id="quizArea"></div></section>'
    shell = f'<div class="shell"><nav class="toc"><div class="toc-title">{bi("Contents","المحتويات")}</div>{toc}</nav><main>{hero}{recap_sec}{"".join(body_sections)}{quiz_sec}</main></div>'
    
    url_map = {
        "01-introduction_to_the_osi_model.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/introduction-to-the-osi-model",
        "02-ipv4.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/ipv4", 
        "03-ipv4-header.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/ipv4-packet-header",
        "04-arp.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/arp-address-resolution-protocol",
        "05-tcp-udp.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/introduction-to-tcp-and-udp",
        "06-tcp-header.pdf": "https://networklessons.com/cisco/ccna-routing-switching-icnd1/tcp-header",
        "07-tcp window size scaling.pdf": "https://networklessons.com/cisco/ccna-routing-switching/tcp-window-size-scaling",
        "08-icmp (internet control message protocol).pdf": "https://networklessons.com/ip-routing/icmp-internet-control-message-protocol",
    }
    real_url = url_map.get(source_pdf, "https://networklessons.com/cisco/ccna-200-301")
    
    foot = f'''<div class="lesson-nav">
<a class="prev" href="{prev_href}"><span class="k">{bi('Previous Lesson','الدرس السابق')}</span><strong>{prev_label}</strong></a>
<a class="next" href="{next_href}"><span class="k">{bi('Next Lesson','الدرس التالي')}</span><strong>{next_label}</strong></a>
</div>
<div class="source-footer">
    <div class="en">
      📝 <strong>Source Material:</strong> This lesson is officially sourced from <a href="{real_url}" target="_blank">NetworkLessons.com</a> (PDF: <a href="pdfs/{source_pdf}" target="_blank">{source_pdf}</a>). We transformed it into an interactive, bilingual format with extra simplified notes (yellow boxes) and realistic exam questions for an optimal learning experience!
    </div>
    <div class="ar">
      📝 <strong>المصدر الرسمي:</strong> هذا الدرس مأخوذ رسمياً من <a href="{real_url}" target="_blank">NetworkLessons.com</a> (ملف الـ PDF: <a href="pdfs/{source_pdf}" target="_blank">{source_pdf}</a>). لقد قمنا بتحويله إلى شكل تفاعلي ثنائي اللغة مع إضافة شروحات مبسطة (المربعات الصفراء) وأسئلة امتحانات حقيقية لتسهيل المذاكرة!
    </div>
</div>'''
    tail = SCRIPT + "<script>\nbuildQuiz('recapArea',[" + ','.join(recap_items) + "]);\nbuildQuiz('quizArea',[" + ','.join(quiz_items) + "]);\n</script>\n</body>\n</html>\n"
    out = head + shell + foot + tail
    with open(out_path, 'w', encoding='utf8') as f:
        f.write(out)
    return out
