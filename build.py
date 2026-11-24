# Builds the VoxType website pages (shared header and footer, page content below).
# Run:  python build.py     Edit this file (and src/privacy-policy.html), not the generated .html files.
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT

VERSION, SIZE, DATE, APK = "1.1.0", "159 KB", "24 November 2026", "downloads/VoxType-1.1.0.apk"
SHA256 = "88594b090a72d5862c6c8f5fd88a2c94f630b6b9c1b516b0944f3182eeac4a10"
CERT = "52:5B:2F:12:A2:2F:F3:5B:D2:0E:71:F5:61:83:73:1B:EF:B8:4A:D0:28:DC:85:5D:95:39:55:66:2F:FA:D5:92"

MIC = '<svg viewBox="0 0 24 24"><path fill="#fff" d="M12 14c1.66 0 3-1.34 3-3V5c0-1.66-1.34-3-3-3S9 3.34 9 5v6c0 1.66 1.34 3 3 3zm5.3-3c0 3-2.54 5.1-5.3 5.1S6.7 14 6.7 11H5c0 3.41 2.72 6.23 6 6.72V21h2v-3.28c3.28-.48 6-3.3 6-6.72h-1.7z"/></svg>'
DL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg>'

def ic(path):  # outline icon
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{path}</svg>'

I_MIC = ic('<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0014 0M12 18v3"/>')
I_TYPE = ic('<rect x="2" y="6" width="20" height="12" rx="2"/><path d="M6 10h.01M10 10h.01M14 10h.01M18 10h.01M7 14h10"/>')
I_INF = ic('<path d="M18.2 8.2a5 5 0 110 7.6L12 12l-6.2 3.8a5 5 0 110-7.6L12 12z"/>')
I_SPARK = ic('<path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/>')
I_SLIDERS = ic('<path d="M4 6h10M18 6h2M4 12h4M12 12h8M4 18h12"/><circle cx="16" cy="6" r="2"/><circle cx="10" cy="12" r="2"/><circle cx="18" cy="18" r="2"/>')
I_BOLT = ic('<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>')
SHIELD = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg>'

NAV = [("index.html", "Home"), ("index.html#features", "Features"), ("download.html", "Download"),
       ("guide.html", "Setup Guide"), ("faq.html", "FAQ"), ("privacy.html", "Privacy")]

def page(file, doc_title, desc, body):
    nav = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == file else ""}>{n}</a></li>' for h, n in NAV)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{doc_title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#ffd23f">
<link rel="preload" href="assets/fonts/archivo-black-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="icon" href="assets/logo.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>

<header class="header"><div class="wrap">
  <a class="logo" href="index.html"><img src="assets/logo.svg" alt="" width="36" height="36">VoxType</a>
  <ul class="nav">{nav}</ul>
  <a class="btn btn-sm" href="download.html">{DL}Download</a>
</div></header>

{body}

<footer class="footer"><div class="wrap">
  <div class="giant" aria-hidden="true">SPEAK<span>ER</span></div>
  <div class="cols">
    <div>
      <a class="logo" href="index.html"><img src="assets/logo.svg" alt="" width="36" height="36">VoxType</a>
      <p>Voice typing for every Android app. Speak naturally and your words appear wherever you're writing.</p>
    </div>
    <div><h4>Product</h4><ul><li><a href="index.html#features">Features</a></li><li><a href="index.html#ai">AI rewrite</a></li><li><a href="download.html">Download</a></li><li><a href="download.html#releases">Release notes</a></li></ul></div>
    <div><h4>Help</h4><ul><li><a href="guide.html">Setup guide</a></li><li><a href="faq.html">FAQ</a></li><li><a href="mailto:contact.sarvesh.swami@gmail.com">Contact us</a></li></ul></div>
    <div><h4>Legal</h4><ul><li><a href="privacy.html">Privacy policy</a></li></ul></div>
  </div>
  <div class="base"><span>&copy; 2026 Sarvesh Swami. All rights reserved.</span><span>Android is a trademark of Google LLC.</span></div>
</div></footer>

</body>
</html>
'''

def page_hero(title, sub):
    return f'''<section class="page-hero"><span class="shape s-circle p1"></span><span class="shape s-half p2"></span><span class="shape p3"></span><div class="wrap">
  <h1>{title}</h1>
  <p>{sub}</p>
