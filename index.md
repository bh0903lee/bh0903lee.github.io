---
layout: default
title: Home
permalink: /
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
POSTECH in 2012 and 2019, where I studied correlated bursty dynamics and complex
networks, and I was a Staff Engineer at Samsung Research before joining ETRI in
2021.

My research connects complex systems with machine learning along two lines:
temporal point processes, from the study of burstiness and memory in event
sequences, and graph learning, from network structure and constraints. A
recurring question in this work is when structural information improves a
learned model and when explicit computation or search remains necessary. I
currently apply this to AI for Science, working on sequence encoders for
scientific data and on protein–ligand representation learning.

<ul class="keywords">
  <li>Temporal point processes</li>
  <li>Burstiness and memory</li>
  <li>Graph learning</li>
  <li>Constrained graph generation</li>
  <li>Scientific representation learning</li>
  <li>AI for Science</li>
  <li>Multimodal speech-language modelling</li>
</ul>

[Read more about my research →]({{ '/research/' | relative_url }})

## News

<ul class="news">
  <li>
    <time datetime="2025-08">Aug 2025</time>
    <p><em>Multimodal Alzheimer's disease recognition from image, text and
    audio</em> published in <em>Scientific Reports</em>.</p>
  </li>
  <li>
    <time datetime="2025">2025</time>
    <p>Selected as an IEEE Access Exceptional Reviewer.</p>
  </li>
  <li>
    <time datetime="2025-01">Jan 2025</time>
    <p><em>Alzheimer's disease recognition using graph neural network by
    leveraging image-text similarity from vision language model</em> published
    in <em>Scientific Reports</em>.</p>
  </li>
  <li>
    <time datetime="2023-12">Dec 2023</time>
    <p><em>Burst and Memory-aware Transformer: capturing temporal
    heterogeneity</em> published in <em>Frontiers in Computational
    Neuroscience</em>.</p>
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
