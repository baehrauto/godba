# Distribution By Air Brand Guide

## Table of Contents
1. [Brand Overview](#brand-overview)
2. [Logo](#logo)
3. [Color Palette](#color-palette)
4. [Typography](#typography)
5. [Design Elements](#design-elements)
6. [Components](#components)
7. [Spacing & Layout](#spacing--layout)
8. [Animation & Interactions](#animation--interactions)
9. [Usage Guidelines](#usage-guidelines)

---

## Brand Overview

**Distribution By Air (DBA)** is a logistics and shipping company that emphasizes reliability, care, and professional service. The brand identity reflects trustworthiness, efficiency, and a human-centered approach to logistics solutions.

**Tagline:** "Logistics Solutions From People Who Care"

---

## Logo

### Logo File
- **File Name:** `logodba.png`
- **Location:** `images/logodba.png`
- **Format:** PNG with transparency

### Logo Usage

#### Header Logo
- **Size:** `h-56 md:h-64` (responsive)
- **Width:** Auto (maintains aspect ratio)
- **Object Fit:** `object-contain`
- **Fallback:** Text-based logo with "DBA" initials in a gradient box if image fails to load

```html
<img src="images/logodba.png" 
     alt="Distribution By Air Logo" 
     class="h-56 md:h-64 w-auto object-contain" 
     onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
```

#### Footer Logo
- **Size:** `h-16` (fixed)
- **Color Treatment:** White version using CSS filter
- **Filter:** `filter: brightness(0) invert(1);`

```html
<img src="images/logodba.png" 
     alt="Distribution By Air Logo" 
     class="h-16 w-auto object-contain" 
     style="filter: brightness(0) invert(1);">
```

### Logo Guidelines
- Always maintain aspect ratio
- Never stretch or distort the logo
- Use the white version in dark backgrounds (footer)
- Ensure minimum clear space around the logo
- Logo should always link to the homepage (`index.html`)

---

## Color Palette

### Primary Colors

#### Primary Green
- **Default:** `#1e7e34`
- **Usage:** Primary buttons, links, accents, brand elements
- **CSS Variable:** `primary` or `primary-DEFAULT`

#### Primary Dark
- **Hex:** `#155724`
- **Usage:** Darker variants, hover states, depth
- **CSS Variable:** `primary-dark`

#### Primary Light
- **Hex:** `#2d8650`
- **Usage:** Gradients, lighter accents, highlights
- **CSS Variable:** `primary-light`

### Accent Color

#### Amber/Orange
- **Hex:** `#f59e0b`
- **Usage:** Accent highlights, call-to-action variations, alerts
- **CSS Variable:** `accent`

### Neutral Colors

#### Grays
- **Gray-900:** `#111827` - Primary text
- **Gray-800:** `#1f2937` - Secondary text
- **Gray-700:** `#374151` - Tertiary text
- **Gray-600:** `#4b5563` - Muted text
- **Gray-500:** `#6b7280` - Placeholder text
- **Gray-400:** `#9ca3af` - Disabled text
- **Gray-300:** `#d1d5db` - Borders
- **Gray-200:** `#e5e7eb` - Light borders
- **Gray-100:** `#f3f4f6` - Backgrounds, subtle borders
- **Gray-50:** `#f9fafb` - Light backgrounds

#### Base Colors
- **White:** `#ffffff` - Primary background, text on dark
- **Black:** `#000000` - Text (rarely used directly)

### Color Usage Guidelines

#### Primary Green
- Use for primary CTAs, active states, and brand elements
- Can be used in gradients: `from-primary via-primary-light to-primary`
- Works well with white text for contrast

#### Accent Orange
- Use sparingly for emphasis and secondary CTAs
- Creates visual interest without overwhelming
- Best used in combination with primary green

#### Grays
- Maintain hierarchy: darker grays for important text, lighter for secondary
- Use gray-100 for subtle backgrounds and borders
- Gray-600 to gray-400 for body text and descriptions

---

## Typography

### Font Families

#### Headings: Poppins
- **Weights Available:** 400 (Regular), 500 (Medium), 600 (Semi-bold), 700 (Bold), 800 (Extra-bold)
- **Usage:** All headings (h1-h6), display text, emphasis
- **Google Fonts Link:**
```html
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
```

#### Body Text: Inter
- **Weights Available:** 300 (Light), 400 (Regular), 500 (Medium), 600 (Semi-bold), 700 (Bold), 800 (Extra-bold), 900 (Black)
- **Usage:** Body text, paragraphs, UI elements, navigation
- **Google Fonts Link:**
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
```

### Typography Scale

#### Headings
- **H1:** `text-6xl md:text-7xl lg:text-8xl` (Hero headlines)
- **H1 (Standard):** `text-5xl md:text-6xl`
- **H2:** `text-4xl md:text-5xl`
- **H3:** `text-3xl md:text-4xl`
- **H4:** `text-2xl md:text-3xl`
- **H5:** `text-xl md:text-2xl`
- **H6:** `text-lg md:text-xl`

#### Body Text
- **Large:** `text-xl md:text-2xl` (Hero subheadlines)
- **Standard:** `text-base` (16px) - Default body text
- **Small:** `text-sm` (14px) - Secondary text, captions
- **Extra Small:** `text-xs` (12px) - Fine print, labels

#### Font Weights
- **Light:** `font-light` (300) - Rarely used
- **Regular:** `font-normal` (400) - Default body text
- **Medium:** `font-medium` (500) - Emphasis, navigation
- **Semi-bold:** `font-semibold` (600) - Subheadings, important text
- **Bold:** `font-bold` (700) - Headings, strong emphasis
- **Extra-bold:** `font-extrabold` (800) - Display text, hero headlines

### Typography Guidelines
- Always use Poppins for headings
- Always use Inter for body text
- Maintain sufficient line height for readability
- Use font weights to create hierarchy
- Ensure adequate contrast ratios (WCAG AA minimum)

---

## Design Elements

### Gradients

#### Primary Gradient
- **Direction:** 135deg (diagonal)
- **Colors:** `from-primary to-primary-light`
- **Usage:** Buttons, backgrounds, text effects
```css
background: linear-gradient(135deg, #1e7e34 0%, #2d8650 100%);
```

#### Text Gradient
- **Usage:** Hero headlines, emphasis
- **Implementation:** Background clip to text
```css
.gradient-text {
    background: linear-gradient(135deg, #1e7e34 0%, #2d8650 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
```

### Border Radius

#### Standard Radius
- **Small:** `rounded-lg` (0.5rem / 8px) - Small elements
- **Medium:** `rounded-xl` (0.75rem / 12px) - Cards, buttons
- **Large:** `rounded-2xl` (1rem / 16px) - Large cards, containers
- **Full:** `rounded-full` - Pills, badges, circular elements

### Shadows

#### Shadow Scale
- **Small:** `shadow-sm` - Subtle elevation
- **Medium:** `shadow-lg` - Cards, elevated elements
- **Large:** `shadow-2xl` - Mega menus, modals, prominent elements

#### Custom Shadows
- **Glow Effect:** Used for primary buttons
- **Hover Shadows:** Enhanced on interactive elements

### Grid Patterns

#### Background Grid
- **Pattern:** 40px x 40px grid
- **Color:** Primary green at 10% opacity
- **Usage:** Hero sections, background decoration
```css
.bg-grid-pattern {
    background-image: 
        linear-gradient(to right, rgba(30, 126, 52, 0.1) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(30, 126, 52, 0.1) 1px, transparent 1px);
    background-size: 40px 40px;
}
```

---

## Components

### Buttons

#### Primary Button
- **Background:** Gradient from primary to primary-light
- **Text:** White
- **Border Radius:** `rounded-2xl`
- **Padding:** `px-12 py-6`
- **Font:** Bold, large text
- **Hover:** Scale transform, enhanced shadow, glow effect
- **Example:**
```html
<a href="#" class="bg-gradient-to-r from-primary via-primary-light to-primary text-white px-12 py-6 rounded-2xl hover:shadow-2xl transition-all transform hover:scale-105 font-bold text-lg">
    Get Started Today
</a>
```

#### Secondary Button
- **Background:** White with transparency or white/10 backdrop blur
- **Text:** White or primary
- **Border:** Optional border (white/30 or primary)
- **Border Radius:** `rounded-2xl`
- **Padding:** `px-12 py-6`
- **Hover:** Background opacity increase, shadow enhancement
- **Example:**
```html
<a href="#" class="bg-white/10 backdrop-blur-md text-white px-12 py-6 rounded-2xl hover:bg-white/20 transition-all border-2 border-white/30 font-bold text-lg">
    Explore Services
</a>
```

### Cards

#### Standard Card
- **Background:** White
- **Border:** `border border-gray-100`
- **Border Radius:** `rounded-2xl`
- **Shadow:** `shadow-lg` or `shadow-xl`
- **Padding:** `p-6` to `p-12` (responsive)
- **Hover:** `card-hover` class with transform and shadow enhancement

#### Card Hover Effect
```css
.card-hover {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.card-hover:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
}
```

### Navigation

#### Header
- **Background:** White with backdrop blur
- **Shadow:** `shadow-sm`
- **Border:** `border-b border-gray-100`
- **Position:** Sticky top
- **Height:** `h-20` (80px)
- **Z-index:** `z-50`

#### Mega Menu
- **Background:** White
- **Border Radius:** `rounded-2xl`
- **Shadow:** `shadow-2xl`
- **Border:** `border border-gray-100`
- **Width:** Responsive (900px max, full width on mobile)
- **Padding:** `p-8`
- **Animation:** Fade in/out with opacity and visibility transitions

### Links

#### Standard Link
- **Color:** `text-gray-700`
- **Hover:** `hover:text-primary`
- **Transition:** `transition-colors`
- **Font Weight:** Medium to semibold

#### Link with Indicator
- **Indicator:** Small primary-colored dot that appears on hover
- **Implementation:**
```html
<a href="#" class="text-sm text-gray-700 hover:text-primary transition-colors flex items-center group/item">
    <span class="w-1.5 h-1.5 bg-primary rounded-full mr-3 opacity-0 group-hover/item:opacity-100 transition-opacity"></span>
    Link Text
</a>
```

---

## Spacing & Layout

### Container Widths
- **Max Width:** `max-w-7xl` (1280px)
- **Padding:** `px-4 sm:px-6 lg:px-8` (responsive)

### Spacing Scale
- **Tight:** `space-y-2` or `gap-2` (0.5rem / 8px)
- **Standard:** `space-y-3` or `gap-3` (0.75rem / 12px)
- **Comfortable:** `space-y-4` or `gap-4` (1rem / 16px)
- **Loose:** `space-y-6` or `gap-6` (1.5rem / 24px)
- **Extra Loose:** `space-y-8` or `gap-8` (2rem / 32px)

### Section Spacing
- **Small Sections:** `py-12` to `py-16` (48px to 64px)
- **Standard Sections:** `py-20` (80px)
- **Large Sections:** `py-32` (128px)
- **Hero Sections:** `py-32` or `min-h-screen` with flex centering

### Grid Layouts
- **2 Columns:** `grid grid-cols-1 md:grid-cols-2`
- **3 Columns:** `grid grid-cols-1 md:grid-cols-3`
- **4 Columns:** `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4`

---

## Animation & Interactions

### Transitions
- **Standard:** `transition-all duration-300`
- **Colors:** `transition-colors`
- **Transform:** `transition-transform`
- **Opacity:** `transition-opacity`

### Keyframe Animations

#### Fade In Up
```css
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
```

#### Float
```css
@keyframes float {
    0%, 100% {
        transform: translateY(0px);
    }
    50% {
        transform: translateY(-20px);
    }
}
```

#### Pulse Glow
```css
@keyframes pulse-glow {
    0%, 100% {
        box-shadow: 0 0 20px rgba(30, 126, 52, 0.3);
    }
    50% {
        box-shadow: 0 0 40px rgba(30, 126, 52, 0.6);
    }
}
```

### Hover Effects
- **Scale:** `hover:scale-105` (5% increase)
- **Translate:** `hover:-translate-y-2` (lift effect)
- **Shadow Enhancement:** Increased shadow on hover
- **Color Transitions:** Smooth color changes
- **Glow Effects:** Border glow on primary elements

---

## Usage Guidelines

### Do's ✅
- Use primary green for brand elements and CTAs
- Maintain consistent spacing using the scale
- Use Poppins for all headings
- Use Inter for all body text
- Apply rounded corners consistently (rounded-xl or rounded-2xl)
- Use gradients for primary buttons and hero sections
- Ensure sufficient contrast for accessibility
- Use hover states on all interactive elements
- Maintain logo aspect ratio
- Use white logo version in dark backgrounds

### Don'ts ❌
- Don't use colors outside the defined palette
- Don't mix font families (Poppins for headings only, Inter for body only)
- Don't stretch or distort the logo
- Don't use sharp corners (always use rounded corners)
- Don't use flat shadows (use layered shadows for depth)
- Don't skip hover states on interactive elements
- Don't use primary green for large text blocks (use grays)
- Don't overuse the accent orange color
- Don't use animations that are too fast or jarring
- Don't compromise on accessibility for design

### Responsive Design
- Always design mobile-first
- Use Tailwind responsive prefixes: `sm:`, `md:`, `lg:`, `xl:`
- Test on multiple screen sizes
- Ensure touch targets are at least 44x44px on mobile
- Maintain readability at all sizes

### Accessibility
- Maintain WCAG AA contrast ratios (4.5:1 for text, 3:1 for UI)
- Use semantic HTML elements
- Provide alt text for all images
- Ensure keyboard navigation works
- Use ARIA labels where appropriate
- Test with screen readers

---

## Technical Implementation

### Tailwind Configuration
```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                primary: {
                    DEFAULT: '#1e7e34',
                    dark: '#155724',
                    light: '#2d8650',
                },
                accent: '#f59e0b',
            }
        }
    }
}
```

### CSS Custom Properties (Alternative)
```css
:root {
    --primary: #1e7e34;
    --primary-dark: #155724;
    --primary-light: #2d8650;
    --accent: #f59e0b;
}
```

### Font Loading
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
```

---

## Brand Voice & Tone

### Voice Characteristics
- **Professional yet Approachable:** Maintain professionalism while being human and caring
- **Confident:** Express expertise and reliability
- **Clear:** Use straightforward language, avoid jargon
- **Caring:** Emphasize the human element and customer focus

### Messaging Guidelines
- Focus on solutions and outcomes
- Highlight reliability and trust
- Emphasize the "people who care" aspect
- Use active voice
- Be specific about capabilities
- Avoid overly technical language unless necessary

---

## Contact & Resources

### External Links
- **Track Order:** `https://globalship.dbaco.com/caad/login/`
- **Schedule Shipment:** `https://globalship.dbaco.com/caad/login/`
- **Book LTL:** `https://dba.7lfreight.com/login`
- **Make Payment:** `https://payments.dbaco.com/`
- **Submit Claim:** `https://dbaco.com/submit-a-claim`

### Link Behavior
- External links open in new tabs: `target="_blank" rel="noopener noreferrer"`
- Internal links navigate within the site
- All links should have clear hover states

---

*This brand guide is a living document and should be updated as the brand evolves.*

**Last Updated:** 2024




