with open('src/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('href="assets/css/style.css"', 'href="assets/css/style.css?v=2.0"')
html = html.replace('src="assets/js/main.js"', 'src="assets/js/main.js?v=2.0"')

with open('src/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
