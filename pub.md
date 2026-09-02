---
layout: default
title: Publications
permalink: /pub/
description: "Publications and dissertations by Tianyue Yang."
---

{% assign publications = "" | split: "" %}
{% if site.publications %}{% assign publications = site.publications | sort: "year" | reverse %}{% endif %}
{% assign grouped_publications = publications | group_by: "year" %}
{% assign selected_publications = publications | where: "selected", true %}

<div class="archive-shell" data-collection-default="all-publications">
  {% include components/page-intro.html title="Publications" description="Papers, preprints, and dissertations across AI, physics, chemistry, and scientific computing." %}

  <div class="archive-layout">
    <aside class="archive-sidebar">
      <nav class="archive-nav polygon-panel" aria-label="Publication filters">
        <ul>
          <li><a class="collection-filter" href="#all-publications" data-filter="all-publications"><span>All publications</span><b>{{ publications | size }}</b></a></li>
          {% if selected_publications.size > 0 %}<li><a class="collection-filter" href="#selected-publications" data-filter="selected-publications"><span>Selected</span><b>{{ selected_publications | size }}</b></a></li>{% endif %}
          {% for group in grouped_publications %}
            {% if group.name and group.name != "" %}<li><a class="collection-filter" href="#year-{{ group.name | slugify }}" data-filter="year-{{ group.name | slugify }}"><span>{{ group.name }}</span><b>{{ group.items | size }}</b></a></li>{% endif %}
          {% endfor %}
        </ul>
      </nav>
    </aside>

    <section class="archive-index" id="all-publications" aria-live="polite">
      {% if publications.size > 0 %}
        {% if selected_publications.size > 0 %}
          <section class="series-block" id="selected-publications" data-group="selected-publications" data-show-in-all="false">
            <header class="series-heading"><span class="series-mark" aria-hidden="true">S</span><div><h2>Selected publications</h2></div><small>{{ selected_publications | size }} records</small></header>
            <div class="publication-list">
              {% for pub in selected_publications %}{% include components/publication-card.html publication=pub %}{% endfor %}
            </div>
          </section>
        {% endif %}

        {% for group in grouped_publications %}
          {% if group.name and group.name != "" %}
            {% assign year_items = group.items | sort: "date" | reverse %}
            <section class="series-block" id="year-{{ group.name | slugify }}" data-group="year-{{ group.name | slugify }}">
              <header class="series-heading"><span class="series-mark" aria-hidden="true">{{ group.name | slice: -2, 2 }}</span><div><h2>{{ group.name }}</h2></div><small>{{ group.items | size }} records</small></header>
              <div class="publication-list">
                {% for pub in year_items %}{% include components/publication-card.html publication=pub %}{% endfor %}
              </div>
            </section>
          {% endif %}
        {% endfor %}
      {% else %}
        <div class="empty-state"><p>No publication records are indexed yet.</p></div>
      {% endif %}
    </section>
  </div>
</div>

<script src="{{ '/assets/js/collection-filter.js' | relative_url }}" defer></script>
