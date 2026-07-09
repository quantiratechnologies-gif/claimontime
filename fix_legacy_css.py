css_append = '''
/* --------------------------------------------------------------------------
   LEGACY COMPONENT MAPPINGS
   (Mapping old HTML structural classes into the new Design System tokens)
   -------------------------------------------------------------------------- */
.insurance-card, .claim-card, .doc-card, .hospital-card, .market-card {
  background-color: var(--bg-surface);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-sm);
  padding: var(--space-5);
  margin-bottom: var(--space-4);
  border: 1px solid var(--border-color);
  transition: transform var(--transition-fast), box-shadow var(--transition-fast);
}
.insurance-card:hover, .claim-card:hover, .market-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.insurance-card h3, .claim-card h3, .market-card h3 {
  font-size: var(--text-lg);
  color: var(--text-main);
  margin-bottom: var(--space-2);
  margin-top: var(--space-2);
}

.insurance-card p, .claim-card p, .hospital-card p {
  font-size: var(--text-sm);
  color: var(--text-muted);
  line-height: 1.5;
  margin-bottom: var(--space-2);
}

.corp-tag, .price-tag {
  display: inline-block;
  padding: var(--space-1) var(--space-2);
  background-color: var(--warning-50);
  color: var(--warning-700);
  border-radius: var(--radius-sm);
  font-size: var(--text-xs);
  font-weight: 600;
  margin-bottom: var(--space-2);
  text-transform: uppercase;
}
.price-tag {
  background-color: var(--success-50);
  color: var(--success-700);
  font-size: var(--text-xl);
}

.insurance-logo {
  font-weight: 700;
  color: var(--primary-600);
  margin-bottom: var(--space-2);
  display: flex;
  align-items: center;
  gap: var(--space-2);
}

.coverage-bar {
  width: 100%;
  height: 8px;
  background-color: var(--border-color);
  border-radius: 4px;
  margin: var(--space-2) 0;
  overflow: hidden;
}
.coverage-fill {
  height: 100%;
  background-color: var(--primary-500);
  border-radius: 4px;
  transition: width 1s ease-in-out;
}

/* AI Chat Components */
.chat-container {
  background-color: var(--bg-surface);
  border-radius: var(--radius-lg);
  border: 1px solid var(--border-color);
  display: flex;
  flex-direction: column;
  height: 60vh;
}
.chat-messages {
  flex: 1;
  padding: var(--space-4);
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}
.chat-message {
  padding: var(--space-3) var(--space-4);
  border-radius: var(--radius-md);
  max-width: 80%;
  font-size: var(--text-sm);
  line-height: 1.5;
}
.user-message {
  align-self: flex-end;
  background-color: var(--primary-600);
  color: var(--text-inverse);
  border-bottom-right-radius: 0;
}
.bot-message {
  align-self: flex-start;
  background-color: var(--bg-body);
  color: var(--text-main);
  border-bottom-left-radius: 0;
}
.chat-input {
  display: flex;
  padding: var(--space-3);
  border-top: 1px solid var(--border-color);
  gap: var(--space-2);
}

/* Modals extra fixes */
.modal-overlay .modal-content {
  background-color: var(--bg-surface);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-xl);
  padding: var(--space-6);
  width: 90%;
  max-width: 600px;
  max-height: 90vh;
  overflow-y: auto;
}
.modal-overlay h2 {
  margin-top: 0;
  margin-bottom: var(--space-4);
  font-size: var(--text-xl);
  color: var(--text-main);
}
'''
with open('assets/css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_append)

# Also fix the missing emojis globally
import os
for root, _, files in os.walk('components/screens'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            content = content.replace('📋', '<i data-lucide="clipboard-list" class="icon-sm"></i>')
            content = content.replace('🛒', '<i data-lucide="shopping-cart" class="icon-sm"></i>')
            content = content.replace('💳', '<i data-lucide="credit-card" class="icon-sm"></i>')
            content = content.replace('🏥', '<i data-lucide="hospital" class="icon-sm"></i>')
            content = content.replace('📄', '<i data-lucide="file-text" class="icon-sm"></i>')
            content = content.replace('🤖', '<i data-lucide="bot" class="icon-sm"></i>')
            content = content.replace('🛡️', '<i data-lucide="shield" class="icon-sm"></i>')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