</div></section>'''

def table(head, rows):
    th = "".join(f"<th>{h}</th>" for h in head)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="table"><tr>{th}</tr>{tr}</table>'

def side(title, items):
    lis = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in items)
    return f'<aside class="side"><div class="box"><h4>{title}</h4><ul>{lis}</ul></div></aside>'

# ================================================================ HOME
home = f'''<section class="hero">
  <div class="wrap">
    <div class="hero-copy">
      <span class="tag"><b>NEW</b>VoxType {VERSION} &middot; now with AI rewrite</span>
      <h1><span>Talk.</span><span class="stripes">It types.</span><span><span class="hl">Anywhere.</span></span></h1>
      <p class="lead">A floating microphone for every app on your Android phone. Tap it, say the thing, and your words land right where you're writing.</p>
      <div class="actions">
        <a class="btn" href="download.html">{DL}Download free</a>
        <a class="btn btn-white btn-round" href="#how">How it works &rarr;</a>
      </div>
    </div>
    <div class="hero-art" aria-hidden="true">
      <span class="shape s-circle s1"></span>
      <span class="shape s2"></span>
      <span class="shape s-half s3"></span>
      <span class="shape s-circle s4"></span>
      <div class="device"><span class="cam"></span><div class="scr">
        <div class="bar"><i></i>Alex</div>
        <div class="m">tomorrow's review still on?</div>
        <div class="m me">yes! 10am, main room</div>
        <div class="m">bring the printed copies?</div>
        <div class="mic">{MIC}</div>
        <div class="typing">Sure, I'll bring them along<span class="caret"></span></div>
      </div></div>
      <span class="sticker st1">Tap &amp; talk</span>
      <span class="sticker st2">&#10024; AI rewrite</span>
      <div class="burst">NO<br>ADS</div>
      <svg class="spin" viewBox="0 0 150 150"><defs><path id="ring" d="M75 75m-58 0a58 58 0 1 1 116 0a58 58 0 1 1-116 0"/></defs><circle cx="75" cy="75" r="72" fill="#fff" stroke="#111" stroke-width="3"/><circle cx="75" cy="75" r="22" fill="#ffd23f" stroke="#111" stroke-width="3"/><text><textPath href="#ring">voice typing &#10033; for android &#10033; free &#10033; </textPath></text></svg>
    </div>
  </div>
</section>

<div class="marquee" aria-hidden="true"><div class="track">
  <span>Talk</span><span>&#10033; Type</span><span>Send</span><span>&#10033; Any app</span><span>No keyboard</span><span>&#10033; No account</span><span>Talk</span><span>&#10033; Type</span><span>Send</span><span>&#10033; Any app</span><span>No keyboard</span><span>&#10033; No account</span>
  <span>Talk</span><span>&#10033; Type</span><span>Send</span><span>&#10033; Any app</span><span>No keyboard</span><span>&#10033; No account</span><span>Talk</span><span>&#10033; Type</span><span>Send</span><span>&#10033; Any app</span><span>No keyboard</span><span>&#10033; No account</span>
</div></div>

