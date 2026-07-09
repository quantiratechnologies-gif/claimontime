# World-Class CSS Design System Implementation Plan

## Goal
To completely rewrite `assets/css/style.css` using a highly structured, scalable Custom CSS-Variable Design System. This will guarantee that every single component in the Health Claims Portal looks precisely crafted, matching the premium aesthetics of world-class platforms (like Apple, Stripe, and IBM Carbon).

## User Review Required
> [!IMPORTANT]
> This is my guarantee to you. I do not use random styling. Every single pixel, color, and animation will be governed by the strict mathematical rules defined below. 
> 
> Please review the design tokens and architecture below. If you approve, I will write the CSS exactly to this specification.

## 1. The Design Tokens (`:root`)
To guarantee consistency across every component, I will establish strict design tokens using CSS Custom Properties. Nothing will be hardcoded.

### Typography Scale (Precision Readability)
We will use **Inter** (the industry standard for clean UI) via Google Fonts. 
- `--font-sans`: 'Inter', system-ui, -apple-system, sans-serif
- `--text-xs`: 0.75rem (12px) - For badges and timestamps
- `--text-sm`: 0.875rem (14px) - For secondary text and table data
- `--text-base`: 1rem (16px) - For primary body text and inputs
- `--text-lg`: 1.125rem (18px) - For subheaders
- `--text-xl`: 1.25rem (20px) - For modal titles
- `--text-2xl`: 1.5rem (24px) - For main screen headers

### Color Palette (Trust & Action)
Colors will be defined using semantic names to ensure perfect contrast and consistency.
- **Surface & Backgrounds:**
  - `--bg-body`: `#F4F7F9` (Soft, cool gray for the main app background)
  - `--bg-surface`: `#FFFFFF` (Pure white for cards and modals)
  - `--bg-surface-hover`: `#F8FAFC`
- **Primary Brand (Trust):**
  - `--primary-main`: `#1A56DB` (Deep, trustworthy blue)
  - `--primary-hover`: `#1E429F`
  - `--primary-light`: `#E1EFFE` (For subtle backgrounds behind blue text)
- **Semantic Status (Action/Urgency):**
  - `--success-main`: `#057A55` (Approved claims)
  - `--success-bg`: `#DEF7EC`
  - `--danger-main`: `#E02424` (SOS / Rejected)
  - `--warning-main`: `#D03801` (Pending)
- **Typography:**
  - `--text-primary`: `#111928` (Near black for maximum readability)
  - `--text-secondary`: `#6B7280` (Muted gray for descriptions)

### Spacing System (The 4pt/8pt Grid)
Every margin and padding will follow a strict 8-pixel multiplier grid to guarantee perfect alignment.
- `--space-1`: 4px
- `--space-2`: 8px
- `--space-3`: 12px
- `--space-4`: 16px (Standard padding)
- `--space-6`: 24px (Large padding for modals)
- `--space-8`: 32px (Section spacing)

### Elevation & Depth (The Soft UI)
We will use layered, soft drop-shadows to create physical depth, exactly like Apple's HIG.
- `--shadow-sm`: `0 1px 2px 0 rgba(0, 0, 0, 0.05)` (For buttons)
- `--shadow-md`: `0 4px 6px -1px rgba(0, 0, 0, 0.1)` (For standard cards)
- `--shadow-lg`: `0 10px 15px -3px rgba(0, 0, 0, 0.1)` (For dropdowns)
- `--shadow-xl`: `0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 0 0 100vw rgba(0,0,0,0.5)` (For modals)
- `--radius-md`: `8px`
- `--radius-lg`: `12px`

## 2. Component Architecture
Once the tokens are set, I will apply them to the specific HTML components we built:

### Buttons (`.btn`, `.btn-secondary`)
- **Interaction:** All buttons will have a `--shadow-sm` that slightly lifts (`transform: translateY(-1px)`) and increases to `--shadow-md` on hover, governed by a `0.2s cubic-bezier(0.4, 0, 0.2, 1)` transition.
- **Padding:** Exactly `--space-2` vertically and `--space-4` horizontally.

### Cards & Tables (`.card`, `table`)
- **Borders:** Subtle `1px solid #E5E7EB` to define edges without heavy lines.
- **Hover States:** Cards will feature a very subtle background shift (`--bg-surface-hover`) when hovering over list items to provide interactivity.
- **Tables:** Headers will be capitalized, muted (`--text-secondary`), and small (`--text-xs`) to prioritize the actual data rows.

### Modals (`.modal`, `.modal-content`)
- **Backdrop:** A smooth, animated fade-in for the dark overlay.
- **Window:** The modal content will slide up slightly (`translateY(20px)` to `0`) and fade in. It will have `--radius-lg` and `--shadow-xl` to ensure it floats perfectly above the main UI.

## Verification Plan
1. Completely replace `assets/css/style.css` with this new system.
2. Run `scripts/build.js` to ensure the final output is intact.
3. Verify that the SOS button and urgent modals render beautifully and retain their immediate accessibility.
