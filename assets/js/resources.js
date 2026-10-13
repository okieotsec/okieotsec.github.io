// Search and filters for the Resources page. The full list is already in the page, so without JavaScript nothing is lost.
// Everything is read from data attributes and shown or hidden; no resource text is ever inserted as HTML.
(function () {
  'use strict';
  var form = document.getElementById('res-controls');
  if (!form) { return; }
  var q = document.getElementById('res-q');
  var topic = document.getElementById('res-topic');
  var audience = document.getElementById('res-audience');
  var access = document.getElementById('res-access');
  var status = document.getElementById('res-status');
  var empty = document.getElementById('res-empty');
  var clear = document.getElementById('res-clear');
  var cards = Array.prototype.slice.call(document.querySelectorAll('.res-card'));
  var groups = Array.prototype.slice.call(document.querySelectorAll('[data-group]'));
  var sections = Array.prototype.slice.call(document.querySelectorAll('[data-section]'));

  function anyVisible(container) { return container.querySelector('.res-card:not([hidden])') !== null; }

  function apply() {
    var terms = q.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
    var shown = 0;
    cards.forEach(function (card) {
      var d = card.dataset;
      var ok = (!topic.value || d.category === topic.value) &&
        (!audience.value || d.audience.split(' ').indexOf(audience.value) !== -1) &&
        (!access.value || d.access === access.value) &&
        terms.every(function (t) { return d.text.indexOf(t) !== -1; });
      card.hidden = !ok;
      if (ok) { shown += 1; }
    });
    groups.forEach(function (g) { g.hidden = !anyVisible(g); });
    sections.forEach(function (s) { s.hidden = !anyVisible(s); });
    status.textContent = 'Showing ' + shown + ' of ' + cards.length + ' resources.';
    empty.hidden = shown !== 0;
  }

  form.hidden = false;
  form.addEventListener('input', apply);
  form.addEventListener('change', apply);
  form.addEventListener('reset', function () { window.setTimeout(apply, 0); });
  form.addEventListener('submit', function (e) { e.preventDefault(); });
  clear.addEventListener('click', function () { form.reset(); apply(); q.focus(); });
  apply();
})();
