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
    information can be combined. Evaluation under
    similarity-controlled data splits assesses generalization beyond closely
    related proteins and molecules.
  </p>
</div>

<div class="theme">
  <h3>Temporal point processes and burst structure</h3>
  <p>
    This line of work uses temporal point processes to predict event-time
    distributions and tests when explicit burst-history features improve prediction.
    Controlled experiments separate burstiness from dependence between
    successive event intervals to identify the source of predictive gains,
    while validation guides whether to use the added features on real data.
  </p>
</div>

<div class="theme">
  <h3>Graph generation under structural constraints</h3>
  <p>
    My graph-generation research asks how to satisfy multiple structural
    constraints simultaneously while preserving each node's degree. By comparing learned
    rewiring policies with search that explicitly evaluates candidate edits,
    I investigate when local information can predict an edit's global effects
    and when direct evaluation remains necessary.
  </p>
</div>

## Selected research contributions

<div class="theme">
  <h3>1. Multimodal learning for cognitive assessment</h3>
  <p>
    Picture-description speech connects what people say with the visual scene
    they describe. To study how these relationships reflect cognitive function,
    I developed graph models of image–sentence relationships and combined them with text
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
    Using street networks from 22 Korean cities, I examined how urban
    structure relates to demographic and economic characteristics. Using
    centrality measures, planning regularity and population–road-length
    scaling, I related differences in network topology to the characteristics
    of each city.
  </p>
  {% include research-papers.html keys="P09" %}
</div>

## Industrial machine learning

Industrial applications have shaped how I evaluate predictive models, connecting
prediction accuracy with the decisions the predictions support. At Samsung
Research, I assessed inventory forecasts through their effects on simulated
ordering and stock levels.

## Collaboration and deployment

In clinical collaborations, I developed models with domain specialists to
analyse observed treatment choices. Other collaborations explored predictive coding for
recognition with limited or imbalanced data and classifiers that accommodate
new features.

{% include research-papers.html keys="P05,P06,P04" %}

For applied development and technology transfer, see
[Projects]({{ '/projects/' | relative_url }}).
