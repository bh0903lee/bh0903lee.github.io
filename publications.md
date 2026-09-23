---
layout: page
title: Publications
subtitle: Peer-reviewed journal and conference papers, newest first.
permalink: /publications/
description: Peer-reviewed publications of Byounghwa Lee.
---

Names in **bold** are mine; the list is also available on
[Google Scholar]({{ site.links[0].url }}) and
[ORCID]({{ site.links[1].url }}).

{% assign pubs = site.data.publications | sort: "date" | reverse %}
{% assign years = pubs | map: "year" | uniq %}

{% for y in years %}
## {{ y }}

<ol class="pub-list">
{% for p in pubs %}{% if p.year == y %}{% include publication.html pub=p %}{% endif %}{% endfor %}
</ol>
{% endfor %}

## Demonstrations and other contributions

<ul class="pub-list">
  <li class="pub">
    <p class="pub-title">Intelligent System for Early Detection of Mild Cognitive Impairment and Dementia Risk Through Spoken Language Analysis</p>
    <p class="pub-authors">Byung Ok Kang, <strong>Byounghwa Lee</strong>, Jeong-Uk Bang, Hwa Jeon Song, Young Jin Park</p>
    <p class="pub-meta"><span class="venue">IEEE ICASSP 2025, Show &amp; Tell</span>, April 2025 <span class="tag">Demonstration</span></p>
    <p class="pub-summary">A demonstration of a screening system for cognitive-decline risk based on spoken language analysis. Listed separately from refereed technical papers.</p>
  </li>
  <li class="pub">
    <p class="pub-title">DementiaBank Korean Kang Corpus</p>
    <p class="pub-authors"><strong>Byounghwa Lee</strong> (contributor)</p>
    <p class="pub-meta"><span class="venue">TalkBank / DementiaBank</span> <span class="tag">Dataset</span></p>
    <p class="pub-links"><a href="https://doi.org/10.21415/PJVS-9X49" rel="noopener">doi:10.21415/PJVS-9X49</a></p>
  </li>
</ul>

<p class="foot-meta">Manuscripts currently under peer review are not listed here.</p>
