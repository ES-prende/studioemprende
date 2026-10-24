// Casos de éxito: anima la línea de tiempo una sola vez, al entrar en pantalla.
(function () {
  var el = document.querySelectorAll('.cr-ruta');
  if (!el.length) return;
  var quieto = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (quieto || !('IntersectionObserver' in window)) {
    el.forEach(function (s) { s.classList.add('visible'); });
    return;
  }
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (x) {
      if (x.isIntersecting) { x.target.classList.add('visible'); io.unobserve(x.target); }
    });
  }, { threshold: 0.4 });
  el.forEach(function (s) { io.observe(s); });
})();
