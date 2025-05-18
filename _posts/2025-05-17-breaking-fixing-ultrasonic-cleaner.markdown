---
layout: default
title:  "Breaking and Fixing an Ultrasonic Cleaner"
date:   2025-05-17 13:48:56 -0700
thumbnail: assets/images/breaking_fixing_ultrasonic_cleaner/ultrasonic_cleaner_thumbnail.webp
permalink: /projects/breaking-fixing-ultrasonic-cleaner
categories: repairs, ultrasonic cleaner, tools, electronics
---

I have a cheap Vevor ultrasonic cleaner. It works well for the price. Notably, the instructions really emphasize not to run the cleaner without water at least to the fill line. I assumed that the main reason for this was that without enough water, the transducers would overheat or perhaps vibrate too strongly without a load and detach.

These issues might be valid, but I found out the hard way that the heater is also very sensitive to a low water level. The heating element is a ceramic element that is adhered to one side of the tank. If the water level starts to get a little low, the heater will be partially above the water line. On its own, this is bad because of the temperature difference between the top and bottom of the header. Ceramic heating elements are very vulnerable to cracking.

![broken heater](/assets/images/breaking_fixing_ultrasonic_cleaner/broken_cleaner.webp)

Worse though, the temperature sensor for the controller is on the opposite side of the tank. This is good if you're trying to ensure that the entire water bath is at the right temperature but bad once the water level gets low. The sensor and heater will be partially above the water line, and the controller will keep trying to heat the tank. 

Unlike the ultrasonic transducers, there is no timer on the heater. I forgot to turn off the heater, and overnight, the water level dropped due to evaporation. By the morning, the heater was dead. It's my fault for leaving it on, but I think the design is a little flawed.

![ultrasonic cleaner PCB](/assets/images/breaking_fixing_ultrasonic_cleaner/cleaner_pcb.webp)

I opened the cleaner up and found the cracked heating element. It was wired to a relay on the controller board, and the heater had been running on 120V AC. I was having a hard time finding an exact replacement, so I bought a cheap ($6-8) immersion heater intended for heating water for tea/coffee.

I cut off the wall plug and soldered the wires to the relay terminals. I can clip the heater to the side of the tank, and it works well with the existing sensor and controller. The original heater was rated for 180W, and the immersion heater is rated for 300W. Fortunately, the electronics don't seem to mind, and the water does heat up faster now.

![ultrasonic cleaner PCB closeup](/assets/images/breaking_fixing_ultrasonic_cleaner/new_heater_close.webp)

My new setup will work just fine, but I do have two concerns. The immersion heater could fall out of the tank and remain turned on. I'm also concerned about the longevity of the immersion heater. It is designed to be submerged, but it is not designed to be submerged in a tank that vibrates at ultrasonic frequencies. I have no idea if this will cause the heater to fail prematurely, but at that price, I'm willing to take the risk.