<section class="section" id="features"><div class="wrap">
  <div class="head">
    <span class="label">Features</span>
    <h2>Your voice, <span class="outline">every</span> <span class="hl pink">app.</span></h2>
    <p>Simple enough to use in seconds. Flexible enough to fit the way you work.</p>
  </div>
  <div class="bento">
    <div class="tile t-wide t-yellow"><div class="glyph">{I_MIC}</div><h3>Floating microphone</h3><p>A bubble that sits over every app. Tap to start, tap to stop, drag it wherever you like.</p><span class="big">01</span></div>
    <div class="tile t-round t-pink"><div class="glyph round">{I_TYPE}</div><h3>Types where you are</h3><p>Straight into the text box you're using.</p></div>
    <div class="tile t-tall t-purple t-arch"><div class="glyph round">{I_SPARK}</div><h3>AI rewrite</h3><p>Say it your way, check the draft, then send it once for clean, punctuated text in your own style. Works with OpenAI, Claude, Gemini, Groq or your own server.</p></div>
    <div class="tile t-cut t-mint"><div class="glyph">{I_INF}</div><h3>No time limit</h3><p>Keeps listening through pauses, so you can stop and think.</p></div>
    <div class="tile t-blob t-lime"><div class="glyph round">{I_SLIDERS}</div><h3>Pick your engine</h3><p>Free built-in, or bring your own key.</p></div>
    <div class="tile t-yellow"><div class="glyph">{ic('<rect x="6" y="4" width="12" height="17" rx="2"/><path d="M9 4V3h6v1M9 10h6M9 14h4"/>')}</div><h3>Clipboard backup</h3><p>No text box selected? Your words are copied, never lost.</p></div>
    <div class="tile t-wide t-pill t-orange"><div class="glyph round">{I_BOLT}</div><div><h3>Start it your way</h3><p>The bubble, the notification, a Quick Settings tile, or the big button in the app.</p></div></div>
    <div class="tile t-wide t-stripes"><div class="glyph round">{ic('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>')}</div><h3>Recent dictations</h3><p>Optionally keep your last 50 dictations and their AI versions on the phone, ready to copy. Long-press the bubble for a quick menu.</p><span class="big">50</span></div>
  </div>
</div></section>

<section class="section yellow" id="how"><div class="wrap">
  <div class="head center center-text" style="text-align:center">
    <span class="label">How it works</span>
    <h2>Three steps. <span class="outline">Zero</span> typing.</h2>
  </div>
  <div class="steps">
    <div class="step"><span class="n">01</span><h3>Install VoxType</h3><p>Download the app and follow the quick setup card: microphone, bubble and auto-typing.</p></div>
    <div class="step"><span class="n">02</span><h3>Open any app</h3><p>Messages, email, notes, a browser. Tap into the box where you want to write.</p></div>
    <div class="step"><span class="n">03</span><h3>Tap &amp; talk</h3><p>Tap the bubble and speak. Your words appear as you pause. Tap again when you're done.</p></div>
  </div>
</div></section>

<section class="section blue" id="ai"><div class="wrap">
  <div class="head">
    <span class="label" style="color:#111">AI rewrite</span>
    <h2>Say it <span class="dots-text">messy.</span><br>Send it <span class="hl lime" style="color:#111">clean.</span></h2>
    <p>Your words collect in a draft card next to the bubble. Fix anything you like, tap Send, and the whole thing is rewritten at once, with full context.</p>
  </div>
  <div class="ba">
    <div class="card-say say-before"><small>You said</small><s>um</s> so yeah i can send the summary tonight after i check the numbers with priya and <s>uh</s> let you know</div>
    <div class="ba-arrow"><svg viewBox="0 0 110 60" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 40 C 25 5, 45 55, 65 20 S 90 30, 100 30"/><path d="M88 18l14 12-16 8"/></svg>one tap</div>
    <div class="card-say say-after"><small>VoxType typed</small>I can send the summary tonight, after I check the numbers with Priya. I'll let you know.</div>
  </div>
  <ul class="ai-points">
    <li>Edit before sending</li><li>Full context, one rewrite</li><li>Your own prompt</li><li>OpenAI &middot; Claude &middot; Gemini &middot; Groq</li><li>Clipboard backup</li>
  </ul>
</div></section>

<section class="section" id="engines"><div class="wrap">
  <div class="head center" style="text-align:center">
    <span class="label">Speech engines</span>
    <h2>Bring your <span class="circled">own</span> engine</h2>
    <p>Start free with your phone's own recognition, or plug in a key for any of these. Model names are editable, so new models work right away.</p>
  </div>
  <div class="tags">
    <div class="etag"><b>Android</b><span>Built-in recognition</span><em>Free &middot; no key</em></div>
    <div class="etag"><b>Groq</b><span>Very fast Whisper</span><em>Free tier</em></div>
    <div class="etag"><b>OpenAI</b><span>High accuracy</span><em>Your key</em></div>
    <div class="etag"><b>Gemini</b><span>Multilingual</span><em>Your key</em></div>
    <div class="etag"><b>Deepgram</b><span>Nova models</span><em>Your key</em></div>
    <div class="etag"><b>Custom</b><span>OpenAI-compatible</span><em>Your key</em></div>
  </div>
