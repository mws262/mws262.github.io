---
layout: default
title:  "A tiny gripe about the T-Display-S3"
date:   2025-03-10 16:13:00 -0700
thumbnail: assets/images/lilygo_dim/t_display_thumbnail.webp
permalink: /projects/t-display-dimensions
categories: esp32, mcu, "dev board", CAD, STEP
---

The LILYGO T-Display-S3 is really pretty great. Their non-touchscreen version is $13. For some projects, I'd normally get a custom PCB made and assembled by JLCPCB. Usually I can get a custom board for prices not all that different from what it would take to buy all the little dev board modules and smoosh them together. Lately though, I've been just using the T-Display-S3 for any ESP32 project that requires a display. It's cheaper, and I don't have to fool around with the tiny-pitch flat printed circuit connectors for the LCD. I highly recommend.

![full t-display-s3 cad](/assets/images/lilygo_dim/t-display-s3-full.webp)

Now my very tiny gripe. The last few times I've designed 3D printed enclosures for the T-Display, the external buttons have always taken some fine tuning to line up correctly with the surface mount tactile switches on the PCB. Today, I took a closer look, and noticed that the two buttons didn't seem to line up with each other on the board. I figured maybe one of the buttons had drifted a bit during reflow. Nope. I found LILYGO's CAD model for the T-Display-S3 and noticed this:

![dimensions on t-display-s3-cad](/assets/images/lilygo_dim/t-display-s3-full_dim.webp)

I'm guessing the designer just eyeballed the location when placing the buttons. Again, not a huge deal, but be careful when assuming symmetry.



