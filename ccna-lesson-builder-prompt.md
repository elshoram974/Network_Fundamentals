# CCNA Lesson Builder — reusable prompt

Paste this whole file as your instructions whenever you hand me one or more new
CCNA PDF lessons, plus attach `lesson_lib.py` (the shared builder module) if it's not
already in the conversation. I should then build the lesson(s) end-to-end without
asking clarifying questions, following every rule below exactly.

## 1. What to build
For each PDF, produce one self-contained `lesson-NN-slug.html` study file (NN =
sequence number across the whole course, slug = short kebab-case topic name),
using the shared `lesson_lib.py` module (functions: `T`, `bi`, `bl`, `h2`, `src`,
`extra`, `img`, `cli`, `diagram`, `osi_stack`, `stack_h`, `Q`, `build`). Write a
`build_lNN.py` script per lesson that imports `lesson_lib` — do not hand-roll HTML
outside that system, so every lesson stays visually and behaviourally identical.

## 2. Content fidelity — nothing gets left out
- Transcribe **everything** in the PDF: every paragraph, list, table, CLI example,
  forum Q&A worth keeping. Nothing gets summarized away or skipped.
- Every piece of source content goes inside a `src()` block, labeled "From the
  source (PDF)".
- If something in the source is genuinely hard to follow as written, add a
  **separate, clearly marked `extra()` box** ("Extra explanation — not from the
  PDF, a different way to picture it") with an alternate explanation, analogy, or
  real-world comparison. Use 2–4 of these per lesson wherever a concept could use
  a second angle (a different analogy each time, not the same one reworded).
  These boxes must never be mistaken for source material — that's the whole
  point of the yellow styling and the label.
- Also use `extra()` for genuinely useful additions the source doesn't cover:
  exam tips, real-world habits, memory tricks. Keep them short and clearly
  optional.

## 3. Language behavior — English by default, everywhere
- The **entire file** — headings, body text, lists, tables, quiz questions,
  quiz options, quiz explanations, buttons, nav, footer — defaults to English.
  `<body class="lang-en">` and `<html lang="en" dir="ltr">`.
- **Nothing in Arabic is visible by default.** The only exception: term tooltips
  (see §4), which always show Arabic on hover/tap regardless of language mode —
  that's intentional so key vocabulary always keeps its Arabic gloss even while
  studying in English.
- A top-bar `EN / AR` toggle (`setGlobalLang`) flips **every** English/Arabic
  pair on the page at once (content + quiz + UI chrome), via `.en` / `.ar` classes
  and the `body.lang-en` / `body.lang-ar` CSS rules already defined in
  `lesson_lib.py`. Never add Arabic text that isn't wrapped in `.ar` (or inside a
  `bi()`/`bl()` pair) — anything not wrapped will leak through untranslated.
- Every paragraph written with `bl(en, ar)` gets its own translate button that
  flips just that paragraph, independent of the global toggle (`toggleParaLang`,
  already wired up).
- Every quiz question (built via `Q()` + `buildQuiz()`) gets its own 🌐 button
  that flips just that question, independent of the global toggle.
- Write real, natural Arabic (Egyptian-friendly, not overly formal, not a stiff
  literal translation) — never machine-translation-quality filler.
- Technical terms stay in English even inside Arabic text/translations — wrap
  them with `T(term, arabic_explanation)` so hovering always explains them,
  instead of translating the term itself.

## 4. Term tooltips
- Wrap key technical terms (protocol names, field names, jargon) with
  `T('Term', 'شرح أو ترجمة بالعربي')` the first time they appear in a section.
  Hovering (desktop) or tapping (mobile) shows the Arabic explanation — this
  already works via the `.term` / `.tip` CSS and the tap-to-toggle JS in
  `lesson_lib.py`. Don't over-wrap the same term five times in one paragraph —
  once per section is enough.

## 5. Images — reliability over decoration
Default to the **lightweight self-drawn CSS diagrams** already built into
`lesson_lib.py` (`diagram()`, `osi_stack()`, `stack_h()`, and the `.ip32`,
`.bits-row`, `.class-bar`, `.hdr-grid` CSS classes). These always render, cost
almost no tokens, and need no network access. Prefer them for anything that's
essentially a labeled box/flow diagram (layer stacks, header fields, address
structure, request/reply flows).

