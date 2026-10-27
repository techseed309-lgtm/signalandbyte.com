"""Build the Signal & Byte site's written pages.

    python tools/build.py

Reads content/articles/*.md and content/blog/*.md (front matter + Markdown), writes
articles/<slug>/index.html, blog/<slug>/index.html, the two listing pages, feed.xml and
sitemap.xml, and refreshes the shared header, footer and "latest writing" block in
index.html, privacy.html and 404.html. Standard library only.

Front matter (between --- lines): title, description, date (YYYY-MM-DD), tags (comma list),
video (YouTube id, optional), image (optional path or URL for the card/share image).
"""
import datetime as dt
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://signalandbyte.com"
CHANNEL = "https://www.youtube.com/channel/UCQav0b3vZaTlio1zetRh4ig"
SOCIAL = [  # key, label, url, css class, call to action
    ("youtube", "YouTube", CHANNEL, "yt", "Explainers and Shorts"),
    ("tiktok", "TikTok", "https://www.tiktok.com/@signalandbyte", "tt", "Shorts, every story"),
    ("x", "X", "https://x.com/techseedhq", "x", "Threads and quick takes"),
    ("linkedin", "LinkedIn", "https://www.linkedin.com/company/signalandbyte", "li", "For builders and teams"),
]
COLLECTIONS = {
    "articles": ("Articles", "Written explainers", "The story behind each video, in writing: what happened, how it works, and every source we used."),
    "blog": ("Blog", "Notes from the channel", "News about Signal & Byte, how we check our stories, and what we learn along the way."),
}


def icon(name):
    svg = (ROOT / "tools" / "icons" / f"{name}.svg").read_text(encoding="utf-8")
    d = re.search(r'<path d="([^"]+)"', svg).group(1)
    return f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="{d}"/></svg>'


ICONS = {k: icon(k) for k, *_ in SOCIAL}
MARK = ('<svg viewBox="0 0 160 64" aria-hidden="true"><path d="M8 32 C18 8, 28 8, 38 32 S58 56, 68 32" fill="none" stroke="#3D5CFF" stroke-width="7" stroke-linecap="round"/>'
        '<g fill="#FFB020"><rect x="78" y="42" width="7" height="10" rx="1.5"/><rect x="88" y="12" width="7" height="40" rx="1.5"/><rect x="98" y="42" width="7" height="10" rx="1.5"/>'
        '<rect x="108" y="12" width="7" height="40" rx="1.5"/><rect x="118" y="42" width="7" height="10" rx="1.5"/><rect x="128" y="42" width="7" height="10" rx="1.5"/>'
        '<rect x="138" y="12" width="7" height="40" rx="1.5"/><rect x="148" y="12" width="7" height="40" rx="1.5"/></g></svg>')

HEADER = f"""<header>
  <div class="wrap">
    <a class="brand" href="/" aria-label="Signal &amp; Byte home">
      {MARK}
      Signal &amp; Byte
    </a>
    <button class="menu" aria-label="Open menu" aria-expanded="false" aria-controls="nav"><span></span></button>
    <nav class="nav" id="nav" aria-label="Main">
      <a href="/#videos">Videos</a>
      <a href="/articles/">Articles</a>
      <a href="/blog/">Blog</a>
      <a href="/#about">About</a>
      <a href="/#partners">Work with us</a>
      <a href="/#contact">Contact</a>
      <a class="btn yt sm" href="{CHANNEL}?sub_confirmation=1" target="_blank" rel="noopener">Subscribe</a>
    </nav>
  </div>
</header>"""


def follow_buttons():
    return "\n".join(f'<a class="fbtn {c}" href="{u}" target="_blank" rel="noopener">{ICONS[k]}{l}</a>' for k, l, u, c, _ in SOCIAL)


FOOTER = f"""<footer>
  <div class="wrap">
    <div>
      <div style="font:800 15px Unbounded,sans-serif;color:var(--ink)">Signal &amp; Byte</div>
      <div class="legal">© <span id="y">2026</span> Signal &amp; Byte · <a href="/articles/">Articles</a> · <a href="/blog/">Blog</a> · <a href="/feed.xml">RSS</a> · <a href="/privacy.html">Privacy</a></div>
    </div>
    <nav class="follow" aria-label="Follow Signal &amp; Byte">
{follow_buttons()}
    </nav>
  </div>
</footer>"""

