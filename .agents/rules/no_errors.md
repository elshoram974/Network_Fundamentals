---
description: Ensure zero errors, strict validation, and bug-free output.
---

# Zero Errors Rule

1. **Strict Validation:** Before outputting any code, HTML, CSS, or script, mentally dry-run the syntax to ensure it is valid.
2. **No Placeholder Errors:** Never leave un-interpolated variables (like `{PCT}` or `{TITLE}`) in production files.
3. **Self-Correction:** If an error occurs, identify the root cause fully before applying a fix. Don't rely on band-aids.
4. **Cross-file Consistency:** Any change made to a template or a library must be carefully propagated to all dependent files without introducing syntax errors during the synchronization.
5. **Quality Assurance:** Treat every file modification as a production deployment. Ensure complete integrity of closing tags, brackets, and logical properties.
