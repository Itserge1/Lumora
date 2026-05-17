---
name: Luminous Intelligence
colors:
  surface: '#111418'
  surface-dim: '#111418'
  surface-bright: '#36393e'
  surface-container-lowest: '#0b0e12'
  surface-container-low: '#191c20'
  surface-container: '#1d2024'
  surface-container-high: '#272a2f'
  surface-container-highest: '#32353a'
  on-surface: '#e1e2e8'
  on-surface-variant: '#bacac5'
  inverse-surface: '#e1e2e8'
  inverse-on-surface: '#2e3135'
  outline: '#859490'
  outline-variant: '#3c4a46'
  surface-tint: '#3cddc7'
  primary: '#57f1db'
  on-primary: '#003731'
  primary-container: '#2dd4bf'
  on-primary-container: '#00574d'
  inverse-primary: '#006b5f'
  secondary: '#c0c1ff'
  on-secondary: '#1000a9'
  secondary-container: '#3131c0'
  on-secondary-container: '#b0b2ff'
  tertiary: '#eacfff'
  on-tertiary: '#490080'
  tertiary-container: '#d7acff'
  on-tertiary-container: '#7003bf'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#62fae3'
  primary-fixed-dim: '#3cddc7'
  on-primary-fixed: '#00201c'
  on-primary-fixed-variant: '#005047'
  secondary-fixed: '#e1e0ff'
  secondary-fixed-dim: '#c0c1ff'
  on-secondary-fixed: '#07006c'
  on-secondary-fixed-variant: '#2f2ebe'
  tertiary-fixed: '#f0dbff'
  tertiary-fixed-dim: '#ddb7ff'
  on-tertiary-fixed: '#2c0051'
  on-tertiary-fixed-variant: '#6900b3'
  background: '#111418'
  on-background: '#e1e2e8'
  surface-variant: '#32353a'
  background-obsidian: '#080B0F'
  surface-charcoal: '#111418'
  market-bull: '#10B981'
  market-bear: '#EF4444'
  data-blue: '#3B82F6'
  border-subtle: '#1E293B'
  glow-teal: rgba(45, 212, 191, 0.15)
typography:
  display-lg:
    fontFamily: Syne
    fontSize: 48px
    fontWeight: '800'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Syne
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Syne
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
  title-md:
    fontFamily: Syne
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  mono-data:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: -0.01em
  mono-label:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 32px
  container-max: 1440px
---

## Brand & Style

This design system is engineered for high-stakes financial analysis, blending the raw data density of a Bloomberg Terminal with the refined, minimalist aesthetic of modern high-growth SaaS. The brand personality is **Institutional-grade**, yet **Forward-thinking**, prioritizing clarity and analytical calm over decorative flair.

The visual style follows a **High-Contrast Dark Mode** approach. It utilizes deep, obsidian-like backgrounds to minimize eye strain during extended research sessions, accented by sharp, technical typography and luminous teal highlights. Subtle **Glassmorphism** is used sparingly to create a sense of depth and hierarchy, while **Glow effects** are reserved for critical AI insights and active market indicators. The overall feel is architectural, precise, and authoritative.

## Colors

The palette is anchored by a custom **Obsidian** neutral, providing a near-black foundation that allows chromatic elements to pop without causing glare. 

- **Primary Teal:** Used for primary actions, focus states, and AI-driven features. It represents "intelligence" and active energy.
- **Secondary/Tertiary (Blue & Violet):** Reserved for complex data visualizations, gradients, and distinguishing between multiple AI models or data streams.
- **Functional Market Colors:** `market-bull` (Green) and `market-bear` (Red) are strictly reserved for price movement and performance metrics. These use highly legible, accessible shades that maintain contrast against the dark background.
- **Gradients:** Use linear gradients from `secondary` to `primary` at 135 degrees for high-level "pro" features or premium headers.

## Typography

The typographic strategy balances **editorial character** with **mathematical precision**.

- **Headlines (Syne):** Provides a sharp, distinctive geometric look that feels modern and high-end. Use tight tracking for display sizes.
- **Body (Inter):** Leverages a highly legible, neutral grotesque for long-form reports and platform-wide UI.
- **Data & UI Labels (JetBrains Mono):** This is the workhorse of the system. All financial figures, tickers, timestamps, and metadata must use JetBrains Mono to ensure vertical alignment of digits (tabular figures) and a "technical" feel.
- **Hierarchy:** Maintain a clear distinction between "Narrative" (Syne/Inter) and "Data" (JetBrains Mono).

## Layout & Spacing

The layout uses a **Technical Grid System** based on a 4px baseline unit. 

- **Grid Model:** A 12-column fluid grid for desktop with 16px gutters. For data-dense dashboards, a 24-column grid may be used to allow for micro-modular layouts (e.g., small ticker widgets alongside larger charts).
- **Density:** The design system supports "Compact" and "Standard" density modes. Compact mode reduces vertical padding in lists and tables by 50% to maximize information density for expert users.
- **Reflow:** On mobile devices, sidebars collapse into a bottom navigation bar or a hamburger menu. Data tables should transition to card-based views or horizontal scrolling containers with frozen first columns.

## Elevation & Depth

Depth is communicated through **Tonal Layering** rather than heavy shadows.

- **Level 0 (Base):** Obsidian (#080B0F).
- **Level 1 (Surface):** Charcoal (#111418). Used for main content cards and sidebar backgrounds.
- **Level 2 (Float):** Subtle semi-transparent overlays (Glassmorphism). Use `backdrop-filter: blur(12px)` with a 1px solid border at 10% opacity.
- **Highlights:** Instead of drop shadows, use **Inner Glows** and **Outer Glows** using the primary teal color at very low opacity (5-10%) to indicate "active" or "AI-processed" states.
- **Borders:** Use sharp, 1px borders for all containers to maintain the "institutional" precision.

## Shapes

The shape language is **Soft-Geometric**. By using 4px (`0.25rem`) as the base radius, we maintain a professional, serious tone that avoids the "playfulness" of highly rounded consumer apps.

- **Inputs & Small Buttons:** 4px radius.
- **Cards & Modals:** 8px (`rounded-lg`) radius.
- **Contextual Chips:** 2px or sharp corners to denote technical data tags.
- **Visual Contrast:** Maintain sharp 90-degree angles for structural grid dividers and sidebar separators to reinforce the "terminal" aesthetic.

## Components

### Buttons
- **Primary:** Solid Teal background with Black text. No shadow, but a subtle teal glow on hover.
- **Secondary:** Ghost style with 1px Teal border and Teal text.
- **Actionable Data:** Tickers and price points should act as "Quiet Buttons," showing a subtle `surface-charcoal` background on hover.

### Inputs & Fields
- **Search/Command Bar:** Large, centered, glassmorphic blur with a monospaced "CMD+K" shortcut hint.
- **Technical Inputs:** Sharp corners, 1px `border-subtle`, using JetBrains Mono for all typed values.

### Cards & Modules
- Use **1px borders** instead of shadows. 
- Header areas of cards should use `mono-label` typography for titles to distinguish from content.

### Data Visualizations
- **Charts:** Use thin 1px lines. Avoid area fills unless they use a very subtle gradient (e.g., 5% opacity).
- **Indicators:** Use the `market-bull` and `market-bear` functional colors for performance indicators.

### AI Insight "Glow"
- Components containing AI-generated intelligence should feature a "shimmer" border or a very faint `tertiary-color` glow to signal that the data has been synthesized by the platform.