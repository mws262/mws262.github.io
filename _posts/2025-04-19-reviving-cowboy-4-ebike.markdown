---
layout: default
title:  "Reviving a Cowboy 4 eBike"
date:   2025-04-19 07:54:19 -0700
thumbnail: assets/images/reviving_cowboy_4_ebike/cowboy_thumbnail.webp
permalink: /projects/reviving-cowboy-4-ebike
categories: ebikes, bikes, Cowboy, repairs, batteries
---

I inherited an unresponsive Cowboy ebike from the startup I worked at. At the time, the only known issue was that the hydraulic brake levers were both broken. There seems to be a weak point where the lever attaches to the brake piston. A downside of the Cowboy bikes is that they use a lot of proprietary parts. I replaced the brake levers with Shimano MT200 levers. They fit the bar diameter just fine, but they don't aesthetically line up with the other features of the bars. One of the calipers seemed clogged, so I replaced it with one of the Shimano ones while I was at it. It required messing around with spacers to get the alignment right, but it did fit.

I couldn't get the app to connect to the bike, since the bike was locked to a company email that no longer existed. Even after getting my company to re-create that email address, the password reset emails never arrived. Cowboy customer support pretty much just kept trying to hit the "reset password" button for me. Yes, I could receive other email to that address; yes, I checked the spam folder. I eventually gave up on the app.

The Cowboy is supposed to manually turn when the battery is removed for a few seconds and reinserted. Sadly, the bike was completely unresponsive. I had left the battery charging for a day, so I assumed it was charged. There are no charge indicators on the battery itself. The bike has basically no status indicators or user controls as a whole. My big pet peeve is devices that essentially require an app when a few buttons and LEDs would cover most of the functionality. Everyone thinks they're Apple now, but I digress. A few of the pins on the battery showed some low voltages, which isn't too surprising for proprietary batteries that have to do a handshake with the device in order to power on.

![full cowboy electronics](/assets/images/reviving_cowboy_4_ebike/full_electronics_harness.webp)

I wanted to check the power pins with the battery attached to the bike. I opened up the bike's electronics, partially just out of curiosity. There were two main components: a motor controller and a main logic/communications board. The motor controller (model "2B Tube") is this funny aluminum cylinder made by a 3rd party, Accelerated Systems Inc. Having designed quite a few motor controllers, I was interested to see the layout, but the cylinder was encapsulated with some goop like Sylgard. The logic board had a lot of communications components. It had a LTE data module with a surface mount eSIM card, a GPS module with a large external antenna, and a Bluetooth module that I believe was also used as the main microcontroller. Depending on your perspective, this is either excellent constantly-internet-connected tracking or a a potential privacy nightmare.

I case anyone finds it useful, here is what I learned about the main PCB on the Cowboy:

![cowboy logic board](/assets/images/reviving_cowboy_4_ebike/cowboy_main_board.webp)

![cowboy logic board connector](/assets/images/reviving_cowboy_4_ebike/cowboy_main_board_connector.webp)

The logic board also had a holder for a single 18650 battery cell. I assume that this is to maintain tracking when the main battery is removed. The battery was very dead, so I carefully recharged it with a power supply. Bosch ebikes have a small battery on the screen that lets them send the initial CAN messages required to turn the bike on. I was hopeful that the Cowboy was similar with this 18650 cell. Still nothing.

![backup battery](/assets/images/reviving_cowboy_4_ebike/backup_batt.webp)

I took the main battery pack off the bike and hooked 36V directly to the bike's power leads. The bike partially turned on. A light on the motor controller cylinder began flashing a pattern that I assume was a fault code. Most likely, the logic board entered an error state when it couldn't talk to the battery. I decided the battery pack was the most likely culprit, so I took it apart. This was a real pain. The pack wasn't fully-encapsulated, but it did have a generous application of goop all around the cells. The whole pack was in an aluminum extrusion tube, so sliding the pack out required a lot of finagling. The only more difficult pack I've disassembled was the Boosted Rev Scooter's.

And yeah, the cells were all at about 0.9V. The BMS had rightly deemed the pack over-discharged and had refused charging. I'd say that the battery hadn't been charged in 1-2 years. I'm guessing that even in sleep mode, the BMS drew a small amount of power to continue monitoring the battery or to keep GPS tracking active on the bike. I don't know whether to consider this a design flaw or not. This had been a healthy battery with a low number of charge cycles. People sometimes don't use their bikes for a year, and it's reasonable to expect the bike to still work. If you do have a Cowboy bike you rarely use, definitely take the battery off of the bike for storage, and give it a bit of charge occasionally. Who's going to remember to do that though?

Anywho, I bypassed the BMS to directly charge the cells slowly (<0.5A) with a power supply. I did it outside and monitored for hot spots. Please note that you really shouldn't do this. If you properly want to recover cells like this, you should disassemble the pack, check each cell's properties individually, cycle test them, ensure they hold charge, etc. Even then, new cells would be a better option. Safety aside, the pack did hold a charge, and the bike was rideable once I reassembled everything.

I have a few normal bike things to adjust, but I think the Cowboy is back!