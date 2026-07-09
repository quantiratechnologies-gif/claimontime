const fs = require('fs');
const path = require('path');

const screensDir = path.join(__dirname, '../components/screens');
const files = fs.readdirSync(screensDir);

files.forEach(file => {
    if (file.endsWith('.html')) {
        const filePath = path.join(screensDir, file);
        let content = fs.readFileSync(filePath, 'utf8');

        // Replace form-control with antd-input
        content = content.replace(/class="form-control/g, 'class="antd-input');
        
        // Remove redundant inline styles that conflict with antd-input
        content = content.replace(/style="width: 100%; padding: 8px; border: 1px solid var\(--antd-border\); border-radius: var\(--antd-radius-sm\);"/g, '');
        content = content.replace(/style="width: 100%; padding: 8px; border: 1px solid var\(--antd-border\); border-radius: var\(--antd-radius-sm\);"/g, '');
        
        // Fix any rogue .btn classes that aren't antd-btn
        // Find class="btn btn-primary" -> class="antd-btn antd-btn-primary"
        content = content.replace(/class="btn btn-primary"/g, 'class="antd-btn antd-btn-primary"');
        content = content.replace(/class="btn btn-secondary"/g, 'class="antd-btn"');
        
        // Edge case: class="btn" where it's not already antd-btn
        content = content.replace(/class="btn"/g, 'class="antd-btn antd-btn-primary"');
        
        // We might have double antd-btn if it was already antd-btn btn
        content = content.replace(/class="antd-btn antd-btn-primary antd-btn-primary"/g, 'class="antd-btn antd-btn-primary"');
        content = content.replace(/class="antd-btn antd-btn antd-btn-primary"/g, 'class="antd-btn antd-btn-primary"');
        content = content.replace(/class="antd-btn antd-btn"/g, 'class="antd-btn"');

        fs.writeFileSync(filePath, content);
        console.log(`Migrated ${file}`);
    }
});
