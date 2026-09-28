---
layout: page
title: Research
subtitle: Temporal and relational structure in complex data.
permalink: /research/
description: Research by Byounghwa Lee on multimodal cognitive assessment, temporal dynamics, complex networks, industrial machine learning, and scientific representations.
---

I use temporal and relational structure to model complex data. My work spans
statistical physics, industrial machine learning and multimodal cognitive
assessment. I currently apply this approach to scientific sequence modelling
and protein–ligand binding-affinity prediction.

## Research themes

<div class="theme">
  <h3>1. Multimodal learning for cognitive assessment</h3>
  <p>
    I study how picture-description speech reflects cognitive function by
    connecting what people say with the visual scene they describe. I developed
    graph models of image–sentence relationships and combined them with text
    and audio representations through co-attention. This work examines how
    visual, linguistic and acoustic cues contribute to Alzheimer's disease
    classification on the ADReSSo benchmark.
  </p>
  {% include research-papers.html keys="P01,P02" %}
</div>

<div class="theme">
  <h3>2. Bursty dynamics and temporal point processes</h3>
  <p>
    Events in complex systems often cluster in time. I developed a hierarchical
    model of bursty dynamics and contributed to a copula-based method for
    controlling inter-event time distributions and memory. Building on this
    work, I incorporated burstiness and memory statistics into a Transformer
    for event-time prediction, linking statistical descriptions of temporal
    heterogeneity with neural sequence models.
  </p>
  {% include research-papers.html keys="P03,P08,P07" %}
</div>

<div class="theme">
  <h3>3. Complex networks and urban structure</h3>
  <p>
    I analysed street networks in 22 Korean cities to examine how urban
    structure relates to demographic and economic characteristics. Using
    centrality measures, planning regularity and population–road-length
    scaling, I related differences in network topology to the characteristics
    of each city.
  </p>
  {% include research-papers.html keys="P09" %}
</div>

## Industrial machine learning

At Samsung Research, I developed demand and material-order forecasting models
and evaluated order predictions through inventory simulations, including
overstock and shortages. I led the development of a self-attention
model for multi-touch advertising attribution and designed a self-supervised
architecture for cross-domain recommendation. These applications involved
modelling demand over time, sequences of advertising interactions, and user
behaviour across domains.

## Collaboration and deployment

In clinical collaborations, I developed models and analysed treatment choices
with domain specialists. Other collaborations explored predictive coding for
recognition with limited or imbalanced data and classifiers that accommodate
new features.

I also developed a Korean speech-based model for mild cognitive impairment
and contributed to field deployment and technology transfer. For an interactive
assessment system, I worked on real-time speech processing and model–server
integration.

{% include research-papers.html keys="P05,P06,P04" %}

## Current work and direction

I am developing scientific sequence encoders and protein–ligand binding-affinity
models using pretrained representations and three-dimensional interaction
features. I examine measurement types and units, dataset splits, and molecular
similarity to distinguish modelling gains from evaluation effects.

My next direction is to turn these models into research tools with defined
inputs, reproducible evaluation and researcher review. I also continue to
explore temporal point processes and constrained graph generation.

## Background

Ph.D. in physics at POSTECH, advised by Woo-Sung Jung and Hang-Hyun Jo;
thesis *Generative Model and Method for Correlated Bursty Dynamics*.

See also: [Publications]({{ '/publications/' | relative_url }}) &middot;
[Projects and patents]({{ '/projects/' | relative_url }})
