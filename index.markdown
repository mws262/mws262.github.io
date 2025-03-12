---
layout: default
---
<!-- filepath: /home/matt/git/mws262.github.io/index.markdown -->
<div class="post-list">
  {% for post in site.posts %}
    <a href="{{ post.url }}" class="post-item-link">
      <div class="post-item">
        <div class="post-thumbnail">
          {% if post.thumbnail %}
            <img src="{{ post.thumbnail }}" alt="{{ post.title }}">
          {% else %}
            <img src="/assets/images/default_thumb.webp" alt="Default Thumbnail">
          {% endif %}
        </div>
        <div class="post-content">
          <h2>{{ post.title }}</h2>
          <p class="post-excerpt">{{ post.excerpt | strip_html | truncate: 150 }}</p>
          <span class="post-date">{{ post.date | date: "%B %d, %Y" }}</span>
        </div>
      </div>
    </a>
  {% endfor %}
</div>