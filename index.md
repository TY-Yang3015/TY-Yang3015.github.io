---
layout: default
title: Home
description: "Tianyue Yang builds generative models for physics, chemistry, and scientific computing."
---

<section class="home-hero" aria-labelledby="home-title">
  <div class="home-hero-copy">
    <h1 id="home-title">Models for <span>matter, motion,</span> and scientific discovery.</h1>
    <p class="hero-lead">
      I work at the intersection of AI, physics, and chemistry, building generative methods for scientific machine learning and physics-informed computation.
    </p>
    <div class="action-row">
      <a class="button button--primary" href="{{ '/projects/' | relative_url }}">Explore projects <span aria-hidden="true">↗</span></a>
      <a class="button" href="{{ '/assets/documents/cv.pdf' | relative_url }}" target="_blank" rel="noopener noreferrer">Download CV</a>
      <a class="button" href="mailto:15210283759a@gmail.com">Email</a>
    </div>
  </div>

  <div class="signal-mark" aria-hidden="true">
    <div class="signal-frame"><span>Y</span></div>
    <span class="signal-line signal-line--a"></span>
    <span class="signal-line signal-line--b"></span>
    <span class="signal-line signal-line--c"></span>
  </div>
</section>

<section class="home-facts" aria-label="Research profile">
  <article>
    <span class="fact-label">Focus</span>
    <p>Generative modelling for dynamical systems, computational physics, and quantum chemistry.</p>
  </article>
  <article>
    <span class="fact-label">Current</span>
    <p>Research Assistant at CCS@UCL and CSE@CUHK; MPhil student at the University of Cambridge.</p>
  </article>
  <article>
    <span class="fact-label">Approach</span>
    <p>Physics-aware design, scalable learning systems, and theory that explains model behaviour.</p>
  </article>
</section>

{% assign homepage_publications = "" | split: "" %}
{% if site.publications %}
  {% assign homepage_publications = site.publications | where: "indexed", true | sort: "year" | reverse %}
{% endif %}

<section class="home-section" aria-labelledby="selected-publications-title">
  <header class="section-heading">
    <h2 id="selected-publications-title">Selected publications</h2>
    <a class="text-link" href="{{ '/pub/' | relative_url }}">Full archive <span aria-hidden="true">↗</span></a>
  </header>

  {% if homepage_publications.size > 0 %}
    <div class="publication-list publication-list--home">
      {% for pub in homepage_publications %}
        {% include components/publication-card.html publication=pub variant="compact" %}
      {% endfor %}
    </div>
  {% else %}
    <p class="empty-state">No indexed publications yet.</p>
  {% endif %}
</section>

<section class="home-section" aria-labelledby="project-links-title">
  <header class="section-heading">
    <h2 id="project-links-title">Project links</h2>
    <a class="text-link" href="{{ '/projects/' | relative_url }}">All projects <span aria-hidden="true">↗</span></a>
  </header>

  <div class="project-list project-list--home">
    {% for project in site.data.projects limit: 2 %}
      {% include components/project-card.html project=project %}
    {% endfor %}

    <article class="project-card project-card--more polygon-panel">
      <div class="project-card-body">
        <h2>More experiments</h2>
        <p>Browse research code, model implementations, and scientific side projects.</p>
      </div>
      <a class="text-link project-link" href="{{ '/projects/' | relative_url }}">Open archive <span aria-hidden="true">↗</span></a>
    </article>
  </div>

  <details class="interest-panel polygon-panel">
    <summary>
      <span class="summary-mark" aria-hidden="true">+</span>
      <span>Outside the lab</span>
    </summary>
    <div class="interest-content">
      <p>Sichuan cuisine, theoretical chemistry, and modern political philosophy—especially the work of <a href="https://en.wikipedia.org/wiki/Giorgio_Agamben" target="_blank" rel="noopener noreferrer">Giorgio Agamben</a>.</p>
      <span>Per aspera ad astra</span>
    </div>
  </details>
</section>
