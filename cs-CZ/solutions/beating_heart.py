from picozero import LED, Pot
from time import sleep

led = LED(13)
dial = Pot(0)

heart_min = 40
heart_max = 180
heart_range = heart_max - heart_min
            
while True: 
    bpm = heart_min + dial.value * heart_range
    print(bpm)
    beat = 60/bpm
    brighter_time = beat / 2 # Spend half a beat getting brighter
    dimmer_time = beat / 2 # Spend half a beat getting dimmer

    led.pulse(brighter_time, dimmer_time, n=1, wait=True)  # pulse 1 time, waiting until finished   
