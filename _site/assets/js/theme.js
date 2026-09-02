(function () {
  var root = document.documentElement;
  var toggle = document.querySelector("[data-theme-toggle]");
  var themeMeta = document.querySelector('meta[name="theme-color"]');
  var media = window.matchMedia("(prefers-color-scheme: dark)");
  var transitionTimer;

  function savedTheme() {
    try { return localStorage.getItem("site-theme"); } catch (error) { return null; }
  }

  function updateControl(theme) {
    if (!toggle) return;
    var nextTheme = theme === "day" ? "night" : "day";
    toggle.setAttribute("aria-label", "Switch to " + nextTheme + " mode");
    toggle.setAttribute("title", "Switch to " + nextTheme + " mode");
    toggle.setAttribute("aria-pressed", theme === "night" ? "true" : "false");
  }

  function applyTheme(theme, persist, animate) {
    if (animate) {
      window.clearTimeout(transitionTimer);
      root.classList.add("is-theme-changing");
      transitionTimer = window.setTimeout(function () {
        root.classList.remove("is-theme-changing");
      }, 560);
    }

    root.dataset.theme = theme;
    if (themeMeta) themeMeta.setAttribute("content", theme === "night" ? "#080808" : "#fbfaff");
    updateControl(theme);

    if (persist) {
      try { localStorage.setItem("site-theme", theme); } catch (error) {}
    }
  }

  if (toggle) {
    toggle.addEventListener("click", function () {
      applyTheme(root.dataset.theme === "night" ? "day" : "night", true, true);
    });
  }

  if (media.addEventListener) {
    media.addEventListener("change", function (event) {
      if (!savedTheme()) applyTheme(event.matches ? "night" : "day", false, true);
    });
  }

  applyTheme(root.dataset.theme === "night" ? "night" : "day", false, false);
})();
