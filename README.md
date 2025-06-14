# ARPIGlasses

**Description:**
ArpiGlasses is my take on a pair of affordable and sleek smart AR glasses. Featuring 2 0.2" flcos displays, a custom mainboard with a 9axis imu and camera and the ability to wirelessly sideload processing to another device. These glasses while currently not small will hopefully be improved over time and become more practical. This will be able to display over lays on the realworld like a hologram offering many possibilities. Like nutrition monitoring through the camera and ML or build plans etc the list goes on. Mainboard is powered by an AWH618 and 4GB of LPDDR4 RAM.

**Why:**
I made this beacuse I wanted to push myself into leanring about new things especially optics. Through countless calculations and simulating lenses and beam splitter I was able to figure out what I need to get an image to focus into my eye at a super short distance. And Now I just need to test it irl. I also wanted to test my pcb skills and make a super tiny mcu. I have big ones before but when you scale down it gets really hard. And also glasses with displays in them are just super cool and with the ability to do whatever I want with them with my own electronics and software.

CAD:

![Screenshot 2025-06-13 at 7 13 52 PM](https://github.com/user-attachments/assets/fc58f8f2-bcb0-4f0d-b6d2-7d7ca5b731cd)
![Screenshot 2025-06-13 at 7 13 37 PM](https://github.com/user-attachments/assets/cab84248-3f02-4494-96e8-c4291fa2785e)

MainBoard (its ugly I know):

<img width="544" alt="Screenshot 2025-06-13 at 7 10 16 PM" src="https://github.com/user-attachments/assets/2a859685-62e6-40df-867c-217c61df1535" />
<img width="497" alt="Screenshot 2025-06-13 at 7 09 51 PM" src="https://github.com/user-attachments/assets/78121033-06c5-4d4e-8096-377a4727a8ea" />

Optical Sim: 

![Screenshot 2025-06-13 at 7 14 47 PM](https://github.com/user-attachments/assets/5d442107-ea4b-4510-a704-6c0d2aa82215)

BOM:
| Part                          | QTY | Total Price |
|------------------------------|-----:|-------------:|
| Semi Transperent Mirror       | 2   | 12.44        |
| 7v to 5v Buck Converter       | 1   | 2.29         |
| 2S lipo charger module        | 1   | 4.19         |
| LPDDR4 BGA Stencil            | 1   | 4.66         |
| Orange Pi Zero 2 W            | 1   | 24           |
| LPDDR4 BGA Chip (4GB)         | 1   | 4            |
| LOCA (Optical Clear Glue)     | 1   | 9            |
| 3.7v 300mah LIPO              | 2   | 7            |
| Polarizing Beam Splitter Cube | 2   | 24           |
| MPU 9250                      | 1   | 5            |
| OV5640 AF Camera module       | 1   | 15           |
| USBC Data Cable               | 1   | 1.39         |
| 0.2" FLCOS Display            | 2   | 102.3        |
| Soldering Misc. (Paste, etc.) | 1   | 40.23        |
| Shipping                      | 1   | 35.41        |
| PCB + Stencil                 | 1   | 60           |
|                               |     |              |
|                               |     | TOTAL COST:   |
|                               |     | 350.91        |
