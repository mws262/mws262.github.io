---
layout: default
title:  "A note about rebuilding a Dyson V8 battery"
date:   2025-04-10 17:00:00 -0700
thumbnail: assets/images/dyson_battery/dyson_thumbnail.webp
permalink: /projects/dyson-battery
categories: electronics, battery, repair, dyson, vacuum
---

I rebuilt the battery pack for my Dyson V8 vacuum cleaner. This isn't particularly interesting in itself, but there are a few niche things to be aware of if you are also using some 18650 cells you have lying around. 

The TL;DR is that there's a magnet on the vacuum body that needs to be near a reed switch on the battery. If you use 18650s, the pack will likely be smaller and may not be close enough to trigger the sensor.

![whole old pack](/assets/images/dyson_battery/old_pack_whole.webp)

Removing the pack from the vacuum body is easy, but opening the pack is a pain. There are 3 visible screws and no screws hidden under the labels. There are 6 plastic snap tabs holding the two sides of the enclosure together. To limit damage, I had to individually shim each tab before I could pull it apart.

![cell comparison](/assets/images/dyson_battery/old_cell_new_cell.webp)

The Dyson pack actually contained 20700 cells, which are larger than the common 18650 size cells. 20mm x 70mm vs. 18mm x 65mm in case you thought the numbers were arbitrary like I did for a long time. I have plenty of salvaged and tested 18650 cells, but no 20700 cells. The original pack says 2800mAh capacity, and the 18650 cells I have tested at about 2500mAh. That seemed good enough to me.

![pack comparison](/assets/images/dyson_battery/old_pack_new_pack.webp)

Since the cells are smaller, I simply made another pack and transplanted the control board (BMS) onto the new pack. I removed it by snipping the nickel strips just outside the original cells. I cut new nickel strips and soldered them to the onto the old strips to replace the lost section. I spot welded the cells to the new strips.

![BMS reed switch](/assets/images/dyson_battery/reed_switch.webp)

Like a dummy, I reassembled the pack and was surprised when it didn't work. On further inspection, I found that the BMS board has a reed switch on it. This switch is open unless a magnet is nearby. The battery won't turn on without closing the reed switch. Because my new pack was smaller and had slightly moved the BMS location, the reed switch was no longer close enough to the magnet. I moved some little fridge magnets around the vacuum body to find the built-in magnet location:

![magnet location](/assets/images/dyson_battery/magnet_location.webp)

The magnet is connected to the the part of the vacuum that you pull up when emptying the dust bin. So, it seems that the purpose is to disable the vacuum while emptying the dust bin. I imagine that if the vacuum were to turn on, it could cause a mess, or worse -- debris could be sucked directly into the motor with the filter out of the way.

![magnet slide location](/assets/images/dyson_battery/sliding_magnet_location.webp)

As a side note, the power trigger is just a mechanical lever that pushes a momentary switch in the battery pack. Dyson was probably trying to keep most of the electronics in the battery pack and have only the motor wires connecting the pack to the body. I'm guessing this is why they used a reed switch instead of putting a mechanical switch in the vacuum body.

I decided not to worry about the magnet at all. I just soldered a wire across the reed switch leads, and it works well.

For my own projects, I usually use hall effect sensors, but this reminded me how cool reed switches are. They're incredibly simple and easy to work with when you're dealing with slow switching speeds and digital signals.