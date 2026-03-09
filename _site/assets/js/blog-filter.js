document.addEventListener("DOMContentLoaded", function () {
  const filterLinks = Array.from(document.querySelectorAll(".collection-filter"));
  const blocks = Array.from(document.querySelectorAll(".series-block"));

  if (!filterLinks.length || !blocks.length) return;

  function showAllBlocks() {
    blocks.forEach((block) => {
      block.style.display = "";
    });
  }

  function showOnlyGroup(groupName) {
    blocks.forEach((block) => {
      block.style.display = block.dataset.group === groupName ? "" : "none";
    });
  }

  function setActiveLink(activeName) {
    filterLinks.forEach((link) => {
      if (link.dataset.filter === activeName) {
        link.setAttribute("aria-current", "page");
      } else {
        link.removeAttribute("aria-current");
      }
    });
  }

  function applyFilter(filterName) {
    if (filterName === "all-posts") {
      showAllBlocks();
    } else {
      showOnlyGroup(filterName);
    }

    setActiveLink(filterName);
  }

  filterLinks.forEach((link) => {
    link.addEventListener("click", function (event) {
      event.preventDefault();

      const filterName = this.dataset.filter;
      const href = this.getAttribute("href");

      applyFilter(filterName);

      if (window.history && window.history.replaceState) {
        window.history.replaceState(null, "", href);
      } else {
        window.location.hash = href;
      }
    });
  });

  const initialHash = window.location.hash.replace("#", "");
  const validFilters = filterLinks.map((link) => link.dataset.filter);
  const initialFilter = validFilters.includes(initialHash)
    ? initialHash
    : "all-posts";

  applyFilter(initialFilter);
});