SCRIPT = """<script>
  const btn = document.querySelector('.menu'), nav = document.getElementById('nav');
  btn.addEventListener('click', () => { const o = nav.classList.toggle('open'); btn.setAttribute('aria-expanded', o); btn.setAttribute('aria-label', o ? 'Close menu' : 'Open menu'); });
  nav.addEventListener('click', e => { if (e.target.closest('a')) { nav.classList.remove('open'); btn.setAttribute('aria-expanded', false); } });
  document.getElementById('y').textContent = new Date().getFullYear();
  document.querySelectorAll('.yt-lite').forEach(b => b.addEventListener('click', () => {
    const f = document.createElement('iframe');
    f.src = 'https://www.youtube-nocookie.com/embed/' + b.dataset.id + '?autoplay=1&rel=0';
    f.title = b.getAttribute('aria-label'); f.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen'; f.allowFullscreen = true;
    b.replaceChildren(f);
  }, { once: true }));
  document.querySelectorAll('[data-copy]').forEach(b => b.addEventListener('click', async () => {
    try { await navigator.clipboard.writeText(b.dataset.copy); b.lastChild.textContent = 'Link copied'; } catch { b.lastChild.textContent = 'Copy failed'; }
    setTimeout(() => b.lastChild.textContent = 'Copy link', 2000);
  }));
</script>"""


def head(title, description, url, image, kind="website", extra=""):
    t, d = html.escape(title), html.escape(description)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{url}">
