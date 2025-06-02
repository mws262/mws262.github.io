---
layout: default
title:  "Label Printer as 1D CNC"
date:   2025-06-01 15:47:45 -0700
thumbnail: assets/images/label_printer_as_1d_cnc/thumbnail.webp
permalink: /projects/label-printer-as-1d-cnc
categories: hacks, automation, packaging
---

I had to cut a bunch of equal-length segments of anti-static poly tubing to package the [encoder boards I sell](https://www.amazon.com/AS5047P-Magnetic-Position-Breakout-Compatible/dp/B0DLJ6XDNM). I rarely turn down the opportunity to automate a task that I should just do by hand. So, I used my label printer with a built-in cutter to do the job for me.

My Zebra GX430t label printer accepts ZPL (Zebra Programming Language) commands, which allows me to control the printer's functions programmatically. I made a Python script to send ZPL commands to the printer, instructing it to feed a specific amount of material and cut it. The tricky part was keeping the printer from going into an error state. Depending on settings, it may decide that the material is not the expected size or that a translucent material is not present at all. With some experimentation, I ended up with [this code](https://github.com/mws262/zebra-printer-cutter).

<video class="responsive-video" autoplay loop muted playsinline controls><source src="{{ '/assets/images/label_printer_as_1d_cnc/printer_cutter.mp4' | relative_url }}" type="video/mp4">
  [VIDEO]
</video>

I was able to feed the tubing through a slot on the back of the printer. I found that the my heavy roll of tubing initially provided too much resistance for the feed roller. I was getting inconsistent tube cut lengths. I ended up placing the roll sideways on a lazy Susan to allow it to spin freely.

I was surprised how well the cutter worked on the relatively-thick poly tubing. I'm curious what other kinds of materials I could feed through. I think heat-shrink tubing would work, if I ever have a project that requires many segments of it.