</div></section>

<section class="section yellow"><div class="wrap">
  <div class="privacy">
    <div class="copy">
      <span class="label">Privacy</span>
      <h2>Your words.<br><span class="outline">Not ours.</span></h2>
      <p style="font-size:19px;font-weight:500">VoxType has no servers, so we never receive your voice, your text or your keys. Your speech goes only to your phone's own service or to the provider you choose.</p>
      <ul><li>No account</li><li>No ads, no analytics</li><li>Keys stay on your phone</li><li>You pick every provider</li></ul>
      <a class="btn btn-white" href="privacy.html">Read the privacy policy</a>
    </div>
    <div class="star-badge"><span>100%<br>yours</span></div>
  </div>
</div></section>

<section class="cta">
  <span class="shape s-circle s-a"></span><span class="shape s-half s-b"></span><span class="shape s-c"></span>
  <div class="wrap">
    <h2>Stop typing.<br><span class="outline">Start talking.</span></h2>
    <p>VoxType is free for Android 8.0 and later.</p>
    <a class="btn btn-lime" href="download.html">{DL}Download VoxType {VERSION}</a>
    <p class="fine">Google Play listing coming soon.</p>
  </div>
</section>'''

# ================================================================ DOWNLOAD
download = page_hero("Download VoxType", "Free for Android. Open this page on your phone, tap Download, and install it directly.") + f'''
<div class="wrap">
  <div class="dl">
    <div class="dl-card">
      <div class="burst">FREE!</div>
      <img class="ico" src="assets/logo.svg" alt="" width="104" height="104">
      <h2>VoxType</h2>
      <div class="ver">Version {VERSION} &middot; {SIZE}</div>
      <a class="btn btn-lg" href="{APK}" download>{DL}Download APK</a>
      <div class="facts">
        <div><small>Released</small><b>{DATE}</b></div>
        <div><small>Requires</small><b>Android 8.0+</b></div>
        <div><small>Price</small><b>Free</b></div>
        <div><small>Size</small><b>{SIZE}</b></div>
      </div>
    </div>
    <div class="dl-main article">
      <h2>How to install</h2>
      <p>VoxType isn't on Google Play yet, so Android asks you to confirm a couple of things the first time.</p>
      <ol class="numbered">
        <li><b>Download the file.</b> If your browser asks whether to keep it, choose <i>Download anyway</i>.</li>
        <li><b>Open it</b> from the download notification or your Downloads folder.</li>
        <li><b>Allow installs from your browser.</b> When asked, tap <i>Settings</i>, switch on <i>Allow from this source</i>, and go back.</li>
        <li><b>Tap Install.</b> If Google Play Protect asks about an unrecognised app, tap <i>More details</i>, then <i>Install anyway</i>.</li>
        <li><b>Open VoxType</b> and follow the <a href="guide.html">setup guide</a>. It takes about two minutes.</li>
      </ol>
      <div class="note"><b>Android 13 and later:</b> the <i>VoxType auto-type</i> switch starts out restricted for apps installed from a website. The <a href="guide.html#restricted">setup guide</a> shows the one-time fix.</div>
      <h2>Updating</h2>
      <p>Download the newer version here and install it over the one you have. Don't uninstall first: your settings and keys are kept. After updating, open VoxType and tap <b>Start floating bubble</b> again.</p>
    </div>
  </div>

  <div class="layout" style="padding-top:30px">
    <div class="article" style="max-width:none">
      <h2 id="requirements">System requirements</h2>
      {table(["Item", "Requirement"], [["Android", "8.0 (Oreo) or later"], ["Microphone", "Built-in or headset"], ["Storage", "Less than 1 MB"], ["Internet", "Only for online engines and AI rewrite"], ["API key", "Optional, only for online providers"]])}
      <h2 id="releases">What's new in {VERSION}</h2>
      <ul>
        <li>Speaker is now <b>VoxType</b>. Same app, new name. Install this version over the old one: your settings and keys are kept.</li>
        <li>Meet the new floating character: he leans on the edge of your screen, pulls his headphones down and types on his laptop while you talk.</li>
        <li>Save your own AI rewrite prompts with a name, and switch prompts from the app or from the bubble's quick menu.</li>
        <li>AI rewrite uses a draft card: your words collect next to the bubble, you can edit them, and the whole text is rewritten at once when you tap Send.</li>
        <li>Long-press the bubble for a quick menu to switch AI rewrite on or off, change the prompt, or open the app.</li>
        <li>When no text box is selected, the result is copied to the clipboard.</li>
        <li>Recent dictations: optionally keep your last 50 dictations and their AI versions on the phone.</li>
        <li>Model lists load from each provider and show only the models your key can use.</li>
      </ul>
      <h2 id="verify">Check your download</h2>
      <p>Optional. Compare these values to make sure the file is genuine and unchanged.</p>
      {table(["Item", "Value"], [["SHA-256", f'<span class="code">{SHA256}</span>'], ["Signing certificate", f'<span class="code">{CERT}</span>'], ["Package name", '<span class="code">app.speaker.dictate</span>']])}
    </div>
  </div>
