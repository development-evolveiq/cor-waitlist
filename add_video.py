#!/usr/bin/env python3
"""Merge the 45s intro video (hero button + how-it-works card + modal) into src/index.njk"""
import sys

PATH = "src/index.njk"

with open(PATH, "r", encoding="utf-8") as f:
    content = f.read()

original = content

# --- 1. CSS block: insert before the closing {% endblock %} of the styles block ---
css_anchor = """  .flow-animated .flow-arrow-down svg { animation: fade-in 0.4s ease-out 0.1s forwards; }
{% endblock %}"""

css_block = """  .flow-animated .flow-arrow-down svg { animation: fade-in 0.4s ease-out 0.1s forwards; }

  /* VIDEO — hero trigger */
  .btn-video { display: inline-flex; align-items: center; gap: 8px; background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.14); color: var(--dark-text); padding: 11px 20px 11px 12px; border-radius: 9px; font-size: 15px; font-weight: 500; font-family: var(--font); cursor: pointer; transition: background 0.2s, border-color 0.2s; }
  .btn-video:hover { background: rgba(255,255,255,0.1); border-color: rgba(255,255,255,0.26); }
  .btn-video-icon { width: 26px; height: 26px; border-radius: 50%; background: var(--blue); display: flex; align-items: center; justify-content: center; flex-shrink: 0; }

  /* VIDEO — how-it-works card */
  .how-video-card { display: flex; align-items: center; gap: 1.25rem; width: 100%; max-width: 560px; margin: 0 auto 3rem; background: var(--light-surface); border: 1px solid var(--light-border); border-radius: var(--radius-lg); padding: 0.85rem; cursor: pointer; transition: box-shadow 0.2s, border-color 0.2s; text-align: left; font-family: inherit; -webkit-appearance: none; appearance: none; }
  .how-video-card:hover { box-shadow: 0 8px 28px rgba(0,0,0,0.08); border-color: rgba(43,124,233,0.3); }
  .how-video-thumb { position: relative; width: 148px; height: 84px; flex-shrink: 0; border-radius: 8px; overflow: hidden; background: #0D0F14; }
  .how-video-thumb img { width: 100%; height: 100%; object-fit: cover; display: block; }
  .how-video-play { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 36px; height: 36px; border-radius: 50%; background: rgba(43,124,233,0.92); display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 14px rgba(0,0,0,0.35); }
  .how-video-duration { position: absolute; bottom: 6px; right: 6px; font-size: 10px; font-family: var(--mono); color: #fff; background: rgba(0,0,0,0.55); padding: 2px 6px; border-radius: 4px; }
  .how-video-label-title { display: block; font-size: 15px; font-weight: 600; color: var(--text-primary); margin-bottom: 4px; }
  .how-video-label-sub { display: block; font-size: 13px; color: var(--text-secondary); line-height: 1.5; }

  /* VIDEO — modal */
  .video-modal-overlay { position: fixed; inset: 0; background: rgba(6,7,10,0.86); z-index: 1000; display: flex; align-items: center; justify-content: center; padding: 2rem; opacity: 0; pointer-events: none; transition: opacity 0.2s; }
  .video-modal-overlay.open { opacity: 1; pointer-events: auto; }
  .video-modal { position: relative; width: 100%; max-width: 900px; }
  .video-modal-frame { position: relative; width: 100%; aspect-ratio: 16 / 9; background: #000; border-radius: 12px; overflow: hidden; box-shadow: 0 24px 64px rgba(0,0,0,0.5); }
  .video-modal-frame video { width: 100%; height: 100%; display: block; }
  .video-modal-close { position: absolute; top: -44px; right: 0; width: 34px; height: 34px; border-radius: 50%; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: #fff; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: background 0.2s; border: none; }
  .video-modal-close:hover { background: rgba(255,255,255,0.2); }
  @media (max-width: 600px) {
    .how-video-card { flex-direction: column; align-items: stretch; }
    .how-video-thumb { width: 100%; height: 160px; }
  }
{% endblock %}"""

# --- 2. Hero trigger button ---
hero_anchor = """      <div class="hero-actions">
        <a href="https://app.corgtm.com/signup" class="btn-primary">Try for free →</a>
        <a href="#waitlist" class="btn-ghost">Book a demo ↗</a>
      </div>"""

hero_block = """      <div class="hero-actions">
        <a href="https://app.corgtm.com/signup" class="btn-primary">Try for free →</a>
        <a href="#waitlist" class="btn-ghost">Book a demo ↗</a>
        <button type="button" class="btn-video" onclick="openCorVideo()">
          <span class="btn-video-icon"><svg width="10" height="10" viewBox="0 0 10 10" fill="none"><path d="M1.5 0.8L9 5 1.5 9.2V0.8z" fill="#fff"/></svg></span>
          Watch 45s intro
        </button>
      </div>"""

