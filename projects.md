---
layout: default
title: Projects
permalink: /projects/
description: "Research code and scientific machine-learning projects by Tianyue Yang."
---

<div class="projects-shell">
  {% include components/page-intro.html title="Projects" description="Research code, model implementations, and experiments across scientific machine learning." %}

  {% if site.data.projects and site.data.projects.size > 0 %}
    <section class="project-list project-list--archive" aria-label="Projects">
      {% for project in site.data.projects %}
        {% include components/project-card.html project=project %}
      {% endfor %}
    </section>
  {% else %}
    <section class="empty-state"><p>No projects are indexed yet.</p></section>
  {% endif %}
</div>
