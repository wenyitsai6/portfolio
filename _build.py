#!/usr/bin/env python3
"""Builds the static portfolio. Run:  python3 -I build.py"""
import os, pathlib

_here = pathlib.Path(__file__).parent
# Works whether this script sits beside the site folder or inside it.
OUT = _here if (_here / "css").is_dir() else _here / "site"

NAV = """<nav class="nav">
  <a class="brand" href="index.html">
    <img src="img/wt-logo.png" alt="" width="34" height="31">
    Wenyi Tsai
  </a>
  <button class="burger" aria-label="Menu">Menu</button>
  <div class="nlinks">
    <a href="index.html#work">Work</a>
    <a href="index.html#about">About</a>
    <a href="playground.html">Playground</a>
    <a href="mailto:wenyitsai6@gmail.com" class="cta">Contact me</a>
    <button class="tog" aria-label="Toggle dark mode">&#9790;</button>
  </div>
</nav>"""

DEFS = """<svg width="0" height="0" aria-hidden="true" style="position:absolute"><defs>
  <path id="bp" d="M44.62 0.00 C41.23 1.27 37.90 4.50 35.23 7.63 C32.55 10.76 30.59 16.41 28.57 18.79 C26.55 21.17 26.55 20.97 23.09 21.92 C19.63 22.86 11.68 22.54 7.83 24.46 C3.98 26.39 1.30 30.30 0.00 33.46 C-1.30 36.63 -1.96 39.63 0.00 43.44 C1.96 47.26 9.43 53.26 11.74 56.36 C14.06 59.46 13.76 58.15 13.89 62.04 C14.02 65.92 12.07 75.51 12.52 79.65 C12.98 83.79 14.81 84.87 16.63 86.89 C18.46 88.91 20.68 90.97 23.48 91.78 C26.29 92.60 29.42 93.05 33.46 91.78 C37.51 90.51 43.87 85.23 47.75 84.15 C51.63 83.07 53.62 84.05 56.75 85.32 C59.88 86.59 63.21 90.70 66.54 91.78 C69.86 92.86 73.32 93.51 76.71 91.78 C80.10 90.05 85.32 86.37 86.89 81.41 C88.45 76.45 85.71 66.44 86.11 62.04 C86.50 57.63 86.92 58.06 89.24 54.99 C91.55 51.92 98.21 47.26 100.00 43.64 C101.79 40.02 101.60 36.59 100.00 33.27 C98.40 29.94 94.88 25.86 90.41 23.68 C85.94 21.49 78.41 23.78 73.19 20.16 C67.97 16.54 62.04 5.32 59.10 1.96 C56.16 -1.40 57.99 0.33 55.58 0.00 C53.16 -0.33 48.01 -1.27 44.62 0.00 Z"/>
  <clipPath id="bc" clipPathUnits="objectBoundingBox">
    <path d="M0.4462 0.0000 C0.4123 0.0139 0.3790 0.0490 0.3523 0.0832 C0.3255 0.1173 0.3059 0.1787 0.2857 0.2047 C0.2655 0.2306 0.2655 0.2285 0.2309 0.2388 C0.1963 0.2491 0.1168 0.2456 0.0783 0.2665 C0.0398 0.2875 0.0130 0.3301 0.0000 0.3646 C-0.0130 0.3991 -0.0196 0.4318 0.0000 0.4733 C0.0196 0.5149 0.0943 0.5803 0.1174 0.6141 C0.1406 0.6478 0.1376 0.6336 0.1389 0.6759 C0.1402 0.7182 0.1207 0.8227 0.1252 0.8678 C0.1298 0.9129 0.1481 0.9247 0.1663 0.9467 C0.1846 0.9687 0.2068 0.9911 0.2348 1.0000 C0.2629 1.0089 0.2942 1.0139 0.3346 1.0000 C0.3751 0.9861 0.4387 0.9286 0.4775 0.9168 C0.5163 0.9051 0.5362 0.9158 0.5675 0.9296 C0.5988 0.9435 0.6321 0.9883 0.6654 1.0000 C0.6986 1.0117 0.7332 1.0188 0.7671 1.0000 C0.8010 0.9812 0.8532 0.9410 0.8689 0.8870 C0.8845 0.8330 0.8571 0.7239 0.8611 0.6759 C0.8650 0.6279 0.8692 0.6326 0.8924 0.5991 C0.9155 0.5657 0.9821 0.5149 1.0000 0.4755 C1.0179 0.4360 1.0160 0.3987 1.0000 0.3625 C0.9840 0.3262 0.9488 0.2818 0.9041 0.2580 C0.8594 0.2342 0.7841 0.2591 0.7319 0.2196 C0.6797 0.1802 0.6204 0.0579 0.5910 0.0213 C0.5616 -0.0153 0.5799 0.0036 0.5558 0.0000 C0.5316 -0.0036 0.4801 -0.0139 0.4462 0.0000 Z"/>
  </clipPath>
</defs></svg>"""

CURSOR = """<img id="cur" src="img/wt-logo.png" alt="" aria-hidden="true">"""

FOOTER = """<div class="wrap"><footer>
  <span>© 2026 Wenyi Tsai — Product Designer &amp; UX Researcher</span>
  <span><a href="mailto:wenyitsai6@gmail.com">wenyitsai6@gmail.com</a> · <a href="index.html#work">Work</a> · <a href="index.html#about">About</a></span>
</footer></div>"""

SHELL = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sour+Gummy:wght@400;600;700&family=Baloo+2:wght@600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<script>document.documentElement.classList.add('js');
try{{var t=localStorage.getItem('wt-theme');if(t)document.documentElement.dataset.theme=t;}}catch(e){{}}</script>
</head>
<body>
{defs}
{nav}
{body}
{footer}
{cursor}
<script src="js/app.js"></script>
</body>
</html>"""


def page(slug, title, desc, body):
    html = SHELL.format(title=title, desc=desc, body=body,
                        nav=NAV, defs=DEFS, footer=FOOTER, cursor=CURSOR)
    (OUT / slug).write_text(html, encoding="utf-8")
    print(f"  {slug:22} {len(html)//1024}KB")


# ═══════════════════════════════════════════════════════════════
# project card helper
# ═══════════════════════════════════════════════════════════════
def card(href, cover, fans, tags, h3, p, nums, soon=False, vid=None):
    """vid: path to a looping screen recording, e.g. 'media/rvfb-preview.mp4'.
    It is lazy-loaded (no src until hover/in-view) exactly like rachelchen.tech,
    and falls back to the fanned stills when no video is supplied."""
    fan_html = "".join(
        f'<div class="fan"><img src="{s_}" alt="" loading="lazy"></div>' for s_ in fans)
    tag_html = "".join(
        f'<span class="tag{" win" if w else ""}">{t}</span>' for t, w in tags)
    num_html = "".join(
        f'<div class="num"><b>{b}</b><span>{s_}</span></div>' for b, s_ in nums)
    cover_html = (f'<div class="cover"><img src="{cover}" alt="" loading="lazy"></div>'
                  if cover else '')
    vid_html = (f'<video class="preview" data-src="{vid}" muted loop playsinline '
                f'preload="none" aria-hidden="true"></video>' if vid else '')
    cls = "proj rv soon" if soon else "proj rv"
    ext = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
    return f"""<a class="{cls}" href="{href}"{ext}>
  <div class="blob">
    <svg viewBox="0 0 100 91.78" aria-hidden="true"><use href="#bp" class="blobfill"/></svg>
    <div class="stage">{cover_html}{vid_html}{fan_html}</div>
    {'<div class="hint">In progress</div>' if soon else ''}
  </div>
  <div>
    <div class="tagrow">{tag_html}</div>
    <h3>{h3}</h3>
    <p>{p}</p>
    <div class="nums">{num_html}</div>
  </div>
