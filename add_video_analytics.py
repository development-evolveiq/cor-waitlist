#!/usr/bin/env python3
"""Add Google Analytics (GA4) tracking for the intro video: start, complete, and which button was clicked."""
import sys

PATH = "src/index.njk"

with open(PATH, "r", encoding="utf-8") as f:
    content = f.read()

original = content

replacements = []

# --- 1. Hero button: tag which source it was clicked from ---
replacements.append((
    "Hero button source tag",
    '<button type="button" class="btn-video" onclick="openCorVideo()">',
    '<button type="button" class="btn-video" onclick="openCorVideo(\'hero\')">',
))

# --- 2. How-it-works button: tag which source it was clicked from ---
replacements.append((
    "How-it-works button source tag",
    '<button type="button" class="how-video-card" onclick="openCorVideo()">',
    '<button type="button" class="how-video-card" onclick="openCorVideo(\'how_it_works\')">',
))

# --- 3. JS: accept source, track start/complete via gtag ---
old_js = """(function() {
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
})();"""

new_js = """(function() {
  var VIDEO_SRC = '/videos/cor-intro.mp4';
  var overlay = document.getElementById('corVideoOverlay');
  var videoEl = document.getElementById('corVideoEl');
  var hasStarted = false;

  function track(eventName, source) {
    if (typeof gtag === 'function') {
      gtag('event', eventName, {
        video_title: 'COR 45s Intro',
        video_source: source || 'unknown'
      });
    }
  }

  window.openCorVideo = function(source) {
    hasStarted = false;
    videoEl.dataset.source = source || 'unknown';
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

  videoEl.addEventListener('play', function() {
    if (!hasStarted) {
      hasStarted = true;
      track('video_start', videoEl.dataset.source);
    }
  });
  videoEl.addEventListener('ended', function() {
    track('video_complete', videoEl.dataset.source);
  });
})();"""

replacements.append(("Analytics tracking in video JS", old_js, new_js))

errors = []
for name, anchor, block in replacements:
    count = content.count(anchor)
    if count == 0:
        errors.append(f"NOT FOUND: {name} — no changes made for this piece.")
        continue
    if count > 1:
        errors.append(f"AMBIGUOUS: {name} — appears {count} times, expected 1. No changes made for this piece.")
        continue
    content = content.replace(anchor, block)
    print(f"OK: {name} inserted.")

if errors:
    print("\n--- ISSUES ---")
    for e in errors:
        print(e)
    print("\nAborting — file was NOT changed since not all pieces matched.")
    sys.exit(1)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(content)

print(f"\nAll pieces inserted successfully. {PATH} updated ({len(original)} -> {len(content)} bytes).")
