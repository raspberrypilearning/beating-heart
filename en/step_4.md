## LED heart beat

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Add an introductory sentence. What will learners achieve by the end of this step?
</div>
<div>
Image, gif or video showing what they will achieve by the end of the step. ![](images/image.png){:width="300px"}
</div>
</div>

<mark>Add warning about flashing lights. Reduce max if this could be an issue. Mention that this is an importand design consideration. Only flash the LED if the rate is below a certain value?</mark>

--- task ---

Find a **red** LED connected to a resistor and jumper wires. 

You can make your own if you need to.

<mark>ingredients</mark>

--- /task ---

--- task ---

Add code so that you can program your LED:

--- code ---
---
language: python
filename: 
line_numbers: true
line_number_start: 1
line_highlights: 1, 5
---
from picozero import Pot, LED # Add LED
from time import sleep

dial = Pot(0)
led = LED(13) # Make sure this is the correct pin

--- /code ---

--- /task ---

--- task ---

Add code to your `while` loop so that the LED blinks on and off based on the heart rate:

--- code ---
---
language: python
filename: 
line_numbers: true
line_number_start: 7
line_highlights: 10-14
---

while True:
    bpm = min_heart_rate + dial.value * heart_range
    print(bpm)
    beat = 60 / bpm
    led.on()
    sleep(beat / 2)
    led.off()
    sleep(beat / 2)

--- /code ---

--- /task ---

--- task ---
**Test:** Run your code to see the LED blink on and off. Turn the potentiometer to it's lowest value to represent a very slow heart rate and see how the LED blinks. Gradually increase the heart rate by turning the potentiometer to see the LED blink faster. 

<mark>Blink warning</mark>

--- /task ---

--- save ---

