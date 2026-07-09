with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix grid layout to be strictly 4 columns on desktop
css = css.replace('grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));', 'grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));')

# Fix flex layout issues for notifications if any
css = css.replace('.notification-item {\n  padding: var(--space-4);\n  border-bottom: 1px solid var(--border-color);\n  display: flex;\n  gap: var(--space-3);\n  align-items: flex-start;\n  background-color: var(--bg-surface);\n}', '.notification-item {\n  padding: var(--space-4);\n  border-bottom: 1px solid var(--border-color);\n  background-color: var(--bg-surface);\n}')

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
