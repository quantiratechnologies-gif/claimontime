# Strategic Code Structuring Plan

The `index.html` file has grown into a massive monolith containing all screens, modals, and the sidebar. To structure this code properly and strategically while maintaining the ability to run it without complex build tools, I propose a **Component-Based File Architecture**.

## Proposed Changes

### 1. Component Architecture Setup
We will break the monolithic `index.html` into logical, reusable components.

**Proposed Directory Structure:**
```text
claim-on-time/
├── index.html           # The main entry shell
├── assets/
│   ├── css/
│   │   └── style.css    # Centralized stylesheet
│   └── js/
│       └── main.js      # Centralized logic
├── components/
│   ├── layout/          # Core structural elements
│   │   ├── sidebar.html
│   │   └── topbar.html
│   ├── screens/         # Individual page views
│   │   ├── dashboard.html
│   │   ├── policies.html
│   │   ├── claims.html
│   │   ├── cashless.html
│   │   └── ...
│   └── modals/          # All popups and dialogs
│       ├── emergency-modal.html
│       ├── cashless-request-modal.html
│       ├── upload-document-modal.html
│       └── ...
└── scripts/
    └── build.js         # A lightweight script to compile the components together
```

### 2. Assembly Strategy (To avoid `file://` CORS issues)
Because browsers block JavaScript `fetch()` from loading local files if you just double-click `index.html`, dynamically loading screens via JS won't work out-of-the-box for local testing.
Instead, we will use a **lightweight Node.js build script** (`scripts/build.js`). 
- We will define placeholder tags in the main `index.html` (e.g., `<!-- INCLUDE: components/screens/dashboard.html -->`).
- The build script will automatically stitch all the components together into a single `/dist/index.html` file.
- This gives you the best of both worlds: a highly organized, modular workspace for development, and a single, unified file for deployment/usage.

## User Review Required
> [!IMPORTANT]  
> Does this Component-Based Architecture align with your vision for "proper and strategic" structuring? 
> By splitting the files, it will be much easier to maintain, and the `build.js` script will ensure you can still run it anywhere without setting up a complex local server.
> 
> If you approve, I will immediately execute this restructuring.
