## Calculate beats per minute (BPM) 

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
The potentiometer values go from 0 to 1. To use the potentiometer to control the heart rate you need to turn these values into a corresponding number from 40 (very fit athlete) to 180 beats per minute. 
</div>
<div>
![An animation of the plotter showing BPM values from 40 to 180.](images/plotter-bpm.gif){:width="300px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
BPM stands for **beats per minute**. We can use BPM to measure our heart rate (as well as the tempo of music). The higher the number, the faster the heartrate. BPM is used in health and fitness to measure how intense an exercise is. You can work out your maximum heartrate by taking away your age from 220. For example, a 12 year old's maximum heart rate is 208. When exercising, it is advised that your heartrate doesn't exceed 85% of your maximum heart rate. In the case of a 12 year old, this would be 176 bpm! (About the same tempo as a Drum n' Bass track.)
</p>

You are now going to use the potentiometer to adjust the heartbeat of your project. You will turn the dial to increase or decrease the heart beat. 

--- task ---

Update your code so that the value that is printed and plotted corresponds to a heart rate between 40 and 180 beats per minute.

--- code ---
---
language: python
filename: 
line_numbers: true
line_number_start: 1
line_highlights: 6-13
---
from picozero import Pot
from time import sleep

dial = Pot(0)

heart_min = 40
heart_max = 180
heart_range = heart_max - heart_min # calculate the difference

while True:
    bpm = heart_min + dial.value * heart_range # convert dial value to bpm
    print(bpm)
    sleep(0.1)

--- /code ---

Notice that the `heart_range` variable is calculated **once** at the beginning of your script, but the `bpm` variable depends on the value of the potentiometer so it gets calculated inside the `while` loop.

--- /task ---

--- task ---

**Test:** Run your code and turn the potentiometer and see how the number in the Shell and the labels in the Thonny plotter change. You should now see numbers between 40 and 180.

![A screenshot of values plotted with a range from 0 to 180.](images/plotter-bpm.png) 

--- /task ---

--- task ---

**Debug:** 

You have a syntax error:
+ Check that you code matches the example above

The potentiometer stopped working:
+ Check that your jumper wires are still securely attached

--- /task ---


--- save ---
