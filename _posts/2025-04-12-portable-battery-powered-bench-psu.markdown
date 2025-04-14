---
layout: default
title:  "Portable Battery-Powered Bench PSU"
date:   2025-04-12 13:53:49 -0700
thumbnail: assets/images/portable_battery_powered_bench_psu/riden_psu_thumbnail.webp
permalink: /projects/portable-battery-powered-bench-psu
categories: PSU, electronics, batteries, power supply, 3d printing
---
This is from this past year, but I hadn't written anything down until now.

I often do electronics projects that can't be easily brought to my workbench. So, I'll unplug my bench power supply and take it with me. This is usually a mess of cables, and is in general a pain. A portable, battery-powered CC/CV power supply is pretty handy for these cases and can be done pretty cheaply.

![enclosed psu with battery](/assets/images/portable_battery_powered_bench_psu/riden_w_batt.webp)

I discovered that Riden sells their power supplies in modular form. You can buy the front panel alone, which contains the display, buttons, and step-down converter. Their full units are just the front panel with an off-the-shelf 60V AC/DC converter in an enclosure behind it. So, it's very easy to pair a Riden front panel with a battery to make a portable power supply.

![riden psu components](/assets/images/portable_battery_powered_bench_psu/riden_psu_components.webp)

They have a bunch of models, but I've only used the [RD6018](https://riden.aliexpress.com/store/1102012359/pages/all-items.html?productGroupId=40000001142062) (rated for 60V, 18A). I have the full unit, and while I wouldn't trust it for anything critical, it's a good workhorse for the price (~$200). The front panel by itself is only $80. You don't have to supply it with the full 60V either. A 36V or 48V battery will work fine, though the controller only steps the voltage down; it won't boost you to 60V. I have some salvaged scooter and ebike battery packs, so I use any of those.

![enclosed psu alone](/assets/images/portable_battery_powered_bench_psu/riden_enclosed.webp)

The back of the Riden panel has an exposed PCB, so I made a quick 3D-printed enclosure with a vent for the fan. If I used it constantly, I would probably make an enclosure for both the battery and the Riden panel. For now, I just have an XT60 connector coming out of the enclosure. 

![opened psu](/assets/images/portable_battery_powered_bench_psu/riden_opened.webp)

The 3D print is pretty simple, but the PSU controller snaps in pretty snugly. I'll link to the part on [Thingiverse](https://www.thingiverse.com/thing:7009418). I've since then realized that I'm not the first person to have this idea, so you might find other designs on Thingiverse that are more suitable for your use.

![psu enclosure back](/assets/images/portable_battery_powered_bench_psu/riden_enclosure_back.webp)







