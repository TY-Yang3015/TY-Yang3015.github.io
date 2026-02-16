---
layout: default
title: Projects
permalink: /projects/
---

<div class="prose">
  <h1>Projects</h1>
  <p>Projects I worked on...</p>
</div>

<div class="grid">
  {% for p in site.data.projects %}
  <div class="card">
    <h3>{{ p.name }}</h3>
    <p>{{ p.description }}</p>
    <div class="badges">
      {% for t in p.tags %}
        <span class="badge">{{ t }}</span>
      {% endfor %}
    </div>
    <p style="margin-top:12px;"><a href="{{ p.link }}">Open ↗</a></p>
  </div>
  {% endfor %}
</div>
