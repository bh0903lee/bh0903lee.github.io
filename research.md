---
layout: page
title: Research
subtitle: Machine learning from the structure of scientific, clinical and industrial data.
permalink: /research/
description: Research by Byounghwa Lee on AI for science and complex systems, graph learning and constrained generation, event-sequence learning, and multimodal cognitive assessment.
---

I work on machine learning for scientific, clinical and industrial data, with a
background in statistical physics and complex systems. My research asks how the
structure of a system, the timing of its events, the relations among its parts
and the several modalities in which it is observed, can be turned into models
that predict, generate and explain. The work spans four connected areas:

- **AI for science and complex systems.** Representation learning for
  scientific data, relations between structure and dynamics, and model
  validation.
- **Graph learning and constrained generation.** Complex networks, graph
  representations, and generating or editing graphs under structural
  constraints.
- **Event-sequence learning.** Temporal point processes, bursty dynamics,
  memory and temporal dependence, and probabilistic prediction.
- **Multimodal and data-efficient learning.** Combining images, language and
  speech for cognitive assessment, and learning from limited or imbalanced
  data.

<figure class="figure">
  <a href="{{ '/assets/img/research-overview.svg' | relative_url }}" target="_blank" rel="noopener" title="Open full-size figure">
    <img src="{{ '/assets/img/research-overview.svg' | relative_url }}" width="1280" height="716" alt="Overview of research threads: healthcare AI, bursty dynamics and complex networks lead to multimodal cognitive assessment, event-sequence learning and constrained graph generation, and converge on AI for science.">
  </a>
  <figcaption>
    How the threads connect. Healthcare AI, bursty dynamics and complex
    networks lead to multimodal cognitive assessment, event-sequence learning
    and constrained graph generation, and converge on representation learning
    for scientific data. Colours mark where the work was done; dashed boxes
    are ongoing. Click to open at full size.
  </figcaption>
</figure>

## Current work

<div class="theme" id="current-drug-discovery">
  <h3>Scientific representation learning for drug discovery</h3>
  <p>
    At ETRI, I develop science-specialized encoders and tokenizers for
    molecules and proteins, using protein–ligand binding-affinity prediction as
    the application. The question is how pretrained sequence representations
    and three-dimensional structure should be combined, and how well the
    resulting models generalize beyond the proteins and molecules they were
    trained on.
  </p>
  <p class="basis">
    New application area since 2026, building on the multimodal and graph-based
    representation work below. Ongoing; no results published yet.
  </p>
</div>

<div class="theme" id="current-event-sequences">
  <h3>Event-sequence learning</h3>
  <p>
    Temporal point processes model when events happen. This work asks how the
    statistical signatures of bursty activity, which I studied in my doctoral
    research, should enter neural event-sequence models, and under which
    conditions they change what the models predict.
  </p>
  <p class="basis">
    Extends the Burst and Memory-aware Transformer (2023) and my patent
    applications on time-series pattern prediction. Manuscripts under review.
  </p>
</div>

<div class="theme" id="current-graph-generation">
  <h3>Graph generation under structural constraints</h3>
  <p>
    Many scientific and engineered systems must satisfy several structural
    constraints at once. This work studies how to generate and edit graphs
    under such constraints, and which parts of that process learned models can
    take over from explicit evaluation and search.
  </p>
  <p class="basis">
    Grows out of my granted Korean patent on constrained network generation
    (<a href="{{ '/cv/#patent-t01' | relative_url }}">KR 10-3005917</a>) and the
    complex-network work below. Manuscript under review.
  </p>
</div>

## Selected research contributions

<div class="theme" id="cognitive-assessment">
  <h3>1. Multimodal learning for cognitive assessment</h3>
  <p>
    Picture-description speech connects what people say with the visual scene
    they describe. To study how these relationships reflect cognitive function,
    I developed graph models of image–sentence relationships and combined them
    with text and audio representations through co-attention, examining how
    visual, linguistic and acoustic cues contribute to Alzheimer's disease
    classification on the ADReSSo benchmark.
  </p>
  <p class="finding">
    <strong>Key finding.</strong> The image–sentence graph supported
    Alzheimer's disease classification on its own, and removing the image–text
    relations lowered performance, so the relational structure itself carries
    diagnostic signal. Combining the graph with text and audio through
    co-attention improved mean accuracy further, with most of the gain coming
    from co-attention rather than from adding audio. These are results on an
    English picture-description benchmark, not a clinical validation.
  </p>
  <p class="basis">
    First and corresponding author on both papers. The method is covered by a
    granted Korean patent
    (<a href="{{ '/cv/#patent-t04' | relative_url }}">KR 10-2968743</a>, first
    inventor) and led to the Korean speech-based MCI model described under
    <a href="{{ '/projects/#technology-transfer' | relative_url }}">Projects</a>.
  </p>
  {% include research-papers.html keys="P01,P02" %}
</div>

<div class="theme" id="bursty-dynamics">
  <h3>2. Bursty dynamics and temporal point processes</h3>
  <p>
    Events in complex systems often cluster in time. I developed a hierarchical
    model of bursty dynamics and contributed to a copula-based method for
    controlling inter-event time distributions and memory. Building on this
    work, I incorporated burstiness and memory statistics into a Transformer
    for event-time prediction, linking statistical descriptions of temporal
    heterogeneity with neural sequence models.
  </p>
  <p class="finding">
    <strong>Key finding.</strong> In the hierarchical model, the known relation
    between the inter-event time exponent and the autocorrelation exponent
    (α + γ = 2) still holds when successive intervals are correlated, while
    burst sizes follow a stretched-exponential rather than a power-law
    distribution, which marks what a hierarchical mechanism alone can and
    cannot explain. In the Transformer, burst and memory statistics improved
    next-event time prediction mainly where temporal heterogeneity was strong,
    not uniformly across datasets.
  </p>
  {% include research-papers.html keys="P03,P08,P07" %}
</div>

<div class="theme" id="complex-networks">
  <h3>3. Complex networks and urban structure</h3>
  <p>
    Using street networks from 22 Korean cities, I examined how urban
    structure relates to demographic and economic characteristics, through
    centrality measures, planning regularity and population–road-length
    scaling.
  </p>
  <p class="finding">
    <strong>Key finding.</strong> Cities grouped by the inequality of their
    centrality measures shared demographic and planning characteristics, and
    population–road-length scaling differed between urban and urban–rural
    cities, so the relation depends on how cities are grouped.
  </p>
  {% include research-papers.html keys="P09" %}
</div>

## Research directions

Looking ahead, my research program asks what can be learned from the structure
and observations of a complex system, and what additional observation or
computation is needed to tell competing scientific explanations apart. It
rests on the two foundations above: generative models of bursty dynamics
leading to event-sequence learning, and complex-network analysis leading to
graph learning under structural constraints. Over the next two to three years
I plan to build controlled benchmarks that identify which temporal statistics
a sequence model needs, to develop constraint-aware graph generation that
combines learning with explicit evaluation, and to extend both toward
representation learning that preserves the large-scale dynamics of scientific
systems, with cost-aware sequential experimental design as a longer-term goal.
This is a plan for the coming years rather than completed work.

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