Only reach for a real `<img>` (via the `img()` helper, which already wires up
`onerror` → graceful fallback text) when:
- You actually found the URL **inside a search result's text**, or confirmed it
  independently in two different search results (never invent or guess a
  filename/path — guessed URLs mostly 404 and just show the fallback anyway,
  which wastes the attempt).
- The fallback (`img()`'s `fb` argument) always includes a short English+Arabic
  description of what the image would show, plus a suggested search phrase, so
  the reader can find it themselves if it fails to load.
- Never hand-draw an elaborate multi-shape SVG scene as a substitute — that
  burns a large amount of effort for something the cheap CSS diagrams already
  do just as clearly. Save real illustration effort only for cases the CSS
  diagram system genuinely can't express.

## 6. Quiz structure
- **Recap quiz** at the top of every lesson except the very first one in a
  course: 2–3 questions on the *previous* lesson only, badge-labeled "🔁 Recap
  — previous lesson: X". Lesson 1 gets a single placeholder question explaining
  there's nothing to recap yet.
- **Lesson quiz** at the bottom: 5–7 questions covering this lesson's content
  end to end (don't cluster them all on one sub-topic).
- Every question: 4 options, exactly one `correct` index, and an `explain`
  string that teaches the underlying reasoning (not just "because the PDF says
  so"). Both `en` and `ar` for the question, every option, and the explanation.
- Behavior (already wired up in `lesson_lib.py`'s `buildQuiz`): picking an
  answer and clicking "Check answer" colors the chosen option red if wrong,
  always colors the correct option green, and reveals the explanation.
  "Reveal correct answer" works at any time without requiring a guess first.

## 7. Structure & navigation
- Every lesson: sticky top bar (brand · progress bar · EN/AR toggle · lesson
  N/total) → sticky left-hand TOC on desktop (≥1020px) → hero (chip showing
  OSI-layer position + title + subtitle) → recap quiz → content sections →
  summary section → lesson quiz → prev/next nav → source footer.
- `build()`'s `pct` argument = lesson number / total lessons × 100, so the top
  progress bar always reflects real course position.
- `prev_href` / `next_href` must point to the real neighboring lesson filenames
  so the whole set stays one clickable chain — update the *previous* lesson's
  `next_href` too if you're inserting a new lesson in the middle of an existing
  sequence.
- Source footer always names the exact source PDF filename and repeats that
  yellow boxes are extra material, not exam-source facts.

## 8. Layout / responsiveness — must work on phone, tablet, and laptop
- Already handled by `lesson_lib.py`'s CSS (logical properties for RTL/LTR-safe
  spacing, `overflow-wrap`/`word-break` everywhere, horizontally-scrollable
  `.table-wrap` for wide tables, responsive TOC that only appears ≥1020px,
  `clamp()` sized headings). Don't override these with fixed pixel widths or
  non-logical `margin-left`/`padding-right` properties — always use
  `-inline-start` / `-inline-end` so it keeps working when the page flips to
  RTL for Arabic UI chrome.
- Keep tables inside `<div class="table-wrap">`, keep code inside `.cli`, and
  keep every new custom diagram inside `diagram()` so overflow behavior stays
  consistent.

## 9. Before presenting any file
Run these checks yourself and fix anything that fails — don't hand back a file
you haven't verified:
1. `python3 -c "import ast; ast.parse(open('build_lNN.py',encoding='utf8').read())"`
   — must succeed before running the builder.
2. After building, check opening/closing tag counts match for `section`, `div`,
   `table`, `ul`, `ol`, `tr`, `td` (a quick regex count is enough).
3. Extract the `<script>` block and run it through `new Function(...)` (e.g. via
   `node -e`) to confirm it's syntactically valid JS.
4. Confirm `<body class="lang-en">` and `<html lang="en" dir="ltr">` are present
   (English-by-default did not regress).
5. Copy the finished file to `/mnt/user-data/outputs/` and call `present_files`
   on it — every lesson gets handed back as an actual file, never pasted as raw
   HTML in the chat.

## 10. What to tell the user afterward
Keep the wrap-up short: what lesson this was, source PDF filename, and one line
per meaningfully new thing (not a repeat of this whole spec every time). If
something couldn't be verified (e.g. a real image URL is a best-effort guess),
say so plainly in one line rather than promising it will definitely work.
