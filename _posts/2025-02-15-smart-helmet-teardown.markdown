---
layout: default
title:  "Smart Bike Helmet Teardown"
date:   2025-02-14 17:58:36 -0800
thumbnail: assets/images/smart_helmet/helmet_thumbnail.webp
permalink: /projects/smart-helmet
categories: bikes, electronics, teardown
---

Here are photos from taking apart the Brooklyness/Classon smart bike helmet. I found the product to be a great idea with half-assed software. It was too dependent on the phone app for things as simple as turning the lights on. Worse though, you could rarely get videos to transfer off of the helmet at all. And, I don't believe they ever actually got the rear camera fully working. Let's see how the hardware looks!

![helmet exterior removed](/assets/images/smart_helmet/IMG_9624.webp)

The hard plastic shell was easy to remove. It just had a few globs of glue. The molded polystyrene feels like any other bike helmet. It's kind of clever the way the pink 18650 lithium battery cell is nestled in there. 
Flat flexible cables (FFC) run across the top of the helmet connecting the rear lights and camera to the front electronics package. It's a relatively long, unshielded cable. I wonder if the signals from the rear camera weren't very reliable.

![helmet rear with exterior removed](/assets/images/smart_helmet/IMG_9626.webp)

I'm most interested in the energy budget though. That single cell probably holds 10-12Wh. The helmet is supposed to record from 2 cameras, run lights, manage some sensors, communicate via WIFI/BT, etc. It should be possible to get a few hours of runtime, but that involves careful use of power saving features. The framerates from the cameras were pretty low (also rear camera disabled), and this may have been partially to keep the battery life at the reported 2-2.5hrs.

![side transducer](/assets/images/smart_helmet/IMG_9628.webp)

There is a pocket molded in the foam along the side of the helmet. There is a small copper coil device tucked in there. It looks a lot like bone conduction transducer. It doesn't seem anchored in a way that would provide effective conduction of vibrations though. Plus, I don't recall the helmet making any noise! There are two wires, red and black, that you can see going back to the main electronics in the first photo.

![helmet under brim](/assets/images/smart_helmet/IMG_9627.webp)

The electronics are almost all tidily tucked under the front brim of the helmet. It's nicely done. The electronics enclosure is secured to the foam by screws that go into expanding anchors, much like drywall anchors actually.

![electronics package top](/assets/images/smart_helmet/IMG_9629.webp)

This is the top of the electronics enclosure once unscrewed from the polystyrene part of the helmet. The 18650 battery cell is actually just in a holder (i.e. not spot welded).

![pcb cover removed](/assets/images/smart_helmet/IMG_9630.webp)

Now the good stuff! There are a bunch of large ICs on the PCB, The colored plastic pieces along the edge are for directing the light from surface mount LEDs out the side as turn signals and running lights.

![mcu close up](/assets/images/smart_helmet/IMG_9631.webp)

Here's the massive main brain of the beast, the [MCIMX6U5EVM10AC](https://www.nxp.com/docs/en/data-sheet/IMX6SDLCEC.pdf), made by NXP. This titan is a ball grid array (BGA) component with 624 connections on the bottom. It's a 1GHz MPU that costs \$50 each from Digikey! Even [JLCPCB charges \$30 per unit](https://jlcpcb.com/partdetail/NxpSemicon-MCIMX6U5EVM10AC/C394782). This single component must be a HUGE part of the BOM.

![ddr3 ram](/assets/images/smart_helmet/IMG_9632.webp)

These are Samsung 2GB DDR3 RAM chips (model K4B2G1646F). There are 2 more on the other side of the board for a total of 8GB!

On the right is a [power management IC](https://www.nxp.com/docs/en/data-sheet/MMPF0100.pdf) that has up to 6 buck or boost converters, 6 linear regulators, and a bunch of other things. The MMPF0100 is about \$4 from JLCPCB.

In the top right corner there's a one cell USB battery charge controller, the BQ24295. Just off screen there's a BQ27441, a battery "fuel gauge."

![emmc and codec](/assets/images/smart_helmet/IMG_9634.webp)
At the bottom right is a 16GB Samsung eMMC (KLMAG1JETD-B041). It's ~\$6 from JLCPCB.

You can also see the MAX9867, a stereo audio codec. It can handle 2 input and 2 output channels. \$3-4. I'm guessing to the left of the MAX9867 is an audio amplifier. You can see the red and black wires that go to the transducer. It looks like there are holes for a second speaker. I wonder if they had plans for the helmet to be a Bluetooth speaker.

![turn signal sensors](/assets/images/smart_helmet/IMG_9635.webp)
These are IR reflectance sensors -- a little IR LED and a phototransistor combo. Users are supposed to put their finger up to the sensor window to trigger the turn signals.

![pcb back](/assets/images/smart_helmet/IMG_9637.webp)
You can see the other 2x 2GB RAM on the back of the PCB. On the far left and right corners of the PCB are a pair of microphones (I think). They correspond to 

![wireless chip](/assets/images/smart_helmet/IMG_9639.webp)
WIFI/BLE IC, I believe. There is a surface mount antenna nearby also.

![rear board front](/assets/images/smart_helmet/IMG_9641.webp)
This is the rear board which has the tail lights, the second camera, and the USB connector. I did not identify the largest IC, but I'm guessing it's an LED current driver.

![rear board back](/assets/images/smart_helmet/IMG_9642.webp)

The electronics in this helmet are more impressive than I figured, actually. A lot of the components are targeted at tablets and similar products. You could run a decent Linux distro on a bike helmet.












