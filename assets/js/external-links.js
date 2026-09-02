(function () {
  var links = document.querySelectorAll("a[href]");

  Array.prototype.forEach.call(links, function (link) {
    var url;
    try { url = new URL(link.getAttribute("href"), window.location.href); } catch (error) { return; }

    var isWebLink = url.protocol === "http:" || url.protocol === "https:";
    var isPdf = /\.pdf$/i.test(url.pathname);
    var isExternal = isWebLink && url.origin !== window.location.origin;
    if (!isExternal && !isPdf) return;

    link.target = "_blank";
    var rel = (link.getAttribute("rel") || "").split(/\s+/).filter(Boolean);
    if (rel.indexOf("noopener") === -1) rel.push("noopener");
    if (rel.indexOf("noreferrer") === -1) rel.push("noreferrer");
    link.setAttribute("rel", rel.join(" "));
  });
})();
