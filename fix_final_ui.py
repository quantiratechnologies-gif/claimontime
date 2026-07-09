import re

# 1. Fix duplicate classes in sidebar.html
with open('components/layout/sidebar.html', 'r', encoding='utf-8') as f:
    sidebar = f.read()

sidebar = sidebar.replace('class="app-sidebar" id="main-sidebar" class="app-sidebar"', 'class="app-sidebar" id="main-sidebar"')
sidebar = sidebar.replace('class="app-nav-link" class="active"', 'class="app-nav-link active"')
sidebar = sidebar.replace('class="app-nav-link" class="app-nav-link active"', 'class="app-nav-link active"')
sidebar = sidebar.replace('class="app-nav-link"  class="app-nav-link"', 'class="app-nav-link"')

with open('components/layout/sidebar.html', 'w', encoding='utf-8') as f:
    f.write(sidebar)

# 2. Fix JS modal logic
with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace("modal.style.display = 'flex';", "modal.classList.add('active');")
js = js.replace("modal.style.display = 'none';", "modal.classList.remove('active');")

with open('assets/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

# 3. Add background color to .btn in style.css
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if 'background-color: var(--primary-600);' not in css.split('.btn {')[1].split('}')[0]:
    css = css.replace('.btn {\n', '.btn {\n  background-color: var(--primary-600);\n  color: var(--text-inverse);\n')

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

