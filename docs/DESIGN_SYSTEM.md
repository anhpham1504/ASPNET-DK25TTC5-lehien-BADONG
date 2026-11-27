# Design system

The shipped visual direction is **Premium Coastal Editorial**: warm ivory paper, deep ocean blue, seafoam panels, and a restrained sunset accent. The system is documented in [DESIGN.md](../DESIGN.md) and implemented in `src/BaDong.CoastalEscape/wwwroot/css/app.css`. Release `ec0d53f` is the frozen reference for this document.

## Tokens

| Token | Value | Use |
| --- | --- | --- |
| `--ocean-950` | `#082D36` | Footer, deepest surface |
| `--ocean-900` | `#123C47` | Hero, headings, primary CTA |
| `--ocean-700` | `#1D6971` | Links and active filters |
| `--seafoam-100` | `#E3F0ED` | Soft panels |
| `--sand-50` | `#FAF7F1` | Page background |
| `--sand-200` | `#E9D9BD` | Dividers and quiet borders |
| `--sunset-500` | `#C88A51` | Accent and primary warm CTA |

## Components

`MainLayout` owns the responsive header, mobile drawer, skip link, and footer. `DestinationCard` and `FoodCard` are data-driven links. Destinations whose imagery is still `PENDING` use an editorial card rather than a large pseudo-photograph: the visual treatment identifies the record without inventing a location image. `PhotoLightbox` supports Escape/Left/Right. `FaqAccordion` exposes `aria-expanded`. `ContentService` loads and caches static JSON with empty fallbacks.

Be Vietnam Pro is the primary typeface, with local system sans-serif fallbacks when the remote font is delayed or unavailable. The hierarchy uses display-scale headings, compact uppercase labels and readable body text. Semantic color tokens carry meaning across surfaces instead of page-specific literal colors. Visible focus styles, reduced-motion rules and focus management for overlays are part of the shipped interaction contract.

## Responsive contract

The final production matrix covers four recorded viewports, including 320 × 568, 390 × 844, 768 × 1024 and 1440 × 900. Grids collapse from three to two to one column. Gallery uses CSS columns, while lightbox becomes a stacked, scrollable panel on mobile. During candidate review, a CSS cascade at the 820 px breakpoint caused the editorial split to remain in two columns; `92691a8` restored the intended single-column layout below the desktop breakpoint without changing the design system.

## Image system

Photographs are local static assets under `wwwroot/images/{locations,food}` with compact and large variants where the source resolution allows. Razor uses intrinsic-width `srcset` descriptors, `sizes`, fixed dimensions, `decoding="async"`, and lazy loading outside the first viewport. The home hero is eager/high-priority; overlays and object positions are tuned for the real Ba Động photograph.

Every source image is registered in `wwwroot/data/image-manifest.json`. Unverified subjects use the project-native `pending-verification.svg`, which clearly identifies itself as a non-photographic placeholder. This prevents unrelated imagery from being interpreted as Ba Động.
