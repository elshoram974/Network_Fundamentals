import os

replacements = {
    "html.lang-en": "html.lang-en",
    "html.lang-ar": "html.lang-ar",
    "document.documentElement.classList.toggle('lang-ar'": "document.documentElement.classList.toggle('lang-ar'",
    "document.documentElement.classList.toggle('lang-en'": "document.documentElement.classList.toggle('lang-en'",
    "document.documentElement.classList.contains('lang-ar')": "document.documentElement.classList.contains('lang-ar')",
    "document.documentElement.classList.add('lang-'+l)": "document.documentElement.classList.add('lang-'+l)",
    "document.documentElement.classList.remove('lang-en', 'lang-ar')": "document.documentElement.classList.remove('lang-en', 'lang-ar')"
}

for f in os.listdir('.'):
    if f.endswith('.html') or f.endswith('.py'):
        with open(f, 'r') as file:
            content = file.read()
        
        patched = False
        for old, new in replacements.items():
            if old in content:
                content = content.replace(old, new)
                patched = True
                
        if patched:
            with open(f, 'w') as file:
                file.write(content)
            print(f"Patched {f}")