</div>'''

# ================================================================ GUIDE
guide = page_hero("Setup guide", "Everything you need to get VoxType running, from the first launch to AI rewrite.") + f'''
<div class="wrap"><div class="layout">
  {side("On this page", [("#permissions", "Permissions"), ("#restricted", "Restricted settings"), ("#battery", "Background &amp; battery"), ("#engine", "Speech engines"), ("#bubble", "The floating bubble"), ("#ai", "AI rewrite"), ("#history", "Recent dictations"), ("faq.html", "FAQ")])}
  <article class="article">
    <h2 id="permissions">Permissions</h2>
    <p>When you first open VoxType, the <b>Finish setup</b> card lists four steps. Tap each one in turn.</p>
    {table(["Step", "What to do", "Why"], [
      ["Microphone", "Tap <i>Allow</i>, then <i>While using the app</i>.", "To hear you while you dictate."],
      ["Display over apps", "Tap <i>Allow</i>, find VoxType and switch it on.", "Shows the floating bubble."],
      ["Auto-typing", "Tap <i>Enable</i>, read the note, tap <i>Agree &amp; continue</i>, then switch on <i>VoxType auto-type</i>.", "Types your words into the text box."],
      ["Run in background", "Tap <i>Allow</i> and choose <i>Unrestricted</i>.", "Stops the phone closing VoxType."]])}
    <p>Auto-typing is optional. Without it, VoxType copies what you said to the clipboard. In Accessibility settings, <i>VoxType auto-type</i> may be under <i>Installed apps</i> or <i>Downloaded apps</i>.</p>

    <h2 id="restricted">Restricted settings</h2>
    <p>Android 13 and later protect Accessibility for apps installed from outside Google Play. If the <i>VoxType auto-type</i> switch is greyed out:</p>
    <ol class="numbered">
      <li>Try to switch it on once so Android shows the message, then close it.</li>
      <li>Open <b>Settings &rarr; Apps &rarr; VoxType</b>.</li>
      <li>Tap the <b>&#8942;</b> menu and choose <b>Allow restricted settings</b>. Confirm with your PIN or fingerprint.</li>
      <li>Go back to <b>Settings &rarr; Accessibility &rarr; VoxType auto-type</b> and switch it on.</li>
    </ol>

    <h2 id="battery">Background &amp; battery</h2>
    <p>Some phones close apps in the background to save battery. When that happens, the bubble disappears and Android also switches auto-typing off.</p>
    <div class="note warn"><b>Realme, Oppo, OnePlus, Xiaomi, Vivo and Samsung:</b> set battery use to <i>Unrestricted</i>, turn on <i>Auto launch</i> or <i>Autostart</i> for VoxType if your phone has it, and lock VoxType in the recent-apps screen.</div>

    <h2 id="engine">Speech engines</h2>
    {table(["Engine", "Key", "Notes"], [
      ["Android built-in", "Not needed", "Free. Your phone's own speech recognition."],
      ["Groq", "Required", "Fast Whisper models. Free tier available."],
      ["OpenAI", "Required", "Accurate transcription models."],
      ["Google Gemini", "Required", "Gemini models."],
      ["Deepgram", "Required", "Nova models."],
      ["Custom", "Required", "Any OpenAI-compatible server."]])}
    <p>For an online engine, create an API key on the provider's website and paste it under <b>API keys</b>. Tap <b>Refresh</b> beside <i>Model</i> to load the models your key can use. Leave <i>Language</i> blank to detect it automatically. Providers charge for usage under their own terms; VoxType itself is free.</p>

    <h2 id="bubble">The floating bubble</h2>
    <p>Tap <b>Start floating bubble</b>. The bubble appears at the edge of the screen, with a VoxType notification while it runs.</p>
    {table(["Action", "What it does"], [["Tap", "Start or stop dictation"], ["Drag", "Move the bubble"], ["Long-press", "Quick menu: AI rewrite on or off, or open VoxType"]])}
    <p>You can also use the <b>Dictate</b> button in the notification, or add the <b>Dictate</b> tile to Quick Settings.</p>

    <h2 id="ai">AI rewrite</h2>
    <ol class="numbered">
      <li>In <b>AI rewrite</b>, switch it on, pick a provider (OpenAI, Anthropic Claude, Google Gemini, Groq or custom) and a model, and add the key under <b>API keys</b>.</li>
      <li>Tap the bubble and speak. Your words collect in a <b>draft card</b> next to the bubble.</li>
      <li>Tap the text in the card to fix anything with the keyboard.</li>
      <li>Tap <b>Send</b> or the bubble. It shows <i>Processing</i>, then the rewritten text is typed in, or copied to the clipboard if no text box is selected.</li>
    </ol>
    {table(["Draft card", "What it does"], [["&#10005;", "Discard the draft"], ["More", "Keep talking and add to it"], ["Send", "Rewrite the whole draft. If it fails, the draft is kept and you can retry."]])}

    <h2 id="history">Recent dictations</h2>
    <p>With AI rewrite on, switch on <b>Keep recent dictations on this phone</b> to keep your last 50 dictations with their AI versions, ready to copy. They stay only on your phone, and switching the setting off clears them.</p>
  </article>
