import os
import re

for filename in sorted(os.listdir('.')):
    if filename.startswith('lesson-') and filename.endswith('.html'):
        num_str = re.search(r'lesson-(\d+)', filename)
        if not num_str:
            continue
        num = int(num_str.group(1))
        pct = round((num / 11) * 100)
        
        with open(filename, 'r', encoding='utf8') as f:
            content = f.read()
        
        # Replace {PCT} in the style block with the correct percentage
        # Also handle if it was mistakenly replaced with another number that we want to unify
        content = re.sub(r'\.progress-bar\{height:100%;width:(?:\{PCT\}|\d+)%;', f'.progress-bar{{height:100%;width:{pct}%;', content)
        
        with open(filename, 'w', encoding='utf8') as f:
            f.write(content)
        print(f"Fixed {filename} with pct={pct}")
