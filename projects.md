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
<article class="patent-card">
  <h4 class="patent-heading">{{ pt.topic | escape }}</h4>
  <p class="patent-assignee">{{ pt.assignee }}</p>
  {% include patent-record.html country="South Korea" title=pt.title application=pt.filed status=pt.status_text links=pt.links %}
  {%- if pt.us %}
  {% include patent-record.html country="United States" title=pt.us.title application=pt.us.application publication=pt.us.publication url=pt.us.url status=pt.us.status %}
  {%- endif %}
  {%- if pt.family %}
  <div class="patent-record">
    <p class="patent-country">International</p>
    <div class="patent-details">
      <dl class="patent-facts">
        <div><dt>PCT</dt><dd>{% for f in pt.family %}{{ f | escape }}{% unless forloop.last %}<br>{% endunless %}{% endfor %}</dd></div>
      </dl>
    </div>
  </div>
  {%- endif %}
</article>
{% endfor %}

<h3 class="patent-group-title">Additional U.S. applications as co-inventor</h3>

{% for pt in site.data.us_co_inventions %}
<article class="patent-card">
  <h4 class="patent-heading">{{ pt.topic | escape }}</h4>
  {% include patent-record.html country="United States" title=pt.title application=pt.application publication=pt.publication url=pt.url status=pt.status %}
</article>
{% endfor %}