</a>"""


RVFB_CARD = card(
    "work-rvfb.html", "img/rvfb-d-busbanner.jpg",
    ["img/rvfb-flyer.jpg", "img/rvfb-banner.jpg", "img/rvfb-sticker2.jpg"],
    [("🏆 Engagement Award", True), ("Field study", False),
     ("Segmentation", False), ("Print systems", False)],
    "Covalence × Rainier Valley Food Bank",
    "Neighbors who qualified for a food bank three blocks away weren't showing up. Not a supply "
    "problem — a trust problem. Two quarters of fieldwork, then a physical outreach system the "
    "organization is now pricing with King County Metro.",
    [("53.8%", "Had never heard of it"), ("6", "Languages surveyed"), ("15", "Deliverables shipped")])

LOKO_CARD = card(
    "work-loko.html", "img/loko-ui-explore.jpg",
    ["img/loko-ui-home.jpg", "img/loko-ui-messages.jpg", "img/loko-ui-filter.jpg"],
    [("Product design", False), ("Project lead", False), ("Co-design", False)],
    "Loko — collaboration for local business",
    "Café owners wanted to collaborate and couldn't find each other. Five DMs, an email, a Reddit "
    "post, no replies. I'd worked behind the counter, so I went back with a research protocol — "
    "and designed swipe-to-collaborate for small businesses.",
    [("4", "Research themes"), ("7", "Testing takeaways"), ("10", "Screens designed")])

HINGE_CARD = card(
    "work-hinge.html", "img/hinge-cover.jpg", [],
    [("Usability study", False), ("Think-aloud", False), ("N=10", False)],
    "Hinge — onboarding &amp; dealbreakers",
    "Ten think-aloud sessions on Hinge's new-user experience. Every single participant hit the "
    "same wall: there's no back button during onboarding. We turned that — and seven other "
    "issues — into a prioritized fix list ranked by how many users each one actually affected.",
    [("10/10", "Blocked by one missing button"), ("3", "Core findings"), ("8", "Ranked fixes")])


# ═══════════════════════════════════════════════════════════════
# HOME
# ═══════════════════════════════════════════════════════════════
home = f"""
<header class="hero">
  <div class="hero-bg">
    <img src="img/grass-poster.jpg" alt="" aria-hidden="true">
    <video src="media/grass-loop.mp4" poster="img/grass-poster.jpg"
           autoplay muted loop playsinline aria-hidden="true"></video>
  </div>
  <div class="wrap">
    <h1>Wenyi Tsai</h1>
    <div class="roles" id="roles">
      <i class="on">a product designer</i><i>a UX researcher</i><i>a storyteller</i>
      <i>a first-gen creative</i><i>a former barista</i>
      <i class="final">Product Designer &amp; UX Researcher</i>
    </div>
    <p class="lede">Drawn to the voices behind the products we use and the experiences
      that shape them.</p>
  </div>
</header>



<div class="wrap">
  <section id="work">
    {RVFB_CARD}
    {LOKO_CARD}
    {HINGE_CARD}
  </section>

  <section id="about">
    <div class="sec-head"><h2>About me</h2>
    </div>

    <div class="about-top rv">
      <div class="folder" tabindex="0" role="button" aria-expanded="false"
           aria-label="Open the folder to see a photo of Wenyi">
        <div class="folder-back"></div>
        <div class="folder-doc">
          <img src="img/wenyi-portrait.jpg" alt="Wenyi Tsai">
        </div>
        <div class="folder-front">
          <img class="fc-logo" src="img/wt-logo.png" alt="">
          <div class="fc-meta"><span class="fc-title">WENYI UX</span>
            <span class="fc-sub">Passion and Perseverance</span></div>
          <span class="fc-hint">Open me &rarr;</span>
        </div>
      </div>

      <div id="about-story">
        <h3>Hi there, I'm Wenyi :)</h3>
        <p>I am a product designer and UX researcher recently graduated from the University of
          Washington Seattle with a B.S. in Human-Centered Design &amp; Engineering. My approach
          combines user research, storytelling, and visual crafts to turn human insights into
          products that support users. As I continue learning and growing, I'm excited to bring
          care, curiosity, and purpose into design work that creates positive impact.</p>
        <p>Beyond design, I love creating content for social media, editing videos, surrounding
          myself with people I love, and exploring new places that remind me to appreciate the
          little things in life. I carry that same sense of care, curiosity, and love into the way
          I design.</p>
        <p class="about-now"><span class="label">Currently</span>
          Looking for product design and UX research roles — and always up for a coffee.
          Most of what I notice off the clock ends up in the <a href="playground.html">playground</a>.</p>
      </div>
    </div>

    <div class="xs-grid" id="about-exp">
      <div class="xs-side">
        <h3 class="about-sub">Skills</h3>
        <p class="xs-note">Highlighted are the ones I lean on most.</p>

        <span class="label">Research</span>
        <div class="pills">
          <span class="pill key">UX Research</span><span class="pill key">Usability Testing</span>
          <span class="pill key">User Interviews</span><span class="pill key">Field Research</span>
          <span class="pill">Co-Design</span>
        </div>

        <span class="label">Strategy &amp; synthesis</span>
        <div class="pills">
          <span class="pill key">Journey Mapping</span><span class="pill key">Service Design</span>
          <span class="pill">Information Architecture</span><span class="pill">Product Strategy</span>
          <span class="pill key">Project Management</span>
        </div>

        <span class="label">Design</span>
        <div class="pills">
          <span class="pill key">Product Design</span><span class="pill key">Interaction Design</span>
          <span class="pill key">Prototyping</span><span class="pill key">Visual Systems</span>
          <span class="pill">Accessibility</span><span class="pill">Storytelling</span>
        </div>

        <span class="label">Tools</span>
        <div class="pills">
          <span class="pill key">Figma</span><span class="pill key">FigJam</span>
          <span class="pill key">Miro</span><span class="pill">Framer</span>
          <span class="pill">Notion</span><span class="pill">Adobe Creative Suite</span>
        </div>
      </div>

      <div class="xs-main">
        <h3 class="about-sub">Experience</h3>
        <div class="timeline">
          <div class="tl-item rv"><span class="label">Jan 2026 — Jun 2026 · Rainier Valley Food Bank Capstone</span>
            <h4>Product Designer, UX Researcher &amp; Project Manager</h4>
            <p>Covalence × Rainier Valley Food Bank. Led the visual identity and prototype suite,
              ran recruitment and multilingual survey distribution, and project-managed the phase
              where research became artifacts.</p>
            <p class="tl-res"><span class="label">Result</span> Won the Capstone Engagement award.
              RVFB is pricing transit advertising with King County Metro.
              <a href="work-rvfb.html">Case study →</a></p></div>

          <div class="tl-item rv"><span class="label">2024 — 2026 · Society of Asian Scientists and Engineers at UW</span>
            <h4>Creative Director &amp; Marketing</h4>
            <p>Student-led engineering club at UW. Built the chapter's visual presence and ran
              marketing across events and social.</p>
            <p class="tl-res"><span class="label">Result</span> The longest-running design practice
              on this page — and where most of my instinct for brand and community came from.</p></div>

          <div class="tl-item rv"><span class="label">Sep 2025 — Dec 2025 · Usability Study at UW</span>
            <h4>UX Experience &amp; UX Researcher</h4>
            <p>Hinge onboarding and dealbreakers. Moderated and took notes across think-aloud
              sessions with ten participants, then coded and affinity-mapped the results.</p>
            <p class="tl-res"><span class="label">Result</span> Three findings and eight
              recommendations ranked by how many users each issue affected.
              <a href="work-hinge.html">Case study →</a></p></div>

          <div class="tl-item rv"><span class="label">Mar 2026 — Jun 2026 · Service Design at UW</span>
            <h4>Product Design &amp; Project Lead</h4>
            <p>Loko — a collaboration platform for independent local businesses. Led product design
              and the team, ran café field studies and co-design sessions.</p>
            <p class="tl-res"><span class="label">Result</span> Ten screens, a service blueprint,
              and the profile-depth finding that came out of user testing.
              <a href="work-loko.html">Case study →</a></p></div>
        </div>
      </div>
    </div>
  </section>

  <section id="contact">
    <div class="contact rv">
      <h2>Let's make something reachable</h2>
      <p>I'm looking for product design and UX research roles. Always happy to talk about
         community-centred work, research methods, or coffee.</p>
      <div class="cbtns">
        <a class="btn" href="mailto:wenyitsai6@gmail.com">Email me</a>
        <a class="btn ghost" href="#about">More about me</a>
      </div>
    </div>
  </section>