# --- 3. How-it-works video card ---
how_anchor = """    <p class="how-intro">Paste your URL. COR builds your knowledge base, surfaces warm LinkedIn prospects ranked by ICP fit, and connects every signal to action — automatically.</p>
  </div>

  <div class="flow-wrap">"""

how_block = """    <p class="how-intro">Paste your URL. COR builds your knowledge base, surfaces warm LinkedIn prospects ranked by ICP fit, and connects every signal to action — automatically.</p>
  </div>

  <button type="button" class="how-video-card" onclick="openCorVideo()">
    <div class="how-video-thumb">
      <img src="/videos/cor-intro-poster.jpg" alt="COR 45-second product overview" loading="lazy">
      <span class="how-video-play"><svg width="12" height="12" viewBox="0 0 10 10" fill="none"><path d="M1.5 0.8L9 5 1.5 9.2V0.8z" fill="#fff"/></svg></span>
      <span class="how-video-duration">0:45</span>
    </div>
    <span class="how-video-label">
      <span class="how-video-label-title">Watch the 45-second overview</span>
      <span class="how-video-label-sub">See Blueprint, Scout, AI Presence, and Content Studio in action.</span>
    </span>
  </button>

  <div class="flow-wrap">"""

# --- 4. Modal markup + JS, inserted right after the bottom-cta section closes ---
modal_anchor = """    <p class="form-note" id="ctaNote">We'll reach out to find a time that works.</p>
  </div>
</section>

<script>
(function() {
  // Shared helper: wires the bottom demo email form to /api/waitlist."""

modal_block = """    <p class="form-note" id="ctaNote">We'll reach out to find a time that works.</p>
  </div>
</section>

<!-- VIDEO MODAL -->
<div class="video-modal-overlay" id="corVideoOverlay" onclick="closeCorVideoBackdrop(event)">
  <div class="video-modal">
    <button type="button" class="video-modal-close" aria-label="Close video" onclick="closeCorVideo()">
      <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M1 1l12 12M13 1L1 13" stroke="#fff" stroke-width="1.6" stroke-linecap="round"/></svg>
    </button>
    <div class="video-modal-frame">
      <video id="corVideoEl" controls playsinline preload="none" poster="/videos/cor-intro-poster.jpg"></video>
    </div>
  </div>
</div>
<script>
(function() {
  var VIDEO_SRC = '/videos/cor-intro.mp4';
  var overlay = document.getElementById('corVideoOverlay');
  var videoEl = document.getElementById('corVideoEl');

  window.openCorVideo = function() {
    if (!videoEl.getAttribute('src')) {
      videoEl.setAttribute('src', VIDEO_SRC);
    }
    overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
    videoEl.currentTime = 0;
    var playPromise = videoEl.play();
    if (playPromise && playPromise.catch) { playPromise.catch(function() {}); }
  };
  window.closeCorVideo = function() {
    overlay.classList.remove('open');
    document.body.style.overflow = '';
    videoEl.pause();
  };
  window.closeCorVideoBackdrop = function(e) {
    if (e.target === overlay) { closeCorVideo(); }
  };
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && overlay.classList.contains('open')) { closeCorVideo(); }
  });
})();
</script>

<script>
(function() {
  // Shared helper: wires the bottom demo email form to /api/waitlist."""

replacements = [
    ("CSS block", css_anchor, css_block),
    ("Hero trigger button", hero_anchor, hero_block),
    ("How-it-works video card", how_anchor, how_block),
    ("Video modal + JS", modal_anchor, modal_block),
]

errors = []
for name, anchor, block in replacements:
    count = content.count(anchor)
    if count == 0:
        errors.append(f"NOT FOUND: {name} — anchor text didn't match. No changes made for this piece.")
        continue
    if count > 1:
        errors.append(f"AMBIGUOUS: {name} — anchor text appears {count} times, expected 1. No changes made for this piece.")
        continue
    content = content.replace(anchor, block)
    print(f"OK: {name} inserted.")

if errors:
    print("\n--- ISSUES ---")
    for e in errors:
        print(e)
    print("\nNo file was overwritten where an issue occurred above; matched pieces (if any) were still applied to memory only — aborting write since not all 4 succeeded.")
    if len(errors) == len(replacements):
        sys.exit(1)
    sys.exit(1)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(content)

print(f"\nAll 4 pieces inserted successfully. {PATH} updated ({len(original)} -> {len(content)} bytes).")
