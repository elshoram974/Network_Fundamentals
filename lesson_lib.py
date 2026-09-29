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
    return f'<div class="src"><div class="src-label">{bi("From the source (PDF)", "من المرجع (PDF)")}</div>{inner}</div>'

def extra(en, ar):
    """Yellow box — explicitly anything NOT in the source PDF: alt explanations, analogies, real-world/exam notes."""
    return f'<div class="extra"><div class="lab">{bi("Extra explanation (not from the PDF — a different way to picture it)", "شرح إضافي (مش من المرجع — طريقة تانية تتخيل بيها الفكرة)")}</div>{bl(en, ar)}</div>'

def img(url, alt, cap_en, cap_ar, fb, alt2='', backup_diagram=''):
    """A real hot-linked <img> as the primary visual. If it 404s (checked via onerror,
    with one retry against `alt2` if given), the fallback shows BOTH a short description
    (`fb`, English/Arabic mixed line — keep it short) AND, if provided, `backup_diagram`
    (HTML from diagram()/osi_stack()/stack_h()/etc.) so a real visual still renders either way."""
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
    """items: list of (label, color-class-not-used, flex-css)"""
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
<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{{--bg:#0a121d;--panel:#101b29;--panel2:#0d1622;--line:#1e2f43;--text:#e9eef5;--muted:#8ea3bd;--accent:#3ee6d6;--accent2:#6d8dff;--warn:#f5c451;--good:#38d17a;--bad:#ef5a72;--radius:14px;--maxw:960px}}
*{{box-sizing:border-box;min-width:0}}
html{{scroll-behavior:smooth;scroll-padding-top:76px}}
body{{margin:0;background:var(--bg);color:var(--text);font-family:'IBM Plex Sans','Tajawal',sans-serif;line-height:1.85;padding-bottom:80px;overflow-x:hidden}}
code,.mono{{font-family:'IBM Plex Mono',monospace;overflow-wrap:anywhere}}
img{{max-width:100%;height:auto;display:block;margin:0 auto}}
p,li,td,th,h1,h2,h3{{overflow-wrap:break-word;word-break:break-word}}

body.lang-en .ar{{display:none!important}}
body.lang-ar .en{{display:none!important}}
body.lang-en .flip .en{{display:none!important}}
body.lang-en .flip .ar{{display:block!important}}
body.lang-ar .flip .ar{{display:none!important}}
body.lang-ar .flip .en{{display:block!important}}
.ar{{font-family:'Tajawal',sans-serif;direction:rtl;text-align:right}}
span.ar{{direction:rtl;unicode-bidi:isolate}}
ul.ar,ol.ar{{padding-inline-start:0;padding-inline-end:22px}}

.topbar{{position:sticky;top:0;z-index:50;background:rgba(10,18,29,.94);backdrop-filter:blur(8px);border-bottom:1px solid var(--line);padding:12px 20px;display:flex;align-items:center;justify-content:space-between;gap:14px;flex-wrap:wrap}}
.brand{{display:flex;align-items:center;gap:10px;font-weight:700;white-space:nowrap}}
.brand .dot{{width:10px;height:10px;border-radius:50%;background:var(--accent);box-shadow:0 0 10px var(--accent)}}
.lesson-tag{{color:var(--muted);font-size:.85rem}}
.progress-wrap{{flex:1;min-width:120px;max-width:280px;height:6px;background:var(--panel2);border-radius:99px;overflow:hidden;border:1px solid var(--line)}}
.progress-bar{{height:100%;width:{PCT}%;background:linear-gradient(90deg,var(--accent),var(--accent2))}}
.langswitch{{display:flex;background:var(--panel2);border:1px solid var(--line);border-radius:99px;padding:3px;gap:2px}}
.langswitch button{{border:none;background:transparent;color:var(--muted);font-weight:700;padding:6px 14px;border-radius:99px;cursor:pointer;font-size:.82rem}}
.langswitch button.active{{background:var(--accent);color:#04141a}}

.shell{{max-width:1180px;margin:0 auto;padding:0 20px;display:grid;grid-template-columns:1fr}}
@media(min-width:1020px){{.shell{{grid-template-columns:210px minmax(0,var(--maxw))}}.toc{{display:block!important}}}}
.toc{{display:none;position:sticky;top:78px;align-self:start;padding:28px 0;font-size:.85rem}}
.toc a{{display:block;color:var(--muted);text-decoration:none;padding:7px 0;border-inline-start:2px solid var(--line);padding-inline-start:12px;margin-bottom:2px}}
.toc a:hover,.toc a.active{{color:var(--accent);border-inline-start-color:var(--accent)}}
.toc-title{{color:var(--text);font-weight:700;font-size:.8rem;margin-bottom:10px;padding-inline-start:12px}}

.hero{{padding:34px 0 10px}}
.hero h1{{font-size:clamp(1.5rem,3vw,2.2rem);margin:0 0 4px;font-weight:700}}
.hero .sub{{color:var(--muted);margin-bottom:22px}}
.chip{{display:inline-flex;align-items:center;gap:8px;background:var(--panel);border:1px solid var(--line);padding:8px 14px;border-radius:99px;font-size:.85rem;color:var(--muted);margin-bottom:20px}}
.chip b{{color:var(--accent)}}
main{{min-width:0}}
section{{margin:44px 0;scroll-margin-top:76px}}
h2{{font-size:1.3rem;border-inline-start:4px solid var(--accent);padding-inline-start:12px;margin-bottom:14px}}
h3{{font-size:1.05rem;color:var(--accent2);margin:22px 0 10px}}
p{{margin:0 0 14px;color:#dbe4f0}}
ul,ol{{padding-inline-start:22px;margin:0 0 14px}}
li{{margin-bottom:8px;color:#dbe4f0}}
.badge{{display:inline-block;background:var(--panel2);color:var(--accent);font-size:.75rem;padding:3px 10px;border-radius:99px;margin-bottom:10px}}

.para-block{{margin-bottom:18px}}
.tr-btn{{display:inline-flex;margin-top:2px;font-size:.78rem;color:var(--accent2);background:transparent;border:1px solid var(--line);padding:4px 12px;border-radius:99px;cursor:pointer}}
.tr-btn:hover{{border-color:var(--accent2)}}

.term{{border-bottom:1.5px dotted var(--accent);cursor:help;position:relative;color:#fff;font-weight:600}}
.term .tip{{visibility:hidden;opacity:0;position:absolute;bottom:135%;left:0;background:#04141a;color:var(--accent);border:1px solid var(--accent);padding:8px 12px;border-radius:8px;font-size:.85rem;z-index:20;transition:opacity .15s;font-family:'Tajawal',sans-serif;direction:rtl;text-align:right;box-shadow:0 6px 20px rgba(0,0,0,.5);width:max-content;max-width:min(270px,70vw);font-weight:400}}
.term:hover .tip,.term.tap .tip{{visibility:visible;opacity:1}}

.src{{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);padding:22px 24px;margin:18px 0;overflow:hidden}}
.src-label{{font-size:.75rem;color:var(--muted);margin-bottom:10px}}
.src-label::before{{content:"📘 "}}
.extra{{background:linear-gradient(180deg,rgba(245,196,81,.08),rgba(245,196,81,.03));border:1px solid rgba(245,196,81,.4);border-radius:var(--radius);padding:18px 20px;margin:18px 0}}
.extra .lab{{color:var(--warn);font-weight:700;font-size:.85rem;margin-bottom:8px}}
.extra .lab::before{{content:"⚡ "}}
.extra p,.extra li{{color:#f0e3c0}}

.cli{{background:#050b12;border:1px solid var(--line);border-radius:10px;padding:14px 16px;overflow-x:auto;margin:14px 0;direction:ltr;text-align:left;white-space:pre;font-family:'IBM Plex Mono',monospace;font-size:.82rem;line-height:1.6}}
.cli b{{color:var(--accent)}}
.table-wrap{{overflow-x:auto;margin:14px 0}}
table{{width:100%;border-collapse:collapse;font-size:.88rem;min-width:460px}}
th,td{{border:1px solid var(--line);padding:9px 12px;text-align:start}}
th{{background:var(--panel2);color:var(--accent)}}
.mono-cell{{font-family:'IBM Plex Mono',monospace;direction:ltr;text-align:left}}

.img-card{{background:#050b12;border:1px solid var(--line);border-radius:12px;padding:14px;margin:16px 0}}
.img-card figcaption{{font-size:.8rem;color:var(--muted);text-align:center;margin-top:10px}}
.img-fallback{{display:none;padding:18px 14px;background:var(--panel2);border:1px dashed var(--line);border-radius:10px;color:#dbe4f0;font-size:.9rem}}
.img-fallback .fb-desc{{text-align:center;padding:0 4px 14px;color:#c7d4e6}}
.img-fallback .fb-diagram{{border-top:1px solid var(--line);padding-top:14px}}
.img-fallback .fb-diagram .diagram{{margin:0;border:none;background:transparent;padding:0}}

.quiz-intro{{color:var(--muted);font-size:.9rem;margin-bottom:18px}}
.q-card{{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);padding:20px 22px;margin-bottom:16px}}
.q-top{{display:flex;justify-content:space-between;align-items:center;gap:10px;margin-bottom:6px}}
.q-num{{color:var(--accent);font-size:.8rem;font-weight:700}}
.q-text{{font-weight:600;margin-bottom:14px;font-size:1.02rem}}
.q-card[data-lang=ar] .q-text,.q-card[data-lang=ar] .explain,.q-card[data-lang=ar] .opt span{{font-family:'Tajawal',sans-serif;direction:rtl;text-align:right}}
.opt{{display:flex;align-items:center;gap:10px;padding:10px 14px;border:1px solid var(--line);border-radius:8px;margin-bottom:8px;cursor:pointer;transition:.15s}}
.opt:hover{{border-color:var(--accent2)}}
.opt input{{accent-color:var(--accent)}}
.opt.correct{{border-color:var(--good);background:rgba(56,209,122,.1)}}
.opt.wrong{{border-color:var(--bad);background:rgba(239,90,114,.1)}}
.opt.disabled{{pointer-events:none;opacity:.9}}
.q-actions{{display:flex;gap:10px;margin-top:12px;flex-wrap:wrap}}
.btn{{background:var(--accent2);color:#04141a;border:none;padding:9px 18px;border-radius:8px;font-weight:700;cursor:pointer;font-size:.9rem}}
.btn.secondary{{background:transparent;border:1px solid var(--line);color:var(--muted)}}
.btn.tiny{{padding:5px 12px;font-size:.75rem}}
.btn:disabled{{opacity:.4;cursor:not-allowed}}
.explain{{display:none;margin-top:12px;padding:12px 14px;background:var(--panel2);border-radius:8px;border-inline-start:3px solid var(--accent);font-size:.9rem;color:#c7d4e6}}
.explain.show{{display:block}}
.q-result{{font-size:.85rem;font-weight:700;margin-top:8px}}
.q-result.ok{{color:var(--good)}}.q-result.no{{color:var(--bad)}}

.lesson-nav{{max-width:1180px;margin:50px auto 0;padding:20px;display:flex;justify-content:space-between;border-top:1px solid var(--line);gap:12px}}
.lesson-nav a{{color:var(--text);text-decoration:none;background:var(--panel);border:1px solid var(--line);padding:12px 18px;border-radius:10px;font-size:.9rem;display:flex;flex-direction:column;gap:2px;flex:1}}
.lesson-nav a .k{{color:var(--muted);font-size:.75rem}}
.lesson-nav a strong{{color:var(--accent)}}
.lesson-nav a.next{{text-align:right;align-items:flex-end}}
.source-footer{{max-width:1180px;margin:20px auto;padding:0 20px;color:var(--muted);font-size:.78rem;text-align:center}}

/* ===== reusable self-drawn diagrams (cheap CSS, always renders, no image download needed) ===== */
.diagram{{background:#050b12;border:1px solid var(--line);border-radius:12px;padding:20px;margin:16px 0}}
.diagram .cap{{text-align:center;color:var(--muted);font-size:.78rem;margin-top:10px}}
.osi-stack{{display:flex;flex-direction:column;gap:4px}}
.osi-stack .layer{{display:flex;align-items:center;justify-content:space-between;padding:10px 16px;border-radius:8px;font-weight:600;color:#04141a}}
.osi-stack .layer span.num{{opacity:.65;font-size:.8rem;margin-inline-end:8px}}
.L7{{background:#3ee6d6}}.L6{{background:#5fd1e6}}.L5{{background:#6dbaf0}}.L4{{background:#6d8dff}}.L3{{background:#8f7dfc}}.L2{{background:#b57bf0}}.L1{{background:#e07be0}}
.stack-h{{display:flex;gap:4px;direction:ltr;flex-wrap:wrap}}
.stack-h .seg{{flex:1;min-width:90px;text-align:center;padding:14px 8px;border-radius:8px;color:#04141a;font-family:'IBM Plex Mono',monospace;font-size:.82rem}}
.ip32{{display:flex;gap:4px;direction:ltr}}
.ip32 .oct{{flex:1;text-align:center;padding:14px 6px;border-radius:8px;font-family:'IBM Plex Mono',monospace}}
.ip32 .net{{background:#6d8dff;color:#04141a}}.ip32 .host{{background:#e07be0;color:#04141a}}
.ip32 .lbl{{font-size:.7rem;opacity:.85;display:block;margin-top:4px}}
.bits-row{{display:flex;direction:ltr;gap:2px;margin:8px 0;font-family:'IBM Plex Mono',monospace;font-size:.82rem}}
.bits-row .bit{{flex:1;text-align:center;background:var(--panel2);border:1px solid var(--line);padding:6px 2px;border-radius:4px}}
.class-bar{{display:flex;direction:ltr;border-radius:8px;overflow:hidden;margin:6px 0;font-family:'IBM Plex Mono',monospace;font-size:.78rem}}
.class-bar div{{padding:10px 4px;text-align:center;color:#04141a}}
.cb-net{{background:#6d8dff}}.cb-host{{background:#e07be0}}
.hdr-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:3px;direction:ltr}}
.hdr-grid .f{{background:var(--panel2);border:1px solid var(--line);padding:10px 6px;text-align:center;font-size:.72rem;border-radius:5px;color:#cfe3f7}}
.hdr-grid .f b{{display:block;font-size:.8rem;color:var(--accent);margin-bottom:2px;font-family:'IBM Plex Mono',monospace}}
.hdr-grid .span2{{grid-column:span 2}}.hdr-grid .span4{{grid-column:span 4}}
</style>
</head>
<body class="lang-en">

<div class="topbar">
  <div class="brand"><span class="dot"></span>
    <span class="en">CCNA 200-301 Study</span><span class="ar">مذاكرة CCNA 200-301</span>
    <span class="lesson-tag">— Network Fundamentals</span></div>
  <div class="progress-wrap"><div class="progress-bar"></div></div>
  <div class="langswitch">
    <button id="btnEn" class="active" onclick="setGlobalLang('en')">EN</button>
    <button id="btnAr" onclick="setGlobalLang('ar')">AR</button>
  </div>
  <div class="lesson-tag">{NUM} / 11</div>
</div>
'''

SCRIPT = '''
<script>
const UI = {
  en:{tr:'🌐 Translate to Arabic', trBack:'🌐 Show English', check:'Check answer', reveal:'Reveal correct answer', q:'Question', ok:'✔ Correct', no:'✘ Not quite — the correct answer is green', qlang:'🌐 العربية'},
  ar:{tr:'🌐 Translate to Arabic', trBack:'🌐 عرض بالإنجليزية', check:'تحقق من الإجابة', reveal:'إظهار الإجابة الصحيحة', q:'سؤال', ok:'✔ إجابة صحيحة', no:'✘ غير صحيحة — الصح باللون الأخضر', qlang:'🌐 English'}
};
const curLang = () => document.body.classList.contains('lang-ar') ? 'ar' : 'en';
function arShown(pb){ return (curLang()==='ar') !== pb.classList.contains('flip'); }
function updBtn(pb){
  const b = pb.querySelector(':scope > .tr-btn'); if(!b) return;
  b.textContent = arShown(pb) ? '🌐 Show English' : UI.en.tr;
  if(curLang()==='ar'){ b.textContent = arShown(pb) ? UI.ar.trBack : '🌐 Translate to Arabic'; }
}
function toggleParaLang(btn){ const pb = btn.closest('.para-block'); pb.classList.toggle('flip'); updBtn(pb); }
function setGlobalLang(l){
  document.body.classList.toggle('lang-ar', l==='ar');
  document.body.classList.toggle('lang-en', l==='en');
  document.documentElement.lang = l;
  document.getElementById('btnEn').classList.toggle('active', l==='en');
  document.getElementById('btnAr').classList.toggle('active', l==='ar');
  document.querySelectorAll('.para-block').forEach(pb=>{ pb.classList.remove('flip'); updBtn(pb); });
  document.querySelectorAll('.q-card').forEach(c=>applyQuizLang(c, l));
}
function imgFail(img){
  if(img.dataset.alt && !img.dataset.tried){ img.dataset.tried='1'; img.src=img.dataset.alt; return; }
  img.style.display='none';
  const f=img.parentElement.querySelector('.img-fallback'); if(f) f.style.display='block';
}
document.querySelectorAll('.para-block').forEach(updBtn);
document.querySelectorAll('.term').forEach(t=>t.addEventListener('click',e=>{e.stopPropagation();document.querySelectorAll('.term.tap').forEach(o=>{if(o!==t)o.classList.remove('tap')});t.classList.toggle('tap');}));
document.addEventListener('click',()=>document.querySelectorAll('.term.tap').forEach(o=>o.classList.remove('tap')));
const tocLinks=[...document.querySelectorAll('.toc a')], secs=tocLinks.map(a=>document.querySelector(a.getAttribute('href')));
window.addEventListener('scroll',()=>{let i=0;secs.forEach((s,k)=>{if(s&&s.getBoundingClientRect().top<120)i=k});tocLinks.forEach(a=>a.classList.remove('active'));tocLinks[i]&&tocLinks[i].classList.add('active');});

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
'''

def Q(q, qa, opts, c, e, ea):
    o = ','.join('{en:%r,ar:%r}' % (a, b) for a, b in opts)
    return '{q:{en:%r,ar:%r},opts:[%s],correct:%d,explain:{en:%r,ar:%r}}' % (q, qa, o, c, e, ea)

def build(num, pct, title, sub, chip_en, chip_ar, toc_items, body_sections,
          prev_href, prev_label, next_href, next_label, source_pdf, extra_footnote, recap_items, quiz_items, out_path):
    head = HEAD.format(NUM=num, PCT=pct, TITLE=title)
    hero = f'''<div class="hero"><div class="chip">📍 {bi(chip_en, chip_ar)}</div>
<h1>{title}</h1><div class="sub">{bi(sub[0], sub[1])}</div></div>'''
    toc = ''.join(f'<a href="#{i}">{bi(e,a)}</a>' for i,e,a in toc_items)
    recap_sec = f'<section id="recap"><span class="badge">{bi(f"🔁 Recap — previous lesson", "🔁 مراجعة — الدرس السابق")}</span><h2>{bi("Quick recap quiz","اختبار مراجعة سريع")}</h2><div id="recapArea"></div></section>'
    quiz_sec = f'<section id="quiz"><h2>{bi("🧠 Lesson quiz","🧠 اختبار الدرس")}</h2><p class="quiz-intro">{bi("Wrong = red, correct = green. Reveal the answer any time and translate any question with the 🌐 button.","غلط = أحمر، صح = أخضر. تقدر تشوف الإجابة في أي وقت وتترجم أي سؤال بزرار 🌐.")}</p><div id="quizArea"></div></section>'
    shell = f'<div class="shell"><nav class="toc"><div class="toc-title">{bi("On this page","في الصفحة")}</div>{toc}</nav><main>{hero}{recap_sec}{"".join(body_sections)}{quiz_sec}</main></div>'
    foot = f'''<div class="lesson-nav">
<a class="prev" href="{prev_href}"><span class="k">{bi('Previous','السابق')}</span><strong>{prev_label}</strong></a>
<a class="next" href="{next_href}"><span class="k">{bi('Next','التالي')}</span><strong>{next_label}</strong></a>
</div>
<div class="source-footer">Source: {source_pdf} — NetworkLessons.com (CCNA 200-301, Unit 2) · Yellow boxes = extra explanations outside the source, alternate ways to picture the idea, not for memorization as exam-source facts · {extra_footnote}</div>'''
    tail = SCRIPT + "\nbuildQuiz('recapArea',[" + ','.join(recap_items) + "]);\nbuildQuiz('quizArea',[" + ','.join(quiz_items) + "]);\n</script>\n</body>\n</html>\n"
    out = head + shell + foot + tail
    with open(out_path, 'w', encoding='utf8') as f:
        f.write(out)
    return out
