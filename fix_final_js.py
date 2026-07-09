import re

with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace(".querySelectorAll('.sidebar a')", ".querySelectorAll('.app-sidebar a')")
js = js.replace(".querySelectorAll('.app-nav-link')", ".querySelectorAll('.app-sidebar a')") # just in case

with open('assets/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

