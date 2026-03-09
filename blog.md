---
layout: default
title: Blog
permalink: /blog/
---

{% assign grouped_posts = site.posts | group_by: "series" %}
{% assign standalone_count = 0 %}
{% for post in site.posts %}
  {% if post.series == nil or post.series == "" %}
    {% assign standalone_count = standalone_count | plus: 1 %}
  {% endif %}
{% endfor %}

<div class="blog-shell">
  <section class="blog-hero">
    <div class="kicker">Notes</div>
    <h1 class="glitch" data-text="Blog">Blog</h1>
    <p class="blog-lead">
      Research notes, technical thoughts, and small explorations across AI, physics, and chemistry ♪
    </p>
  </section>

  <div class="blog-layout">
    <aside class="blog-sidebar">
      <div class="collection-panel mystic-archive">
        <div class="collection-head">
          <span class="collection-sigil main-sigil">✦</span>
          <div class="collection-head-copy">
            <h2>Collections</h2>
            <p class="collection-whisper">sealed archive</p>
          </div>
        </div>

        <ul class="collection-list">
          <li>
            <a class="collection-filter"
               href="#all-posts"
               data-filter="all-posts">
              <span class="collection-link-main">
                <span class="collection-item-sigil">◎</span>
                <span>All Posts</span>
              </span>
              <span class="collection-count">{{ site.posts | size }}</span>
            </a>
          </li>

          {% for group in grouped_posts %}
            {% if group.name and group.name != "" %}
              {% assign first_post = group.items | first %}
              <li>
                <a class="collection-filter"
                   href="#series-{{ group.name | slugify }}"
                   data-filter="series-{{ group.name | slugify }}">
                  <span class="collection-link-main">
                    <span class="collection-item-sigil">{{ first_post.series_icon | default: "✦" }}</span>
                    <span>{{ group.name }}</span>
                  </span>
                  <span class="collection-count">{{ group.items | size }}</span>
                </a>
              </li>
            {% endif %}
          {% endfor %}

          {% if standalone_count > 0 %}
            <li>
              <a class="collection-filter"
                 href="#series-standalone"
                 data-filter="series-standalone">
                <span class="collection-link-main">
                  <span class="collection-item-sigil">◇</span>
                  <span>Standalone</span>
                </span>
                <span class="collection-count">{{ standalone_count }}</span>
              </a>
            </li>
          {% endif %}
        </ul>

        <p class="collection-note">Sort Blogs by Collections ♪</p>
      </div>
    </aside>

    <section class="blog-index" id="all-posts">
      {% if site.posts.size > 0 %}

        {% for group in grouped_posts %}
          {% if group.name and group.name != "" %}
            {% assign first_post = group.items | first %}
            <div class="series-block"
                 id="series-{{ group.name | slugify }}"
                 data-group="series-{{ group.name | slugify }}">
              <div class="series-heading">
                <div class="series-heading-main">
                  <span class="series-sigil">{{ first_post.series_icon | default: "✦" }}</span>
                  <h2>{{ group.name }}</h2>
                </div>
                <span class="series-count">{{ group.items | size }} entries</span>
              </div>

              <div class="post-list">
                {% for post in group.items %}
                  <article class="post-card">
                    <div class="post-meta">
                      <span class="post-tag">Post</span>
                      <time class="post-date">{{ post.date | date: "%-d %b %Y" }}</time>
                    </div>

                    <h3>
                      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
                    </h3>

                    {% if post.excerpt %}
                      <p class="post-excerpt">
                        {{ post.excerpt | strip_html | truncate: 180 }}
                      </p>
                    {% endif %}

                    <div class="post-links">
                      <a class="post-link" href="{{ post.url | relative_url }}">
                        Read entry ✦
                      </a>

                      {% if post.zh_url %}
                        {% if post.zh_url contains '://' %}
                          <a class="post-link" href="{{ post.zh_url }}">中文阅读 ♪</a>
                        {% else %}
                          <a class="post-link" href="{{ post.zh_url | relative_url }}">中文阅读 ♪</a>
                        {% endif %}
                      {% endif %}
                    </div>
                  </article>
                {% endfor %}
              </div>
            </div>
          {% endif %}
        {% endfor %}

        {% if standalone_count > 0 %}
          <div class="series-block"
               id="series-standalone"
               data-group="series-standalone">
            <div class="series-heading">
              <div class="series-heading-main">
                <span class="series-sigil">◇</span>
                <h2>Standalone</h2>
              </div>
              <span class="series-count">{{ standalone_count }} entries</span>
            </div>

            <div class="post-list">
              {% for post in site.posts %}
                {% if post.series == nil or post.series == "" %}
                  <article class="post-card">
                    <div class="post-meta">
                      <span class="post-tag">Post</span>
                      <time class="post-date">{{ post.date | date: "%-d %b %Y" }}</time>
                    </div>

                    <h3>
                      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
                    </h3>

                    {% if post.excerpt %}
                      <p class="post-excerpt">
                        {{ post.excerpt | strip_html | truncate: 180 }}
                      </p>
                    {% endif %}

                    <div class="post-links">
                      <a class="post-link" href="{{ post.url | relative_url }}">
                        Read entry ✦
                      </a>

                      {% if post.zh_url %}
                        {% if post.zh_url contains '://' %}
                          <a class="post-link zh-link" href="{{ post.zh_url }}">中文阅读 ♪</a>
                        {% else %}
                          <a class="post-link zh-link" href="{{ post.zh_url | relative_url }}">中文阅读 ♪</a>
                        {% endif %}
                      {% endif %}
                    </div>
                  </article>
                {% endif %}
              {% endfor %}
            </div>
          </div>
        {% endif %}

      {% else %}
        <div class="empty-blog">
          <p>No posts yet — the archive is still sleeping ♪</p>
        </div>
      {% endif %}
    </section>
  </div>
</div>

<script src="{{ '/assets/js/blog-filter.js' | relative_url }}"></script>
