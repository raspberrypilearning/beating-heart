from picozero import LED, Pot
from time import sleep

led = LED(13)
instelwiel = Pot(0)

hart_min = 40
hart_max = 180
hart_bereik = hart_max - hart_min
            
while True: 
    bpm = hart_min + instelwiel.value * hart_bereik
    print(bpm)
    slagen = 60/bpm
    helder_tijd = slagen / 2 # Geef een halve beat door die helderder wordt
    dimmer_tijd = slagen / 2 # Geef een halve beat door om donkerder te worden

    led.pulse(helder_tijd, dimmer_tijd, n=1, wait=True)  # Pulseer 1 keer, wacht tot je klaar bent   
