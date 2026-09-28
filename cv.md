---
layout: page
title: Curriculum Vitae
subtitle: Education, appointments and professional activities.
permalink: /cv/
description: Curriculum vitae of Byounghwa Lee - education, appointments, teaching, service and awards.
---

<ul class="linkbar">
  <li><a class="primary" href="{{ site.author.cv | relative_url }}">Download full CV (PDF)</a></li>
  {% for l in site.links %}
  <li><a href="{{ l.url }}" rel="noopener">{{ l.name }}</a></li>
  {% endfor %}
</ul>

## Appointments

<div class="rows">
  <div class="row">
    <div class="row-when">Aug 2021 – present</div>
    <div class="row-what">
      <p><strong>Senior Researcher</strong>, Electronics and Telecommunications Research Institute (ETRI)</p>
      <p class="sub">Integrated Intelligence Research Section (Jan 2024 – present) · Cyber Brain Research Section (Aug 2021 – Dec 2023)</p>
    </div>
  </div>
  <div class="row">
    <div class="row-when">Mar 2019 – Jul 2021</div>
    <div class="row-what">
      <p><strong>Staff Engineer</strong>, Samsung Research, Samsung Electronics</p>
      <p class="sub">Global AI Center, Big Data Team, Data Analytics Lab</p>
    </div>
  </div>
</div>

## Education

<div class="rows">
  <div class="row">
    <div class="row-when">Mar 2012 – Feb 2019</div>
    <div class="row-what">
      <p><strong>Ph.D. in Physics</strong>, POSTECH (integrated M.S./Ph.D. program)</p>
      <p class="sub">Statistical physics and complex systems. Advisors: Woo-Sung Jung, Hang-Hyun Jo</p>
      <p class="sub">Thesis: <em>Generative Model and Method for Correlated Bursty Dynamics</em></p>
    </div>
  </div>
  <div class="row">
    <div class="row-when">Mar 2007 – Feb 2012</div>
    <div class="row-what">
      <p><strong>B.S. in Physics</strong>, POSTECH</p>
    </div>
  </div>
  <div class="row">
    <div class="row-when">Mar 2005 – Feb 2007</div>
    <div class="row-what">
      <p><strong>Incheon Science High School</strong></p>
      <p class="sub">Graduated early after two years</p>
    </div>
  </div>
</div>

## Awards

<div class="rows">
  {% for a in site.data.service.awards %}
  <div class="row">
    <div class="row-when">{{ a.year }}</div>
    <div class="row-what"><p>{{ a.text }}</p></div>
  </div>
  {% endfor %}
</div>

## Teaching

<div class="rows">
  {% for t in site.data.service.teaching %}
  <div class="row">
    <div class="row-when">{{ t.term }}</div>
    <div class="row-what">
      <p>{{ t.course }}</p>
      <p class="sub">{{ t.role }}, {{ t.org }}</p>
    </div>
  </div>
  {% endfor %}
</div>

## Selected peer review

<div class="rows">
  {% for r in site.data.service.reviewing %}
  <div class="row">
    <div class="row-when">{{ r.years }}</div>
    <div class="row-what"><p>{{ r.journal }}</p></div>
  </div>
  {% endfor %}
</div>

## Other activities

<div class="rows">
  {% for o in site.data.service.other %}
  <div class="row">
    <div class="row-when">{{ o.year }}</div>
    <div class="row-what"><p>{{ o.text }}</p></div>
  </div>
  {% endfor %}
</div>
