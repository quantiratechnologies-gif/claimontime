import os
import re

# 1. Update style.css to support legacy grid and stat-card using the new tokens
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '.grid-4' not in css:
    css_append = '''
/* App-Specific Layout Mappings to Design System */
.grid-4 { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: var(--space-4); }
.grid-2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: var(--space-4); }
.stat-card {
  background-color: var(--bg-surface);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-sm);
  border: 1px solid var(--border-color);
  padding: var(--space-4);
  transition: transform var(--transition-fast), box-shadow var(--transition-fast);
}
.stat-card:hover { transform: translateY(-2px); box-shadow: var(--shadow-md); }
.stat-card h3 { font-size: var(--text-sm); color: var(--text-muted); margin-bottom: var(--space-2); font-weight: 500; }
.stat-card .value { font-size: var(--text-2xl); font-weight: 700; color: var(--text-main); margin-bottom: var(--space-1); }
.stat-card .change { font-size: var(--text-xs); color: var(--text-muted); }
.stat-card .change.positive { color: var(--success-700); font-weight: 500; }
.stat-card .change.negative { color: var(--danger-700); font-weight: 500; }

.alert {
  padding: var(--space-3) var(--space-4);
  border-radius: var(--radius-md);
  margin-bottom: var(--space-4);
  font-size: var(--text-sm);
  border: 1px solid transparent;
}
.alert-success { background-color: var(--success-50); border-color: var(--success-500); color: var(--success-700); }
.alert-warning { background-color: var(--warning-50); border-color: var(--warning-500); color: var(--warning-700); }
.alert-info { background-color: var(--primary-50); border-color: var(--primary-500); color: var(--primary-700); }
.alert-danger { background-color: var(--danger-50); border-color: var(--danger-500); color: var(--danger-700); }
'''
    with open('assets/css/style.css', 'a', encoding='utf-8') as f:
        f.write(css_append)


# 2. Update all HTML files to map old classes to new Design System classes
def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Map badges
    content = content.replace('badge-green', 'badge-success')
    content = content.replace('badge-yellow', 'badge-warning')
    content = content.replace('badge-red', 'badge-danger')
    content = content.replace('badge-blue', 'badge-primary')
    
    # Map tables
    content = re.sub(r'<table([^>]*)>', lambda m: f'<table{m.group(1)}>' if 'class="table"' in m.group(1) else f'<table class="table"{m.group(1)}>', content)
    
    if original != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            print(f"Applied design system to: {filepath}")

for root, _, files in os.walk('components'):
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))

