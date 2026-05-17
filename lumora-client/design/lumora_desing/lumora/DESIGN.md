---
name: Lumora
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#bacac6'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#859491'
  outline-variant: '#3b4a47'
  surface-tint: '#2addcd'
  primary: '#46eedd'
  on-primary: '#003732'
  primary-container: '#00d1c1'
  on-primary-container: '#00544d'
  inverse-primary: '#006a62'
  secondary: '#c4c6ce'
  on-secondary: '#2d3037'
  secondary-container: '#464950'
  on-secondary-container: '#b6b8c0'
  tertiary: '#d6d6dc'
  on-tertiary: '#2f3035'
  tertiary-container: '#babac0'
  on-tertiary-container: '#494a4f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#57fae9'
  primary-fixed-dim: '#2addcd'
  on-primary-fixed: '#00201d'
  on-primary-fixed-variant: '#005049'
  secondary-fixed: '#e1e2ea'
  secondary-fixed-dim: '#c4c6ce'
  on-secondary-fixed: '#191c22'
  on-secondary-fixed-variant: '#44474d'
  tertiary-fixed: '#e2e2e8'
  tertiary-fixed-dim: '#c6c6cc'
  on-tertiary-fixed: '#1a1c20'
  on-tertiary-fixed-variant: '#45474b'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: Sora
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Sora
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Sora
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Sora
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  container-max: 1440px
---

## Brand & Style

The design system is anchored in a philosophy of **Institutional Futurism**. It aims to evoke a sense of precision, authority, and cutting-edge intelligence, tailored for a high-end audience that values both technical depth and aesthetic sophistication.

The visual style is a blend of **Minimalism** and **Glassmorphism**. It utilizes expansive negative space to allow premium typography to breathe, while employing translucent layers and subtle background blurs to create a sense of digital depth. This approach ensures the UI feels like a high-performance instrument—stable and reliable, yet visionary.

## Colors

The palette is strictly optimized for a **dark-mode-first** experience. The primary color is a vibrant, high-energy **Teal**, used sparingly for interactive states and critical indicators to maintain a premium feel. 

The background utilizes deep, tiered neutrals to create visual hierarchy without relying on heavy lines. Surfaces are built from charcoal and obsidian tones, providing a low-strain environment that emphasizes content and technical data. Accent colors beyond teal should be desaturated to preserve the "institutional" aesthetic.

## Typography

The typography strategy transitions from high-impact geometric display faces to hyper-functional mono fonts. 

- **Headlines:** Use **Sora**. Its wide stance and geometric construction provide a contemporary, "tech-luxury" feel. Use tight tracking for larger headlines to enhance the architectural look.
- **Body:** Use **Hanken Grotesk**. This font provides exceptional legibility and a sharp, contemporary edge that feels more "institutional" than standard system fonts.
- **Technical/Labels:** Use **JetBrains Mono**. Reserved for data points, code snippets, and metadata. This font reinforces the cutting-edge, developer-friendly nature of the product.

## Layout & Spacing

This design system utilizes a **12-column fluid grid** for desktop and a **4-column grid** for mobile. The spacing rhythm is based on an 8px root unit to ensure mathematical harmony across all components.

- **Desktop:** Generous outer margins (64px) create an "inset" look that feels premium and curated.
- **Mobile:** Margins compress to 16px, with focus on vertical stacking and full-width interactive elements.
- **Alignment:** All technical data should be strictly aligned to the grid, while editorial content can utilize offset columns to create a dynamic, modern flow.

## Elevation & Depth

Depth is achieved through **Tonal Layering** and **Glassmorphism**. Rather than traditional heavy shadows, the system uses "elevation by luminosity."

1.  **Level 0 (Background):** Base neutral (#0A0A0A).
2.  **Level 1 (Cards/Containers):** Secondary neutral (#1A1D23) with a subtle 1px border at 10% opacity.
3.  **Level 2 (Overlays/Popovers):** Semi-transparent surfaces with a `backdrop-filter: blur(20px)` and a subtle "inner glow" top-border to simulate light catching the edge of glass.

Shadows, when used, are "Ambient Shadows"—ultra-diffused (40px+ blur), low opacity (15%), and tinted with the primary teal color to create a soft, neon-underglow effect.

## Shapes

The shape language is defined by **Soft Precision**. A standard border radius of `4px (0.25rem)` is applied to most UI elements (inputs, buttons, small cards). This small radius maintains a professional, "squared-off" institutional look while removing the harshness of 90-degree corners.

Large containers and modal windows may scale up to `8px (0.5rem)` to soften the overall interface without losing the technical edge. Interactive elements like toggle switches or status chips may use "Pill" shapes to distinguish them from structural components.

## Components

- **Buttons:** Primary buttons use a solid Teal fill with black JetBrains Mono text for high contrast. Secondary buttons use a "Ghost" style with a 1px teal border and no fill.
- **Inputs:** Dark surfaces with a bottom-only border are preferred for a clean, editorial look. On focus, the border transitions to the primary Teal with a subtle outer glow.
- **Cards:** Use Level 1 elevation. Titles in Sora (Medium weight), metadata in JetBrains Mono. Borders should be barely visible, appearing only as a slight change in surface tone.
- **Technical Lists:** Use JetBrains Mono for all numerical data. Align decimals and use mono-spaced figures to ensure data remains readable at a glance.
- **Chips/Status:** Use pill shapes with a low-opacity background tint of the status color (e.g., Teal for active, Red for error) and high-contrast text.