---
layout: page
title: Projects
subtitle: Research programs I have worked on, and the invention families that came out of them.
permalink: /projects/
description: Research programs and patents of Byounghwa Lee at ETRI and Samsung Research.
---

Each entry describes my own role and technical contribution. Programs are run by
teams and institutions; budgets, internal project numbers and institutional
figures are deliberately left out.

## Research programs

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
    The classification model I developed for Korean spontaneous speech was
    transferred out of ETRI following field deployment.
  </p>
</div>

## Patents

Invention families in which I am the first inventor. Status is as confirmed in
September 2026 against filing and registration documents; public patent
databases lag official registers, so the numbers below are the verified ones.

{% for pt in site.data.patents %}
<div class="card">
  <h3>{{ pt.title }}</h3>
  <p class="card-meta">
    {{ pt.assignee }} &middot; Filed {{ pt.filed }}
    <span class="status status-{{ pt.status }}">{{ pt.status_text }}</span>
  </p>
  {%- if pt.note %}<p>{{ pt.note }}</p>{% endif %}
  {%- if pt.family %}
  <p class="card-role">Family: {% for f in pt.family %}{{ f }}{% unless forloop.last %}; {% endunless %}{% endfor %}</p>
  {%- endif %}
  {%- if pt.links %}
  <p class="card-links">{% for l in pt.links %}<a href="{{ l.url }}" rel="noopener">{{ l.name }}</a>{% unless forloop.last %} &middot; {% endunless %}{% endfor %}</p>
  {%- endif %}
</div>
{% endfor %}

<p class="foot-meta">
  I am also a co-inventor on further filings where I am not the first inventor;
  those are not counted in the families above.
</p>
