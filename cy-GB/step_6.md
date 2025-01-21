## Make it portable

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Bring your heart to life with an embedded LED heartbeat. You can power your Raspberry Pi Pico away from the computer with a USB power supply or battery pack. When you turn on the Pico it will run a file called `main.py`. 
</div>
<div>
![An image showing a red origami heart with a pulsing red LED inside the folds.](images/heart-static.png){:width="300px"}
</div>
</div>

### Automatically run your beating heart program using main.py

--- task ---

Use the **File** menu to save your code to your Raspberry Pi Pico device, using the **Save as...** option.

![The file menu in Thonny shown, with the Save As option highlighted.](images/file_menu.png)

--- /task ---

--- task ---

Choose to save your code to your Raspberry Pi Pico.

![Option to choose to save on the computer or on the Pico shown.](images/save_to_pico.png)

--- /task ---

--- task ---

Call your file `main.py` to have it automatically run when your Pico is powered from an external power supply, not connected to your computer.

![The Save menu option, with main.py chosen as a filename.](images/main.png)

--- /task ---

--- task ---

If it is saved as `main.py` on the Raspberry Pi Pico, then the program will load when the device is powered from an external power supply, such as a battery.

--- /task ---

### Power your beating heart using a USB supply

The Raspberry Pi Pico requires a power supply capable of delivering a minimum of 1.8V and a maximum of 5.5V.

Most micro USB transformers can provide power to your Raspberry Pi Pico in this range. For instance, the official Raspberry Pi micro USB transformer provides up to 2.5A of current at 5.1V.

![Official Raspberry Pi power supply shown from the pin side.](images/transformer.png)

A battery pack with a USB to micro USB cable can also power a Raspberry Pi Pico. This battery pack provides up to 2.1A of current at 5V.

![A generic battery pack showing the side and the technical specifications.](images/battery_pack.png)

--- task ---

Disconnect your Raspberry Pi Pico from your computer.

--- /task ---

--- task ---

Connect the Raspberry Pi Pico to your transformer or battery pack.

![A micro-USB being connected to the Raspberry Pi Pico.](images/connect-micro-usb.gif)

--- /task ---

--- task ---

**Test:** Turn on your USB power supply or battery.

You should be able to turn the potentiometer to adjust the speed of the heartbeat.

<video width="640" height="360" controls>
<source src="images/beating-heart.mp4" type="video/mp4">
Your browser does not support WebM video, try FireFox or Chrome
</video>

--- /task ---

--- task ---

**Difa chwilod:**

--- collapse ---
---
title: The LED does not light up
---

+ Is your battery working? Is the battery turned on? You could test another USB-powered device to make sure.

+ Did you save the file as `main.py`? Plug your Pico back into your computer and save the file again. Check the file name and the `.py` extension carefully.

--- /collapse ---

--- /task ---