</div>"""


# ═══════════════════════════════════════════════════════════════
# WORK INDEX
# ═══════════════════════════════════════════════════════════════
work = f"""
<div class="cs-hero">
  <div class="wrap">
    <span class="label">Selected work</span>
    <h1>Three projects, told properly.</h1>
    <p class="lede">Community service design, a platform concept for independent businesses, and a
      usability study of a product millions of people use. Each one starts with fieldwork.</p>
  </div>
</div>

<div class="wrap">
  <section>
    {RVFB_CARD}
    {LOKO_CARD}
    {HINGE_CARD}
  </section>

</div>"""


# ═══════════════════════════════════════════════════════════════
# RVFB CASE STUDY
# ═══════════════════════════════════════════════════════════════
rvfb = """
<div class="cs-hero">
  <div class="wrap">
    <span class="label">🏆 2026 HCDE Capstone Award — Engagement</span>
    <h1>Being nearby isn't the same as being reachable.</h1>
    <p class="lede">The Rainier Valley Food Bank sits in one of Seattle's most diverse
      neighborhoods. Residents living steps away were underrepresented among its users. We spent
      two quarters finding out why — and designed for what we found.</p>
    <div class="facts">
      <div class="fact"><span class="label">Role</span><b>Product Designer · UX Researcher · PM</b></div>
      <div class="fact"><span class="label">Team</span><b>Covalence — 4 researchers</b></div>
      <div class="fact"><span class="label">Duration</span><b>Winter–Spring 2026</b></div>
      <div class="fact"><span class="label">Partner</span><b>Rainier Valley Food Bank</b></div>
    </div>
  </div>
</div>

