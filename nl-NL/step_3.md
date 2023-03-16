## Bereken slagen per minuut (BPM)

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
De potentiometerwaarden gaan van 0 naar 1. Om de potentiometer te gebruiken om de hartslag te regelen, moet je deze waarden veranderen in een overeenkomstig getal van 40 (zeer fitte atleet) tot 180 slagen per minuut. 
</div>
<div>
![een animatie van de plotter met BPM-waarden van 40 tot 180.](afbeeldingen/plotter-spm.gif){:width="300px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
BPM staat voor **slagen per minuut**. Je kunt BPM gebruiken om je hartslag (en het tempo van de muziek) te meten. Hoe hoger het getal, hoe sneller de hartslag. BPM wordt gebruikt in gezondheid en fitness om te meten hoe intens een oefening is. Je kunt je maximale hartslag berekenen door je leeftijd af te halen van het getal 220. Bijvoorbeeld, de maximale hartslag van een 12-jarige is 208. Bij het sporten wordt geadviseerd dat je hartslag niet hoger is dan 85% van je maximale hartslag. In het geval van een 12-jarige zou dit 176 BPM zijn. Dat is ongeveer hetzelfde tempo als een Drum 'n' Bass track.
</p>

Je gaat nu de potentiometer gebruiken om de hartslag van je project aan te passen. Je draait aan het instelwiel om de hartslag te verhogen of te verlagen.

--- task ---

Werk je code bij zodat de waarde die wordt afgedrukt en geplot overeenkomt met een hartslag tussen 40 en 180 slagen per minuut.

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

instelwiel = Pot(0)

hart_min = 40
hart_max = 180
hart_bereik = hart_max - hart_min # Bereken het verschil

while True:
    bpm = hart_min + instelwiel.value * hart_bereik # Zet de waarde van het instelwiel om in BPM
    print(bpm)
    sleep(0.1)

--- /code ---

Merk op dat de `hart_bereik` variabele **eenmaal** aan het begin van je script wordt berekend, maar de `bpm` variabele hangt af van de waarde van de potentiometer zodat deze wordt berekend binnen de `while` lus.

--- /task ---

--- task ---

**Test:** Voer je code uit en draai de potentiometer om te zien hoe het nummer in de shell en de labels in de Thonny-plotter veranderen. Je zou nu getallen tussen 40 en 180 moeten zien.

![Een schermafdruk van waarden die zijn uitgezet met een bereik van 0 tot 180.](images/plotter-bpm.png)

--- /task ---

--- task ---

**Fouten oplossen:**

Je hebt een syntaxisfout:
+ Controleer of de code overeenkomt met het bovenstaande voorbeeld

De potentiometer is gestopt met werken:
+ Controleer of de jumperkabels nog steeds goed vastzitten

--- /task ---


