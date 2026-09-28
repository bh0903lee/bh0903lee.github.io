---
layout: page
title: Projects
subtitle: Applied research, technical contributions, and patents.
permalink: /projects/
description: Applied research and patents of Byounghwa Lee at ETRI and Samsung Research.
---

Selected research and development projects at ETRI and Samsung Research.
Graduate research is described under
[Research]({{ '/research/' | relative_url }}) and
[Publications]({{ '/publications/' | relative_url }}).

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
  <h3>Korean speech-based classification model for mild cognitive impairment</h3>
  <p class="card-meta">ETRI &middot; 2025</p>
  <p class="card-role"><strong>Role:</strong> Lead developer</p>
  <p>
    I developed the Korean speech-based classification model and contributed
    to its field deployment and technology transfer.
  </p>
</div>

## Patents

Status as of September 2026.

<h3 class="patent-group-title">First-inventor patent families</h3>

{% for pt in site.data.patents %}
<article class="patent-card" aria-labelledby="patent-{{ pt.key | downcase }}">
  <header class="patent-header">
    <h4 id="patent-{{ pt.key | downcase }}">{{ pt.topic | escape }}</h4>
    <span class="patent-assignee">{{ pt.assignee | escape }}</span>
  </header>
  <div class="patent-records">
  {% include patent-record.html country="KR" title=pt.title application=pt.filed status=pt.status_text links=pt.links %}
  {%- if pt.us %}
  {% include patent-record.html country="US" title=pt.us.title application=pt.us.application publication=pt.us.publication url=pt.us.url status=pt.us.status %}
  {%- endif %}
  {%- if pt.family %}
  <p class="patent-meta patent-family">{% for f in pt.family %}{{ f | escape }}{% unless forloop.last %} &middot; {% endunless %}{% endfor %}</p>
  {%- endif %}
  </div>
</article>
{% endfor %}

<h3 class="patent-group-title">Additional U.S. applications as co-inventor</h3>

{% for pt in site.data.us_co_inventions %}
<article class="patent-card" aria-labelledby="co-patent-{{ forloop.index }}">
  <header class="patent-header">
    <h4 id="co-patent-{{ forloop.index }}">{{ pt.topic | escape }}</h4>
  </header>
  <div class="patent-records">
  {% include patent-record.html country="US" title=pt.title application=pt.application publication=pt.publication url=pt.url status=pt.status %}
  </div>
</article>
{% endfor %}
