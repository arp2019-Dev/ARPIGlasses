---
title: "ARPIGlasses"
author: "arp"
description: "Affordable and sleek Smart AR Glasses to help your lifestyle"
created_at: "2025-05-23"
---
**Total Time Spent:** 48 Hours

# MAY 23rd: Started the major research for some optics

I looked at how many expensive smart glasses work, and most use a micro OLED display with some optics to move the image down and into your eyes. This, however, looks bulky and is not nice to use according to users. This is our challenge when it comes to smart glasses since it's hard to get a high-res image to focus at such a close distance to your eyes. Many use prisms and beam splitters to combine the 2 sources of light (1 is the display and the other is the world).

A great example of an optics system is the Google Glass Explorer, which uses a beam splitter and mirror to focus the light.
<img width="563" alt="Screenshot 2025-05-23 at 10 08 52 PM" src="https://github.com/user-attachments/assets/a083e56a-e7a4-4376-aa7e-06108bcde340" />

**Session time spent: 4h**

# MAY 24th: More research on the optics for some types of glasses

So, I spent some time looking at more glasses and methods for projecting the image. I initially thought I could put the display far back on the side of the head and then use a bunch of mirrors to "move" the image, but after a lot of calculations, I realized it wouldn't work unless the size was big. Instead, I will just need to stick with the beam splitter and a  combo of lenses to focus the image closer.