<meta property="og:site_name" content="Signal &amp; Byte">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="{kind}">
<meta property="og:image" content="{image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#F7F8FC">
<link rel="icon" href="/avatar-signal-bits.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="alternate" type="application/rss+xml" title="Signal &amp; Byte" href="/feed.xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@700;800&family=Schibsted+Grotesk:wght@400;500;700&family=Martian+Mono:wght@400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
{extra}</head>
<body>
{HEADER}
"""


# --- Markdown (the subset our posts use) -------------------------------------------------------

def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)

    def link(m):
        label, url = m.group(1), m.group(2).replace('"', "%22")
        ext = url.startswith("http") and not url.startswith(SITE)
        return f'<a href="{url}"' + (' target="_blank" rel="noopener"' if ext else "") + f">{label}</a>"
    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, text)


def markdown(src):
    out, para, items, kind = [], [], [], None

    def flush():
        nonlocal para, items, kind
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
        if items:
            out.append(f"<{kind}>" + "".join(f"<li>{inline(i)}</li>" for i in items) + f"</{kind}>")
        para, items, kind = [], [], None

    quote = []
    for line in src.splitlines() + [""]:
        s = line.rstrip()
        if s.startswith(">"):
            flush(); quote.append(s[1:].strip()); continue
        if quote:
            out.append(f"<blockquote><p>{inline(' '.join(quote))}</p></blockquote>"); quote = []
        if not s.strip():
            flush(); continue
        if m := re.match(r"^(#{2,3}) (.+)", s):
            flush(); n = len(m.group(1))
            hid = re.sub(r"[^a-z0-9]+", "-", m.group(2).lower()).strip("-")
            out.append(f'<h{n} id="{hid}">{inline(m.group(2))}</h{n}>'); continue
        if m := re.match(r"^(-|\d+\.) (.+)", s):
            k = "ul" if m.group(1) == "-" else "ol"
            if para or (kind and kind != k):
                flush()
            kind = k; items.append(m.group(2)); continue
        if items and line.startswith("  "):
            items[-1] += " " + s.strip(); continue
        if items:
            flush()
        para.append(s.strip())
    return "\n".join(out)


# --- content ------------------------------------------------------------------------------------

def load(collection):
    posts = []
    for f in sorted((ROOT / "content" / collection).glob("*.md")):
        raw = f.read_text(encoding="utf-8")
        m = re.match(r"---\n(.*?)\n---\n(.*)", raw, re.S)
        if not m:
            sys.exit(f"{f}: missing front matter")
        meta = dict(line.split(":", 1) for line in m.group(1).splitlines() if ":" in line)
        meta = {k.strip(): re.sub(r"^'(.*)'$|^\"(.*)\"$", lambda m: m.group(1) or m.group(2) or "", v.strip()) for k, v in meta.items()}
        for key in ("title", "description", "date"):
            if not meta.get(key):
                sys.exit(f"{f}: front matter needs {key}")
        slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", f.stem)
        body = m.group(2)
        words = len(re.findall(r"\w+", body))
        vid = meta.get("video", "")
        image = meta.get("image") or (f"https://i.ytimg.com/vi/{vid}/hq720.jpg" if vid else "/og.png")
        posts.append({
            **meta, "collection": collection, "slug": slug, "body": body, "minutes": max(1, round(words / 230)),
            "tags": [t.strip() for t in meta.get("tags", "").split(",") if t.strip()], "video": vid,
            "image": image, "url": f"/{collection}/{slug}/",
        })
    return sorted(posts, key=lambda p: p["date"], reverse=True)


def nice_date(d):
    return dt.date.fromisoformat(d).strftime("%-d %B %Y") if sys.platform != "win32" else dt.date.fromisoformat(d).strftime("%#d %B %Y")


def abs_url(u):
    return u if u.startswith("http") else SITE + u


def card(p, show_kind=False):
    kind = COLLECTIONS[p["collection"]][0][:-1] if p["collection"] == "articles" else "Blog"
    tags = "|".join(p["tags"])
    return (f'<a class="acard" href="{p["url"]}" data-tags="{html.escape(tags)}" data-text="{html.escape((p["title"] + " " + p["description"] + " " + tags).lower())}">'
            f'<img src="{p["image"]}" alt="" loading="lazy" width="1280" height="720">'
            f'<span class="body"><span class="meta">{(kind + " · ") if show_kind else ""}{nice_date(p["date"])} · {p["minutes"]} min read</span>'
            f'<h3>{html.escape(p["title"])}</h3><p>{html.escape(p["description"])}</p></span></a>')


def article_page(p, siblings):
    name, _, _ = COLLECTIONS[p["collection"]]
    url = abs_url(p["url"])
    ld = {"@context": "https://schema.org", "@type": "Article" if p["collection"] == "articles" else "BlogPosting",
          "headline": p["title"], "description": p["description"], "datePublished": p["date"], "image": abs_url(p["image"]),
          "author": {"@type": "Organization", "name": "Signal & Byte", "url": SITE},
          "publisher": {"@type": "Organization", "name": "Signal & Byte", "logo": {"@type": "ImageObject", "url": SITE + "/logo-400.png"}},
          "mainEntityOfPage": url}
    extra = f'<script type="application/ld+json">{json.dumps(ld)}</script>\n'
    video = ""
    if p["video"]:
        video = (f'<button class="yt-lite" data-id="{p["video"]}" aria-label="Play video: {html.escape(p["title"])}">'
                 f'<img src="https://i.ytimg.com/vi/{p["video"]}/hq720.jpg" alt="" width="1280" height="720">'
                 f'<span class="play" aria-hidden="true"></span><span class="cap">Watch the video</span></button>')
    tags = " · ".join(html.escape(t) for t in p["tags"])
    q = html.escape(p["title"])
    from urllib.parse import quote
    share = (f'<div class="share"><span>Share</span>'
             f'<a class="fbtn x" href="https://x.com/intent/post?text={quote(p["title"], safe="")}&amp;url={quote(url, safe="")}" target="_blank" rel="noopener">{ICONS["x"]}Post</a>'
             f'<a class="fbtn li" href="https://www.linkedin.com/sharing/share-offsite/?url={quote(url, safe="")}" target="_blank" rel="noopener">{ICONS["linkedin"]}Share</a>'
             f'<button class="fbtn" type="button" data-copy="{url}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M10 14a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1M14 10a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg><span>Copy link</span></button></div>')
    more = [s for s in siblings if s["slug"] != p["slug"]][:3]
    related = ""
    if more:
        related = (f'<section class="alt"><div class="wrap"><div class="head"><div><p class="kicker">Keep reading</p><h2>More {name.lower()}</h2></div>'
                   f'<a class="btn" href="/{p["collection"]}/">All {name.lower()}</a></div><div class="grid3">{"".join(card(s) for s in more)}</div></div></section>')
    return (head(f'{p["title"]} · Signal & Byte', p["description"], url, abs_url(p["image"]), "article", extra) +
            f"""<main>
