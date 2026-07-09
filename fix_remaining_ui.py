css_append = '''
/* --------------------------------------------------------------------------
   FINAL COMPONENT MAPPINGS (Fixing the 27 Missing UI Classes)
   -------------------------------------------------------------------------- */

/* Tab Navigation System */
.tab-container {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
  margin-top: var(--space-4);
}
.tab-buttons {
  display: flex;
  gap: var(--space-2);
  border-bottom: 1px solid var(--border-color);
  padding-bottom: var(--space-2);
  overflow-x: auto;
}
.tab-btn {
  background: transparent;
  border: none;
  padding: var(--space-2) var(--space-4);
  font-size: var(--text-sm);
  font-weight: 500;
  color: var(--text-muted);
  cursor: pointer;
  border-bottom: 2px solid transparent;
  transition: all var(--transition-fast);
}
.tab-btn:hover {
  color: var(--primary-600);
}
.tab-btn.active {
  color: var(--primary-600);
  border-bottom-color: var(--primary-600);
}
.tab-content {
  display: none;
}
.tab-content.active {
  display: block;
  animation: fadeIn var(--transition-fast);
}

/* Accordions / FAQs */
.accordion {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}
.accordion-header {
  background-color: var(--bg-surface);
  padding: var(--space-4);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  cursor: pointer;
  font-weight: 600;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.accordion-content {
  display: none;
  padding: var(--space-4);
  background-color: var(--bg-surface-hover);
  border: 1px solid var(--border-color);
  border-top: none;
  border-bottom-left-radius: var(--radius-md);
  border-bottom-right-radius: var(--radius-md);
}

/* Stepper / Progress (New Claim Wizard) */
.stepper {
  display: flex;
  justify-content: space-between;
  margin-bottom: var(--space-6);
  position: relative;
}
.stepper::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  height: 2px;
  background-color: var(--border-color);
  z-index: 0;
}
.stepper .step {
  background-color: var(--bg-surface);
  border: 2px solid var(--border-color);
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  z-index: 1;
  color: var(--text-muted);
}
.stepper .step.active {
  border-color: var(--primary-500);
  background-color: var(--primary-500);
  color: var(--text-inverse);
}
.progress-fill {
  background-color: var(--success-500);
  height: 100%;
  transition: width 0.3s;
}

/* Notifications */
.notification-item {
  padding: var(--space-4);
  border-bottom: 1px solid var(--border-color);
  display: flex;
  gap: var(--space-3);
  align-items: flex-start;
  background-color: var(--bg-surface);
}
.notification-item.unread {
  background-color: var(--primary-50);
  border-left: 4px solid var(--primary-500);
}

/* Corporate specific */
.badge-corp {
  background-color: #1a2b4a;
  color: #ffd700;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 10px;
  font-weight: 800;
  margin-left: 6px;
}
.btn-corp {
  background: linear-gradient(135deg, #1a2b4a, #2d3e5f);
  color: #ffd700;
  border: none;
}
.btn-corp:hover {
  background: linear-gradient(135deg, #2d3e5f, #1a2b4a);
}
.card-highlight {
  border: 2px solid #ffd700;
  background-color: #fff9e6;
}

/* Insurance Brands (Text Colors) */
.star-health { color: #e11d48; }
.hdfc { color: #dc2626; }
.aditya { color: #b91c1c; }
.care { color: #2563eb; }
.maxbupa { color: #059669; }

/* File Upload Area */
.file-upload-area {
  border: 2px dashed var(--border-color);
  border-radius: var(--radius-lg);
  padding: var(--space-8);
  text-align: center;
  background-color: var(--bg-surface-hover);
  cursor: pointer;
  transition: all var(--transition-fast);
}
.file-upload-area:hover {
  border-color: var(--primary-500);
  background-color: var(--primary-50);
}

/* Login specific layout */
.login-form {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}
.otp-input-group {
  display: flex;
  gap: var(--space-2);
  justify-content: center;
}
.otp-input-group input {
  width: 45px;
  height: 50px;
  text-align: center;
  font-size: var(--text-2xl);
  font-weight: bold;
}

/* Misc / AI Chat mapping */
.chat-box {
  background-color: var(--bg-surface);
  border-radius: var(--radius-lg);
  border: 1px solid var(--border-color);
  display: flex;
  flex-direction: column;
  height: 60vh;
}
.msg {
  padding: var(--space-3) var(--space-4);
  border-radius: var(--radius-md);
  max-width: 80%;
  font-size: var(--text-sm);
  line-height: 1.5;
  align-self: flex-end;
  background-color: var(--primary-600);
  color: var(--text-inverse);
  border-bottom-right-radius: 0;
}
.msg-ai {
  align-self: flex-start;
  background-color: var(--bg-body);
  color: var(--text-main);
  border-bottom-left-radius: 0;
  border-bottom-right-radius: var(--radius-md);
}
.urgent {
  color: var(--danger-600);
  font-weight: bold;
}
'''
with open('assets/css/style.css', 'a', encoding='utf-8') as f:
    f.write(css_append)

# Update HTML cache buster to v4.0 to force Vercel to download this final fix
with open('src/index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('?v=3.0', '?v=4.0')
with open('src/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

