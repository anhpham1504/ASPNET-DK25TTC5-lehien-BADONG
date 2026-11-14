// GitHub Pages serves deep links through 404.html. Restore the requested route
// before Blazor starts so the router renders the intended page from a 200 shell.
(function restoreGitHubPagesRoute() {
  const storageKey = 'ba-dong-spa-path';
  let requestedPath = null;

  try {
    requestedPath = window.sessionStorage.getItem(storageKey);
    window.sessionStorage.removeItem(storageKey);
  } catch (_) {
    return;
  }

  if (!requestedPath) return;

  const basePath = document.querySelector('base')?.getAttribute('href') || '/';
  const target = new URL(requestedPath, window.location.origin);
  if (target.origin === window.location.origin && target.pathname.startsWith(basePath)) {
    window.history.replaceState(null, '', target.pathname + target.search + target.hash);
  }
})();

const dialogStates = new Map();
const focusableSelector = [
  'a[href]',
  'button:not([disabled])',
  'input:not([disabled])',
  'select:not([disabled])',
  'textarea:not([disabled])',
  '[tabindex]:not([tabindex="-1"])'
].join(',');

function getFocusableElements(dialog) {
  return Array.from(dialog.querySelectorAll(focusableSelector)).filter(function (element) {
    return !element.hidden && !element.inert && element.getAttribute('aria-hidden') !== 'true' && element.getClientRects().length > 0;
  });
}

function updateBodyLock() {
  const hasActiveDialog = Array.from(dialogStates.values()).some(function (state) { return state.active; });
  document.body.classList.toggle('body-locked', hasActiveDialog);
}

function releaseDialog(state) {
  if (state.dialog && state.keydown) state.dialog.removeEventListener('keydown', state.keydown);
  (state.inerted || []).forEach(function (element) { element.inert = false; });

  state.dialog = null;
  state.keydown = null;
  state.inerted = [];
  state.active = false;
  updateBodyLock();
}

function restoreDialogFocus(state, fallbackSelector) {
  let target = state.returnFocus;
  if (!(target instanceof HTMLElement) || !target.isConnected || target.inert || target.closest('[inert]')) {
    target = fallbackSelector ? document.querySelector(fallbackSelector) : null;
  }

  if (target instanceof HTMLElement && target.isConnected && !target.inert && !target.closest('[inert]')) {
    target.focus({ preventScroll: true });
  }
}

window.siteUi = {
  init: function () {
    var header = document.querySelector('.site-header');
    if (!header) return;
    var onScroll = function () { header.classList.toggle('is-scrolled', window.scrollY > 24); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  },
  setBodyLock: function (locked) {
    document.body.classList.toggle('body-locked', locked);
  },
  focus: function (id) {
    window.setTimeout(function () {
      var element = document.getElementById(id);
      if (element) element.focus();
    }, 40);
  },
  rememberDialogFocus: function (id) {
    const state = dialogStates.get(id) || {};
    state.returnFocus = document.activeElement instanceof HTMLElement ? document.activeElement : null;
    dialogStates.set(id, state);
  },
  activateDialog: function (id, initialFocusSelector) {
    const dialog = document.getElementById(id);
    if (!dialog) return;

    const state = dialogStates.get(id) || {};
    if (state.active) return;

    state.dialog = dialog;
    state.inerted = [];

    let current = dialog;
    while (current && current !== document.body) {
      const parent = current.parentElement;
      if (!parent) break;

      Array.from(parent.children).forEach(function (sibling) {
        if (sibling === current || sibling.getAttribute('data-dialog-allow') === id || sibling.inert) return;
        sibling.inert = true;
        state.inerted.push(sibling);
      });

      current = parent;
    }

    state.keydown = function (event) {
      if (event.key !== 'Tab') return;

      const focusable = getFocusableElements(dialog);
      if (focusable.length === 0) {
        event.preventDefault();
        dialog.focus({ preventScroll: true });
        return;
      }

      const first = focusable[0];
      const last = focusable[focusable.length - 1];
      const activeElement = document.activeElement;

      if (event.shiftKey && (activeElement === first || !dialog.contains(activeElement))) {
        event.preventDefault();
        last.focus({ preventScroll: true });
      } else if (!event.shiftKey && (activeElement === last || !dialog.contains(activeElement))) {
        event.preventDefault();
        first.focus({ preventScroll: true });
      }
    };

    dialog.addEventListener('keydown', state.keydown);
    state.active = true;
    dialogStates.set(id, state);
    updateBodyLock();

    window.requestAnimationFrame(function () {
      const preferred = initialFocusSelector ? dialog.querySelector(initialFocusSelector) : null;
      const target = preferred || getFocusableElements(dialog)[0] || dialog;
      target.focus({ preventScroll: true });
    });
  },
  beginDialogClose: function (id) {
    const state = dialogStates.get(id);
    if (!state) return;

    releaseDialog(state);
    dialogStates.set(id, state);
  },
  completeDialogClose: function (id, fallbackSelector) {
    const state = dialogStates.get(id);
    if (!state) return;

    dialogStates.delete(id);
    updateBodyLock();
    restoreDialogFocus(state, fallbackSelector);
  },
  deactivateDialog: function (id, restoreFocus, fallbackSelector) {
    const state = dialogStates.get(id);
    if (!state) return;

    releaseDialog(state);
    dialogStates.delete(id);
    updateBodyLock();
    if (restoreFocus !== false) restoreDialogFocus(state, fallbackSelector);
  },
  copyText: async function (text) {
    try {
      await navigator.clipboard.writeText(text);
      return true;
    } catch (_) {
      return false;
    }
  }
};
