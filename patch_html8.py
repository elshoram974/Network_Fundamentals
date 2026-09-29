import os
import re
from lesson_lib import HEAD

# Extract the script block from HEAD
head_script_match = re.search(r'(<script>.*?</script>)\s*</head>', HEAD, flags=re.DOTALL)
head_script = head_script_match.group(1)

def patch_file(filename):
    with open(filename, 'r', encoding='utf8') as f:
        html = f.read()
    
    # Check if script is missing
    head_content = html.split('</head>')[0]
    if 'function toggleTheme()' not in head_content:
        html = html.replace('</head>', head_script + '\n</head>')
        with open(filename, 'w', encoding='utf8') as f:
            f.write(html)
        print(f"Patched {filename}")
    else:
        print(f"Already has toggleTheme in {filename}")

for f in os.listdir('.'):
    if f.startswith('lesson-0') and f.endswith('.html'):
        patch_file(f)