An image to visualize the law of reflection. (courtesy of https://courses.lumenlearning.com/suny-physics/chapter/25-2-the-law-of-reflection/)
<img width="571" alt="Screenshot 2025-05-25 at 12 36 12 AM" src="https://github.com/user-attachments/assets/5521a7ed-f70f-4ce0-8019-eef70ea63e25" />

Unfortunately, idk where my paper with some of my calculations went since I just did some while researching. If I find it, ill place it here.

**Session time spent: 3h**

# MAY 25th: Did some display research

So turns out there is this really cool display tech that projects the image directly into your retina using low-power lasers. Super intriguing and I was gonna use it, but 1. super expensive and hard to find. 2. Safety, you need hella precision to not wreck your eyes.
I also found a nice simulator that allows me to test different lenses and custom optics. To get this, I put together a quick prism and beam splitter.

https://phydemo.app/ray-optics/simulator/
<img width="566" alt="Screenshot 2025-05-25 at 10 27 39 PM" src="https://github.com/user-attachments/assets/e305404b-c046-46ca-82e4-b8c9de7e55bf" />


**Session time spent: 2h**

# MAY 31st: Optics and Electronics

So I forgot to log my previous 3 days, so I'm gonna  put a very long one here. I did some more simulating to try to visualize how the beam splitter will be positioned in front of my eyes to be in focus. For version 1, I plan to have a beam splitter cube perpendicular to the display on each side, as shown in the drawing below. To get the image to translate to the side a bit, I'll use a 45-degree mirror to reflect the incoming image towards the beam splitter, which then combines the light from outside and the image. Additionally, I started thinking about my image processing. In order to minimize the size of the glasses and increase power, I am going to sideload the processing to a phone that then transmits the image and data to a smaller processor on the glasses. I'm probably going to use a Raspberry Pi chip. I will also need to control the display, and controlling two micro OLEDs is not easy. I have 2 options, the safer one is using a dual display set used for VR goggles, and downsizing the PCB. The better cooler method is to fully make my own PCB for this. I'll need to use an HDMI bridge and an LVDS driver. Currently thinking of using the ADV7513 for HDMI encoding, TFP401A for HDMI to RGB, SN75LVDS83B	for RGB to LVDS, ECX334AF for the display (Sony display nice), VS23S010 for SPI video mem.

Image for optic placement:
![IMG_3280](https://github.com/user-attachments/assets/bfef72bd-345f-455f-a6eb-777c6332f06f)


**Session time spent: 8h**

# JUNE 1st: Optical Calculations & display considerations

So I worked more on the calculations for the lens I need to use to focus the display into my eye. Essentially, using the thin lens equation, I can see from what distances the focal length needed for the image to comfortably focus on my eye. I want to follow a similar design to the BirdBath lens system, which works like this (image below). The image goes down and away from the eye using a beam splitter, then is reflected back into the eye. My calculation for the focus lens gave me a 13.8mm focal length when the display is ~12mm away from the eye.
In order to keep this low cost and easy to code, and small, I'm going to be using 2 Y16A 0.2 VGA displays and a 5MP OV5693 AF camera for the ML.

Birdbath lens:
<img width="1137" alt="Screenshot 2025-06-02 at 10 57 34 PM" src="https://github.com/user-attachments/assets/63ea4ddf-44d8-4277-b187-0add3d887775" />

My focal length calculations:
![IMG_3285](https://github.com/user-attachments/assets/b2a1f4d8-a304-4253-bbe0-c6f6113ca08f)
![IMG_3284](https://github.com/user-attachments/assets/6c4954e8-edbc-4f8d-8755-5a182f0dcbcb)

Optics Sim for simplified lens system:
<img width="557" alt="Screenshot 2025-06-02 at 10 59 40 PM" src="https://github.com/user-attachments/assets/37ca5210-65b4-4a37-bd04-abc210b6db69" />

**Session time spent: 4h**

# JUNE 7th: Mainbaord

Started work on the main board that will control all this. I am taking a small pause from the optics to focus on how I'm going to control the displays and sensors. I am going to be using an Allwinner H618 MCU with 1 GB of DDR4, similar to the Orange Pi Zero 2 W. I'm currently designing my PCB for this and facing a few issues with signal timing. Ram needs very specific signal timing and track lengths in order to work, so it's gonna take a lot of manual routing for that. I'm first going to design the schematic for the main part, then integrate the display drivers, camera, and sensors I want for this first version. I also started thinking about the BoM and yeah ima a need the full 350 lol this stuff gets expensive so fast I hate it. In order to gather good data for the head position, I'm using an MPU9520, which is a 9-DOF gyro that's great for sensor fusion. I would go with a BNO500, but that's too expensive and not needed for this. 

Easy EDA MCU basic schematic:
<img width="704" alt="Screenshot 2025-06-07 at 5 05 34 PM" src="https://github.com/user-attachments/assets/a04e4be5-e596-4af2-ac76-eab7742071a0" />

**Session time spent: 8h**

# JUNE 8th: Mainboard and some rough CAD

Continued my work on the main board, with so many connections, and I have immense respect for people who do this for a living. I figured out what wireless chip to use, and I'm using the CDW-20U5622-00, which has Wi-Fi+BT. I'm also looking at different cameras since the current one I'm thinking of may be too big, and I need something small. I also worked on a small model for the glasses and how and what shape the mainboard is gonna be, and where it's mounting. It's gonna be at the top in front of my eyes and the displays under it. It's gonna be big, but hey, it's a start. Update from before I got the power chip connected in the schematic and most of the LPDDR4 connections.

Current Schematic:
<img width="629" alt="Screenshot 2025-06-08 at 11 24 08 PM" src="https://github.com/user-attachments/assets/d5373d1d-0313-41d3-b561-2f8e6725a92e" />

CAD of glasses and Board Position Version 1:
<img width="714" alt="Screenshot 2025-06-08 at 11 28 55 PM" src="https://github.com/user-attachments/assets/b76f4066-e343-4b74-9fa4-a14d31a08cdd" />

**Session time spent: 5h**

# JUNE 10th: Mainboard RAM

I finally finished the schematic for the RAM part. The harder part is later when it's time to route traces :(. I still need to work on the wireless chips and pads for IO and one USB-C port, for the AV displays, I'm just using the native TV out on the H618 chip, and then splitting it into two outs. The displays will show the same things, but that's fine for this prototype. Later on, I might implement an HDMI to AV chip so we can have two different displays. Going to work on some optics layout CAD now. Wish me luck.

Current Schematic:
<img width="623" alt="Screenshot 2025-06-10 at 9 40 05 PM" src="https://github.com/user-attachments/assets/cfd5adfe-8ff3-4e38-a9f2-005d01109cce" />

**Session time spent: 2h**

# JUNE 12th: Glass CAD

I started working on the CAD for the glasses using what I know will be used and the measurements I'm sure about. Turns out I need to use a polarizing beam splitter instead of a regular one due to how the light from an lcd is emitted. The polarized light will go into my eye, and then the unpolarized light from the sun will go in too, without degrading quality. I will also be using a 2s lipo for power and step it down to 5v so that it can power the displays and the mainboard without dying. I also did some optical simulations for how the light should theoretically travel. Also, did some research on how to figure out my lens system. To focus and magnify the image, I'll be using two lenses. Calculated using the thin lens equation and the angular magnification equation. For the magnification, I'll just use a Fresnel lens since it's small and thin. As an intermediary between lenses, I'll be using clear acrylic that will be polished with heat and sandpaper.
| Setup            | Lenses | Best For                            | Trade-Offs                              |
| ---------------- | ------ | ----------------------------------- | --------------------------------------- |
| Single lens      | 1      | Simplicity and small form factor    | Distortion & limited FOV                |
| Galilean system  | 2      | Compact with decent image placement | Narrower FOV & trickier optics          |
| Keplerian system | 2      | Best clarity and FOV                | Bigger & heavier & cleaere image formed |

| Material            | Refractive Index (n)  |
| ------------------- | --------------------- |
| Acrylic             | ~1.49                 |
| Glass               | ~1.52–1.54            |
| Optical Glass       | ~1.5168               |



Prototype Model #1:
![Screenshot 2025-06-12 at 1 16 24 AM](https://github.com/user-attachments/assets/28891fa9-70c4-4d1f-b296-b02b9a37f980)
![Screenshot 2025-06-12 at 1 16 40 AM](https://github.com/user-attachments/assets/a92a192f-efa8-4822-b036-b716a88348c2)

Optical Sim (Front View):
![Screenshot 2025-06-12 at 1 17 56 AM](https://github.com/user-attachments/assets/7e8c64c6-c331-481a-be06-26217e7821f0)

Optical Sim (Top View):
![Screenshot 2025-06-12 at 1 18 18 AM](https://github.com/user-attachments/assets/99b74de7-5ea2-4385-9ab9-749323f121ee)

**Session time spent: 6h**

# JUNE 13th: Version 1 is finally done!

I finally finished! I got the main board all routed and used the datasheet specifications to figure out my differential pair routing and length tuning. My CAD is also final, at least from what I can do right now, since the final measurements will come when I can get real-life measurements of the parts and test focal lengths. I dont have much to write for this since I spent all my time just working on the routing, and there isnt really much to say about that. It was challenging to get the layers in order and not have any conflicting paths, but I got there in the end. It looks very messy though :(. Oh also did a color sim for the optics.

Main Board:
<img width="622" alt="Screenshot 2025-06-13 at 7 20 20 PM" src="https://github.com/user-attachments/assets/ac41a733-495e-4154-bf05-285997981da4" />
<img width="544" alt="Screenshot 2025-06-13 at 7 10 16 PM" src="https://github.com/user-attachments/assets/cc22e23f-93c0-4b7a-a7ba-60c415722952" />
<img width="497" alt="Screenshot 2025-06-13 at 7 09 51 PM" src="https://github.com/user-attachments/assets/096f708b-ff3b-4546-837e-66c23d4f193d" />

ColorSim:
![Screenshot 2025-06-13 at 7 14 47 PM](https://github.com/user-attachments/assets/a8635c24-3d4c-49e7-b48d-491694bb5472)

**Session time spent: 5h**

# JUNE 13th: New optics design

I repositioned where the optics would be and found a small model of the display to use. The display will be on the temple side, and then use a mirror to reflect the image into the beam splitter. This would let me increase the size of the PCB on top and make things a little easier for me. For testing, I will just use the whole Orange Pi Zero 2W and then move the stuff to the new PCB.

New Optics mount:
<img width="425" alt="Screenshot 2025-06-14 at 9 45 32 PM" src="https://github.com/user-attachments/assets/e6fe9f93-693e-4e51-924c-03b7d8fe0989" />

**Session time spent: 1h**

# JUNE 17th: Starter Code for app and hardware

Worked on the code base for the glasses. The orange pi will handle all the onboard driving and handling in and outs of sensor data and camera, and displays, and then it uses websockets to wirelessly transmit data to my iPhone running an app using SwiftUI ui, where it will then do all the heavy processing there. Right now, I just have a basic code and apple Core ML model for object detection and classification, and then it sends the data back to the Orange Pi, where it displays it. I couldn't fully test since Apple SwiftUI preview doesn't support live image previews, and I also need the IP and network capabilities. But there were no build errors. For libraries, I'm using the Swift Vision and ARKit for handling the CoreML model and AR processing, I'm using AVFoundation for audio input for future proofing, and NWConnection for the TCP socket from Orange Pi to the iPhone. On the Python code, I'm using CV2 and smbus for the camera handling and I2C for the imu, and aiohttp for the websockets

**Session time spent: 7h**


