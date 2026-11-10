# VYRO STUDIO PRO

A GitHub-ready, local-first browser editing workspace built with HTML, CSS and modular JavaScript, plus an optional Python development server.

## Run locally
- Simplest: open `index.html` in a modern Chrome or Edge browser.
- Optional Python server:
  ```bash
  python server/server.py
  ```
  Then visit http://127.0.0.1:8000

## Publish on GitHub Pages
1. Create a GitHub repository.
2. Upload the contents of this folder (not the enclosing zip).
3. Open **Settings → Pages**.
4. Set deployment source to **Deploy from a branch**, choose `main` and `/ (root)`.
5. Save and wait for GitHub Pages to publish.

## Included
- Futuristic responsive editing workspace.
- Media library for images, video and audio.
- 100 CSS-look presets.
- 50 transition presets in the library.
- Timeline lanes, clip selection, clip split, duplicate, delete, reorder by drag, playhead and zoom.
- Clip inspector: timing, color, speed, volume, caption and transition assignment.
- PNG export for image clips.
- WebM video export where supported by the browser.
- Project metadata export (`.vyro` JSON).

## Important scope notes
This is a substantial browser editor foundation, not a replacement for Premiere/DaVinci. The 100 effects are CSS filter looks. The transition library stores transition choices, but full animated transition compositing between two media clips is not implemented yet. The audio lane supports importing and arranging audio metadata, but audio mixing/rendering is not implemented. Project files store edit metadata, not copies of source media; re-import media when reopening. Browser WebM export is real-time and browser-dependent.
