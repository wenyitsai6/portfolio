# Wenyi Tsai — portfolio

Static site. No build step required: open `index.html`, or drag this whole folder onto
Netlify / Vercel and it deploys as-is.

## Structure

```
index.html          Home — everything. Video hero + rotator, #work (3 project cards),
                    #about (folder reveal + timeline + skills), #contact
work-rvfb.html      Case study 01 — Rainier Valley Food Bank (complete)
work-loko.html      Case study 02 — Loko (complete: research + 10 UI screens + testing)
work-hinge.html     Case study 03 — Hinge (complete: 10 participants, 3 findings, ranked fixes)
playground.html     Draggable shelves — awaiting assets
css/style.css       All styling. Tokens at the top.
js/app.js           Theme, cursor, rotator, meadow, reveal, mobile nav
img/                32 images rasterized from the project PDFs + Figma exports
media/              grass-loop.mp4 — the hero background video
_build.py           Regenerates the HTML pages (python3 -I _build.py)
```

## Editing

**Content** lives in `_build.py` as Python strings, one per page. Edit there and re-run
`python3 -I _build.py` to regenerate the HTML. The nav, footer, cursor and `<head>` are
shared in the `SHELL` / `NAV` / `FOOTER` constants, so a change there hits every page.

If you'd rather edit HTML directly, just delete `_build.py` and edit the `.html` files —
but then the shared chrome has to be kept in sync by hand.

**Design tokens** are the `:root` block at the top of `css/style.css`, sampled from the
Framer site. Dark mode overrides sit directly underneath.

**Playground** items go in the `SHELVES` array inside `playground.html`. Three item types:

```js
{ type:'image', src:'img/poster.jpg', alt:'Spring market poster' }
{ type:'video', src:'img/reel.mp4', poster:'img/reel.jpg' }
{ type:'note',  text:'Made this the night before the event.' }
```

## The hero

`media/grass-loop.mp4` plays muted on loop behind the type, with `img/grass-poster.jpg` as
the first-paint fallback. It pauses when scrolled out of view and never autoplays under
`prefers-reduced-motion`. The readable band over the grass is the radial scrim in
`.hero-bg::after` — adjust its opacity there if the type needs more or less contrast.

## The folder

`.folder` in the About section — three stacked layers (`folder-back`, `folder-doc`,
`folder-front`). Click (or Enter/Space) runs the `coverOpen` + `docOut` keyframes together:
the cover swings open on its left edge while the photo arcs out to the right, then settles
centered on the folder at a slight tilt. Clicking again plays the same keyframes in reverse
via the `.closing` class. Timing and arc live in the `@keyframes` blocks in `style.css`;
the open/close state machine is in `app.js`.

## The project-card star

The shape behind each project preview is traced from `img/wt-logo.png` itself, so it is the
logo's real silhouette rather than an approximation. It lives once in the shared `<defs>` as
`#bp` (the filled shape, viewBox `0 0 100 91.78`) and `#bc` (the same path in
objectBoundingBox units, used to clip the preview images). `.blob` carries the matching
`aspect-ratio: 100/91.78` — if you ever change the logo, retrace it and update all three
together or the fill and the clip will drift apart.

## Project preview videos (not yet wired up)

`card()` in `_build.py` takes an optional `vid=` argument. Pass it a path and the card gets a
lazy-loaded looping video that replaces the fanned stills on hover:

```python
RVFB_CARD = card("work-rvfb.html", "img/rvfb-d-busbanner.jpg", [...],
                 vid="media/rvfb-preview.mp4")
```

How it behaves (the pattern rachelchen.tech uses): the `<video>` ships with `preload="none"`
and **no src**, so nothing downloads on page load. An IntersectionObserver sets the real src
when the card is within 300px of the viewport, and the video only *plays* on hover. It
rewinds on mouse-out. Falls back to the stills if the file is missing, and never autoplays
under `prefers-reduced-motion`.

To add one: record the prototype, export a 10–20s silent MP4 (H.264, ~1200px wide, under
~3MB), drop it in `media/`, and add the `vid=` argument.

## Fonts

- **Sour Gummy** (display) and **Plus Jakarta Sans** load from Google Fonts.
- **Satoshi** is the real body face on the Framer site — it's a free Fontshare licence,
  not on Google Fonts. To use it properly, download from fontshare.com, drop the woff2
  files into `fonts/`, add an `@font-face` block, and it's already first in the `--body`
  stack so it will take over automatically.

## Still to come

- Playground assets (template is live, shelves are empty)
- Real org names for the two unattributed roles in `about.html`
- A "What I bring" section — removed for now, to be rebuilt together

## Sources

- RVFB research: the published case-study site + the Team 15 Drive folder
- RVFB visuals: rasterised from the Figma PDF exports
- Loko: research boards + the Local Business Network App Figma screens
- Hinge: the HCDE 417 Final Report (N=10). Affinity board:
  https://miro.com/app/board/uXjVGtBGY08=/
