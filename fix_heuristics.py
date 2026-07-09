import os
import re

# 1. Update src/index.html with Toast Container
with open('src/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

if 'id="toast-container"' not in html:
    html = html.replace('</body>', '  <!-- TOAST CONTAINER -->\n  <div id="toast-container" class="toast-container"></div>\n</body>')
    with open('src/index.html', 'w', encoding='utf-8') as f:
        f.write(html)

# 2. Update style.css with Toast CSS
with open('assets/css/style.css', 'a', encoding='utf-8') as f:
    f.write('''
/* Toast Notifications */
.toast-container {
  position: fixed;
  bottom: var(--space-6);
  right: var(--space-6);
  z-index: 9999;
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}
.toast {
  background-color: var(--bg-surface);
  color: var(--text-main);
  padding: var(--space-3) var(--space-5);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-lg);
  border-left: 4px solid var(--primary-500);
  font-size: var(--text-sm);
  font-weight: 500;
  display: flex;
  align-items: center;
  justify-content: space-between;
  animation: slideInRight var(--transition-base);
  min-width: 250px;
}
.toast.success { border-left-color: var(--success-500); }
.toast.danger { border-left-color: var(--danger-500); }
.toast.fadeOut { opacity: 0; transform: translateX(100%); transition: all var(--transition-base); }
@keyframes slideInRight {
  from { transform: translateX(100%); opacity: 0; }
  to { transform: translateX(0); opacity: 1; }
}
''')

# 3. Update main.js with Toast Logic
with open('assets/js/main.js', 'a', encoding='utf-8') as f:
    f.write('''
// Toast Notification System
function showToast(message, type = 'success') {
  const container = document.getElementById('toast-container');
  if (!container) return;
  
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.innerHTML = `<span>${message}</span>`;
  
  container.appendChild(toast);
  
  setTimeout(() => {
    toast.classList.add('fadeOut');
    setTimeout(() => toast.remove(), 300);
  }, 3000);
}

// Override alert for the scope of these forms (optional, but finding exact replaces is better)
window.submitClaim = function() {
  showToast('Claim submitted successfully!', 'success');
  claimNext(1);
  closeModal('screen-new-claim');
}
''')

# 4. Process all HTML components
def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Replace alerts with toasts
    content = re.sub(r"alert\('([^']+)'\)", r"showToast('\1', 'success')", content)
    
    # Add form-control class to inputs and selects without it
    content = re.sub(r'<input([^>]*)>', lambda m: f'<input{m.group(1)}>' if 'class=' in m.group(1) else f'<input class="form-control"{m.group(1)}>', content)
    content = re.sub(r'<select([^>]*)>', lambda m: f'<select{m.group(1)}>' if 'class=' in m.group(1) else f'<select class="form-control"{m.group(1)}>', content)
    content = re.sub(r'<textarea([^>]*)>', lambda m: f'<textarea{m.group(1)}>' if 'class=' in m.group(1) else f'<textarea class="form-control"{m.group(1)}>', content)
    
    if original != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

for root, _, files in os.walk('components'):
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))

print("Heuristic fixes applied successfully.")
