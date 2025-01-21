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
    brighter_time = beat / 2 # Låt det ta ett halvt slag att bli ljusare
    dimmer_time = beat / 2 # Låt det ta ett halvt slag att bli mörkare

    led.pulse(brighter_time, dimmer_time, n=1, wait=True)  # Pulsera 1 gång, väntar tills det är klart
