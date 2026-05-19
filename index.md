---
layout: default
title: Home
---


<div class="hero">
  <div class="kicker">AI • Physics • Chemistry</div>
  <h1 class="glitch" data-text="Tianyue Yang">Tianyue Yang</h1>
  <p class="lead">
    I work at the intersection of AI, physics, and chemistry, with a focus on generative modelling for scientific machine learning and physics-inspired methods.
  </p>

  <div class="cta">
    <a class="btn primary" href="{{ '/projects/' | relative_url }}">View Projects</a>
    <a class="btn good" href="mailto:15210283759a@gmail.com">Email Me</a>
    <a class="btn" href="https://github.com/TY-Yang3015">GitHub</a>
    <a class="btn" href="/assets/cv.pdf">Download CV</a>
  </div>
</div>

<div class="grid">
  <div class="card">
    <h3>Research Interests</h3>
    <p>
      I work on generative modelling and AI for science, especially applications in computational fluid dynamics, chemistry, and physics-informed learning.
    </p>
  </div>

  <div class="card">
    <h3>Current Role</h3>
    <p>
      I am a Research Assistant at CCS@UCL and CSE@CUHK, working with Prof. Peter Coveney, Dr. Xiao Xue, and Dr. Shengchao Liu on generative methods for CFD and related scientific problems.
    </p>
  </div>
</div>

<hr />

{% assign homepage_publications = "" | split: "" %}
{% if site.publications %}
  {% assign homepage_publications = site.publications | where: "indexed", true | sort: "year" | reverse %}
{% endif %}

<div class="prose pub-section">
  <h2>★ Selected Publications ★</h2>

  {% if homepage_publications.size > 0 %}
    <div class="pub-list">
      {% for pub in homepage_publications %}
        {% assign primary_url = pub.paper_url | default: pub.url | default: pub.doi_url | default: pub.arxiv_url | default: pub.pdf_url %}
        {% assign pub_type = pub.type | default: pub.entry_type | default: "publication" %}
        {% assign pub_media = pub.image | default: pub.image_url | default: pub.gif | default: pub.gif_url %}
        {% assign pub_media_alt = pub.image_alt | default: pub.gif_alt | default: pub.title %}

        <article class="pub-item publication-card">
  <div class="pub-top">
    <span class="pub-tag">{{ pub_type | replace: "_", " " | replace: "-", " " }}</span>
    {% if pub.year %}<span class="pub-year">{{ pub.year }}</span>{% endif %}
  </div>

  <h3 class="pub-title">
    {% if primary_url %}
      {% if primary_url contains '://' %}
        <a href="{{ primary_url }}" rel="noopener">{{ pub.title }}</a>
      {% else %}
        <a href="{{ primary_url | relative_url }}">{{ pub.title }}</a>
      {% endif %}
    {% else %}
      {{ pub.title }}
    {% endif %}
  </h3>

  {% if pub.authors %}
    <p class="pub-authors pub-authors-above">{{ pub.authors }}</p>
  {% endif %}

  <div class="pub-body">
    {% if pub_media %}
      <figure class="publication-media index-publication-media pub-thumbnail">
        {% if primary_url %}
          {% if primary_url contains '://' %}
            <a href="{{ primary_url }}" rel="noopener" aria-label="Open {{ pub.title | strip_html | escape }}">
          {% else %}
            <a href="{{ primary_url | relative_url }}" aria-label="Open {{ pub.title | strip_html | escape }}">
          {% endif %}
        {% endif %}

        {% if pub_media contains '://' %}
          <img src="{{ pub_media }}" alt="{{ pub_media_alt | strip_html | escape }}" loading="lazy" decoding="async">
        {% else %}
          <img src="{{ pub_media | relative_url }}" alt="{{ pub_media_alt | strip_html | escape }}" loading="lazy" decoding="async">
        {% endif %}

        {% if primary_url %}</a>{% endif %}
      </figure>
    {% endif %}

    <div class="pub-content">
      {% if pub.note or pub.abstract %}
        <p class="pub-note">
          {% if pub.note %}{{ pub.note }}{% endif %}
          {% if pub.abstract %}{% if pub.note %}<br>{% endif %}{{ pub.abstract | strip_html | truncate: 180 }}{% endif %}
        </p>
      {% endif %}

      <div class="post-links pub-links">
        {% if pub.pdf_url %}
          {% if pub.pdf_url contains '://' %}
            <a class="post-link" href="{{ pub.pdf_url }}" rel="noopener">PDF ↗</a>
          {% else %}
            <a class="post-link" href="{{ pub.pdf_url | relative_url }}">PDF ↗</a>
          {% endif %}
        {% endif %}

        {% if pub.doi_url %}
          <a class="post-link" href="{{ pub.doi_url }}" rel="noopener">DOI ↗</a>
        {% endif %}

        {% if pub.arxiv_url %}
          <a class="post-link" href="{{ pub.arxiv_url }}" rel="noopener">arXiv ↗</a>
        {% endif %}

        {% if pub.code_url %}
          <a class="post-link" href="{{ pub.code_url }}" rel="noopener">Code ↗</a>
        {% endif %}

        {% if pub.project_url %}
          <a class="post-link" href="{{ pub.project_url }}" rel="noopener">Project ↗</a>
        {% endif %}
      </div>
    </div>
  </div>
</article>
      {% endfor %}
    </div>
  {% else %}
    <p class="pub-note">No indexed publications yet — the archive is still forming</p>
  {% endif %}
</div>

<div class="prose project-section">
  <h2>Project Links</h2>
  <p class="project-intro">Past projects I've been working on!</p>

  <div class="project-list">
    <article class="project-item">
      <div class="project-top">
        <span class="project-tag">JAX</span>
        <span class="project-kind">AI4Chem</span>
      </div>
      <h3>
        <a href="https://github.com/TY-Yang3015/PsiFlax">
          PsiFlax
        </a>
      </h3>
      <p class="project-desc">
        Deep QMC framework built with JAX and Flax.
      </p>
    </article>

    <article class="project-item">
      <div class="project-top">
        <span class="project-tag">Diffusion</span>
        <span class="project-kind">AI4CFD</span>
      </div>
      <h3>
        <a href="https://github.com/TY-Yang3015/fleiadex">
          Fleiadex
        </a>
      </h3>
      <p class="project-desc">
        Latent diffusion models implemented in JAX.
      </p>
    </article>

    <article class="project-item more-projects">
      <div class="project-top">
        <span class="project-tag">More</span>
        <span class="project-kind">Archive</span>
      </div>
      <h3>
        <a href="{{ '/projects/' | relative_url }}">
          See the project page for more!
        </a>
      </h3>
      <p class="project-desc">
        More experiments, research code, and side projects.
      </p>
    </article>
  </div>

  <details class="interest-box mystic-interest">
    <summary>
      <span class="interest-summary-inner">
        <span class="interest-sigil">✦</span>
        <span class="interest-title">Personal Interests</span>
        <span class="interest-whisper">hidden archive</span>
      </span>
    </summary>

    <div class="interest-content">
      <p class="interest-intro">
        A few things I enjoy outside research:
      </p>

      <ul>
        <li>Sichuan Cuisine is my favourite!</li>
        <li>As a former ChOer, my passion for theoretical chemistry persists...</li>
        <li>
          Interested in modern political philosophy, my favourite modern philosopher is
          <a href="https://en.wikipedia.org/wiki/Giorgio_Agamben">
            Giorgio Agamben
          </a>
        </li>
      </ul>

      <p class="interest-note">
        ✦ Per aspera ad astra ✦
      </p>
    </div>
  </details>
</div>
