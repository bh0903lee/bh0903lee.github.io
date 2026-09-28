---
layout: page
title: Projects
subtitle: Applied research and technical contributions.
permalink: /projects/
description: Applied research and development projects of Byounghwa Lee at ETRI and Samsung Research.
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
  <p class="card-meta">ETRI &middot; 2026</p>
  <p class="card-role"><strong>Role:</strong> Lead developer</p>
  <p>
    As lead developer, I built the Korean speech-based classification model and contributed
    to its field deployment and its transfer to two companies under two technology-transfer agreements.
  </p>
</div>

Patents are listed on the [CV]({{ '/cv/' | relative_url }}).
