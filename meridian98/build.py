#!/usr/bin/env python3
"""Build the installable index.html from game.html.

game.html is written in the form the Claude Artifact viewer expects (no <html>/<head>/<body>).
This wraps it in a full document with the iOS home-screen / PWA tags and registers the
service worker so the game works offline once added to the Home Screen.
"""
from pathlib import Path

here = Path(__file__).parent
game = (here / "game.html").read_text(encoding="utf-8")

head = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, user-scalable=no">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Meridian 98">
<meta name="theme-color" content="#008080">
<meta name="color-scheme" content="light">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="icon" href="icon-192.png">
<style>
:root{padding:env(safe-area-inset-top,0px) env(safe-area-inset-right,0px) env(safe-area-inset-bottom,0px) env(safe-area-inset-left,0px);background:#000}
body{margin:0}
[hidden]{display:none!important}
</style>
</head>
<body>
"""

tail = """
<script>
if ('serviceWorker' in navigator && location.protocol.startsWith('http')) {
  window.addEventListener('load', function () { navigator.serviceWorker.register('sw.js').catch(function () {}); });
}
</script>
</body>
</html>
"""

(here / "index.html").write_text(head + game + tail, encoding="utf-8")
print("wrote index.html", len(head + game + tail), "bytes")
