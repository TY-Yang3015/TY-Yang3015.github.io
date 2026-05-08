---
layout: default
title: Publications
permalink: /pub/
---

{% assign publications = "" | split: "" %}
{% if site.publications %}
  {% assign publications = site.publications | sort: "year" | reverse %}
{% endif %}
{% assign grouped_publications = publications | group_by: "year" %}
{% assign selected_publications = publications | where: "selected", true %}

<div class="blog-shell collection-shell" data-collection-default="all-publications">
  <section class="blog-hero" aria-labelledby="publications-title">
    <p class="kicker">Papers</p>
    <h1 id="publications-title" class="glitch" data-text="Publications">Publications</h1>
    <p class="blog-lead">
      Papers, preprints, and research threads across AI, physics, chemistry, and adjacent curiosities ✦
    </p>
  </section>

  <div class="blog-layout">
    <aside class="blog-sidebar" aria-label="Publication filters">
      <nav class="collection-panel mystic-archive">
        <div class="collection-head">
          <span class="collection-sigil main-sigil">✦</span>
          <div class="collection-head-copy">
            <h2>Archive</h2>
            <p class="collection-whisper">research index</p>
          </div>
        </div>

        <ul class="collection-list">
          <li>
            <a class="collection-filter" href="#all-publications" data-filter="all-publications">
              <span class="collection-link-main"><span class="collection-item-sigil">◎</span><span>All Publications</span></span>
              <span class="collection-count">{{ publications | size }}</span>
            </a>
          </li>

          {% if selected_publications.size > 0 %}
            <li>
              <a class="collection-filter" href="#selected-publications" data-filter="selected-publications">
                <span class="collection-link-main"><span class="collection-item-sigil">★</span><span>Selected</span></span>
                <span class="collection-count">{{ selected_publications | size }}</span>
              </a>
            </li>
          {% endif %}

          {% for group in grouped_publications %}
            {% if group.name and group.name != "" %}
              <li>
                <a class="collection-filter" href="#year-{{ group.name | slugify }}" data-filter="year-{{ group.name | slugify }}">
                  <span class="collection-link-main"><span class="collection-item-sigil">◇</span><span>{{ group.name }}</span></span>
                  <span class="collection-count">{{ group.items | size }}</span>
                </a>
              </li>
            {% endif %}
          {% endfor %}
        </ul>

        <p class="collection-note">Sort papers by categories ♪</p>
      </nav>
    </aside>

    <section class="blog-index" id="all-publications">
      {% if publications.size > 0 %}
        {% if selected_publications.size > 0 %}
          <section class="series-block" id="selected-publications" data-group="selected-publications" aria-labelledby="heading-selected-publications">
            <div class="series-heading">
              <div class="series-heading-main">
                <span class="series-sigil">★</span>
                <h2 id="heading-selected-publications">Selected Publications</h2>
              </div>
              <span class="series-count">{{ selected_publications | size }} entries</span>
            </div>

            <div class="post-list">
              {% for pub in selected_publications %}
                {% assign primary_url = pub.paper_url | default: pub.url | default: pub.doi_url | default: pub.arxiv_url | default: pub.pdf_url %}
                {% assign pub_type = pub.type | default: pub.entry_type | default: "publication" %}
                <article class="post-card publication-card">
                  <div class="post-meta">
                    <span class="post-tag">{{ pub_type | replace: "_", " " | replace: "-", " " }}</span>
                    {% if pub.year %}<time class="post-date">{{ pub.year }}</time>{% endif %}
                  </div>

                  <h3>
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

                  {% if pub.authors %}<p class="post-excerpt authors">{{ pub.authors }}</p>{% endif %}
                  {% if pub.venue or pub.note or pub.abstract %}
                    <p class="post-excerpt">
                      {% if pub.venue %}<strong>{{ pub.venue }}</strong>{% endif %}
                      {% if pub.note %}{% if pub.venue %} · {% endif %}{{ pub.note }}{% endif %}
                      {% if pub.abstract %}<br>{{ pub.abstract | strip_html | truncate: 220 }}{% endif %}
                    </p>
                  {% endif %}

                  <div class="post-links">
                    {% if pub.pdf_url %}{% if pub.pdf_url contains '://' %}<a class="post-link" href="{{ pub.pdf_url }}" rel="noopener">PDF ↗</a>{% else %}<a class="post-link" href="{{ pub.pdf_url | relative_url }}">PDF ↗</a>{% endif %}{% endif %}
                    {% if pub.doi_url %}<a class="post-link" href="{{ pub.doi_url }}" rel="noopener">DOI ↗</a>{% endif %}
                    {% if pub.arxiv_url %}<a class="post-link" href="{{ pub.arxiv_url }}" rel="noopener">arXiv ↗</a>{% endif %}
                    {% if pub.code_url %}<a class="post-link" href="{{ pub.code_url }}" rel="noopener">Code ↗</a>{% endif %}
                    {% if pub.project_url %}<a class="post-link" href="{{ pub.project_url }}" rel="noopener">Project ↗</a>{% endif %}
                    {% if pub.bibtex_url %}{% if pub.bibtex_url contains '://' %}<a class="post-link" href="{{ pub.bibtex_url }}" rel="noopener">BibTeX ♪</a>{% else %}<a class="post-link" href="{{ pub.bibtex_url | relative_url }}">BibTeX ♪</a>{% endif %}{% endif %}
                    {% if pub.zh_url %}{% if pub.zh_url contains '://' %}<a class="post-link zh-link" href="{{ pub.zh_url }}" rel="noopener">中文阅读 ♪</a>{% else %}<a class="post-link zh-link" href="{{ pub.zh_url | relative_url }}">中文阅读 ♪</a>{% endif %}{% endif %}
                  </div>
                </article>
              {% endfor %}
            </div>
          </section>
        {% endif %}

        {% for group in grouped_publications %}
          {% if group.name and group.name != "" %}
            {% assign year_items = group.items | sort: "date" | reverse %}
            <section class="series-block" id="year-{{ group.name | slugify }}" data-group="year-{{ group.name | slugify }}" aria-labelledby="heading-year-{{ group.name | slugify }}">
              <div class="series-heading">
                <div class="series-heading-main">
                  <span class="series-sigil">◇</span>
                  <h2 id="heading-year-{{ group.name | slugify }}">{{ group.name }}</h2>
                </div>
                <span class="series-count">{{ group.items | size }} entries</span>
              </div>

              <div class="post-list">
                {% for pub in year_items %}
                  {% assign primary_url = pub.paper_url | default: pub.url | default: pub.doi_url | default: pub.arxiv_url | default: pub.pdf_url %}
                  {% assign pub_type = pub.type | default: pub.entry_type | default: "publication" %}
                  <article class="post-card publication-card">
                    <div class="post-meta">
                      <span class="post-tag">{{ pub_type | replace: "_", " " | replace: "-", " " }}</span>
                      {% if pub.year %}<time class="post-date">{{ pub.year }}</time>{% endif %}
                    </div>

                    <h3>
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

                    {% if pub.authors %}<p class="post-excerpt authors">{{ pub.authors }}</p>{% endif %}
                    {% if pub.venue or pub.note or pub.abstract %}
                      <p class="post-excerpt">
                        {% if pub.venue %}<strong>{{ pub.venue }}</strong>{% endif %}
                        {% if pub.note %}{% if pub.venue %} · {% endif %}{{ pub.note }}{% endif %}
                        {% if pub.abstract %}<br>{{ pub.abstract | strip_html | truncate: 220 }}{% endif %}
                      </p>
                    {% endif %}

                    <div class="post-links">
                      {% if pub.pdf_url %}{% if pub.pdf_url contains '://' %}<a class="post-link" href="{{ pub.pdf_url }}" rel="noopener">PDF ↗</a>{% else %}<a class="post-link" href="{{ pub.pdf_url | relative_url }}">PDF ↗</a>{% endif %}{% endif %}
                      {% if pub.doi_url %}<a class="post-link" href="{{ pub.doi_url }}" rel="noopener">DOI ↗</a>{% endif %}
                      {% if pub.arxiv_url %}<a class="post-link" href="{{ pub.arxiv_url }}" rel="noopener">arXiv ↗</a>{% endif %}
                      {% if pub.code_url %}<a class="post-link" href="{{ pub.code_url }}" rel="noopener">Code ↗</a>{% endif %}
                      {% if pub.project_url %}<a class="post-link" href="{{ pub.project_url }}" rel="noopener">Project ↗</a>{% endif %}
                      {% if pub.bibtex_url %}{% if pub.bibtex_url contains '://' %}<a class="post-link" href="{{ pub.bibtex_url }}" rel="noopener">BibTeX ♪</a>{% else %}<a class="post-link" href="{{ pub.bibtex_url | relative_url }}">BibTeX ♪</a>{% endif %}{% endif %}
                      {% if pub.zh_url %}{% if pub.zh_url contains '://' %}<a class="post-link zh-link" href="{{ pub.zh_url }}" rel="noopener">中文阅读 ♪</a>{% else %}<a class="post-link zh-link" href="{{ pub.zh_url | relative_url }}">中文阅读 ♪</a>{% endif %}{% endif %}
                    </div>
                  </article>
                {% endfor %}
              </div>
            </section>
          {% endif %}
        {% endfor %}
      {% else %}
        <div class="empty-blog"><p>No publications yet — the archive is still forming ♪</p></div>
      {% endif %}
    </section>
  </div>
</div>

<script src="{{ '/assets/js/publications-filter.js' | relative_url }}" defer></script>
