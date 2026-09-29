"""
Sync all lesson HTML files to use the exact same CSS and head-script from lesson_lib.py.
This ensures every lesson (01-07) looks identical.
"""
import os
import re
from lesson_lib import HEAD

# Extract the <style>...</style> block from HEAD
style_match = re.search(r'<style>.*?</style>', HEAD, flags=re.DOTALL)
CANONICAL_STYLE = style_match.group(0)

# Extract the <script>...</script> block that sits before </head>
head_script_match = re.search(r'(<script>.*?</script>)\s*</head>', HEAD, flags=re.DOTALL)
CANONICAL_HEAD_SCRIPT = head_script_match.group(1)


def sync_file(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        html = f.read()

    original = html

    # 1) Replace the <style> block with canonical one
    html = re.sub(r'<style>.*?</style>', CANONICAL_STYLE, html, count=1, flags=re.DOTALL)

    # 2) Ensure the head-level <script> block exists and is canonical.
    #    The head script sits between </style> and </head>.
    head_part, rest = html.split('</head>', 1)

    # Remove any existing <script> blocks in the <head>
    head_part_no_script = re.sub(r'<script>.*?</script>', '', head_part, flags=re.DOTALL).rstrip()

    # Re-inject canonical head script
    html = head_part_no_script + '\n' + CANONICAL_HEAD_SCRIPT + '\n</head>' + rest

    if html != original:
        with open(filepath, 'w', encoding='utf8') as f:
            f.write(html)
        print(f"  ✅ Synced: {os.path.basename(filepath)}")
    else:
        print(f"  ⏭️  Already synced: {os.path.basename(filepath)}")


print("Syncing all lesson files to lesson_lib.py canonical CSS + head script...\n")
for f in sorted(os.listdir('.')):
    if f.startswith('lesson-') and f.endswith('.html'):
        sync_file(f)

print("\nDone!")
