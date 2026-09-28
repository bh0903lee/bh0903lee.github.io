---
layout: page
title: Research
subtitle: Multimodal learning, temporal dynamics, and complex networks.
permalink: /research/
description: Published research by Byounghwa Lee on multimodal cognitive assessment, bursty dynamics and temporal point processes, and urban networks.
---

I study how relationships in data inform models of complex systems and machine
learning. My published work connects images, language and speech for cognitive
assessment; models burstiness and memory in event sequences; and relates
network structure to the characteristics of cities.

## Research themes

<div class="theme">
  <h3>1. Multimodal learning for cognitive assessment</h3>
  <p>
    Picture-description speech contains information about both what a person
    says and how their description relates to the scene. My two 2025 papers in
    <em>Scientific Reports</em> use this relationship for Alzheimer's disease
    classification on the ADReSSo benchmark. I am the first and corresponding
    author of both papers.
  </p>
  <p>
    The January paper uses a vision-language model to connect picture regions and
    spoken sentences in a similarity-weighted bipartite graph. A graph neural
    network learns from these connections, and ablation studies examine the
    contribution of image–text relationships. The August paper extends this
    approach by combining the graph representation with text and audio
    encoders through co-attention. It analyses the contribution of each
    modality and how linguistic and acoustic cues complement one another.
  </p>
  {% include research-papers.html keys="P01,P02" %}
</div>

<div class="theme">
  <h3>2. Bursty dynamics and temporal point processes</h3>
  <p>
    Events in complex systems often cluster in time, with long inactive periods
    between bursts. My work studies both the distribution of inter-event times
    and the correlations between successive intervals, connecting statistical
    physics with event-sequence prediction.
  </p>
  <p>
    The hierarchical burst model (<em>Physical Review E</em>, 2018) provides a
    generative mechanism for inter-event times, autocorrelation and burst sizes.
    In collaborative work on a copula-based algorithm
    (<em>Physical Review E</em>, 2019), we generated sequences with a prescribed
    inter-event time distribution and memory coefficient. The Burst and
    Memory-aware Transformer (<em>Frontiers in Computational Neuroscience</em>,
    2023) brings burstiness and memory statistics into a neural temporal point
    process, improving event-time prediction for temporally heterogeneous data.
    I am the first author of the hierarchical burst model and the first and
    corresponding author of the Transformer paper.
  </p>
  {% include research-papers.html keys="P03,P08,P07" %}
</div>

<div class="theme">
  <h3>3. Complex networks and urban structure</h3>
  <p>
    My first-author paper in <em>Physica A</em> (2018) analyses street networks
    in 22 Korean cities. It examines centrality, planning regularity and
    population–road-length scaling, relating network structure to demographic
    and economic information. This work provides the network-science foundation
    for my broader interest in relational data and graph-based models.
  </p>
  {% include research-papers.html keys="P09" %}
</div>

## Collaborative publications

I have also co-authored work on explainable models of prostate-cancer treatment
decisions, predictive-coding learning for incremental, long-tailed and few-shot
recognition, and latent-variable classifiers that accommodate newly arriving
features in dynamic environments.

{% include research-papers.html keys="P05,P06,P04" %}

## Ongoing work

I am extending these interests to scientific sequence encoders and
protein–ligand representation learning through ETRI's AI for Science program.
Other ongoing work explores constrained graph generation and temporal
point-process modelling. These directions are work in progress.

## Background

Ph.D. at POSTECH in statistical physics and complex systems, under Woo-Sung Jung
and Hang-Hyun Jo; thesis *Generative Model and Method for Correlated Bursty
Dynamics*. Before joining ETRI, two and a half years at Samsung Research on
industrial machine learning: demand and inventory optimisation, advertising
attribution, and cross-domain recommendation.

See also: [Publications]({{ '/publications/' | relative_url }}) &middot;
[Projects and patents]({{ '/projects/' | relative_url }})
