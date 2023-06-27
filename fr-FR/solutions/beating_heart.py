from picozero import LED, Pot
from time import sleep

led = LED(13)
cadran = Pot(0)

coeur_min = 40
coeur_max = 180
coeur_gamme = coeur_max - coeur_min
            
while True: 
    bpm = coeur_min + cadran.value * coeur_gamme
    print(bpm)
    rythme = 60/bpm
    temps_brillant = rythme / 2 # Passe un demi-temps à devenir plus brillant
    temps_sombre = rythme / 2 # Passe un demi-temps à devenir plus faible

    led.pulse(temps_brillant, temps_sombre, n=1, wait=True)  # Impulsion 1 fois, attendre jusqu'à la fin  