</div></div>'''

# ================================================================ FAQ
def q(question, answer):
    return f'<details class="q"><summary>{question}</summary><div class="a"><p>{answer}</p></div></details>'

faq = page_hero("Frequently asked questions", "Quick answers about installing, using and paying for VoxType.") + f'''
<div class="wrap"><div class="layout">
  {side("Topics", [("#installing", "Installing"), ("#using", "Using VoxType"), ("#costs", "Costs &amp; privacy"), ("#contact", "Contact us"), ("guide.html", "Setup guide")])}
  <article class="article">
    <h2 id="installing">Installing</h2>
    {q("Why isn't VoxType on Google Play?", "It's on its way. Until then you can install it from this website, and we'll link to the Play listing once it's live.")}
    {q("Android warns me about installing the file. Is that normal?", 'Yes. Android shows that warning for any app installed from outside Google Play. VoxType has no ads or trackers and only asks for the permissions it needs. You can check the file against the values on the <a href="download.html#verify">download page</a>.')}
    {q("How do I update?", 'Download the newer version from the <a href="download.html">download page</a> and install it over the one you have. Don\'t uninstall first, so your settings and keys are kept.')}
    {q("Can I switch to the Google Play version later?", "Yes. If Android won't install the Play version over this one, uninstall VoxType first, then install it from Play. You'll need to enter your keys and settings again.")}

    <h2 id="using">Using VoxType</h2>
    {q("My words go to the clipboard instead of the text box.", "Auto-typing is switched off. Open <b>Settings &rarr; Accessibility &rarr; VoxType auto-type</b> and switch it back on. If it keeps turning off, see the next question.")}
    {q("The bubble disappears, or auto-typing keeps switching off.", 'Your phone is closing VoxType in the background to save battery, and Android then switches off its Accessibility service too. Set battery use to <i>Unrestricted</i>, turn on <i>Auto launch</i> or <i>Autostart</i> if your phone has it, and lock VoxType in Recents. See <a href="guide.html#battery">Background &amp; battery</a>.')}
    {q("The auto-type switch is greyed out.", 'That\'s Android 13\'s protection for apps installed outside Google Play. Go to <b>Settings &rarr; Apps &rarr; VoxType &rarr; &#8942; &rarr; Allow restricted settings</b>, then try again. See <a href="guide.html#restricted">Restricted settings</a>.')}
    {q("Auto-typing doesn't work in one particular app.", "A few apps, such as some terminals and games, don't use standard text boxes. In those apps VoxType copies your words to the clipboard. Long-press and choose <i>Paste</i>.")}
    {q("Does dictation stop when I pause?", "No. VoxType keeps listening until you tap the bubble again, so you can stop to think.")}
    {q("Which languages are supported?", "That depends on the engine. Most online engines handle dozens of languages and detect them automatically, or you can set a code such as <span class=\"code\">en</span>, <span class=\"code\">hi</span> or <span class=\"code\">en-IN</span>. The built-in engine supports the languages installed for your phone's speech recognition.")}

    <h2 id="costs">Costs &amp; privacy</h2>
    {q("Is VoxType free?", "Yes. No ads, subscriptions or in-app purchases. The built-in engine costs nothing. If you use an online engine or AI rewrite, you use your own key and pay that provider directly for what you use. Some providers have free tiers.")}
    {q("Can you see what I say?", 'No. VoxType has no servers. Your voice goes either to your phone\'s own speech service or straight from your phone to the provider you chose. See the <a href="privacy.html">privacy policy</a>.')}
    {q("Why does VoxType use Accessibility?", "Accessibility is the Android feature that lets an app type into text boxes in other apps, like a keyboard does. VoxType uses it only to type your dictated words. It doesn't read or collect your screen content.")}
    {q("Where are my API keys stored?", "Only in VoxType's private storage on your phone. They're left out of backups and device transfers, and each key is sent only to the provider it belongs to.")}

    <h2 id="contact">Still need help?</h2>
    <p>Email <a href="mailto:contact.sarvesh.swami@gmail.com">contact.sarvesh.swami@gmail.com</a> with your phone model and Android version. In VoxType, <b>Logs &amp; debugging &rarr; Copy</b> gives you a diagnostic log to paste into your message. It never contains your dictated words or keys.</p>
  </article>