<article class="article">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/{p["collection"]}/">{name}</a></nav>
  <p class="kicker">{tags}</p>
  <h1>{q}</h1>
  <p class="dek">{html.escape(p["description"])}</p>
  <div class="meta"><span>{nice_date(p["date"])}</span><span>{p["minutes"]} min read</span><span>By Signal &amp; Byte</span></div>
  {video}
  <div class="prose">
{markdown(p["body"])}
  </div>
  {share}
</article>
{related}
<section><div class="wrap"><div class="band">
  <div><h2>Get the next story first</h2><p>New explainers and Shorts on YouTube. Subscribe and they show up in your feed.</p></div>
  <a class="btn" href="{CHANNEL}?sub_confirmation=1" target="_blank" rel="noopener">Subscribe on YouTube</a>
</div></div></section>
</main>
{FOOTER}
{SCRIPT}
</body>
</html>
""")


def listing_page(collection, posts):
    name, kicker, lead = COLLECTIONS[collection]
    tags = sorted({t for p in posts for t in p["tags"]})
    chips = "".join(f'<button class="chip" type="button" aria-pressed="false" data-tag="{html.escape(t)}">{html.escape(t)}</button>' for t in tags)
    filt = """<script>
  const cards = [...document.querySelectorAll('.acard')], q = document.getElementById('q'), empty = document.querySelector('.empty');
  let tag = '';
  function apply() {
    const s = q.value.trim().toLowerCase(); let n = 0;
    cards.forEach(c => { const ok = (!s || c.dataset.text.includes(s)) && (!tag || c.dataset.tags.split('|').includes(tag)); c.style.display = ok ? '' : 'none'; n += ok; });
    empty.style.display = n ? 'none' : 'block';
  }
  q.addEventListener('input', apply);
  document.querySelectorAll('.chip').forEach(b => b.addEventListener('click', () => {
    const on = b.getAttribute('aria-pressed') !== 'true';
    document.querySelectorAll('.chip').forEach(x => x.setAttribute('aria-pressed', 'false'));
    b.setAttribute('aria-pressed', on); tag = on ? b.dataset.tag : ''; apply();
  }));
</script>"""
    url = f"{SITE}/{collection}/"
    return (head(f"{name} · Signal & Byte", lead, url, SITE + "/og.png") +
            f"""<main>
<div class="page-hero"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / {name}</nav>
  <p class="kicker">{kicker}</p>
  <h1>{name}</h1>
  <p class="lead">{lead}</p>
</div></div>
<section style="padding-top:8px"><div class="wrap">
  <div class="toolbar">
    <input class="search" id="q" type="search" placeholder="Search {name.lower()}" aria-label="Search {name.lower()}">
    <div class="chips" role="group" aria-label="Filter by topic">{chips}</div>
  </div>
  <div class="grid3">
{chr(10).join(card(p) for p in posts)}
  </div>
  <p class="empty">Nothing matches that yet. Try another word, or <a href="mailto:hello@signalandbyte.com?subject=Topic%20idea">suggest the topic</a>.</p>
</div></section>
<section class="alt"><div class="wrap">
  <p class="kicker">Follow along</p><h2>Get every story</h2>
  <p class="lead" style="margin-bottom:22px">New explainers land on YouTube first, with Shorts on TikTok and quick takes on X and LinkedIn.</p>
  <div class="follow">{follow_buttons()}</div>
  <p style="margin-top:18px;color:var(--soft);font-size:15px">Prefer a reader? <a href="/feed.xml">Subscribe by RSS</a>.</p>
