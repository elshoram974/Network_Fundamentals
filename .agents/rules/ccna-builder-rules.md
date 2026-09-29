# CCNA Lesson Builder Strict Rules

These rules apply whenever you are instructed to generate, update, or build CCNA HTML lessons from PDF sources in this workspace. 

## 1. Zero Omission Policy (100% Fidelity)
- **CRITICAL**: You MUST transcribe **everything** in the original PDF. Do NOT summarize, skip, or shorten any paragraph, list, table, CLI example, or Q&A. 
- We rely on these HTML pages for studying instead of the original PDFs. Any omitted content is a critical failure.
- Every piece of source content goes inside a `src()` block.
- For complex concepts, add an `extra()` block with an alternative explanation (analogy/real-world context), clearly marked so it's not confused with source material.

## 2. Academic & Editorial UI/UX (Anti-AI Look)
- **CRITICAL DESIGN RULE**: The design must NEVER look "AI generated" (no bubbly rounded cards, no heavy drop shadows, no generic purple/blue gradients).
- **Typography**: Use a Serif font (`Lora`) for all headings to give a textbook/academic feel, paired with `IBM Plex Sans` for body text. 
- **Layout & Spacing**: Maintain a narrow, optimal reading width (max 740px for content). Use generous line-height (`1.8`) and larger font sizes for high readability.
- **Components**: Use crisp borders (`border-radius: 4px`), flat colors, and tinted neutrals (e.g., cream/off-white for light mode, deep charcoal for dark mode) instead of stark white/black or standard grays.
- **Theming**: Every page MUST contain a **Dark/Light mode toggle** button in the topbar. User preferences for Theme and Language MUST be saved in `localStorage`.

## 3. Navigation & PDF Linking
- The topbar MUST include an "Index" link pointing back to `index.html` (the central table of contents).
- The footer MUST include a clear, clickable link to the original PDF file (e.g., `pdfs/01-introduction_to_the_osi_model.pdf`).
- The PDF link MUST use `target="_blank"` so it opens in a new tab for reference without closing the lesson.

## 4. Language Behavior (Bilingual)
- **English by default**: `<body class="lang-en">` and `<html lang="en" dir="ltr">`.
- Arabic is hidden by default and only toggled via the UI button, which triggers the `.lang-ar` class.
- Use `T('Term', 'شرح')` for technical terms so the Arabic explanation appears on hover/tap.
- Write natural, Egyptian-friendly Arabic for translations. Do not use stiff machine translation.

## 5. Development Workflow
- NEVER hand-roll HTML templates from scratch. Always use the provided `lesson_lib.py` functions (`build()`, `src()`, `bi()`, `extra()`, `img()`, `diagram()`, etc.) to guarantee that all lessons stay visually and behaviorally identical.
- Check and verify your Python scripts before execution to ensure there are no syntax errors.
