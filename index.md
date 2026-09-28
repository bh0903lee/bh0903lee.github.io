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
      <li><a href="{{ l.url }}" target="_blank" rel="noopener">{{ l.name }}</a></li>
      {% endfor %}
      <li><a href="mailto:{{ site.author.email }}">Email</a></li>
    </ul>
  </div>
</div>

I am a Senior Researcher at the Electronics and Telecommunications Research
Institute (ETRI). I received my B.S. (2012) and Ph.D. (2019) in physics from
Pohang University of Science and Technology (POSTECH), where my doctoral work
addressed the statistical physics of complex systems. Before joining ETRI in
2021, I was a Staff Engineer at Samsung Research, Samsung Electronics.

My research combines statistical physics and machine learning to study the
temporal and relational structure of data, spanning bursty event sequences,
complex networks, and multimodal cognitive assessment across images, language,
and speech. A recurring question runs through this work: when does structural
information improve a model, and when do explicit computation and search remain
necessary for reliable prediction and generation?

My current work develops science-specialized encoders and tokenizers, with
applications to drug discovery.

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
      <p class="inline-list">{% for l in site.links %}<a href="{{ l.url }}" target="_blank" rel="noopener">{{ l.name }}</a>{% unless forloop.last %} &middot; {% endunless %}{% endfor %}</p>
    </div>
  </div>
</div>
