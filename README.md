# COR marketing site

Static site built with [11ty (Eleventy)](https://www.11ty.dev/). Replaces the old
hand-edited HTML files (`index.html`, `product.html`, `pricing.html`) with a
templated build so the nav and footer only need to be edited in one place.

## Setup

```
npm install
```

## Commands

```
npm run build   # builds the site once into _site/
npm run serve   # builds and serves locally with live reload at localhost:8080
```

## Structure

```
src/
  _includes/
    base.njk      <- shared <head> boilerplate, nav/footer placement, block scaffolding
    nav.njk        <- single source of truth for the navbar
    footer.njk      <- single source of truth for the footer
  index.njk        <- homepage (outputs to /index.html)
  product.njk       <- product page (outputs to /product/index.html, served at /product)
  pricing.njk       <- pricing page (outputs to /pricing/index.html, served at /pricing)
  images/           <- logos, copied as-is
  favicon.ico, icon-*.png  <- copied as-is
  sitemap.xml, robots.txt  <- copied as-is
```

## Editing the nav or footer

Edit `src/_includes/nav.njk` or `src/_includes/footer.njk` once — the change
applies to all three pages on the next build. Do not edit the nav/footer
markup inside `index.njk`, `product.njk`, or `pricing.njk` directly; those
files only contain the `{% block content %}` body for their own page.

## Editing page metadata (title, description, OG tags)

Each page's front matter (the `---` block at the top of `index.njk` /
`product.njk` / `pricing.njk`) controls `title`, `description`,
`ogDescription` (optional override), and `canonicalUrl`. These flow into
`base.njk` automatically.

## Editing structured data (JSON-LD)

Each page has its own `{% block structuredData %}` containing its JSON-LD
`<script>` tags. If you change a page's URL, price, or content in a way that
affects what's claimed in structured data (especially `pricing.njk`'s
`AggregateOffer`), update the JSON-LD to match — it is not auto-generated
from the visible page content.

## Deploying

Point Vercel's build command at `npm run build` and the output directory at
`_site`. Clean URLs (`/product`, `/pricing`) work automatically since each
page builds to `<page>/index.html`.

## Known gaps / follow-ups

- `sitemap.xml`'s `<lastmod>` dates are static and were last set manually.
  There is no automation yet to update them when content changes.
- The Open Graph / Twitter Card image (`og:image`) currently points at
  `icon-512.png` (a square icon) as a placeholder. A proper 1200x630
  landscape image would render better in link previews.
