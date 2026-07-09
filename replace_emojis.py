import os
import re

emoji_map = {
    '💰': '<i data-lucide="coins" class="icon-sm"></i>',
    '⚡': '<i data-lucide="zap" class="icon-sm"></i>',
    '🤖': '<i data-lucide="bot" class="icon-sm"></i>',
    '📁': '<i data-lucide="folder" class="icon-lg"></i>',
    '✓': '<i data-lucide="check" class="icon-sm"></i>',
    '⚠': '<i data-lucide="alert-triangle" class="icon-sm"></i>',
    '🚨': '<i data-lucide="alert-circle" class="icon-sm"></i>',
    '🏥': '<i data-lucide="hospital" class="icon-sm"></i>',
    '📅': '<i data-lucide="calendar" class="icon-sm"></i>',
    '🔍': '<i data-lucide="search" class="icon-sm"></i>',
    '🔔': '<i data-lucide="bell" class="icon-sm"></i>',
    '👤': '<i data-lucide="user" class="icon-sm"></i>',
    '💼': '<i data-lucide="briefcase" class="icon-sm"></i>',
    '🛡️': '<i data-lucide="shield" class="icon-sm"></i>',
    '📊': '<i data-lucide="bar-chart" class="icon-sm"></i>',
    '⚙️': '<i data-lucide="settings" class="icon-sm"></i>',
    '📞': '<i data-lucide="phone" class="icon-sm"></i>',
    '📄': '<i data-lucide="file-text" class="icon-sm"></i>',
    '❓': '<i data-lucide="help-circle" class="icon-sm"></i>',
    '🎫': '<i data-lucide="ticket" class="icon-sm"></i>',
    '📷': '<i data-lucide="camera" class="icon-sm"></i>',
    '🎤': '<i data-lucide="mic" class="icon-sm"></i>',
    '📍': '<i data-lucide="map-pin" class="icon-sm"></i>',
    '🚑': '<i data-lucide="activity" class="icon-sm"></i>',
    '📈': '<i data-lucide="trending-up" class="icon-sm"></i>',
    '📱': '<i data-lucide="smartphone" class="icon-sm"></i>',
    '🆔': '<i data-lucide="fingerprint" class="icon-sm"></i>',
    '📧': '<i data-lucide="mail" class="icon-sm"></i>',
    '🏢': '<i data-lucide="building" class="icon-sm"></i>',
    '💡': '<i data-lucide="lightbulb" class="icon-sm"></i>',
    '🔒': '<i data-lucide="lock" class="icon-sm"></i>',
    '←': '<i data-lucide="arrow-left" class="icon-sm"></i>',
    '→': '<i data-lucide="arrow-right" class="icon-sm"></i>',
}

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    for emoji, lucide in emoji_map.items():
        content = content.replace(emoji, lucide)
        
    if original != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

for root, _, files in os.walk('components'):
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))

print("Emojis replaced.")
