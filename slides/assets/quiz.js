/* AI-901 FDP — tiny interactive quiz + Mermaid-in-Reveal glue.
   Quiz markup convention:
   <div class="quiz">
     <div class="q">Question text</div>
     <button class="opt" data-correct="true">Right answer</button>
     <button class="opt" data-correct="false">Wrong answer</button>
     <div class="explain"><b>Why:</b> explanation…</div>
   </div>
*/
(function () {
  function wireQuizzes(root) {
    (root || document).querySelectorAll('.quiz').forEach(function (quiz) {
      if (quiz.dataset.wired) return;
      quiz.dataset.wired = '1';
      var explain = quiz.querySelector('.explain');
      quiz.querySelectorAll('.opt').forEach(function (btn) {
        btn.addEventListener('click', function () {
          var already = quiz.dataset.answered;
          var correct = btn.getAttribute('data-correct') === 'true';
          if (!already) {
            // reveal the correct one regardless, mark the clicked one
            quiz.querySelectorAll('.opt').forEach(function (o) {
              if (o.getAttribute('data-correct') === 'true') o.classList.add('correct');
            });
            if (!correct) btn.classList.add('wrong');
            if (explain) explain.classList.add('show');
            quiz.dataset.answered = '1';
          } else {
            // allow re-highlighting a re-click
            if (correct) btn.classList.add('correct'); else btn.classList.add('wrong');
          }
        });
      });
    });
  }

  function renderMermaid() {
    if (!window.mermaid) return;
    try { window.mermaid.run({ querySelector: '.mermaid:not([data-processed])' }); } catch (e) {}
  }

  document.addEventListener('DOMContentLoaded', function () {
    if (window.mermaid) {
      window.mermaid.initialize({ startOnLoad: false, theme: 'default', securityLevel: 'loose',
        themeVariables: { fontSize: '15px' } });
    }
    wireQuizzes(document);
  });

  window.addEventListener('load', function () {
    if (window.Reveal) {
      Reveal.on('ready', function () { renderMermaid(); wireQuizzes(document); });
      Reveal.on('slidechanged', function (e) { renderMermaid(); wireQuizzes(e.currentSlide); });
    } else {
      renderMermaid();
    }
  });
})();
