# VoxType website

The public website for **VoxType**, a voice-typing app for Android. Plain HTML and CSS, no JavaScript, no cookies,
no third-party requests. It's hosted on GitHub Pages under our own subdomain.

| Path | What it is |
| --- | --- |
| `index.html`, `download.html`, `guide.html`, `faq.html`, `privacy.html` | The pages (generated, don't edit by hand) |
| `build.py` | Page generator: shared header, footer and all page text live here |
| `src/privacy-policy.html` | Privacy policy text used by `privacy.html` |
| `assets/` | Stylesheet, logo, self-hosted fonts (Archivo Black, Space Grotesk; SIL Open Font License) |
| `downloads/VoxType-<version>.apk` | The app download (committed, so GitHub Pages can serve it) |
| `.nojekyll` | Tells GitHub Pages to serve the files as they are |
| `.htaccess` | Only used on Apache/cPanel hosting; ignored by GitHub Pages |

## Editing

Change text in `build.py` (or `src/privacy-policy.html`), then regenerate the pages:

```
python build.py
```

Commit and push. GitHub Pages republishes within a minute or two.

## Before going live: fill in the placeholders

The developer name, contact email and policy date are filled in (`build.py`, `src/privacy-policy.html`). After any change, run
`python build.py`. Copy the same policy text back to `docs/privacy-policy.html` in the app repo so Google Play and the
website stay identical.

## Releasing a new app version

1. In the app repo, build the release APK (`gradlew assembleRelease`), signed with the upload key.
2. Copy `app/build/outputs/apk/release/app-release.apk` here as `downloads/VoxType-<version>.apk` and delete
   the old APK.
3. Get the SHA-256: `certutil -hashfile downloads\VoxType-<version>.apk SHA256`.
4. In `build.py`, update `VERSION`, `SIZE`, `DATE`, `APK` and `SHA256` at the top, and the release notes in the download
   section. Run `python build.py`, then commit and push.

Always sign website builds with the same upload key, or people can't update in place.

## Hosting setup (one time)

Hosting is GitHub Pages with a subdomain from Namecheap, here `voxtype.sarveshh.me`.

1. **Push this folder to a GitHub repo.**
2. **Turn on Pages:** repo **Settings → Pages → Build and deployment**. Set Source to *Deploy from a branch*,
   Branch to `main` and folder `/ (root)`, then Save.
3. **Add the custom domain:** same page, **Custom domain**: enter `voxtype.sarveshh.me` and Save. GitHub commits a
   `CNAME` file to the repo; run `git pull` afterwards so your copy has it.
4. **DNS at Namecheap:** Domain List → **Manage** → **Advanced DNS** → **Add New Record**:
   - Type `CNAME Record`, Host `voxtype`, Value `<your-github-username>.github.io.`, TTL Automatic.
   - Remove any other record with the same host (`voxtype`), such as a URL Redirect or A record.
5. **Wait for the DNS check:** back in Settings → Pages, wait until it says the DNS check succeeded (usually minutes,
   sometimes up to an hour).
6. **HTTPS:** tick **Enforce HTTPS** once it stops being greyed out (GitHub issues the certificate automatically).
7. **Recommended:** verify the domain in your GitHub account (profile **Settings → Pages → Add a domain**, then add the
   TXT record it shows at Namecheap). This stops anyone else from claiming your subdomain on GitHub.

GitHub Pages is free for **public** repos. A private repo needs a paid GitHub plan for Pages.
