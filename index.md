---
layout: default
title: Home
permalink: /
featured_publications: [P01, P02, P03]
---

<div class="hero">
  <img class="hero-photo" src="{{ site.author.photo | relative_url }}" alt="{{ site.author.name }}">
  <div class="hero-text">
    <h1>{{ site.author.name }}</h1>
    <p class="hero-role">{{ site.author.role }}, {{ site.author.affiliation }}</p>
    <p class="hero-place">{{ site.author.lab }} &middot; {{ site.author.location }}</p>
    <ul class="linkbar">
      <li><a class="primary" href="{{ site.author.cv | relative_url }}">CV (PDF)</a></li>
      {% for l in site.links %}
      <li><a href="{{ l.url }}" rel="noopener">{{ l.name }}</a></li>
      {% endfor %}
      <li><a href="mailto:{{ site.author.email }}">Email</a></li>
    </ul>
  </div>
</div>

Trained in physics at POSTECH, I worked at Samsung Research before joining
ETRI in 2021.

My research draws on statistical physics and machine learning to study temporal
and relational structure in data. It spans bursty event sequences, complex
networks, and multimodal cognitive assessment using images, language and speech.

Current projects focus on science-specific encoders and tokenizers,
with applications to drug discovery.

<ul class="keywords">
  <li>Scientific representation learning</li>
  <li>Multimodal cognitive assessment</li>
  <li>Temporal point processes</li>
  <li>Complex networks</li>
</ul>

[Read more about my research →]({{ '/research/' | relative_url }})

## Selected publications

{% assign featured_keys = page.featured_publications | join: "," %}
{% include research-papers.html keys=featured_keys %}

[View all publications →]({{ '/publications/' | relative_url }})

## Contact

<div class="rows">
  <div class="row">
    <div class="row-when">Email</div>
    <div class="row-what">
      <p><a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a></p>
      <p class="sub"><a href="mailto:{{ site.author.email_alt }}">{{ site.author.email_alt }}</a></p>
    </div>
  </div>
  <div class="row">
    <div class="row-when">Profiles</div>
    <div class="row-what">
      <p class="inline-list">{% for l in site.links %}<a href="{{ l.url }}" rel="noopener">{{ l.name }}</a>{% unless forloop.last %} &middot; {% endunless %}{% endfor %}</p>
    </div>
  </div>
</div>
