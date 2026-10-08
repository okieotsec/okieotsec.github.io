---
layout: default
title: Lab notes
permalink: /notes/
---
# Lab notes

<ul class="post-list">
  {% for post in site.posts %}
  <li><span class="meta">{{ post.date | date: "%b %-d, %Y" }}</span> <a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
