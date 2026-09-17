(function () {
  // Viewport-top offset matching .post-body h2/h3 { scroll-margin-top } in _toc.scss.
  var SCROLL_OFFSET = 90;

  function initPostToc() {
    var nav = document.querySelector("nav.post-toc");
    var body = document.querySelector(".post-body");
    if (!nav || !body) return;

    var headings = Array.prototype.slice.call(body.querySelectorAll("h2[id], h3[id]"));
    if (headings.length < 2) {
      if (nav.parentNode) nav.parentNode.removeChild(nav);
      return;
    }

    var label = document.createElement("p");
    label.className = "post-toc-label";
    label.textContent = "Contents";

    var list = document.createElement("ul");
    list.className = "post-toc-list";

    var linksById = {};

    headings.forEach(function (heading) {
      var item = document.createElement("li");
      item.className = heading.tagName === "H3" ? "toc-depth-3" : "toc-depth-2";

      var link = document.createElement("a");
      link.href = "#" + heading.id;
      link.textContent = heading.textContent.trim();
      link.addEventListener("click", function () {
        setActive(link); // native anchor jump still happens
      });

      item.appendChild(link);
      list.appendChild(item);
      linksById[heading.id] = link;
    });

    nav.appendChild(label);
    nav.appendChild(list);

    var activeLink = null;

    function setActive(link) {
      if (link === activeLink) return;
      activeLink = link;
      links.forEach(function (other) {
        other.classList.toggle("is-active", other === link);
      });
      if (link) link.scrollIntoView({ block: "nearest" });
    }

    var links = Array.prototype.slice.call(list.querySelectorAll("a"));

    // Nearest heading whose top is at/above the viewport offset, else null.
    function nearestAbove() {
      var current = null;
      for (var i = 0; i < headings.length; i++) {
        if (headings[i].getBoundingClientRect().top <= SCROLL_OFFSET) current = headings[i];
        else break;
      }
      return current;
    }

    if ("IntersectionObserver" in window) {
      var visibleIds = {};
      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) visibleIds[entry.target.id] = true;
          else delete visibleIds[entry.target.id];
        });
        var active = null;
        for (var i = 0; i < headings.length; i++) {
          if (visibleIds[headings[i].id]) { active = headings[i]; break; }
        }
        // Long sections scroll their heading past the observed band; fall back
        // to the nearest heading above the viewport top so one stays active.
        if (!active) active = nearestAbove();
        setActive(active ? linksById[active.id] : null);
      }, { rootMargin: "-" + SCROLL_OFFSET + "px 0px -60% 0px" });

      headings.forEach(function (heading) { observer.observe(heading); });
    } else {
      var ticking = false;
      function onScroll() {
        if (ticking) return;
        ticking = true;
        window.requestAnimationFrame(function () {
          ticking = false;
          var current = nearestAbove();
          setActive(current ? linksById[current.id] : null);
        });
      }
      window.addEventListener("scroll", onScroll, { passive: true });
      onScroll();
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initPostToc);
  } else {
    initPostToc();
  }
})();
