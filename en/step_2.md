## Read values from a dial

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
A potentiometer (dial) allows you to provide a range of values. The Thonny plotter allows you to display those values so you can see the effect of turning the dial.
</div>
<div>
![An animation of the plotter running in Thonny.](images/thonny-plotter.gif) {:width="300px"}
</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
The Raspberry Pi Pico has three <span style="color: #0faeb0">analog input pins</span> that can be used to read values from analogue input components such as a potentiometer. These pins are labelled as A0, A1 and A2. The Raspberry Pi Pico can read voltages from 0 to 3.3V using these pins.</p>

--- task ---

**Look**: Look at your potentiometer. Notice the dial on the top that allows you to turn it clockwise and anti clockwise.

You will also notice that your potentiometer has **three** pins. 

Hold your potentiometer the same way around as in this image: 

![A blue potentiometer with a small dial on the top and three pins on the bottom.](images/potentiometer.jpg)

When the potentiometer is turned all the way to the left the arrow points to the GND pin, when it is turned all the way to the right, the arrow points to the 3V pin. The middle pin is the pin that the Raspberry Pi Pico reads a value from. 

![An illustration of a potentiometer.](images/illustration-pot.jpg) <mark>to make</mark>

--- /task ---

--- task ---

Make sure your Raspberry Pi Pico is unplugged from your computer. 

**Connect:** Find three socket-socket jumper wires and attach one to each leg of the potentiometer. You may wish to secure the legs with some electrical tape if they feel loose. 

Connect the other end of each jumper to the Raspberry Pi Pico:
+ Connect the labelled with a small 1 to the GND pin between GP 20 and GP 21.
+ Connect the middle pin the GP26_A0.
+ Connect pin labelled with a small 3 to the 3V3 pin.

![A diagram of a potentiometer connected to a Raspberry Pi Pico using the GND, GP26_A0 and 3V3 pin.](images/pot-diagram.png) <mark> to do </mark>

--- /task ---

--- collapse ---

---
title: How does a potentiometer work?
---

A **potentiometer** is an analogue input component that changes its resistance depending on the position of the dial. A potentiometer has three pins that need to be connected to 3V3, an analogue pin and GND. The 3V3 pin provides power to the potentiometer and the voltage reading from the analogue pin will change depending on the resistance of the potentiometer. 

--- /collapse ---

--- task ---

Plug your Raspberry Pi Pico into your computer. 

In Thonny, create a new file and add the following code to `print` the value from the potentiometer. 

--- code ---
---
language: python
filename: 
line_numbers: true
line_number_start: 1
line_highlights: 
---
from time import sleep
from picozero import Pot

dial = Pot(0)

while True:
    print(dial.value)
    sleep(0.1) # slow down the output

--- /code ---

The `sleep(0.1)` line slows down the reading and printing of values from the potentiometer so that Thonny can keep up with the output. 

--- /task ---

--- task ---

**Test:** Run your script and Thonny should start printing values to the Shell. Turn the potentiometer to see the value change. 

![A screenshot of numbers between 0 and 1 in the Thonny Shell.](images/potentiometer-shell.png) 

--- /task ---

It's quite hard to see what's happening when the values are quickly printing. Thonny has a plotter that you can use to visualise the values from the potentiometer. 

--- task ---

In Thonny, choose 'View->Plotter' and the plotter will appear next to the Shell.

--- /task ---

--- task ---

**Test:** Turn the potentiometer and watch the value change in the Plotter. 

![A screenshot of the plotter running in Thonny.](images/thonny-plotter.png) 

The value should be 0 (or close to 0) when the potentiometer is turned all the way to the left and 1 (or close to 1) when it is turned all the way to the right.

**Debug:**

The values are the wrong way around.
+ Swap the jumper wires connected to GND and 3V3 and the values will go from 0 to 1. 

--- /task ---

--- save ---
