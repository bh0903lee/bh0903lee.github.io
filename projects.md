---
layout: page
title: Projects
subtitle: Applied research and technical contributions.
permalink: /projects/
description: Applied research and development projects of Byounghwa Lee at ETRI and Samsung Research, with their publications, patents and technology transfer.
---

Selected research and development projects at ETRI and Samsung Research, each
with the publications, patents and other outputs it produced. The Korean
speech-based model for mild cognitive impairment screening, which I developed
and which was transferred to two companies in 2026, is described under
[Technology transfer](#technology-transfer). Graduate research is described
under [Research]({{ '/research/' | relative_url }}) and
[Publications]({{ '/publications/' | relative_url }}).

## Research and applications

{% for pr in site.data.projects %}
<div class="card">
  <h3>{{ pr.name }}</h3>
  <p class="card-meta">{{ pr.org }} &middot; {{ pr.period }}{% if pr.my_period != pr.period %} &middot; my involvement: {{ pr.my_period }}{% endif %}</p>
  <p class="card-role"><strong>Role:</strong> {{ pr.role }}</p>
  <p>{{ pr.description }}</p>
  {%- if pr.outputs %}
  <div class="card-outputs">
    <strong>Outputs</strong>
    <ul>
    {%- for o in pr.outputs %}
      <li>{% if o.url %}<a href="{{ o.url | relative_url }}">{{ o.text }}</a>{% else %}{{ o.text }}{% endif %}</li>
    {%- endfor %}
    </ul>
  </div>
  {%- endif %}
</div>
{% endfor %}

## Technology transfer

<div class="card">
  <h3>Korean speech-based classification model for mild cognitive impairment</h3>
  <p class="card-meta">ETRI &middot; 2024 – 2026</p>
  <p class="card-role"><strong>Role:</strong> Primary developer of the classification model; lead contributor to field deployment; contributor to the technology transfer</p>
  <p>
    I was the primary developer of the Korean speech-based classification model
    for mild cognitive impairment (MCI) screening, and led its integration into
    an interactive assessment system for field deployment. In 2026 the model was
    transferred to two companies under two technology-transfer agreements, to
    which I contributed as the model's developer. This was a field
    deployment; I do not describe it here as a commercial service or as a
    clinical validation of the model. I took part as a member of the project
    team, and this page describes my own part of the work rather than the
    project as a whole.
  </p>
  <div class="card-outputs">
    <strong>Related</strong>
    <ul>
      <li><a href="{{ '/publications/#p01' | relative_url }}">Research papers on multimodal cognitive assessment (Scientific Reports, 2025)</a></li>
      <li><a href="{{ '/publications/#demonstrations-and-other-contributions' | relative_url }}">IEEE ICASSP 2025 Show &amp; Tell demonstration of the screening system</a></li>
      <li><a href="{{ '/cv/#technology-transfer' | relative_url }}">Technology transfer entry on the CV</a></li>
    </ul>
  </div>
</div>

Patents are listed on the [CV]({{ '/cv/#patents' | relative_url }}).
