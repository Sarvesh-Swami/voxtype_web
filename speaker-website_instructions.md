# speaker-website: agent instructions

Public website for the VoxType Android app (app code lives in the separate `speaker app` repo, package
`app.speaker.dictate`). Hosted on GitHub Pages from `main` / root, under a Namecheap subdomain (`CNAME` file).
Human-facing overview and hosting steps: `README.md`.

## Rules
- The `.html` pages are generated. Edit `build.py` (page text, shared header and footer) or `src/privacy-policy.html`,
  then run `python build.py`. Never hand-edit the generated pages.
- Style: bold art-poster look (thick outlines, hard shadows, flat bright colours, geometric shapes, outlined and
  striped type). All CSS is in `assets/style.css`. Fonts are self-hosted in `assets/fonts/` (OFL).
- No JavaScript, cookies, analytics or third-party requests. The privacy page says so; keep it true.
- `downloads/*.apk` is committed on purpose (Pages can only serve committed files). Keep only the current APK.
  It must be the app's **play** flavor signed with the upload key, so website installs can update in place.
- Keep `src/privacy-policy.html` identical in substance to `docs/privacy-policy.html` in the app repo.
- When the APK changes, update `VERSION`, `SIZE`, `DATE`, `APK` and `SHA256` at the top of `build.py` and the
  release notes.
- Commit locally only; the user pushes. No AI attribution in commits.
