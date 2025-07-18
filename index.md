---
layout: default
title: Home
---

# Welcome to the NexaSQL Blog

Stay updated with our latest posts and insights.

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a> 
      <span>{{ post.date | date: "%b %-d, %Y" }}</span>
    </li>
  {% endfor %}
</ul>
