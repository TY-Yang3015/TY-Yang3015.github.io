(function () {
  function initCollectionFilter() {
    var shells = document.querySelectorAll("[data-collection-default]");

    Array.prototype.forEach.call(shells, function (shell) {
      var links = Array.prototype.slice.call(shell.querySelectorAll(".collection-filter[data-filter]"));
      var blocks = Array.prototype.slice.call(shell.querySelectorAll(".series-block[data-group]"));
      if (!links.length || !blocks.length) return;

      var defaultFilter = shell.dataset.collectionDefault;
      var validFilters = links.map(function (link) { return link.dataset.filter; });

      function applyFilter(filterName, updateHash) {
        var showAll = filterName === defaultFilter;

        blocks.forEach(function (block) {
          var belongsToFilter = block.dataset.group === filterName;
          var belongsInAll = block.dataset.showInAll !== "false";
          block.hidden = showAll ? !belongsInAll : !belongsToFilter;
        });

        links.forEach(function (link) {
          var isActive = link.dataset.filter === filterName;
          link.classList.toggle("is-active", isActive);
          if (isActive) link.setAttribute("aria-current", "true");
          else link.removeAttribute("aria-current");
        });

        if (updateHash && window.history && window.history.replaceState) {
          window.history.replaceState(null, "", "#" + filterName);
        }
      }

      links.forEach(function (link) {
        link.addEventListener("click", function (event) {
          event.preventDefault();
          applyFilter(link.dataset.filter, true);
        });
      });

      var initial = window.location.hash.slice(1);
      applyFilter(validFilters.indexOf(initial) >= 0 ? initial : defaultFilter, false);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initCollectionFilter);
  } else {
    initCollectionFilter();
  }
})();
