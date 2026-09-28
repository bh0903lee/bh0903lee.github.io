---
layout: page
title: Research
subtitle: Temporal and relational structure in complex data.
permalink: /research/
description: Research by Byounghwa Lee on scientific representation learning, multimodal cognitive assessment, temporal dynamics, complex networks, and industrial machine learning.
---

My research examines how temporal patterns and relationships in data can inform
predictive models. It connects statistical physics with machine learning across
scientific, clinical and industrial applications.

## Current work

<div class="theme">
  <h3>Scientific representation learning for drug discovery</h3>
  <p>
    I develop science-specific encoders and tokenizers, using protein–ligand
    binding-affinity prediction to study how sequence and three-dimensional
    information can be combined. I evaluate these representations under
    similarity-controlled data splits to assess generalization beyond closely
    related proteins and molecules.
  </p>
</div>

<div class="theme">
  <h3>Temporal point processes and burst structure</h3>
  <p>
    I develop temporal point processes that predict event-time distributions
    and test when explicit burst-history features improve prediction.
    Controlled experiments separate burstiness from dependence between
    successive event intervals to identify the source of predictive gains,
    while validation guides whether to use the added features on real data.
  </p>
</div>

<div class="theme">
  <h3>Graph generation under structural constraints</h3>
  <p>
    I study graph generation that satisfies multiple structural constraints
    simultaneously while preserving each node's degree. By comparing learned
    rewiring policies with search that explicitly evaluates candidate edits,
    I investigate when local information can predict an edit's global effects
    and when direct evaluation remains necessary.
  </p>
</div>

## Selected research contributions

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

At Samsung Research, I worked on forecasting, advertising attribution and
cross-domain recommendation. These problems involved learning from demand
patterns, sequences of advertising interactions and user behaviour across
domains. In inventory research, I evaluated forecasts through their effects on
simulated ordering and stock levels, connecting model evaluation with the
decisions the predictions support.

## Collaboration and deployment

In clinical collaborations, I developed models with domain specialists to
analyse observed treatment choices. Other collaborations explored predictive coding for
recognition with limited or imbalanced data and classifiers that accommodate
new features.

{% include research-papers.html keys="P05,P06,P04" %}

My applied work also includes a Korean speech-based model for mild cognitive
impairment, with contributions to field deployment and technology transfer.
Details of my development roles are listed under
[Projects]({{ '/projects/' | relative_url }}).

See also: [Publications]({{ '/publications/' | relative_url }}) &middot;
[CV]({{ '/cv/' | relative_url }})
