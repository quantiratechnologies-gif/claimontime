import os
import re

# 1. Parse all defined CSS classes
css_classes = set()
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()
    # Find all classes like .btn, .card, etc.
    matches = re.findall(r'\.([a-zA-Z0-9_-]+)[\s{,:]', css_content)
    css_classes.update(matches)

# 2. Parse all used HTML classes
html_classes = set()
for root, _, files in os.walk('components'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                matches = re.findall(r'class="([^"]+)"', content)
                for match in matches:
                    classes = match.split()
                    html_classes.update(classes)

# 3. Find missing classes
missing = html_classes - css_classes

# 4. Filter out some common non-css things or things handled dynamically
ignore = {'hidden', 'active', 'icon-sm', 'icon-lg', 'lucide'}
missing = missing - ignore

print(f"Total HTML Classes Used: {len(html_classes)}")
print(f"Total CSS Classes Defined: {len(css_classes)}")
print(f"Missing Classes ({len(missing)}):")
for m in sorted(missing):
    print(f" - {m}")

