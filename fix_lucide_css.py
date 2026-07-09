import re

# 1. Update src/index.html to include Lucide Script
with open('src/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

if 'lucide' not in html:
    html = html.replace('</head>', '  <!-- Lucide Icons -->\n  <script src="https://unpkg.com/lucide@latest"></script>\n</head>')
    with open('src/index.html', 'w', encoding='utf-8') as f:
        f.write(html)

# 2. Update style.css with Icon alignments and New Login Screen Layout
with open('assets/css/style.css', 'a', encoding='utf-8') as f:
    f.write('''
/* Lucide Icons */
.icon-sm { width: 18px; height: 18px; vertical-align: middle; margin-right: 4px; display: inline-block; }
.icon-lg { width: 48px; height: 48px; stroke-width: 1.5; color: var(--primary-500); margin-bottom: 10px; }
.btn .icon-sm { margin-right: 6px; }

/* Enhanced World-Class Login Screen */
.login-fullscreen {
  position: fixed; top: 0; left: 0; right: 0; bottom: 0;
  background-color: var(--bg-body);
  display: flex;
  z-index: 9999;
}
.login-image-side {
  flex: 1;
  background: url('https://images.unsplash.com/photo-1579684385127-1ef15d508118?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80') center/cover;
  position: relative;
  display: none;
}
@media (min-width: 900px) {
  .login-image-side { display: block; }
}
.login-image-overlay {
  position: absolute; top: 0; left: 0; right: 0; bottom: 0;
  background: linear-gradient(to right, rgba(26,86,219,0.7), rgba(26,86,219,0.9));
  display: flex; flex-direction: column; justify-content: center; padding: 4rem;
  color: white;
}
.login-image-overlay h1 { color: white; font-size: var(--text-3xl); margin-bottom: var(--space-4); }
.login-image-overlay p { font-size: var(--text-lg); opacity: 0.9; line-height: 1.6; max-width: 500px; }

.login-form-side {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: var(--space-8);
  background-color: var(--bg-surface);
}
.login-box {
  width: 100%; max-width: 420px;
}
.login-box h1 { margin-bottom: var(--space-2); color: var(--text-main); }
.login-box .subtitle { color: var(--text-muted); margin-bottom: var(--space-6); font-size: var(--text-sm); }

.account-type-selector, .login-method {
  display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-4);
}
.account-type-option, .login-method-btn {
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: var(--space-4);
  text-align: center;
  cursor: pointer;
  transition: all var(--transition-fast);
}
.account-type-option:hover, .login-method-btn:hover {
  border-color: var(--primary-500);
  background-color: var(--primary-50);
}
.account-type-option.selected, .login-method-btn.active {
  border-color: var(--primary-500);
  background-color: var(--primary-50);
  box-shadow: 0 0 0 1px var(--primary-500);
}
.account-type-option .icon-sm, .login-method-btn .icon-sm {
  width: 24px; height: 24px; margin-bottom: var(--space-2); color: var(--primary-600);
}
''')

# 3. Update main.js to initialize Lucide
with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()
if 'lucide.createIcons()' not in js:
    js = js.replace("document.addEventListener('DOMContentLoaded', () => {", "document.addEventListener('DOMContentLoaded', () => {\n    lucide.createIcons();")
    with open('assets/js/main.js', 'w', encoding='utf-8') as f:
        f.write(js)
