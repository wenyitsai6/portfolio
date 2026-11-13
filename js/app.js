/* Wenyi Tsai — shared behaviour */
(function () {
  'use strict';
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ── theme (persisted) ─────────────────────────────────── */
  var root = document.documentElement;
  try {
    var saved = localStorage.getItem('wt-theme');
    if (saved) root.dataset.theme = saved;
  } catch (e) {}
  function syncTog() {
    var d = root.dataset.theme === 'dark';
    document.querySelectorAll('.tog').forEach(function (b) {
      b.textContent = d ? '☀' : '☾';
      b.setAttribute('aria-label', d ? 'Switch to light mode' : 'Switch to dark mode');
    });
  }
  syncTog();
  document.addEventListener('click', function (e) {
    var t = e.target.closest('.tog');
    if (!t) return;
    root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('wt-theme', root.dataset.theme); } catch (err) {}
    syncTog();
  });

  /* ── mobile nav ────────────────────────────────────────── */
  document.addEventListener('click', function (e) {
    var b = e.target.closest('.burger');
    if (b) {
      var links = document.querySelector('.nlinks');
      if (links) links.classList.toggle('open');
      return;
    }
    if (!e.target.closest('.nlinks')) {
      var l = document.querySelector('.nlinks.open');
      if (l) l.classList.remove('open');
    }
  });

  /* ── custom WT cursor ──────────────────────────────────── */
  var cur = document.getElementById('cur');
  if (cur && matchMedia('(pointer:fine)').matches) {
    var tx = -99, ty = -99, cx = -99, cy = -99;
    addEventListener('pointermove', function (e) { tx = e.clientX; ty = e.clientY; });
    (function loop() {
      var k = reduce ? 1 : 0.18;
      cx += (tx - cx) * k; cy += (ty - cy) * k;
      cur.style.left = cx + 'px'; cur.style.top = cy + 'px';
      requestAnimationFrame(loop);
    })();
    document.addEventListener('pointerover', function (e) {
      if (e.target.closest('a,button,.shelf')) cur.classList.add('big');
    });
    document.addEventListener('pointerout', function (e) {
      if (e.target.closest('a,button,.shelf')) cur.classList.remove('big');
    });
  }

  /* ── role rotator — cycles once, then settles on the title ─ */
  var roles = document.querySelectorAll('#roles i');
  if (roles.length) {
    var last = roles.length - 1;
    if (reduce) {
      roles.forEach(function (r, k) { r.classList.toggle('on', k === last); });
    } else {
      var i = 0;
      var tick = setInterval(function () {
        roles[i].classList.remove('on');
        i += 1;
        roles[i].classList.add('on');
        if (i === last) clearInterval(tick);   // land on the title and stay
      }, 1500);
    }
  }

  /* ── seamless ticker ───────────────────────────────────── */
  var tk = document.querySelector('.tk-track');
  if (tk) tk.innerHTML += tk.innerHTML;

  /* ── folder reveal ────────────────────────────────────── */
  var folder = document.querySelector('.folder');
  if (folder) {
    var busy = false;
    var toggle = function () {
      if (busy) return;
      busy = true;
      var opening = !folder.classList.contains('open');
      if (opening) {
        folder.classList.remove('closing');
        folder.classList.add('open');
      } else {
        folder.classList.remove('open');
        folder.classList.add('closing');
      }
      folder.setAttribute('aria-expanded', opening ? 'true' : 'false');
      var doc = folder.querySelector('.folder-doc');
      var done = function () {
        folder.classList.remove('closing');
        busy = false;
        doc.removeEventListener('animationend', done);
      };
      doc.addEventListener('animationend', done);
      setTimeout(done, 1200); // safety net if the animation never fires
    };
    folder.addEventListener('click', toggle);
    folder.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); }
    });
  }

  /* ── pause the hero video when off-screen / reduced motion ─ */
  var hv = document.querySelector('.hero-bg video');
  if (hv) {
    if (reduce) { hv.pause(); hv.removeAttribute('autoplay'); }
    else if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) {
        es.forEach(function (e) { e.isIntersecting ? hv.play().catch(function(){}) : hv.pause(); });
      }, { threshold: .01 }).observe(hv);
    }
  }

  /* ── lazy project previews (rachelchen.tech pattern) ───── */
  document.querySelectorAll('video.preview').forEach(function (v) {
    var card = v.closest('.proj');
    if (!card) return;
    var load = function () {
      if (v.dataset.loaded) return;
      v.dataset.loaded = '1';
      v.src = v.dataset.src;
      v.addEventListener('loadeddata', function () { v.dataset.ready = '1'; }, { once: true });
    };
    // warm it as soon as the card is near the viewport, play only on hover
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es, obs) {
        es.forEach(function (e) { if (e.isIntersecting) { load(); obs.disconnect(); } });
      }, { rootMargin: '300px' }).observe(card);
    } else { load(); }
    card.addEventListener('pointerenter', function () {
      load();
      if (!reduce) v.play().catch(function () {});
    });
    card.addEventListener('pointerleave', function () { v.pause(); v.currentTime = 0; });
  });

  /* ── scroll reveal ─────────────────────────────────────── */
  var rv = document.querySelectorAll('.rv');
  if (rv.length) {
    if (reduce || !('IntersectionObserver' in window)) {
      rv.forEach(function (el) { el.classList.add('in'); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: .08 });
      rv.forEach(function (el) { io.observe(el); });
    }
  }

  /* ── mark current nav item ─────────────────────────────── */
  var here = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nlinks a').forEach(function (a) {
    var href = a.getAttribute('href') || '';
    if (href === here || (here.indexOf('work') === 0 && href === 'work.html')) {
      a.setAttribute('aria-current', 'page');
    }
  });
})();