<div class="narrow cs-body">
  <section style="padding-top:44px">
    <div class="figs rv">
      <div class="fig"><b>53.8%</b><span>Had never heard of RVFB</span></div>
      <div class="fig"><b>78%</b><span>Backed transit-stop outreach</span></div>
      <div class="fig"><b>5</b><span>In-depth interviews</span></div>
      <div class="fig"><b>6</b><span>Languages surveyed</span></div>
    </div>

    <h2>The question</h2>
    <p>An internal observation from RVFB staff prompted a paradox: people travelling from further
      away used the food bank more than the neighbors on its doorstep. The obvious explanations —
      supply, hours, marketing — didn't hold up.</p>
    <blockquote><p>How might we increase engagement, trust, and perceived accessibility among
      nearby residents who are not currently using RVFB's services?</p></blockquote>
    <p>We framed it as a problem of trust, visibility and cultural alignment rather than logistics.
      That framing decision shaped everything downstream — and it's the one I'd defend hardest.</p>

    <figure class="rv">
      <img src="img/rvfb-d-busbanner.jpg" alt="Transit ad mockup on a Sound Transit bus reading 'Your neighbors shop here, so can you'">
      <figcaption>Transit advertising concept. RVFB has since contacted King County Metro for pricing.</figcaption>
    </figure>

    <h2>How we worked</h2>
    <div class="phase rv"><span class="label">Phase 01 · Discovery</span>
      <h3>The barrier audit</h3>
      <p>A 90-minute on-site field study: ten rapid-fire interviews with staff and visitors while
        two of us walked the site photographing signage, entry points and wayfinding. We ran the
        field study <em>before</em> waiting for survey saturation — the observations then shaped
        every survey question we wrote.</p></div>
    <div class="phase rv"><span class="label">Phase 02 · Synthesis</span>
      <h3>Trust and cultural synthesis</h3>
      <p>Thirteen survey responses analyzed and visualised. Five persistent themes emerged, which
        became a six-profile audience segmentation framework and a journey map for the Seeker —
        the persona whose barrier is awareness rather than shame, and therefore the one outreach
        design can actually move.</p></div>
    <div class="phase rv"><span class="label">Phase 03 · Development</span>
      <h3>Prototyping a low-barrier experience</h3>
      <p>Five in-depth interviews across three participant groups, then low-fidelity prototypes in
        Figma. We chose physical over digital: field observation and interview data both showed
        this community responds to visible, in-place, tactile materials at trusted locations.</p></div>
    <div class="phase rv"><span class="label">Phase 04 · Evaluation</span>
      <h3>Community validation</h3>
      <p>Structured concept feedback sessions with community members reviewing developed concepts.
        We called them <em>Concept Study Feedback Sessions</em>, not workshops — participants were
        evaluating, not generating, and precise framing mattered for informed consent.</p></div>

    <h2>What the data told us</h2>
    <p>Six findings, each triangulated against survey data and field observation. The one that
      reframed the project:</p>
    <h3>Discovery is entirely passive</h3>
    <p>None of our five participants discovered RVFB through RVFB. Every discovery was
      self-directed or accidental — a Google search, a spotted pamphlet, a visible queue at a
      farmers market. The organization was absent from the awareness path of the people who needed
      it most.</p>
    <blockquote><p>We were at a farmers market and saw a line of people, so we went over to see
      what it was and realized it was a food bank. We decided to stay.</p>
      <cite>Nini — community member</cite></blockquote>

    <h3>Stigma deters the first visit</h3>
    <p>Shame surfaced across all three participant groups, strongest among younger adults. What
      neutralised it wasn't messaging — it was company.</p>
    <blockquote><p>I offered to go with them so they did not have to walk in alone. Once we were
      there, we would make it fun, picking out different things together.</p>
      <cite>B — community volunteer</cite></blockquote>

    <h3>Language access is systemic, not an edge case</h3>
    <p>On-site signage was predominantly English-only despite a majority non-English-speaking
      visitor population. Non-English speakers face compounding barriers: materials they can't
      read, systems they can't navigate, staff who may not share their language.</p>
    <p>We treated this as a constraint on our own method, not just a finding about RVFB. Our
      community survey went out in <strong>five languages besides English</strong> — Spanish,
      Chinese, Vietnamese, Amharic and Arabic — because a survey about language barriers that only
      exists in English answers its own question.</p>

    <h2>What we made</h2>
    <p>Three concept directions, each traceable to a specific finding. Every feature connects back
      to something a participant said.</p>

    <div class="gal rv">
      <a href="img/rvfb-flyer.jpg" target="_blank" rel="noopener"><img src="img/rvfb-flyer.jpg" alt="Outreach flyer in RVFB brand teal with produce photography" loading="lazy"></a>
      <a href="img/rvfb-banner.jpg" target="_blank" rel="noopener"><img src="img/rvfb-banner.jpg" alt="Street pole banner with logo, hours and QR code" loading="lazy"></a>
      <a href="img/rvfb-busad.jpg" target="_blank" rel="noopener"><img src="img/rvfb-busad.jpg" alt="Bus shelter advertisement concept" loading="lazy"></a>
    </div>
    <p class="label" style="margin-top:12px">Flyer · pole banner · transit ad — all built to RVFB's brand style guide</p>

    <figure class="rv">
      <img src="img/rvfb-d-flyer.jpg" alt="Flyer shown in situ on a community noticeboard" loading="lazy">
      <figcaption>In-situ placement: libraries, schools, bus stops, daycares and faith organizations.</figcaption>
    </figure>

    <h3>The sticker set</h3>
    <p>Small, cheap, and the part people actually take home. Flat vector illustration built to sit
      beside the brand without competing with it.</p>
    <div class="gal rv">
      <img src="img/rvfb-sticker1.jpg" alt="RVFB sticker design" loading="lazy">
      <img src="img/rvfb-sticker2.jpg" alt="RVFB grocery bag sticker design" loading="lazy">
      <img src="img/rvfb-sticker3.jpg" alt="RVFB sticker design" loading="lazy">
      <img src="img/rvfb-sticker4.jpg" alt="RVFB sticker design" loading="lazy">
    </div>

    <figure class="rv">
      <img src="img/rvfb-bag.jpg" alt="Branded reusable grocery bag concept" loading="lazy">
      <figcaption>Reusable grocery bag — dignity-centred branding that travels through the neighborhood.</figcaption>
    </figure>

    <h2>What I owned</h2>
    <p>Four of us ran this project and the PM role rotated by phase. I led during Phase 3 — the
      stretch where research turns into artifacts and recruitment either works or sinks you.</p>
    <div class="grid3">
      <div class="cardy rv"><h3>Recruitment at scale</h3>
        <p>I ran participant outreach and interview scheduling. We contacted <strong>50+
          organizations</strong> for survey distribution, which took responses from 12 to 21 in a
          single week. I moved scheduling to Calendly after manual coordination started eating
          days.</p></div>
      <div class="cardy rv"><h3>Multilingual access</h3>
        <p>Language access was a research finding, so it had to be a research practice too. I got
          the survey translated and published online in <strong>five languages</strong> — Spanish,
          Chinese, Vietnamese, Amharic and Arabic — distributed through a single Linktree.</p></div>
      <div class="cardy rv"><h3>Visual direction</h3>
        <p>I led the visual identity and the prototype suite across every deliverable — flyer,
          banner, transit ad, grocery bag, sticker set — all built to RVFB's own brand style
          guide rather than my own.</p></div>
    </div>
    <p>When a participant no-showed and went silent, I handled the follow-up and backfill rather
      than letting the slot disappear. Most of what a PM does on a project like this never appears
      in the final report, which is exactly why I'm listing it here.</p>

    <h2>Where it landed</h2>
    <p>Final mockups were presented to RVFB stakeholders and received positive response from
      marketing and senior leadership. RVFB has contacted King County Metro for transit advertising
      pricing and is exploring city approval for banner holders on Rainier Avenue light posts.</p>
    <p>The full suite — pole banner, flyer, branded grocery bag, informative video and custom
      stickers — was displayed at the UW HCDE Capstone Showcase, where the project won the
      <strong>Engagement award</strong> in the Infrastructure, Society &amp; Community category,
      judged across both bachelor's and master's teams.</p>

    <h2>What I'd do differently</h2>
    <ul>
      <li>Our survey skewed heavily toward 18–24 year olds. A broader age and language distribution
        would have strengthened the quantitative half considerably.</li>
      <li>We'd pilot-test the survey instrument — several questions were accidentally left optional,
        creating avoidable gaps.</li>
      <li>We never interviewed RVFB's core visitor population: elderly, non-English-speaking adults.
        Their view of these barriers may differ from everything we documented.</li>
      <li>We'd treat faith organizations and childcare providers as research collaborators from the
        start, rather than as outreach targets at the end.</li>
    </ul>
    <p>The proximity paradox is documented but not fully explained. Whether dignity-centred
      messaging alone can move someone from <em>Avoider</em> to first visit remains an open
      empirical question.</p>

    <div class="contact rv" style="margin-top:50px">
      <h2>Read the full research</h2>
      <p>The complete two-quarter process — all findings, segments, journey map and references —
        is documented in its own site.</p>
      <div class="cbtns">
        <a class="btn" href="https://unrivaled-figolla-f9df00.netlify.app" target="_blank" rel="noopener">Open the case study →</a>
        <a class="btn ghost" href="index.html#work">Back to work</a>
      </div>
    </div>
  </section>
</div>"""


# ═══════════════════════════════════════════════════════════════
# LOKO CASE STUDY
# ═══════════════════════════════════════════════════════════════
loko = """
<div class="cs-hero">
  <div class="wrap">
    <span class="label">Service design · HCDE 418</span>
    <h1>I'd already worked behind the counter.</h1>
    <p class="lede">Independent café owners want to collaborate with each other. They send DMs,
      emails and Reddit posts into the void. Loko is a platform that makes finding a collaborator
      feel like finding a date — because the hard part was never the wanting.</p>
    <div class="facts">
      <div class="fact"><span class="label">Role</span><b>Product Design &amp; Project Lead</b></div>
      <div class="fact"><span class="label">Methods</span><b>Field study, co-design, narrative prototyping</b></div>
      <div class="fact"><span class="label">Context</span><b>U-District, Seattle</b></div>
      <div class="fact"><span class="label">Year</span><b>2024–2025</b></div>
    </div>
  </div>
</div>

