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
POSTECH in 2012 and 2019, where I studied correlated bursty dynamics and complex
networks, and I was a Staff Engineer at Samsung Research before joining ETRI in
2021.

My research connects complex systems with machine learning, with a focus on
multimodal learning for cognitive assessment and the modelling of bursty event
sequences. In two 2025 papers in *Scientific Reports*, I developed graph-based
and multimodal approaches to Alzheimer's disease recognition from
picture-description speech, linking visual context with language and audio.
My work on temporal dynamics spans generative models in *Physical Review E*
and the Burst and Memory-aware Transformer for event-time prediction in
*Frontiers in Computational Neuroscience*. Earlier work in *Physica A*
examined the structure of urban street networks.

<ul class="keywords">
  <li>Multimodal learning</li>
  <li>Speech-language cognitive assessment</li>
  <li>Graph learning</li>
  <li>Temporal point processes</li>
  <li>Burstiness and memory</li>
  <li>Complex networks</li>
</ul>

[Read more about my research →]({{ '/research/' | relative_url }})

## Selected publications

Recent journal papers as first and corresponding author.

<ol class="pub-list">
{% for key in page.featured_publications %}
{% assign paper = site.data.publications | where: "key", key | first %}
{% include publication.html pub=paper %}
{% endfor %}
</ol>

[View all publications →]({{ '/publications/' | relative_url }})

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
