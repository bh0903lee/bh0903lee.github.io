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

I work on machine learning for scientific, clinical and industrial data,
drawing on statistical physics and complex systems. My research asks how the
structure of a system, the timing of its events, the relations among its parts
and the modalities in which it is observed, can be turned into models that
predict, generate and explain. My current work develops science-specialized
encoders and tokenizers, with applications to drug discovery.

<ul class="keywords">
  <li>AI for science and complex systems</li>
  <li>Graph learning and constrained generation</li>
  <li>Event-sequence learning</li>
  <li>Multimodal cognitive assessment</li>
</ul>

[Read more about my research →]({{ '/research/' | relative_url }})

## Research highlights

<ul class="highlights">
  <li>
    <p class="hl-title">Multimodal cognitive assessment from images, language and speech</p>
    <p>Two first- and corresponding-author papers in <em>Scientific Reports</em> (2025) on Alzheimer's disease recognition from picture-description speech, combining graph models of image–sentence relations with text and audio. The method is covered by a granted Korean patent. The same line of work led to a Korean speech-based MCI screening model, which I developed as primary developer and which was deployed in the field and transferred to two companies in 2026.</p>
    <p class="hl-links"><a href="{{ '/research/#cognitive-assessment' | relative_url }}">Research</a> &middot; <a href="{{ '/publications/#p01' | relative_url }}">Publications</a> &middot; <a href="{{ '/cv/#patent-t04' | relative_url }}">Patent</a> &middot; <a href="{{ '/projects/#technology-transfer' | relative_url }}">Technology transfer</a></p>
  </li>
  <li>
    <p class="hl-title">From bursty dynamics to neural event-sequence models</p>
    <p>Physics-based generative models of bursty dynamics (<em>Physical Review E</em>, 2018 and 2019) led to the Burst and Memory-aware Transformer (2023), which tests when explicit temporal structure improves event-time prediction.</p>
    <p class="hl-links"><a href="{{ '/research/#bursty-dynamics' | relative_url }}">Research</a> &middot; <a href="{{ '/publications/#p03' | relative_url }}">Publications</a></p>
  </li>
  <li>
    <p class="hl-title">From street networks to graph generation under constraints</p>
    <p>Complex-network analysis of the street networks of 22 Korean cities (<em>Physica A</em>, 2018) led to a granted Korean patent on generating networks under complex-network constraints, and to ongoing work on generating and editing graphs under several structural constraints at once.</p>
    <p class="hl-links"><a href="{{ '/research/#complex-networks' | relative_url }}">Research</a> &middot; <a href="{{ '/publications/#p09' | relative_url }}">Publications</a> &middot; <a href="{{ '/cv/#patent-t01' | relative_url }}">Patent</a></p>
  </li>
</ul>

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
