import os
for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r') as file:
            content = file.read()
        content = content.replace(r"\'ccna-lang\'", "'ccna-lang'")
        with open(f, 'w') as file:
            file.write(content)
