with open('src/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('id="main-content" style="display: none;"', 'id="main-content"')

with open('src/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
