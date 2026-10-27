"""Refresh the video sections of index.html from the channel's public YouTube feed.

Rewrites the blocks between <!-- videos:start --> / <!-- videos:end --> and
<!-- shorts:start --> / <!-- shorts:end -->. Standard library only, so it runs
as-is in GitHub Actions (daily) and on the laptop:  python tools/update_videos.py
"""
import html
import pathlib
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

CHANNEL = "UCQav0b3vZaTlio1zetRh4ig"
FEED = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL}"
NS = {"a": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015"}
PAGE = pathlib.Path(__file__).resolve().parent.parent / "index.html"
UA = {"User-Agent": "Mozilla/5.0 (signalandbyte.com video list)"}
LONG_N, SHORTS_N = 6, 4


def is_short(video_id):
    """Only Shorts have the vertical thumbnail oar2.jpg (404 for normal videos)."""
    req = urllib.request.Request(f"https://i.ytimg.com/vi/{video_id}/oar2.jpg", method="HEAD", headers=UA)
    try:
        return urllib.request.urlopen(req, timeout=20).status == 200
    except OSError:
        return False


def fetch():
    with urllib.request.urlopen(urllib.request.Request(FEED, headers=UA), timeout=30) as r:
        root = ET.fromstring(r.read())
    for e in root.findall("a:entry", NS):
        yield e.find("yt:videoId", NS).text, e.find("a:title", NS).text, e.find("a:published", NS).text[:10]


def card(vid, title, date):
    t = html.escape(re.sub(r"\s*#shorts\s*$", "", title, flags=re.I))
    return (f'<a class="vcard" href="https://www.youtube.com/watch?v={vid}" target="_blank" rel="noopener">'
            f'<img src="https://i.ytimg.com/vi/{vid}/hq720.jpg" alt="" loading="lazy" width="1280" height="720"'
            f' onerror="this.onerror=null;this.src=\'https://i.ytimg.com/vi/{vid}/hqdefault.jpg\'">'
            f'<span class="vtitle">{t}</span><span class="vdate">{date}</span></a>')


def short(vid, title):
    t = html.escape(re.sub(r"\s*#shorts\s*$", "", title, flags=re.I))
    return (f'<a class="scard" href="https://www.youtube.com/shorts/{vid}" target="_blank" rel="noopener">'
            f'<img src="https://i.ytimg.com/vi/{vid}/oar2.jpg" alt="" loading="lazy" width="270" height="480"'
            f' onerror="this.onerror=null;this.src=\'https://i.ytimg.com/vi/{vid}/hqdefault.jpg\'">'
            f'<span class="vtitle">{t}</span></a>')


def replace(page, tag, body):
    pat = re.compile(rf"(<!-- {tag}:start -->).*?(<!-- {tag}:end -->)", re.S)
    if not pat.search(page):
        sys.exit(f"marker {tag} missing in {PAGE}")
    return pat.sub(lambda m: m.group(1) + "\n" + body + "\n" + m.group(2), page)


def main():
    longs, shorts = [], []
    for vid, title, date in fetch():
        (shorts if is_short(vid) else longs).append((vid, title, date))
    if not longs:
        sys.exit("feed returned no long videos; leaving the page unchanged")
    page = PAGE.read_text(encoding="utf-8")
    vid, title, _ = longs[0]
    page = replace(page, "featured", (
        f'<a class="feature" href="https://www.youtube.com/watch?v={vid}" target="_blank" rel="noopener">'
        f'<img src="https://i.ytimg.com/vi/{vid}/maxresdefault.jpg" alt="" width="1280" height="720"'
        f' onerror="this.onerror=null;this.src=\'https://i.ytimg.com/vi/{vid}/hqdefault.jpg\'">'
        f'<span class="play" aria-hidden="true"></span>'
        f'<span class="ftext"><span class="kicker">Latest episode</span>{html.escape(title)}</span></a>'))
    page = replace(page, "videos", "\n".join(card(*v) for v in longs[1:LONG_N + 1]))
    page = replace(page, "shorts", "\n".join(short(v, t) for v, t, _ in shorts[:SHORTS_N]))
    PAGE.write_text(page, encoding="utf-8", newline="\n")
    print(f"{len(longs[:LONG_N])} videos, {len(shorts[:SHORTS_N])} shorts")


if __name__ == "__main__":
    main()
