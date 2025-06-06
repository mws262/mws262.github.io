---
layout: default
title:  "Looting a Massage Chair"
date:   2025-06-04 16:20:34 -0700
thumbnail: assets/images/looting_massage_chair/thumbnail.webp
permalink: /projects/looting-massage-chair
categories: teardown, electronics, motors, actuators
---

I found a fancy massage chair on the side of the road near my place. It was very worn and had been rained on a few times. I was curious about the internals, so I brought some tools and starting pulling out the interesting bits. I think it was an Ootori Sofia S5 or similar.

![ootori massage chair](/assets/images/looting_massage_chair/ootori_chair.webp)

Here's the spread of actuators and electronics I found:

![all parts](/assets/images/looting_massage_chair/all_parts.webp)

In total, there were 2 linear actuators, 3 massage motors, an air pump system, and a variety of electronics. There may have even been even more in the foot/leg section, but I didn't take that apart. 

## Massage Mechanism
Clearly the coolest part of the chair. It had a carriage that moved up and down the backrest on a rack and pinion track. The carriage had linkages that moved a two sets of rollers. The linkages could make the rollers do a slow kneading motion and a fast percussive motion. The motors drove the linkages using cams, and the two motions could be combined to create a variety of massage styles.

This is the motor that drove the rack and pinion track:
![rack and pinion motor](/assets/images/looting_massage_chair/rackpinion_motor.webp)


The kneading motion driven by one of the motors:
<video class="responsive-video" autoplay loop muted playsinline controls><source src="{{ '/assets/images/looting_massage_chair/knead_motion.mp4' | relative_url }}" type="video/mp4">
  [VIDEO]
</video>

The percussive motion driven by a different motor:
<video class="responsive-video" autoplay loop muted playsinline controls><source src="{{ '/assets/images/looting_massage_chair/percussion_motion.mp4' | relative_url }}" type="video/mp4">
  [VIDEO]
</video>

Powering both motors at once gives a combined motion:
<video class="responsive-video" autoplay loop muted playsinline controls><source src="{{ '/assets/images/looting_massage_chair/combo_motion.mp4' | relative_url }}" type="video/mp4">
  [VIDEO]
</video>

## Linear Actuators

Two strong linear actuators were used to move the backrest and the footrest. They were 24V DC, rated for 4000-6000N, and had a stroke length of 100mm.


## Air System
The chair had a variety of air bladders throughout, presumably for squeezing the user. The main air pump operated on 24V AC.

![air pump](/assets/images/looting_massage_chair/air_pump.webp)

A manifold of 6 solenoid valve controlled flow to the bladders.

![solenoid manifold](/assets/images/looting_massage_chair/valve_manifold.webp)

## Electronics
![main control board](/assets/images/looting_massage_chair/main_pcb.webp)
There was a main control board with a variety of relays, a smaller board for Bluetooth audio to the built-in speakers, and a large toroidal transformer. I neglected to take the wired remote control for the chair controls. The heavy transforer was for 120V AC to 24V AC at 11A.
![transformer](/assets/images/looting_massage_chair/transformer.webp)

I am curious why the air pump used AC instead of DC like the rest of the chair. If the chair didn't need 24V AC, they could have skipped the heavy, expensive transformer. I've seen some small impeller-based water pumps use AC, as it's probably easier to waterproof the motor without brushes. In this case though, I believe it's a diaphragm air pump. I've not taken it apart to confirm however.