<div class="narrow cs-body">
  <section style="padding-top:44px">
    <h2>The problem, in an owner's words</h2>
    <blockquote><p>I have sent like 5 DMs already. I also emailed people, posted on Reddit, even
      tried reaching out through Instagram and nobody replies.</p>
      <cite>Café owner — narrative prototype, Scene 1</cite></blockquote>
    <blockquote><p>I just wanna host more events or collabs but even finding people is actually
      so hard.</p><cite>Café owner — narrative prototype, Scene 1</cite></blockquote>
    <p>Outreach between small businesses is scattered across Instagram DMs, email and Reddit, with
      slow or no replies. The intent to collaborate is already there. The channel is broken.</p>

    <figure class="rv">
      <img src="img/loko-journey.jpg" alt="User journey map for the small business collaboration platform" loading="lazy">
      <figcaption>Journey map — from the frustration of cold outreach to a completed pop-up event.</figcaption>
    </figure>

    <h2>What we found in the field</h2>
    <p>We ran field studies and co-design sessions across independent cafés in the U-District,
      then synthesized findings into four themes.</p>

    <h3>Cafés are already community infrastructure</h3>
    <ul>
      <li>Customers use cafés to study, socialise and stay for long stretches</li>
      <li>Physical design drives interaction — community tables, booths, varied seating</li>
      <li>Some customers buy and leave; others stay without ordering at all</li>
      <li>Regulars build real familiarity with staff</li>
    </ul>

    <h3>The collaboration instinct precedes any tool</h3>
    <ul>
      <li>Owners already partner through pop-ups, product displays and shared shelves</li>
      <li>One café runs a mini market featuring smaller brands only available online</li>
      <li>Collaboration measurably brings in more customers</li>
      <li>Events work best when they align with existing customer routines — simple, low-effort, relevant</li>
      <li>Large U-District events (cherry blossom festival, Chow Down, street fair) drive café traffic</li>
    </ul>

    <h3>The barriers are time, staff and language</h3>
    <ul>
      <li>Understaffing — staff multitask between taking orders and cleaning</li>
      <li>Language barriers limit customer interaction; the cashier is often the only fluent English speaker</li>
      <li>Time is the single biggest constraint on planning anything</li>
      <li>Costs must justify hosting an event at all</li>
      <li>Space constraints inside the café</li>
      <li>Lack of promotion leads to low engagement, which discourages the next attempt</li>
    </ul>

    <blockquote><p>Owners want to host events and collaborate. What they need is support planning
      them — and a way to find each other that doesn't cost a week of unanswered messages.</p>
      <cite>Synthesis — "Want more resources" theme</cite></blockquote>

    <figure class="rv">
      <img src="img/loko-findings.jpg" alt="Affinity board of findings grouped by theme" loading="lazy">
      <figcaption>Findings grouped into four themes across field notes and co-design sessions.</figcaption>
    </figure>

    <h2>Mapping the system</h2>
    <p>Before designing anything we mapped who touches whom — owners, staff, customers, student
      groups, neighboring businesses and the district events that already pull people in.</p>
    <div class="gal rv">
      <a href="img/loko-ecosystem.jpg" target="_blank" rel="noopener"><img src="img/loko-ecosystem.jpg" alt="Ecosystem map of local business relationships" loading="lazy"></a>
      <a href="img/loko-blueprint.jpg" target="_blank" rel="noopener"><img src="img/loko-blueprint.jpg" alt="Service blueprint for the collaboration platform" loading="lazy"></a>
    </div>
    <p class="label" style="margin-top:12px">Ecosystem map · service blueprint</p>

    <h2>The service</h2>
    <p>The swipe mechanic came from dating apps for a specific reason: owners told us the hardest
      part is <em>not knowing who's open to it</em>. A directory solves discovery. Swiping solves
      the signal — everyone on the other side has already said yes in principle.</p>
    <div class="grid3">
      <div class="cardy rv"><h3>Discover</h3>
        <p>Search and filter by business type, goals, audience and event interests. Or swipe
           through owners who have already flagged themselves as open to collaborating.</p></div>
      <div class="cardy rv"><h3>Connect</h3>
        <p>Messaging built into the platform, so outreach stops scattering across Instagram,
           email and Reddit. One place, one inbox, one thread per collaboration.</p></div>
      <div class="cardy rv"><h3>Plan</h3>
        <p>Shared event planning and promotion support, community channels, and a discussion forum
           where owners ask questions and share what worked.</p></div>
    </div>

    <figure class="rv">
      <img src="img/loko-structure.jpg" alt="Service design structure listing platform features" loading="lazy">
      <figcaption>Service structure — including onboarding support for businesses with limited online presence.</figcaption>
    </figure>

    <h2>Testing it as a story</h2>
    <p>We wrote a six-scene narrative prototype rather than jumping to screens: a frustrated café
      owner, a friend who recommends the platform, a bakery owner who replies within hours, a Zoom
      call, and a matcha-and-pastry pop-up that brings in both a regular and a first-time customer.</p>
    <p>Writing the story first exposed something a wireframe would have hidden — the moment that
      matters isn't the match. It's the <em>reply</em>. Everything in the interface should be
      working toward a response arriving fast enough to keep the momentum.</p>

    <figure class="rv">
      <img src="img/loko-userflow.jpg" alt="User flow diagram for the Loko app" loading="lazy">
      <figcaption>User flow — sign-up through to a confirmed collaboration.</figcaption>
    </figure>

    <h2>The app</h2>
    <p>Sage and cream, rounded cards, soft shadows. The visual language is deliberately calm:
      owners told us outreach already feels like rejection, so the interface shouldn't add to it.
      Real Seattle businesses populate the prototype — Offline Coffee, Seattle Fish Guys,
      Floranda Pop-Up — because testing against invented brands hides whether the card layout
      actually carries enough information to judge a partner.</p>

    <div class="gal rv phones">
      <a href="img/loko-ui-home.jpg" target="_blank" rel="noopener"><img src="img/loko-ui-home.jpg" alt="Loko home screen showing collaboration matches" loading="lazy"></a>
      <a href="img/loko-ui-explore.jpg" target="_blank" rel="noopener"><img src="img/loko-ui-explore.jpg" alt="Explore page — 24 businesses near you, filtered by category" loading="lazy"></a>
      <a href="img/loko-ui-filter.jpg" target="_blank" rel="noopener"><img src="img/loko-ui-filter.jpg" alt="Filter panel for narrowing collaboration matches" loading="lazy"></a>
      <a href="img/loko-ui-messages.jpg" target="_blank" rel="noopener"><img src="img/loko-ui-messages.jpg" alt="In-app messages so outreach stops scattering across platforms" loading="lazy"></a>
      <a href="img/loko-ui-events.jpg" target="_blank" rel="noopener"><img src="img/loko-ui-events.jpg" alt="Events management screen" loading="lazy"></a>
      <a href="img/loko-ui-detail.jpg" target="_blank" rel="noopener"><img src="img/loko-ui-detail.jpg" alt="Business detail view" loading="lazy"></a>
    </div>
    <p class="label" style="margin-top:12px">Home · explore · filters · messages · events · detail</p>

    <h2>What testing changed</h2>
    <p>We put the prototype in front of users and the headline was encouraging — and then
      specific. People liked it. They also told us exactly where it was thin.</p>
    <blockquote><p>The app is cute, calming and easy to understand. The swipe interaction makes
      business matching feel less stressful.</p><cite>Strongest positive feedback, user testing round</cite></blockquote>
    <p>Seven takeaways came out of the session. The one I owned:</p>

    <div class="phase rv"><span class="label">Takeaway 03 — my finding</span>
      <h3>Business profiles need more depth</h3>
      <p>Users liked the images and short descriptions, but a card doesn't tell you whether someone
        is a <em>good partner</em>. They wanted social and portfolio links, past collaborations,
        business limitations, what the owner can bring to the table, and what they're looking
        for — the things you'd actually weigh before committing a weekend to a joint pop-up.</p></div>

    <h3>The other six</h3>
    <ul>
      <li><strong>The matching idea works, the interaction needs teaching.</strong> Swiping felt
        familiar and low-pressure — but to anyone who has never used a swipe-based app it needs
        prompts or visual cues.</li>
      <li><strong>Filters need more dimensions.</strong> Free vs. paid collaboration, budget range,
        event type, company size, timeframe, distance. People also couldn't tell whether
        "collaboration timeframe" meant the planning window or the event date.</li>
      <li><strong>Trust has to be designed in.</strong> The repeated worry: how do I know this
        business will actually follow through? Response rates, past collaborations, reviews,
        confirmation steps before anything is final.</li>
      <li><strong>Messages need structure</strong> — grouped by prospective partners, active
        collaborations, past collaborations, event planning and saved businesses.</li>
      <li><strong>Onboarding prompts are too open-ended.</strong> Left to free-write, some owners
        write an essay and others write nothing. Structured questions fix the floor and the ceiling
        at once.</li>
      <li><strong>It needs a bigger swing.</strong> The sharpest critique: the prototype is a solid
        foundation but too bare. People wanted features specific to <em>business collaboration</em>,
        not just matching.</li>
    </ul>

    <figure class="rv">
      <img src="img/loko-testing.jpg" alt="User testing takeaways document" loading="lazy">
      <figcaption>Full user-testing synthesis. Takeaway 3 is mine.</figcaption>
    </figure>

    <h2>What I'd do differently</h2>
    <ul>
      <li>We designed the profile card before we knew what owners use to judge a partner. Testing
        caught it, but a single interview question would have caught it sooner.</li>
      <li>The swipe mechanic was borrowed on the assumption everyone knows it. Testing showed that
        assumption is only safe for people who've used dating apps.</li>
      <li>Trust came up repeatedly in research and still didn't make it into the first prototype.
        It should have been a primary design requirement, not a testing discovery.</li>
    </ul>

    <div class="contact rv" style="margin-top:50px">
      <h2>Next case study</h2>
      <p>Ten think-aloud sessions on a dating app — and one missing button that stopped everybody.</p>
      <div class="cbtns">
        <a class="btn" href="work-hinge.html">Hinge usability study →</a>
        <a class="btn ghost" href="index.html#work">All work</a>
      </div>
    </div>
  </section>
