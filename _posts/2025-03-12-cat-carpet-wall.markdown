---
layout: default
title:  "Cat Carpet Wall Theatre"
date:   2025-03-12 13:00:00 -0700
thumbnail: assets/images/carpet_wall/cat_carpet_tv_thumbnail.webp
permalink: /projects/cat-carpet-wall
categories: cats, rpi, kodi, libreelec, "cat toy"
---
I recently made a carpeted wall for my cats to climb. I've now added an old projector to the mix, and it's become a cat theater.

<video class="responsive-video" autoplay loop muted playsinline controls><source src="{{ '/assets/images/carpet_wall/carpet_wall_chaos.mp4' | relative_url }}" type="video/mp4">
  [VIDEO]
</video>

![carpet wall detail](/assets/images/carpet_wall/carpet_wall_detail.webp)

The wall is made from a 4'x8' sheet of plywood, covered in carpet. The carpet is really cheap, but that gives it a rough texture that the cats can easily climb. The carpet is attached to the plywood with carpet adhesive and stapled around the edges of the plywood.

<video class="responsive-video" autoplay loop muted playsinline controls><source src="{{ '/assets/images/carpet_wall/carpet_wall_fish.mp4' | relative_url }}" type="video/mp4">
  [VIDEO]
</video>

I was given an old projector recently, and I thought the cats might enjoy chasing the moving images. The projector is low res, but it's pretty bright. It's old enough that I had to buy a VGA adapter.

![projector](/assets/images/carpet_wall/cat_projector.webp)

The projector is mounted to the wall and is connected to a Raspberry Pi running LibreELEC (a Kodi distribution). I've transferred a bunch of videos to the RPi using the web interface, and Kodi has an app that I can use as a remote control.

The cats also love to chase a laser pointer around the wall, so I made a virtual laser pointer with the projector. I have a python script that makes a video of a red dot moving around the screen in a whole bunch of different ways. I'll link the script soon. It's mostly AI generated, but I did tune up the movements to make them more appealing to the cats.

<video class="responsive-video" autoplay loop muted playsinline controls><source src="{{ '/assets/images/carpet_wall/carpet_wall_dot.mp4' | relative_url }}" type="video/mp4">
  [VIDEO]
</video>

The cats like the videos, but it's the carpet wall that's the real hit. It's really entertaining to watch them play on it. It's a great, easy DIY project that I'd recommend to anyone with cats, as long as you don't mind looking like a crazy cat person :D