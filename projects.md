---
layout: page
title: Projects
subtitle: Applied research, technical contributions, and patents.
permalink: /projects/
description: Applied research and patents of Byounghwa Lee at ETRI and Samsung Research.
---

Selected research activities and my technical contributions, from model design
and evaluation to integration and deployment.

## Research and applications

{% for pr in site.data.projects %}
<div class="card">
  <h3>{{ pr.name }}</h3>
  <p class="card-meta">{{ pr.org }} &middot; {{ pr.period }}{% if pr.my_period != pr.period %} &middot; my involvement: {{ pr.my_period }}{% endif %}</p>
  <p class="card-role"><strong>Role:</strong> {{ pr.role }}</p>
  <p>{{ pr.description }}</p>
</div>
{% endfor %}

## Technology transfer

<div class="card">
  <h3>Korean speech-based screening model for mild cognitive impairment</h3>
  <p class="card-meta">ETRI &middot; 2025</p>
  <p class="card-role"><strong>Role:</strong> Lead developer</p>
  <p>
    I developed the Korean speech-based classification model and contributed
    to its field deployment and technology transfer.
  </p>
</div>

## Patents

Invention families in which I am the first inventor, as of September 2026.

{% for pt in site.data.patents %}
<div class="card">
  <h3>{{ pt.title }}</h3>
  <p class="card-meta">
    {{ pt.assignee }} &middot; Filed {{ pt.filed }}
    <span class="status status-{{ pt.status }}">{{ pt.status_text }}</span>
  </p>
  {%- if pt.note %}<p>{{ pt.note }}</p>{% endif %}
  {%- if pt.us %}
  <div class="patent-us">
    <p class="patent-jurisdiction">U.S. application</p>
    <p class="pub-title"><a href="{{ pt.us.url }}" rel="noopener">{{ pt.us.title | escape }}</a></p>
    <p class="card-meta">{{ pt.us.application }} &middot; {{ pt.us.publication }}</p>
    <p class="card-role">{{ pt.us.status }}</p>
  </div>
  {%- endif %}
  {%- if pt.family %}
  <p class="card-role">Family: {% for f in pt.family %}{{ f }}{% unless forloop.last %}; {% endunless %}{% endfor %}</p>
  {%- endif %}
  {%- if pt.links %}
  <p class="card-links">{% for l in pt.links %}<a href="{{ l.url }}" rel="noopener">{{ l.name }}</a>{% unless forloop.last %} &middot; {% endunless %}{% endfor %}</p>
  {%- endif %}
</div>
{% endfor %}

<p>Additional U.S. applications as co-inventor:</p>
<ul class="research-papers">
{% for pt in site.data.us_co_inventions %}
  <li>
    <strong><a href="{{ pt.url }}" rel="noopener">{{ pt.title | escape }}</a></strong>
    <span class="research-paper-meta">{{ pt.application }} &middot; {{ pt.publication }} &middot; {{ pt.role }} &middot; {{ pt.status }}</span>
  </li>
{% endfor %}
</ul>