</div>"""


# ═══════════════════════════════════════════════════════════════
# HINGE
# ═══════════════════════════════════════════════════════════════
REC_ROWS = [
    ("High",   "Add a back button during onboarding",      "Cannot recover from errors",        10),
    ("Medium", "Improve Dating Preferences visibility",    "Cannot find core features",          7),
    ("Medium", "Clarify free vs. premium features upfront","Lack of system status visibility",   7),
    ("Medium", "Centralize Dealbreaker management",        "Scattered options prevent discovery",5),
    ("Medium", "Add tooltips for unclear terminology",     "Cannot make informed selections",    5),
    ("Medium", "Reduce pop-up interruptions",              "Disrupts task flow",                 4),
    ("High",   "Warn about locked settings during setup",  "Unexpected system constraints",      3),
    ("Medium", "Display a swipe-limit counter",            "No warning before interruption",     1),
]

def rec_chart():
    rows = ""
    for pri, rec, impact, n in REC_ROWS:
        pct = n * 10
        rows += f'''<tr>
      <th scope="row"><span class="pri {pri.lower()}">{pri}</span>{rec}</th>
      <td class="bar-cell"><span class="track"><span class="bar" style="--w:{pct}%"></span></span><b>{n}/10</b></td>
      <td class="impact">{impact}</td>
    </tr>'''
    return f'''<figure class="rv chart">
  <table class="recs">
    <caption>Recommendations ranked by how many of the ten participants each issue affected.</caption>
    <thead><tr><th scope="col">Recommendation</th><th scope="col">Users affected</th>
      <th scope="col">Usability impact</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
</figure>'''


hinge = f"""
<div class="cs-hero">
  <div class="wrap">
    <span class="label">Usability study · HCDE 417 · Team of 5</span>
    <h1>Ten people. One missing button.</h1>
    <p class="lede">We ran think-aloud usability sessions on Hinge's new-user experience with ten
      participants. Every single one of them hit the same wall — you cannot go back during
      onboarding. It became the highest-priority fix in our report.</p>
    <div class="facts">
      <div class="fact"><span class="label">Role</span><b>UX Experience &amp; UX Researcher</b></div>
      <div class="fact"><span class="label">Method</span><b>1:1 think-aloud usability testing</b></div>
      <div class="fact"><span class="label">Participants</span><b>10 — 8 new, 2 lapsed</b></div>
      <div class="fact"><span class="label">Year</span><b>2025</b></div>
    </div>
  </div>
</div>

