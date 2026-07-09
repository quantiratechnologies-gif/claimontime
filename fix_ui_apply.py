import os
import re

# 1. Update src/index.html with app-container
with open('src/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Wrap sidebar and main in app-container if not already wrapped
if 'id="app-container"' not in html:
    html = html.replace('<!-- SIDEBAR (Hidden initially) -->', '<!-- APP CONTAINER (Hidden initially) -->\n<div class="app-container" id="app-container" style="display: none;">\n<!-- SIDEBAR -->')
    html = html.replace('</div> <!-- END MAIN -->', '</div> <!-- END MAIN -->\n</div> <!-- END APP CONTAINER -->')
    with open('src/index.html', 'w', encoding='utf-8') as f:
        f.write(html)

# 2. Update main.js display logic
with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace("document.getElementById('main-sidebar').style.display = 'block';", "")
js = js.replace("document.getElementById('main-content').style.display = 'block';", "document.getElementById('app-container').style.display = 'flex';")

js = js.replace("document.getElementById('main-sidebar').style.display = 'none';", "")
js = js.replace("document.getElementById('main-content').style.display = 'none';", "document.getElementById('app-container').style.display = 'none';")

with open('assets/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

# 3. Update sidebar.html
with open('components/layout/sidebar.html', 'r', encoding='utf-8') as f:
    sidebar = f.read()

sidebar = sidebar.replace('style="display: none;"', '') # Remove from sidebar div
sidebar = sidebar.replace('<a ', '<a class="app-nav-link" ') # Add app-nav-link
sidebar = sidebar.replace('class="active" class="app-nav-link"', 'class="app-nav-link active"') # Fix double class
sidebar = sidebar.replace('🏠', '<i data-lucide="home" class="icon-sm"></i>')
sidebar = sidebar.replace('📋', '<i data-lucide="clipboard-list" class="icon-sm"></i>')
sidebar = sidebar.replace('🛒', '<i data-lucide="shopping-cart" class="icon-sm"></i>')
sidebar = sidebar.replace('💳', '<i data-lucide="credit-card" class="icon-sm"></i>')
sidebar = sidebar.replace('🚪', '<i data-lucide="log-out" class="icon-sm"></i>')

with open('components/layout/sidebar.html', 'w', encoding='utf-8') as f:
    f.write(sidebar)

# 4. Update topbar.html
with open('components/layout/topbar.html', 'r', encoding='utf-8') as f:
    topbar = f.read()

# Add a user icon and style
if 'lucide' not in topbar:
    topbar = topbar.replace('Welcome, <strong>Rahul Sharma</strong>', '<i data-lucide="user-check" class="icon-sm" style="color:var(--primary-600)"></i> Welcome, <strong>Rahul Sharma</strong>')

with open('components/layout/topbar.html', 'w', encoding='utf-8') as f:
    f.write(topbar)

# 5. Fix remaining emojis in dashboard (🛒, 🏠)
with open('components/screens/screen-dashboard.html', 'r', encoding='utf-8') as f:
    dash = f.read()
dash = dash.replace('🏠', '<i data-lucide="home" class="icon-sm"></i>')
dash = dash.replace('🛒', '<i data-lucide="shopping-cart" class="icon-sm"></i>')
dash = dash.replace('🎯', '<i data-lucide="target" class="icon-sm"></i>')
with open('components/screens/screen-dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dash)

