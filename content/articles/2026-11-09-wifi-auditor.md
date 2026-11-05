---
title: "Is your Wi-Fi password crackable? Build a free auditor and find out"
description: Wi-Fi guessing happens offline, so the only real lock is your password's length. We built a free tool that estimates your own crack-time, checks the doors that ignore your password (WPS, evil twins, defaults) and grades your network, with the one thing to fix first.
date: 2026-11-09
tags: Security, Build, Networking
video: xwoUZkj0ytw
---
A stranger parked outside your house should not be able to open your Wi-Fi. Whether they can comes down to one thing most people never think about: how long your password is. So we built a small, free tool that checks your **own** network the way an attacker would look at it, tells you in plain time whether your password would hold, and then checks the ways in that ignore your password completely. **The script, a Windows app and a Claude/ChatGPT skill are free on [our GitHub](https://github.com/techseed309-lgtm/wifi-auditor).**

> This is a defensive audit of a network you own. Testing a network you don't own or have written permission for is a crime (US CFAA, UK Computer Misuse Act, and equivalents). Nothing here touches anyone else's network.

## Why the only real lock is length
When someone attacks Wi-Fi, the guessing does not happen at your router, where a wrong try is slow and noticed. They record the brief "handshake" your device and router exchange when you connect, take it away, and guess against it **offline**, on their own machine, as fast as their hardware allows. Nothing can slow them down there.

That changes what a strong password means. A short or common one falls to a public leaked-password list almost instantly. Length is what wins: every extra character multiplies the time. Four random, unrelated words run past any realistic attacker's patience, and past their lifetime. WPA3's newer handshake (SAE) closes the offline-guessing door, but only when every device uses it; a mixed WPA2/WPA3 network can still be pushed down the old path.

## The doors that ignore your password
A perfect password still won't save you if another door is open, and most break-ins use one:

- **WPS** — the "push to connect" PIN. With a weak router, the Pixie-Dust method can recover the key in seconds, no matter how strong your password is.
- **The evil twin** — a fake network using your name and a "re-enter your Wi-Fi password" page. You type it in; they catch it.
- **Default keys** — routers shipped with a predictable password derived from the network name.
- **The admin sticker** — the router's own login left at the factory default, so the password can be read straight off the settings page.
- **A downgrade** — forcing a mixed network onto the older WPA2 path, where offline guessing works again.

## The tool: two checks and a report card
The auditor runs locally and gives your network a grade from A to F, with a ranked, do-it-tonight fix list.

1. **Password verdict (offline).** Is your passphrase in a public leaked list, and how long would it take to brute-force at several hardware speeds. The passphrase never leaves your machine.
2. **Router check.** It reads what your computer already knows: your security mode (WPA2/WPA3), the cipher, and whether your network name leaks your router's make and model. The few facts only the router knows (WPS, management-frame protection, firmware, admin password, guest network) it asks you to confirm, and marks clearly as *you told us* versus *we measured*.
3. **Neighbourhood check (passive).** A read-only look at the networks in range for a second one using your name (the tell-tale of an evil twin) and for open networks. It never attacks, deauthenticates or connects to anything.

An honest note built into the tool: no laptop can read your router's WPS state or firmware date over the air, and the crack times are labelled estimates. A real attacker with GPUs is faster than a laptop, and the tool says so.

## Fix it tonight, in seven steps
1. Set a long passphrase: four or more random, unrelated words.
2. Turn on WPA3 (or WPA2/WPA3), and WPA3-only once all your devices support it.
3. Turn WPS off.
4. Turn on management-frame protection (PMF).
5. Change the router's admin password from the default.
6. Put smart-home gadgets on a separate guest network.
7. Update the router's firmware.

## Who it's for
Anyone who wants to stop guessing whether their home network is fine. It's also a real service you could offer others, with written permission: a home-network security check that produces a clear, graded report and a fix list. Everything needed to run it, and a written guide, is free in the [repo](https://github.com/techseed309-lgtm/wifi-auditor).

Watch the full build on YouTube, and subscribe for a new build and explainer each week.
