---
name: Premium AI Fintech
colors:
  surface: '#10131a'
  surface-dim: '#10131a'
  surface-bright: '#363941'
  surface-container-lowest: '#0b0e15'
  surface-container-low: '#191b23'
  surface-container: '#1d2027'
  surface-container-high: '#272a31'
  surface-container-highest: '#32353c'
  on-surface: '#e1e2ec'
  on-surface-variant: '#c2c6d6'
  inverse-surface: '#e1e2ec'
  inverse-on-surface: '#2e3038'
  outline: '#8c909f'
  outline-variant: '#424754'
  surface-tint: '#adc6ff'
  primary: '#adc6ff'
  on-primary: '#002e6a'
  primary-container: '#4d8eff'
  on-primary-container: '#00285d'
  inverse-primary: '#005ac2'
  secondary: '#d0bcff'
  on-secondary: '#3c0091'
  secondary-container: '#571bc1'
  on-secondary-container: '#c4abff'
  tertiary: '#ffb786'
  on-tertiary: '#502400'
  tertiary-container: '#df7412'
  on-tertiary-container: '#461f00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc6ff'
  on-primary-fixed: '#001a42'
  on-primary-fixed-variant: '#004395'
  secondary-fixed: '#e9ddff'
  secondary-fixed-dim: '#d0bcff'
  on-secondary-fixed: '#23005c'
  on-secondary-fixed-variant: '#5516be'
  tertiary-fixed: '#ffdcc6'
  tertiary-fixed-dim: '#ffb786'
  on-tertiary-fixed: '#311400'
  on-tertiary-fixed-variant: '#723600'
  background: '#10131a'
  on-background: '#e1e2ec'
  surface-variant: '#32353c'
typography:
  display-lg:
    fontFamily: Sora
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Sora
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Sora
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Sora
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.02em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.04em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  3xl: 64px
  gutter: 24px
  margin-mobile: 16px
  container-max: 1280px
---

## Brand & Style

The visual identity is anchored in a philosophy of **Institutional Precision** meets **AI Intelligence**. This design system targets sophisticated financial users and institutional stakeholders who require high-density information without sacrificing clarity or aesthetic refinement.

The style is **Corporate / Modern** with a curated **Glassmorphic** layer reserved for AI-native features. It communicates reliability through a structured grid and deep neutral tones, while using vibrant accent glows to signal "intelligence" within the interface. The emotional response should be one of absolute control, futuristic efficiency, and technological superiority. Every element is designed to feel intentional, high-performance, and secure.

## Colors

The palette is optimized for a deep-dark environment, reducing eye strain for long-duration technical work. 

- **Foundation:** The background and surfaces use a "Blue-Grey Deep" scale to maintain a cool, professional atmosphere.
- **Accents:** **Primary Blue** is used for core functional actions and navigation. **Secondary Purple** is the "AI Intelligence" signal, used exclusively for insights, automation, and generative features.
- **Semantic:** Success, Danger, and Warning colors follow institutional standards but are calibrated for high legibility against dark backgrounds.
- **AI Highlights:** Use low-opacity gradients blending Blue (#3B82F6) and Purple (#8B5CF6) to create "Auroras" behind primary AI cards or headers.

## Typography

This design system utilizes a three-font strategy to balance character, readability, and technical precision.

1.  **Sora (Headings):** Provides a modern, geometric flair that distinguishes the brand from traditional banking. Use it for page titles and section headers to inject personality.
2.  **Inter (Body/UI):** The workhorse for all interface elements, descriptions, and data lists. It ensures maximum legibility at small sizes.
3.  **JetBrains Mono (Data/Metrics):** Essential for financial values, code snippets, and timestamps. The monospaced nature ensures that columns of numbers align perfectly for easy visual scanning and comparison.

**Formatting Note:** Financial totals should always use `label-md` or `label-sm` to maintain the technical, "AI-native" feel.

## Layout & Spacing

The layout follows a **Fixed Grid** model for desktop to ensure data density is controlled and professional. 

- **Desktop (1280px+):** 12-column grid with 24px gutters. Content is centered with wide margins.
- **Tablet:** 8-column fluid grid with 24px margins.
- **Mobile:** 4-column fluid grid with 16px margins.

The spacing rhythm is based on a 4px baseline. Use `lg` (24px) for padding within cards and `2xl` (48px) for vertical section spacing. AI-driven components may use slightly tighter internal padding to feel more "packaged" and compact.

## Elevation & Depth

Visual hierarchy is established through a **Tonal Layering** system complemented by **Subtle Glassmorphism**.

1.  **Base Layer (#0B0F19):** Used for the main application background.
2.  **Surface Layer (#111827):** Used for the primary content containers, navigation sidebars, and inactive cards.
3.  **Elevated Layer (#1F2937):** Used for hover states, modals, and active elements.
4.  **AI Glassmorphism:** Components featuring AI insights use a 10% opacity Purple (#8B5CF6) fill with a 20px backdrop-blur and a 1px inner border of 20% opacity white.

**Shadows:** Use a single, consistent shadow for floating elements: `0 8px 32px 0 rgba(0, 0, 0, 0.5)`. Do not use drop shadows on flat UI cards; use borders (#1F2937) for separation instead.

## Shapes

The shape language is **Soft (0.25rem)** to maintain an institutional, high-precision feel. 

- **Standard Elements (Buttons, Inputs, Small Cards):** 4px (0.25rem) corner radius.
- **Large Containers (Main Dashboard Cards):** 8px (0.5rem) corner radius.
- **Focus Indicators:** 2px solid Blue (#3B82F6) with a 2px offset.

Sharp corners feel too aggressive, while pill shapes feel too consumer-focused; this 4px standard provides a balanced, engineered aesthetic.

## Components

- **Buttons:** 
    - **Primary:** Solid Blue (#3B82F6) with White text. 
    - **AI-Action:** Gradient background (Blue to Purple) with a subtle outer glow of the same color. 
    - **Ghost:** Transparent background with 1px border (#1F2937).
- **Inputs:** Darker than the surface (#0B0F19 background) with a 1px border (#1F2937). On focus, the border transitions to Blue (#3B82F6).
- **Cards:** 1px solid border (#1F2937). For AI-specific cards, use the Glassmorphic treatment described in the Elevation section.
- **Data Tables:** Use JetBrains Mono for all numeric cells. Use Zebra striping with the Surface color (#111827) and a transparent alternate row.
- **Chips/Status:** Small, condensed labels using `label-sm`. Backgrounds should be 10% opacity of the semantic color (e.g., 10% Success Green) with 100% opacity text.
- **Charts:** Use thin 1.5px lines. AI predictions should be represented by a dashed line using the Secondary Purple (#8B5CF6).