</div></div>'''

# ================================================================ PRIVACY (text from src/privacy-policy.html)
src = (ROOT / "src" / "privacy-policy.html").read_text(encoding="utf-8")
pol = re.search(r"<body>(.*)</body>", src, re.S).group(1)
pol = re.sub(r"<h1>.*?</h1>\s*", "", pol, flags=re.S)
pol = pol.replace("<table>", '<table class="table">')
pol = pol.replace("<h2>Sharing and selling</h2>", "<h2>This website</h2>\n<p>This website uses no cookies, analytics, advertising or third-party scripts. Like any website, our hosting provider may keep standard server logs (such as IP address, browser type and the pages or files requested) for security and to keep the site running.</p>\n\n<h2>Sharing and selling</h2>")
pol = pol.replace("posted at this address", "posted on this page")
privacy = page_hero("Privacy policy", "Short version: no account, no ads, no analytics, and we never receive your voice, text or keys.") + f'''
<div class="wrap"><div class="layout">
  {side("Privacy", [("#top", "Privacy policy"), ("faq.html#costs", "Privacy FAQ"), ("mailto:contact.sarvesh.swami@gmail.com", "Contact us")])}
  <article class="article">
{pol.strip()}
  </article>
</div></div>'''
privacy = privacy.replace('href="#top"', 'href="privacy.html"')

PAGES = {
    "index.html": ("VoxType: Voice Typing for Every Android App", "VoxType puts a microphone over every app on your Android phone. Tap, speak, and your words are typed where you're writing. Free download.", home),
    "download.html": ("Download VoxType for Android", "Download VoxType, the free voice typing app for Android 8.0 and later.", download),
    "guide.html": ("VoxType Setup Guide", "Set up VoxType: permissions, auto-typing, speech engines, the floating bubble and AI rewrite.", guide),
    "faq.html": ("VoxType FAQ", "Answers to common questions about installing and using VoxType for Android.", faq),
    "privacy.html": ("VoxType Privacy Policy", "Privacy policy for VoxType, the voice typing app for Android.", privacy),
}
for f, (t, d, b) in PAGES.items():
    (OUT / f).write_text(page(f, t, d, b), encoding="utf-8", newline="\n")
print("ok")
