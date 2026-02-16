---
layout: default
title: Blog
permalink: /blog/
---

<div class="prose">
  <h1>Blog</h1>
  <ul>
    {% for post in site.posts %}
      <li>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        <span class="muted"> — {{ post.date | date: "%-d %b %Y" }}</span>
      </li>
    {% endfor %}
  </ul>
</div>
