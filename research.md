---
layout: page
title: Research
subtitle: Complex systems and machine learning.
permalink: /research/
description: Research interests of Byounghwa Lee - temporal point processes, graph learning and constrained generation, AI for Science, and multimodal speech-language modelling.
---

My work connects complex systems with machine learning along two lines: how
events are distributed in time, and how relational structure constrains what can
be learned or generated. A recurring question is when structural information
improves a model and under what conditions it does not.

## Research themes

<div class="theme">
  <h3>1. Temporal point processes and bursty dynamics</h3>
  <p>
    Event sequences in many systems show heavy-tailed inter-event times
    (burstiness) and correlations between consecutive intervals (memory). My
    doctoral work built generative models for both, including a hierarchical
    burst model that reproduces the inter-event time distribution, the
    autocorrelation and the burst size distribution from a single mechanism.
  </p>
  <p>
    Later work embeds these statistics in neural temporal point processes and
    examines whether the resulting gains come from the marginal distribution or
    from correlations between intervals.
  </p>
</div>

<div class="theme">
  <h3>2. Graph learning and constrained generation</h3>
  <p>
    Earlier work analysed the street networks of 22 Korean cities, relating
    centrality structure, planning regularity and population–road-length scaling
    to demographic and economic data.
  </p>
  <p>
    Current work concerns generating graphs that satisfy several structural
    constraints simultaneously, and whether a learned policy can replace
    explicit search when evaluating each candidate move is expensive. Across a
    range of learning methods under a unified protocol, learned policies did not
    match search in this setting.
  </p>
</div>

<div class="theme">
  <h3>3. AI for Science</h3>
  <p>
    Since January 2026 I have worked on sequence encoders and tokenizers for
    scientific data within ETRI's strategic research program on AI for Science.
    Protein–ligand representation and binding models serve as the empirical case
    for that work, together with the data splitting and evaluation pipeline used
    to assess it.
  </p>
</div>

<div class="theme">
  <h3>4. Multimodal speech-language modelling for cognitive assessment</h3>
  <p>
    Recognition of cognitive decline from picture-description speech. The
    approach represents picture regions and spoken sentences in a shared
    vision-language space and learns over the resulting similarity-weighted
    bipartite graph, using the relation between image and description rather
    than text or audio alone.
  </p>
  <p>
    I also developed the Korean speech-based screening model for mild cognitive
    impairment, ran it in field deployment, and was lead developer for its
    technology transfer.
  </p>
</div>

## Background

Ph.D. at POSTECH in statistical physics and complex systems, under Woo-Sung Jung
and Hang-Hyun Jo; thesis *Generative Model and Method for Correlated Bursty
Dynamics*. Before joining ETRI, two and a half years at Samsung Research on
industrial machine learning: demand and inventory optimisation, advertising
attribution, and cross-domain recommendation.

See also: [Publications]({{ '/publications/' | relative_url }}) &middot;
[Projects and patents]({{ '/projects/' | relative_url }})
