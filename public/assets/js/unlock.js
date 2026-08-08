// ── Sistema de desbloqueo progresivo (localStorage, client-side) ─────
// Modo "sequential": la clase N requiere completar la clase N-1.
// El progreso vive en localStorage['ecoudea-progress-<courseId>']
// (array de classIds — mismo storage que el botón de check de la clase).
(function () {
  'use strict';

  window.EcoudeaUnlock = {
    getProgress: function (courseId) {
      try {
        return new Set(JSON.parse(localStorage.getItem('ecoudea-progress-' + courseId) || '[]'));
      } catch (e) {
        return new Set();
      }
    },
    isAdminUnlocked: function () {
      try { return localStorage.getItem('ecoudea-unlock-all') === '1'; } catch (e) { return false; }
    },
    isLocked: function (unlockMode) {
      return unlockMode === 'sequential' && !this.isAdminUnlocked();
    },
    // orderedIds: los classIds del curso en orden de clase.
    // Devuelve true si la clase está bloqueada.
    isClassLocked: function (courseId, unlockMode, classId, orderedIds) {
      if (!this.isLocked(unlockMode)) return false;
      var idx = (orderedIds || []).indexOf(classId);
      if (idx <= 0) return false;
      var prev = orderedIds[idx - 1];
      return !this.getProgress(courseId).has(prev);
    },
  };
})();
