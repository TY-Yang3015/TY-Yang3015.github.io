---
layout: default
title: Projects
permalink: /projects/
---

<section class="page-hero prose">
  <p class="kicker">Projects</p>
  <h1>Projects</h1>
  <p>Research code, experiments, and side projects.</p>
</section>

{% if site.data.projects and site.data.projects.size > 0 %}
  <section class="grid project-grid" aria-label="Projects">
    {% for p in site.data.projects %}
      <article class="card project-data-card">
        <h2>{{ p.name }}</h2>
        {% if p.description %}<p>{{ p.description }}</p>{% endif %}

        {% if p.tags %}
          <div class="badges" aria-label="Tags">
            {% for t in p.tags %}<span class="badge">{{ t }}</span>{% endfor %}
          </div>
        {% endif %}

        {% if p.link %}
          {% if p.link contains '://' %}
            <p class="card-action"><a href="{{ p.link }}" rel="noopener">Open ↗</a></p>
          {% else %}
            <p class="card-action"><a href="{{ p.link | relative_url }}">Open ↗</a></p>
          {% endif %}
        {% endif %}
      </article>
    {% endfor %}
  </section>
{% else %}
  <section class="empty-blog">
    <p>No projects found in <code>_data/projects.yml</code> yet.</p>
  </section>
{% endif %}
