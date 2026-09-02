---
layout: default
title: Blog
permalink: /blog/
description: "Research notes on AI, physics, chemistry, and scientific machine learning."
---

{% assign grouped_posts = site.posts | group_by: "series" %}
{% assign standalone_count = 0 %}
{% for post in site.posts %}
  {% if post.series == nil or post.series == "" %}{% assign standalone_count = standalone_count | plus: 1 %}{% endif %}
{% endfor %}

<div class="archive-shell" data-collection-default="all-posts">
  {% include components/page-intro.html title="Blog" description="Research notes and technical explorations across learning systems, physics, and chemistry." %}

  <div class="archive-layout">
    <aside class="archive-sidebar">
      <nav class="archive-nav polygon-panel" aria-label="Blog collections">
        <ul>
          <li><a class="collection-filter" href="#all-posts" data-filter="all-posts"><span>All posts</span><b>{{ site.posts | size }}</b></a></li>
          {% for group in grouped_posts %}
            {% if group.name and group.name != "" %}
              <li><a class="collection-filter" href="#series-{{ group.name | slugify }}" data-filter="series-{{ group.name | slugify }}"><span>{{ group.name }}</span><b>{{ group.items | size }}</b></a></li>
            {% endif %}
          {% endfor %}
          {% if standalone_count > 0 %}
            <li><a class="collection-filter" href="#series-standalone" data-filter="series-standalone"><span>Standalone</span><b>{{ standalone_count }}</b></a></li>
          {% endif %}
        </ul>
      </nav>
    </aside>

    <section class="archive-index" id="all-posts" aria-live="polite">
      {% if site.posts.size > 0 %}
        {% for group in grouped_posts %}
          {% if group.name and group.name != "" %}
            <section class="series-block" id="series-{{ group.name | slugify }}" data-group="series-{{ group.name | slugify }}">
              <header class="series-heading">
                <span class="series-mark" aria-hidden="true">{{ group.items.first.series_icon | default: "N" }}</span>
                <div><h2>{{ group.name }}</h2></div>
                <small>{{ group.items | size }} entries</small>
              </header>
              <div class="post-list">
                {% for post in group.items %}
                  <article class="post-record polygon-panel">
                    <div class="post-record-meta"><time>{{ post.date | date: "%d.%m.%Y" }}</time></div>
                    <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
                    {% if post.excerpt %}<p>{{ post.excerpt | strip_html | truncate: 180 }}</p>{% endif %}
                    <div class="record-links">
                      <a href="{{ post.url | relative_url }}">Read note <span aria-hidden="true">↗</span></a>
                      {% if post.zh_url %}<a href="{% if post.zh_url contains '://' %}{{ post.zh_url }}{% else %}{{ post.zh_url | relative_url }}{% endif %}">中文</a>{% endif %}
                    </div>
                  </article>
                {% endfor %}
              </div>
            </section>
          {% endif %}
        {% endfor %}

        {% if standalone_count > 0 %}
          <section class="series-block" id="series-standalone" data-group="series-standalone">
            <header class="series-heading"><span class="series-mark" aria-hidden="true">N</span><div><h2>Standalone</h2></div><small>{{ standalone_count }} entries</small></header>
            <div class="post-list">
              {% for post in site.posts %}
                {% if post.series == nil or post.series == "" %}
                  <article class="post-record polygon-panel">
                    <div class="post-record-meta"><time>{{ post.date | date: "%d.%m.%Y" }}</time></div>
                    <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
                    {% if post.excerpt %}<p>{{ post.excerpt | strip_html | truncate: 180 }}</p>{% endif %}
                    <div class="record-links"><a href="{{ post.url | relative_url }}">Read note <span aria-hidden="true">↗</span></a></div>
                  </article>
                {% endif %}
              {% endfor %}
            </div>
          </section>
        {% endif %}
      {% else %}
        <div class="empty-state"><p>No research notes are indexed yet.</p></div>
      {% endif %}
    </section>
  </div>
</div>

<script src="{{ '/assets/js/collection-filter.js' | relative_url }}" defer></script>
