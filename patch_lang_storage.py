import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the setGlobalLang function and ensure it has localStorage.setItem('ccna-lang', l);
    if 'localStorage.setItem(\'ccna-lang\', l);' not in content:
        # We need to insert it right before the closing brace of setGlobalLang
        # First, let's find function setGlobalLang(l){ ... }
        # The easiest robust way is to just replace 'function setGlobalLang(l){' and then add it inside somewhere
        # But maybe it's better to just regex replace
        pattern = r'(function setGlobalLang\(l\)\{)'
        replacement = r"\1\n  localStorage.setItem('ccna-lang', l);"
        
        content = re.sub(pattern, replacement, content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Patched language storage in {file}")
