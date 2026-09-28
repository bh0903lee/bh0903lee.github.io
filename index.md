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

I am a Senior Researcher at the Electronics and Telecommunications Research
Institute (ETRI) in Daejeon, Korea. I received my B.S. and Ph.D. in physics from
POSTECH and worked as a Staff Engineer at Samsung Research before joining ETRI
in 2021.

I study temporal and relational structure in data, drawing on statistical
physics and machine learning. My work spans bursty event sequences, complex
networks, and multimodal cognitive assessment using images, language and speech.

At Samsung Research, I applied machine learning to demand forecasting,
inventory optimisation, advertising attribution and cross-domain recommendation.
My current work focuses on science-specific encoders and tokenizers,
with applications to drug discovery. I aim to develop scientific prediction tools that
combine clear data requirements, reproducible evaluation and researcher review.

<ul class="keywords">
  <li>Multimodal learning</li>
  <li>Speech-language cognitive assessment</li>
  <li>Graph learning</li>
  <li>Temporal point processes</li>
  <li>Burstiness and memory</li>
  <li>Complex networks</li>
  <li>Scientific representation learning</li>
</ul>

[Read more about my research →]({{ '/research/' | relative_url }})

## Selected publications

{% assign featured_keys = page.featured_publications | join: "," %}
{% include research-papers.html keys=featured_keys %}

[View all publications →]({{ '/publications/' | relative_url }})

## News

<ul class="news">
  <li>
    <time datetime="2025">2025</time>
    <p>Selected as an IEEE Access Exceptional Reviewer.</p>
  </li>
</ul>

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
    <div class="row-when">Address</div>
    <div class="row-what">
      <p>{{ site.author.affiliation }}</p>
      <p class="sub">{{ site.author.location }}</p>
    </div>
  </div>
  <div class="row">
    <div class="row-when">Profiles</div>
    <div class="row-what">
      <p class="inline-list">{% for l in site.links %}<a href="{{ l.url }}" rel="noopener">{{ l.name }}</a>{% unless forloop.last %} &middot; {% endunless %}{% endfor %}</p>
    </div>
  </div>
</div>
