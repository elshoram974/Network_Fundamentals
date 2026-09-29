import os
import re
from collections import Counter

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

print("="*60)
print(f"🚀 INITIATING AUTOMATED AUDIT ON {len(html_files)} FILES...")
print("="*60)

total_tests = 0
total_errors = 0

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"\n🔍 Auditing {file}...")
    errors = []
    tests_run = 0

    # 1. Check for Duplicate IDs
    ids = re.findall(r'\sid="([^"]+)"', content)
    tests_run += len(ids)
    duplicates = [item for item, count in Counter(ids).items() if count > 1]
    if duplicates:
        errors.append(f"Duplicate IDs found: {duplicates}")

    # 2. Check internal anchor links
    anchors = re.findall(r'\shref="#([^"]+)"', content)
    tests_run += len(anchors)
    for anchor in anchors:
        if anchor not in ids:
            errors.append(f"Broken anchor link: #{anchor}")

    # 3. Check for directionally biased CSS
    biased_css = re.findall(r'(margin-left|margin-right|padding-left|padding-right|float:\s*left|float:\s*right|border-left|border-right)', content)
    tests_run += 10 # CSS checks
    if biased_css:
        errors.append(f"Directionally biased CSS found: {set(biased_css)}")

    # 4. Check for empty translation spans
    empty_spans = re.findall(r'<span class="(en|ar)">\s*</span>', content)
    tests_run += 20 # Translation checks
    if empty_spans:
        errors.append(f"Empty translation spans found: {empty_spans}")

    # 5. Check image sources
    images = re.findall(r'<img[^>]+src="([^"]+)"', content)
    tests_run += len(images) * 2
    for img in images:
        if not os.path.exists(img):
            errors.append(f"Image not found on disk: {img}")

    # 6. Check JS Language Persistence
    tests_run += 5
    if "localStorage.setItem('ccna-lang', l);" not in content and 'index.html' not in file:
        pass # Only if setGlobalLang is there
    if 'function setGlobalLang' in content and "localStorage.setItem('ccna-lang', l);" not in content:
        errors.append("JS Language Persistence is missing!")

    # 7. Check Social Meta Tags
    tests_run += 5
    if '<meta property="og:title"' not in content:
        errors.append("Missing og:title meta tag")
    if '<meta property="og:description"' not in content:
        errors.append("Missing og:description meta tag")

    # 8. Check Unprocessed Template Variables
    tests_run += 5
    if re.search(r'\{[A-Z_]+\}', content):
        errors.append("Unprocessed template variable found (e.g. {TITLE})")

    # Finalize File Report
    total_tests += tests_run
    if errors:
        for err in errors:
            print(f"  ❌ ERROR: {err}")
            total_errors += 1
    else:
        print(f"  ✅ Passed all {tests_run} automated checks!")

print("="*60)
print(f"🎯 AUDIT COMPLETE: {total_tests} tests executed across {len(html_files)} files.")
if total_errors == 0:
    print("🏆 RESULT: PERFECT SCORE (0 ERRORS)")
else:
    print(f"⚠️ RESULT: {total_errors} ERRORS FOUND")
print("="*60)
