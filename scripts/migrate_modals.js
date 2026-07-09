const fs = require('fs');
const path = require('path');

const modalsDir = path.join(__dirname, '../components/modals');
const files = fs.readdirSync(modalsDir);

files.forEach(file => {
    if (file.endsWith('.html')) {
        const filePath = path.join(modalsDir, file);
        let content = fs.readFileSync(filePath, 'utf8');

        // Modal structural classes
        content = content.replace(/class="modal-content"/g, 'class="antd-modal-content"');
        content = content.replace(/class="modal-header"/g, 'class="antd-modal-header"');
        
        // Forms
        content = content.replace(/class="form-control"/g, 'class="antd-input"');
        
        // Buttons: Order matters! Replace longest specific classes first.
        content = content.replace(/class="btn btn-secondary"/g, 'class="antd-btn"');
        content = content.replace(/class="btn btn-outline"/g, 'class="antd-btn"');
        content = content.replace(/class="btn"/g, 'class="antd-btn antd-btn-primary"');
        
        // Sometimes buttons have inline styles like `class="btn"` but single quotes `class='btn'`
        content = content.replace(/class='btn btn-secondary'/g, "class='antd-btn'");
        content = content.replace(/class='btn'/g, "class='antd-btn antd-btn-primary'");
        
        fs.writeFileSync(filePath, content);
        console.log(`Migrated ${file}`);
    }
});
