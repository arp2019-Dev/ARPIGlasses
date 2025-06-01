---
title: "ARPIGlasses"
author: "arp"
description: "Affordable and sleek Smart AR Glasses to help your lifestyle"
created_at: "2025-05-23"
---


# MAY 23rd: Started the major research for some optics

I looked at how many expensive smart glasses work, and most use a micro OLED display with some optics to move the image down and into your eyes. This, however, looks bulky and is not nice to use according to users. This is our challenge when it comes to smart glasses since it's hard to get a high-res image to focus at such a close distance to your eyes. Many use prisms and beam splitters to combine the 2 sources of light (1 is the display and the other is the world).

A great example of an optics system is the Google Glass Explorer, which uses a beam splitter and mirror to focus the light.
<img width="563" alt="Screenshot 2025-05-23 at 10 08 52 PM" src="https://github.com/user-attachments/assets/a083e56a-e7a4-4376-aa7e-06108bcde340" />

**Total time spent: 4h**

# MAY 24th: More research on the optics for some types of glasses

So, I spent some time looking at more glasses and methods for projecting the image. I initially thought I could put the display far back on the side of the head and then use a bunch of mirrors to "move" the image, but after a lot of calculations, I realized it wouldn't work unless the size was big. Instead, I will just need to stick with the beam splitter and a  combo of lenses to focus the image closer.

An image to visualize the law of reflection. (courtesy of https://courses.lumenlearning.com/suny-physics/chapter/25-2-the-law-of-reflection/)
<img width="571" alt="Screenshot 2025-05-25 at 12 36 12 AM" src="https://github.com/user-attachments/assets/5521a7ed-f70f-4ce0-8019-eef70ea63e25" />

Unfortunately, idk where my paper with some of my calculations went since I just did some while researching. If I find it, ill place it here.

**Total time spent: 3h**

# MAY 25th: Did some display research

So turns out there is this really cool display tech that projects the image directly into your retina using low-power lasers. Super intriguing and I was gonna use it, but 1. super expensive and hard to find. 2. Safety, you need hella precision to not wreck your eyes.
I also found a nice simulator that allows me to test different lenses and custom optics. To get this, I put together a quick prism and beam splitter.

https://phydemo.app/ray-optics/simulator/
<img width="566" alt="Screenshot 2025-05-25 at 10 27 39 PM" src="https://github.com/user-attachments/assets/e305404b-c046-46ca-82e4-b8c9de7e55bf" />


**Total time spent: 2h**

# MAY 31st: Optics and Electronics

So I forgot to log my previous 3 days, so I'm gonna  put a very long one here. I did some more simulating to try to visualize how the beam splitter will be positioned in front of my eyes to be in focus. For version 1, I plan to have a beam splitter cube perpendicular to the display on each side, as shown in the drawing below. To get the image to translate to the side a bit, I'll use a 45-degree mirror to reflect the incoming image towards the beam splitter, which then combines the light from outside and the image. Additionally, I started thinking about my image processing. In order to minimize the size of the glasses and increase power, I am going to sideload the processing to a phone that then transmits the image and data to a smaller processor on the glasses. I'm probably going to use a Raspberry Pi chip. I will also need to control the display, and controlling two micro OLEDs is not easy. I have 2 options, the safer one is using a dual display set used for VR goggles, and downsizing the PCB. The better cooler method is to fully make my own PCB for this. I'll need to use an HDMI bridge and an LVDS driver. Currently thinking of using the ADV7513 for HDMI encoding, TFP401A for HDMI to RGB, SN75LVDS83B	for RGB to LVDS, ECX334AF for the display (Sony display nice), VS23S010 for SPI video mem.

Image for optic placement:
![IMG_3280](https://github.com/user-attachments/assets/bfef72bd-345f-455f-a6eb-777c6332f06f)


**Total time spent: 8h**
