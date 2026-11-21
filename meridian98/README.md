# Meridian 98

A short adventure game that plays out inside a fake 1999 operating system. Somebody left a computer on, and left in a hurry. You are Sam, and you have until midnight on New Year's Eve to find out where your sibling went.

It is plain HTML, CSS and JavaScript with no dependencies and no build step to play. It runs in Safari on iPhone and iPad, and in any desktop browser.

## Play on iOS

Safari can only run it from a web address, so the folder needs to be hosted somewhere (GitHub Pages, Netlify, any static host). Then on the iPhone:

1. Open the address in Safari.
2. Tap Share, then **Add to Home Screen**.
3. Launch it from the new icon. It opens full screen and works offline after the first load.

Phone-width screens get one maximised window at a time with a large taskbar. Wider screens (iPad, landscape, desktop) get draggable, resizable windows.

## Files

| File | Purpose |
|---|---|
| `game.html` | The whole game: styles, markup and script. Edit this one. |
| `build.py` | Wraps `game.html` into `index.html` with the iOS home-screen tags and service worker registration. Run `python3 build.py` after editing. |
| `index.html` | Generated, installable version. |
| `manifest.webmanifest`, `sw.js`, `*.png` | Home-screen install and offline support. |

To try it locally: `python3 -m http.server 8000` inside this folder, then open `http://localhost:8000`.

## Stuck?

The in-game Sam's Notes app has progressive hints. A spoiler walkthrough follows.

<details>
<summary>Walkthrough</summary>

1. Log on as Guest. The photo of the lighthouse says it has been dark since 1987 and that Dad said never to go there. The password is `marrow1987`.
2. Read Dex's mail. The Harbor site admin PIN is Tuesday's three tides, high, low, high.
3. In Navigator, open Starlight Harbor, then the Tide Chart. Tuesday is 9, 2, 6. Enter `926` on the admin page.
4. The private journal says to ask Dex about the lamp. In PalPager, ask him. The lamp is called Marigold.
5. In MS-DOS Prompt, run `decrypt LAST.MSG marigold`, then press Enter.

</details>

Meridian 98 is original work. It imitates the look of 1990s desktop software and web pages but uses no Microsoft code, artwork or sounds. Sound effects are synthesised in the browser.
