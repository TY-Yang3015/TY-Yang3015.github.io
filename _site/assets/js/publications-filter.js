(function () {
  function initCollectionFilter() {
    var shell = document.querySelector(".collection-shell");
    var links = Array.prototype.slice.call(document.querySelectorAll(".collection-filter[data-filter]"));
    var blocks = Array.prototype.slice.call(document.querySelectorAll(".series-block[data-group]"));

    if (!links.length || !blocks.length) return;

    var defaultFilter = shell ? shell.getAttribute("data-collection-default") : links[0].dataset.filter;
    var validFilters = links.map(function (link) { return link.dataset.filter; });

    function setActive(filterName) {
      links.forEach(function (link) {
        var isActive = link.dataset.filter === filterName;
        link.classList.toggle("is-active", isActive);
        if (isActive) link.setAttribute("aria-current", "page");
        else link.removeAttribute("aria-current");
      });
    }

    function applyFilter(filterName, updateHash) {
      var showAll = filterName === defaultFilter;

      blocks.forEach(function (block) {
        block.hidden = !showAll && block.dataset.group !== filterName;
      });

      setActive(filterName);

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

    var initial = window.location.hash ? window.location.hash.slice(1) : defaultFilter;
    applyFilter(validFilters.indexOf(initial) >= 0 ? initial : defaultFilter, false);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initCollectionFilter);
  } else {
    initCollectionFilter();
  }
})();
