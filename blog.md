---
layout: default
title: Blog
permalink: /blog/
---

<div class="blog-shell">
  <section class="blog-hero">
    <div class="kicker">Notes ♪</div>
    <h1 class="glitch" data-text="Blog">Blog</h1>
    <p class="blog-lead">
      Research notes, technical thoughts, and small explorations across AI, physics, and chemistry ✦
    </p>
  </section>

  <section class="blog-index">
    {% if site.posts.size > 0 %}
      <div class="post-list">
        {% for post in site.posts %}
          <article class="post-card">
            <div class="post-meta">
              <span class="post-tag">Post</span>
              <time class="post-date">{{ post.date | date: "%-d %b %Y" }}</time>
            </div>

            <h2>
              <a>{{ post.title }}</a>
            </h2>

            {% if post.excerpt %}
              <p class="post-excerpt">
                {{ post.excerpt | strip_html | truncate: 180 }}
              </p>
            {% endif %}

            <a class="post-link" href="{{ post.url | relative_url }}">
              Read entry ✦
            </a>
          </article>
        {% endfor %}
      </div>
    {% else %}
      <div class="empty-blog">
        <p>No posts yet — the archive is still sleeping ♪</p>
      </div>
    {% endif %}
  </section>
</div>