<div class="narrow cs-body">
  <section style="padding-top:44px">
    <div class="figs rv">
      <div class="fig"><b>10</b><span>Participants</span></div>
      <div class="fig"><b>30–45</b><span>Minutes per session</span></div>
      <div class="fig"><b>3</b><span>Core findings</span></div>
      <div class="fig"><b>8</b><span>Ranked recommendations</span></div>
    </div>

    <h2>What we were asking</h2>
    <p>Hinge markets itself as "designed to be deleted" — a dating app built for intentional
      relationships. But getting to the app itself means answering 20+ demographic questions
      first, covering everything from age to political and religious belief.</p>
    <p>We evaluated two things: the new-user experience through onboarding, and whether people
      could find and understand <strong>Dating Preferences</strong> and <strong>Dealbreakers</strong>
      — the controls that shape who you see and who sees you.</p>

    <h3>Who we tested with</h3>
    <p>Ten participants aged 18–29, split into two groups: eight who had never used Hinge, and two
      lapsed users inactive for six months or more. That split let us separate genuine first-run
      confusion from habits formed by prior use.</p>

    <h3>How we ran it</h3>
    <p>Each session was moderated 1:1 over Zoom with phone screen-sharing, one moderator and at
      least one notetaker. Participants thought aloud while completing tasks, then answered
      follow-up interview questions. We scored each task against a shared success-criteria table —
      from <em>Success</em> through <em>Delayed Success</em> to <em>Failed</em> — so results stayed
      comparable across different moderators.</p>
    <p>Afterwards we open-coded the recordings and migrated everything to Miro for affinity
      diagramming: one sticky color per participant, ten categories, then grouped into themes.</p>

    <h2>Finding 01 — Onboarding is long, rigid, and overwhelming</h2>
    <p>This was the biggest section of the study and produced the most severe issues. Six separate
      problems compound into one bad first impression.</p>

    <h3>There is no back button. At all.</h3>
    <p><strong>10 out of 10 participants</strong> were frustrated by this — the single most
      universal finding in the study. Moving forward is effortless; going back is impossible. One
      participant said it would make them consider deleting the app.</p>
    <blockquote><p>You can't, like, go back and adjust your preferences as you're doing it
      initially. You have to go through the whole onboarding and then adjust it later, which I
      think is… a little goofy.</p><cite>P3</cite></blockquote>
    <blockquote><p>There's no clear back path to adjust previous answers during onboarding. [This
      feels] kinda annoying. I'm thinking negatively about that.</p><cite>P4</cite></blockquote>

    <h3>Terminology people can't parse</h3>
    <p>Five of nine participants hit words they didn't understand — and the app offered no
      explanation. Two didn't know what <em>monogamy</em> and <em>non-monogamy</em> meant. Two
      couldn't tell <em>life partner</em> from <em>long-term</em>. One skipped the gender identity
      question entirely rather than answer something they didn't understand.</p>
    <blockquote><p>I'm not entirely sure what these mean. I'm just gonna assume monogamy is, like,
      two people in it… so maybe they should have the definition somewhere.</p><cite>P5</cite></blockquote>

    <h3>Pop-ups fragment the flow</h3>
    <p>Permissions, hints and Hinge+ upsells interrupt setup repeatedly. Participants understood
      why they existed and still found them intrusive — one noted premium prompts appeared before
      they'd had any chance to evaluate the free tier.</p>
    <blockquote><p>I keep getting these pop-ups every two seconds. I'm gonna blow this app up,
      bro… I get that they're necessary, but they break up the flow.</p><cite>P3</cite></blockquote>

    <h3>Skipping is possible but invisible</h3>
    <p>Two participants wanted to skip questions; only one worked out how. The skip control is so
      low-contrast that P8 assumed it didn't exist and tapped at random until something worked.</p>
    <blockquote><p>Oh, I can skip some questions, but it's not obvious that I can.</p><cite>P1</cite></blockquote>

    <h2>Finding 02 — Dealbreakers are hard to find and harder to understand</h2>
    <p>Dating Preferences and Dealbreakers are how you control your match pool. Both fail at the
      first step: discovery.</p>
    <ul>
      <li>Every participant prompted to find Dating Preferences needed multiple attempts, wandering
        between pages until they stumbled on it. The icon is small and gives no clue what it does.</li>
      <li><strong>5 of 10</strong> could not easily locate Dealbreaker options — they're scattered
        across individual preference categories rather than centralized anywhere.</li>
      <li><strong>4 of 10</strong> didn't understand what a Dealbreaker <em>is</em>. One thought it
        was a tiebreaker for choosing between similar profiles, rather than a filter that excludes
        people.</li>
      <li>Hinge does display "Dealbreakers will limit who you see and who sees you" — none of those
        four noticed it.</li>
    </ul>
    <blockquote><p>The dating preference… finding that… I could find everything else but that.
      It's kind of like a small icon on the top left. You would not think that's that.</p>
      <cite>P6</cite></blockquote>
    <blockquote><p>I don't know, that one says Dealbreaker, and nothing else says Dealbreaker,
      so…</p><cite>P8</cite></blockquote>

    <h2>Finding 03 — People can't tell what's free</h2>
    <p>Participants weren't hostile to premium features. They were frustrated by not knowing where
      the line was until they hit it.</p>
    <ul>
      <li><strong>7 of 10</strong> didn't realize how many features were premium-locked until they
        ran into them mid-exploration.</li>
      <li>Two discovered that preferences they'd set during <em>free</em> onboarding — like Dating
        Intentions — couldn't be changed later without upgrading. The choice was made before anyone
        said it was permanent.</li>
      <li>One participant found the swipe limit only by exhausting it. No counter, no warning.</li>
    </ul>
    <blockquote><p>Nope, that takes Hinge+. Dating intentions, that takes Hinge+. Active today,
      that takes Hinge+. Let me guess.</p><cite>P8</cite></blockquote>

    <h2>What we recommended</h2>
    <p>We ranked every fix by frequency and severity — how many participants hit it, and how badly
      it blocked them. Prioritising by user count rather than engineering effort kept the
      conversation on impact.</p>
    {{REC_CHART}}
    <p>The back button tops the list because it is the rare case where severity and reach line up
      perfectly: it affected everyone, it blocks error recovery entirely, and it is a small,
      well-understood piece of interface to add.</p>

    <h2>What I'd do differently</h2>
    <ul>
      <li>We used convenience and snowball sampling — most participants had an existing connection
        to someone on the team. That likely made people more comfortable than a stranger would
        have been, and more generous in their feedback.</li>
      <li>Eight new users to two lapsed users is lopsided. A more even split would have said more
        about what brings someone back after six months away.</li>
      <li>Everyone was 18–29. That's Hinge's core demographic, but it means we can say nothing
        about how the same onboarding reads to someone older.</li>
      <li>Two sessions were disrupted by genuine app bugs. Useful data about reliability, but it
        cost us task time we'd planned for the dealbreaker section.</li>
    </ul>

    <div class="contact rv" style="margin-top:50px">
      <h2>Next case study</h2>
      <p>Two quarters of community research for a Seattle food bank — and the award that came
        with it.</p>
      <div class="cbtns">
        <a class="btn" href="work-rvfb.html">Rainier Valley Food Bank →</a>
        <a class="btn ghost" href="index.html#work">All work</a>
      </div>
    </div>
  </section>
</div>"""
hinge = hinge.replace("{REC_CHART}", rec_chart())


# ═══════════════════════════════════════════════════════════════
# ABOUT
# ═══════════════════════════════════════════════════════════════
about = """
<div class="cs-hero">
  <div class="wrap">
    <span class="label">About Wenyi</span>
    <h1>Hi there, I'm Wenyi :)</h1>
    <p class="lede">Product designer and UX researcher. I combine user research, storytelling and
      visual craft to turn human insight into products that actually support people.</p>
  </div>
</div>

<div class="narrow cs-body">
  <section style="padding-top:44px">
    <h2>My story</h2>
    <p>I'm a recent graduate of the University of Washington Seattle with a B.S. in
      Human-Centered Design &amp; Engineering. My path through HCDE shaped the way I think: start
      with people, notice the context, make the next step easier, and keep refining with care.</p>
    <p>Before any of that, I worked as a barista. It's the reason my second case study is a
      platform for independent cafés — I already knew what a slow Tuesday feels like from behind
      the counter, what it's like when the one fluent English speaker is also the only person on
      register, and how much of a small business runs on relationships nobody has time to
      maintain. Going back into those cafés with a research protocol felt less like fieldwork and
      more like finally asking the questions I'd been sitting on for years.</p>
    <p>That's the thread through everything here. I'm drawn to the gap between something being
      <em>available</em> and someone being able to <em>reach</em> it — a food bank three blocks
      away that nobody's heard of, a café two doors down that can't get a reply.</p>

    <h2>What I'm looking for</h2>
    <p>Product design and UX research roles where research actually reaches the final artifact.
      I care about community-centred work, accessible systems, and teams that let a designer go
      to the site before writing the hypothesis.</p>

    <h2>Experience</h2>
    <div class="timeline">
      <div class="tl-item rv"><span class="label">Jan 2026 — Jun 2026 · Rainier Valley Food Bank Capstone</span>
        <h3>Product Designer, UX Researcher &amp; Project Manager</h3>
        <p>Covalence × Rainier Valley Food Bank. Led the visual identity and prototype suite
          across every deliverable, ran recruitment and multilingual survey distribution, and
          project-managed the phase where research became artifacts. Won the HCDE Capstone
          Engagement award. <a href="work-rvfb.html">Read the case study →</a></p></div>

      <div class="tl-item rv"><span class="label">2024 — 2026 · Society of Asian Scientists and Engineers at UW</span>
        <h3>Creative Director &amp; Marketing</h3>
        <p>Student-led engineering club at UW. Built the
          chapter's visual presence and ran marketing across events and social — the longest-running
          design practice on this page, and where most of my instinct for brand and community
          came from.</p></div>

      <div class="tl-item rv"><span class="label">Sep 2025 — Dec 2025 · Usability Study at UW</span>
        <h3>UX Experience &amp; UX Researcher</h3>
        <p>Hinge usability study. Moderated and took notes across think-aloud sessions with ten
          participants, then open-coded and affinity-mapped the results into three findings and a
          ranked set of recommendations. <a href="work-hinge.html">Read the case study →</a></p></div>

      <div class="tl-item rv"><span class="label">2024 — 2025 · Service Design at UW</span>
        <h3>Product Design &amp; Project Lead</h3>
        <p>Loko — a collaboration platform for independent local businesses. Led the product
          design and the team, ran café field studies and co-design sessions, and owned the
          profile-depth findings that came out of user testing.
          <a href="work-loko.html">Read the case study →</a></p></div>
    </div>

    <h2>Skills</h2>
    <div class="pills">
      <span class="pill">UX Research</span><span class="pill">Interaction Design</span>
      <span class="pill">Prototyping</span><span class="pill">Product Strategy</span>
      <span class="pill">Visual Systems</span><span class="pill">Accessibility</span>
      <span class="pill">Service Design</span><span class="pill">Figma</span>
      <span class="pill">Framer</span><span class="pill">Storytelling</span>
    </div>

    <h2>Beyond design</h2>
    <p>I make content for social media, edit video, and spend as much time as I can with people I
      love and in places I haven't been yet. It keeps me observant — and most of what I notice
      ends up in the <a href="playground.html">playground</a>.</p>

    <div class="contact rv" style="margin-top:50px">
      <h2>Say hi</h2>
      <p>I'd love to hear what you're working on.</p>
      <div class="cbtns">
        <a class="btn" href="mailto:wenyitsai6@gmail.com">wenyitsai6@gmail.com</a>
        <a class="btn ghost" href="work.html">See my work</a>
      </div>
    </div>
  </section>
