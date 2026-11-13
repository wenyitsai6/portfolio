# Wenyi Tsai — portfolio

Static site. No framework, no npm, no build pipeline beyond one Python script.
Owner: Wenyi Tsai (product designer / UX researcher, UW HCDE '26).

## Run it

Open `index.html` in a browser. That's it — nothing to install, nothing to serve.

`python3 _build.py` regenerates the five HTML pages from the content strings inside it.
**CSS and JS are used as-is** — editing `css/style.css` or `js/app.js` needs no rebuild.

## Layout

```
index.html        Home — everything lives here: hero, #work (3 cards), #about, #contact
work-rvfb.html    Case study 01 — Rainier Valley Food Bank (award-winning capstone)
work-loko.html    Case study 02 — Loko, local business collaboration
work-hinge.html   Case study 03 — Hinge usability study (N=10)
playground.html   Draggable shelves — awaiting assets
css/style.css     All styling. Design tokens are the :root block at the top.
js/app.js         Theme, cursor, rotator, folder, lazy previews, reveal, mobile nav
img/ media/       34 images + the hero grass video
_build.py         Regenerates the HTML. Page content lives here as Python strings.
```

`_build.py` is 1,093 lines; page content starts around: home 138, work 298, rvfb 321,
loko 506, hinge 734, playground 979. **This single file is the merge-conflict surface** —
if two people edit different pages they still touch the same file. Split content into
`content/<page>.py` before parallel content editing.

## Design tokens — do not improvise these

Sampled from Wenyi's original Framer site via computed styles. They are measurements, not
guesses. All in `:root` in `style.css`.

| Token | Hex | Role |
|---|---|---|
| `--cream` | `#FFFDF5` | Page background |
| `--sage-bg` | `#EEF5E1` | Section / card background |
| `--lime` | `#C8E878` | Buttons, CTAs, accents |
| `--butter` | `#EAF3B0` | Warm wash |
| `--leaf` | `#E2F5B0` | From the WT logo |
| `--olive` | `#485922` | Primary text, deep fills — the brand green |
| `--sage-ink` | `#8FA56A` | Secondary text, labels |
| `--slate` | `#55595A` | Display colour (her name is slate, not green) |
| `--blob` | `#71B970` | Project-card star (she picked this explicitly) |

Type: **Sour Gummy** (display) + **Satoshi** (body, Fontshare licence — Plus Jakarta Sans
is the loaded stand-in). Radii: 999px pills, 20–28px cards.

Register: soft, rounded, cosy. Nothing sharp. US spelling throughout.

## Things that will break if you touch them carelessly

- **The project-card star** is traced from `img/wt-logo.png`, not hand-drawn. It exists as
  `#bp` (fill, viewBox `0 0 100 91.78`) and `#bc` (clip, objectBoundingBox units), and
  `.blob` carries the matching `aspect-ratio: 100/91.78`. Change one, change all three or
  the fill and clip drift apart.
- **The folder animation** (`.folder` in #about) uses *four* keyframe sets: `coverOpen` +
  `docOut` to open, `coverClose` + `docIn` to close. They are deliberately separate names.
  Reusing one pair with `animation-direction: reverse` does **not** restart the animation —
  the card snaps instead of playing. This was a real bug; don't "simplify" it back.
- **Skill pills** float via the `translate` property and scale on hover via `scale` —
  separate CSS properties on purpose, so they compose. Two `transform`s would overwrite
  each other. The group pauses on hover so nothing is a moving target.
- **The role rotator** cycles once and stops on the final item (`.roles i.final`). Its CSS
  sits just after the `.hero h1` rules — it has been accidentally deleted once while
  editing the hero block.
- `_build.py` uses `str.format()`, so any literal `{` or `}` in page HTML must be doubled.

## Project preview videos (built, not yet populated)

`card()` takes `vid="media/foo.mp4"`. The video ships with `preload="none"` and no `src`;
an IntersectionObserver sets the src near the viewport and it plays only on hover. Falls
back to the fanned stills when absent. Pattern borrowed from rachelchen.tech.
To add: record the prototype, export silent H.264 ≤3 MB, drop in `media/`, pass `vid=`.

## Outstanding

- Playground assets (template live, shelves empty)
- Project preview videos
- A "What I bring" section — removed, to be rebuilt
- Modern tools for the skills list, pending Wenyi confirming which she's used
- Verify the "former barista" / "first-gen creative" lines are true — they came from the
  old Framer site, which contained AI-generated filler. They currently anchor the Loko
  case study headline and the About copy.

## Content sources

Research, numbers and quotes come from Wenyi's own documents — the RVFB capstone Drive
folder, the Loko research boards, and the HCDE 417 Hinge final report. Figures on this
site are real and traceable. **Do not invent statistics or participant quotes.**
