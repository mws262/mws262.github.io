#!/usr/bin/env python3

import os
import sys
import re
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
POSTS_DIR = os.path.join(ROOT_DIR, '_posts')
IMAGES_DIR = os.path.join(ROOT_DIR, 'assets', 'images')

# Common connecting words to remove
CONNECTING_WORDS = {'a', 'an', 'the', 'of', 'in', 'on', 'at', 'to', 'for', 'by', 'with', 'about', 'from', 'into', 'and'}

def slugify(title, separator='-'):
    words = title.lower().split()
    filtered = [w for w in words if w not in CONNECTING_WORDS]
    return re.sub(r'[^a-z0-9]+', separator, ' '.join(filtered)).strip(separator)

def create_post(title):
    slug = slugify(title, separator='-')
    img_dirname = slugify(title, separator='_')
    date = datetime.now()
    date_str = date.strftime('%Y-%m-%d')
    datetime_str = date.strftime('%Y-%m-%d %H:%M:%S') + ' -0700'
    filename = f"{date_str}-{slug}.markdown"
    filepath = os.path.join(POSTS_DIR, filename)

    if os.path.exists(filepath):
        print(f"File already exists: {filepath}")
        return

    img_dir_path = os.path.join(IMAGES_DIR, img_dirname)
    os.makedirs(img_dir_path, exist_ok=True)

    front_matter = f"""---
layout: default
title:  "{title}"
date:   {datetime_str}
thumbnail: assets/images/{img_dirname}/thumbnail.webp
permalink: /projects/{slug}
categories: placeholder, category
---

"""

    with open(filepath, 'w') as f:
        f.write(front_matter)

    print(f"Created post:     {filepath}")
    print(f"Created img dir:  {img_dir_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python _tools/new_post.py \"Post Title Here\"")
        sys.exit(1)

    create_post(sys.argv[1])