</div>"""


# ═══════════════════════════════════════════════════════════════
# PLAYGROUND
# ═══════════════════════════════════════════════════════════════
playground = """
<div class="cs-hero">
  <div class="wrap">
    <span class="label">Playground</span>
    <h1>Everything that isn't a case study.</h1>
    <p class="lede">The things I make when there's no research question attached — posters, film
      photos, edits, doodles at 1am. It's where the taste comes from. Drag them around.</p>
  </div>
</div>

<div class="wrap">
  <section style="padding-top:36px">
    <div class="board" id="board"></div>
    <div class="gv" id="gv">
      <div class="sec-head"><h2 id="gvTitle">—</h2>
        <button class="btn ghost" id="gvClose">← All shelves</button></div>
      <div class="masonry" id="gvGrid"></div>
    </div>
  </section>
</div>

<script>
/* Add work here — see portfolio-content-spec.md §7b for the schema.
   items: {type:'image',src,alt} | {type:'video',src,poster} | {type:'note',text} */
var SHELVES = [
  { id:'posters', title:'Posters & Social', emoji:'🎨', x:3,  y:2,  rot:-4, items:[] },
  { id:'photo',   title:'Photography',      emoji:'📷', x:29, y:22, rot:3,  items:[] },
  { id:'motion',  title:'Motion & Edits',   emoji:'🎞️', x:55, y:1,  rot:-2, items:[] },
  { id:'sketch',  title:'Sketches',         emoji:'✏️', x:14, y:52, rot:5,  items:[] },
  { id:'life',    title:'The Collage',      emoji:'🌱', x:47, y:48, rot:-6, items:[] }
];

(function(){
  var board=document.getElementById('board'), gv=document.getElementById('gv'),
      grid=document.getElementById('gvGrid'), title=document.getElementById('gvTitle'),
      cur=document.getElementById('cur'), H=[300,210,380,250,330,190];

  SHELVES.forEach(function(s){
    var el=document.createElement('div');
    el.className='shelf'; el.tabIndex=0; el.setAttribute('role','button');
    el.style.left=s.x+'%'; el.style.top=s.y+'%'; el.style.transform='rotate('+s.rot+'deg)';
    el.innerHTML='<div class="th">'+s.emoji+'</div><h3>'+s.title+'</h3>'+
      '<div class="cnt">'+(s.items.length?s.items.length+' pieces':'Empty — add yours')+'</div>';
    el.addEventListener('click',function(){ if(!el.dataset.moved) open(s); });
    el.addEventListener('keydown',function(e){
      if(e.key==='Enter'||e.key===' '){ e.preventDefault(); open(s); }});
    drag(el); board.appendChild(el);
  });

  function open(s){
    title.textContent=s.title; grid.innerHTML='';
    if(!s.items.length){
      H.forEach(function(h,i){
        var d=document.createElement('div'); d.className='slot'; d.style.height=h+'px';
        d.innerHTML='<div><em>Slot '+String(i+1).padStart(2,'0')+'</em>'+
                    '<span class="label">'+s.title+'</span></div>';
        grid.appendChild(d);
      });
    } else {
      s.items.forEach(function(it){
        var d=document.createElement('div'); d.className='slot';
        if(it.type==='note'){ d.style.padding='26px';
          d.innerHTML='<p style="margin:0;font-size:.95rem">'+it.text+'</p>'; }
        else { d.style.cssText='padding:0;border-style:solid;overflow:hidden';
          d.innerHTML = it.type==='video'
            ? '<video src="'+it.src+'" poster="'+(it.poster||'')+'" muted loop playsinline autoplay style="width:100%;display:block"></video>'
            : '<img src="'+it.src+'" alt="'+(it.alt||'')+'" style="width:100%;display:block" loading="lazy">'; }
        grid.appendChild(d);
      });
    }
    board.classList.add('off'); gv.classList.add('on');
    window.scrollTo({top:0,behavior:'smooth'});
  }
  document.getElementById('gvClose').onclick=function(){
    gv.classList.remove('on'); board.classList.remove('off'); };

  function drag(el){
    var sx,sy,ox,oy,on=false;
    el.addEventListener('pointerdown',function(e){
      if(matchMedia('(max-width:860px)').matches) return;
      on=true; delete el.dataset.moved; el.setPointerCapture(e.pointerId);
      el.classList.add('drag'); if(cur) cur.classList.add('grabbing');
      sx=e.clientX; sy=e.clientY;
      var r=el.getBoundingClientRect(), p=board.getBoundingClientRect();
      ox=r.left-p.left; oy=r.top-p.top;
    });
    el.addEventListener('pointermove',function(e){
      if(!on) return;
      var dx=e.clientX-sx, dy=e.clientY-sy;
      if(Math.abs(dx)>4||Math.abs(dy)>4) el.dataset.moved='1';
      el.style.left=(ox+dx)+'px'; el.style.top=(oy+dy)+'px';
    });
    function end(){ if(!on) return; on=false; el.classList.remove('drag');
      if(cur) cur.classList.remove('grabbing');
      setTimeout(function(){ delete el.dataset.moved; },60); }
    el.addEventListener('pointerup',end); el.addEventListener('pointercancel',end);
  }
})();
</script>"""


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    print("Building:")
    page("index.html", "Wenyi Tsai — Product Designer & UX Researcher",
         "Product designer and UX researcher working on the gap between available and reachable.", home)
    page("work-rvfb.html", "Rainier Valley Food Bank — Wenyi Tsai",
         "Award-winning community outreach service design for the Rainier Valley Food Bank.", rvfb)
    page("work-loko.html", "Loko — Wenyi Tsai",
         "Service design for independent business collaboration, built from café fieldwork.", loko)
    page("work-hinge.html", "Hinge Usability Study — Wenyi Tsai",
         "A usability study of Hinge's onboarding flow and dealbreaker filters.", hinge)
    page("playground.html", "Playground — Wenyi Tsai",
         "Posters, photography, motion and everything that isn't a case study.", playground)
    print("Done.")