</div></section>
</main>
{FOOTER}
{SCRIPT}
{filt}
</body>
</html>
""")


def feed(posts):
    def item(p):
        return (f"<item><title>{html.escape(p['title'])}</title><link>{abs_url(p['url'])}</link><guid>{abs_url(p['url'])}</guid>"
                f"<pubDate>{dt.datetime.fromisoformat(p['date']).strftime('%a, %d %b %Y 08:00:00 +0000')}</pubDate>"
                f"<category>{COLLECTIONS[p['collection']][0]}</category><description>{html.escape(p['description'])}</description></item>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>Signal &amp; Byte</title>'
            f"<link>{SITE}/</link><description>Tech news, decoded.</description><language>en</language>"
            + "".join(item(p) for p in posts) + "</channel></rss>\n")


def sitemap(posts):
    urls = ["/", "/articles/", "/blog/", "/privacy.html"] + [p["url"] for p in posts]
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "".join(f"  <url><loc>{SITE}{u}</loc></url>\n" for u in urls) + "</urlset>\n")


def swap(text, start, end, body, path):
    pat = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if not pat.search(text):
        sys.exit(f"{path}: block {start!r} not found")
    return pat.sub(lambda _: start + "\n" + body + "\n" + end, text)


def refresh_shell(path, latest=None):
    f = ROOT / path
    s = f.read_text(encoding="utf-8")
    s = re.sub(r"<header>.*?</header>", lambda _: HEADER, s, count=1, flags=re.S)
    s = re.sub(r"<footer>.*?</footer>", lambda _: FOOTER, s, count=1, flags=re.S)
    if "<!-- follow:start -->" in s:
        s = swap(s, "<!-- follow:start -->", "<!-- follow:end -->", follow_buttons(), path)
    if "<!-- followbig:start -->" in s:
        big = "\n".join(f'<a class="fcard {c}" href="{u}" target="_blank" rel="noopener">{ICONS[k]}<strong>{l}</strong><span>{cta}</span></a>' for k, l, u, c, cta in SOCIAL)
        s = swap(s, "<!-- followbig:start -->", "<!-- followbig:end -->", big, path)
    s = re.sub(r"<script>\n  const btn.*?</script>", lambda _: SCRIPT, s, count=1, flags=re.S)
    if latest is not None and "<!-- writing:start -->" in s:
        s = swap(s, "<!-- writing:start -->", "<!-- writing:end -->", "\n".join(card(p, True) for p in latest), path)
    f.write_text(s, encoding="utf-8", newline="\n")


PAGES = {
    "privacy.html": ("Privacy", "How signalandbyte.com handles your data: it collects none.", """
<p>Last updated 27 October 2026.</p>
<h2>What this site collects</h2>
<p>Nothing. This site sets no cookies, runs no analytics or ads, and has no forms or sign-ups.</p>
<h2>Third parties</h2>
<p>The site is hosted on GitHub Pages, which may log visitor IP addresses for security purposes (see GitHub's privacy statement). Fonts load from Google Fonts, and video thumbnails load from YouTube's image servers. A video in an article loads from YouTube's privacy-enhanced player (youtube-nocookie.com) only when you press play. Share and follow buttons are plain links: nothing is sent to those services until you click one, and then their own privacy policies apply.</p>
<h2>Email</h2>
<p>If you email us, we use your message only to reply. We never add you to a mailing list or share your address.</p>
<h2>Contact</h2>
<p><a href="mailto:hello@signalandbyte.com">hello@signalandbyte.com</a></p>"""),
    "404.html": ("Lost the signal", "That page doesn't exist.", """
<p>That page doesn't exist, or it moved.</p>
<p><a class="btn primary" href="/">Back to the home page</a> &nbsp; <a class="btn" href="/articles/">Read the articles</a></p>"""),
}


def simple_page(title, desc, name, body):
    return (head(f"{title} · Signal & Byte", desc, f"{SITE}/{name}", SITE + "/og.png") +
            f"""<main><article class="article">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / {html.escape(title)}</nav>
  <h1>{html.escape(title)}</h1>
  <div class="prose">{body}</div>
</article></main>
{FOOTER}
{SCRIPT}
</body>
</html>
""")


def main():
    everything = []
    for collection in COLLECTIONS:
        posts = load(collection)
        everything += posts
        for p in posts:
            out = ROOT / collection / p["slug"] / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(article_page(p, posts), encoding="utf-8", newline="\n")
        (ROOT / collection / "index.html").write_text(listing_page(collection, posts), encoding="utf-8", newline="\n")
        print(f"{collection}: {len(posts)}")
    everything.sort(key=lambda p: p["date"], reverse=True)
    (ROOT / "feed.xml").write_text(feed(everything), encoding="utf-8", newline="\n")
    (ROOT / "sitemap.xml").write_text(sitemap(everything), encoding="utf-8", newline="\n")
    for name, (title, desc, body) in PAGES.items():
        (ROOT / name).write_text(simple_page(title, desc, name, body), encoding="utf-8", newline="\n")
    refresh_shell("index.html", everything[:3])


if __name__ == "__main__":
    main()
