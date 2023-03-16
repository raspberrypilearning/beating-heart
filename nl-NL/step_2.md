## Lees waarden van een instelwiel

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Met een potentiometer (instelwiel) kun je een reeks waarden opgeven. Met de Thonny-plotter kun je deze waarden weergeven, zodat je het effect kunt zien van het draaien van het instelwiel.
</div>
<div>
![een animatie van de plotter die draait in Thonny.](images/thonny-plotter.gif){:width="300px"}
</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
De Raspberry Pi Pico heeft drie <span style="color: #0faeb0">analoge invoerpinnen</span> die kunnen worden gebruikt om waarden uit analoge ingangscomponenten zoals een potentiometer te lezen. Deze pinnen zijn gelabeld als A0, A1 en A2. De Raspberry Pi Pico kan spanningen van 0 tot 3,3 V lezen met behulp van deze pinnen.</p>

--- task ---

Kijk naar je potentiometer. Let op de knop aan de bovenkant waarmee je hem rechtsom en linksom kunt draaien.

Je zult ook zien dat je potentiometer **drie** pinnen heeft.

Houd de potentiometer op dezelfde manier vast als in dit diagram:

![Een afbeelding van een potentiometer die de wijzerplaat met de klok mee draait en de drie poten: GND, A en 3V3.](images/potentiometer-illustration.png){:width="300px"}

Wanneer de potentiometer helemaal naar links wordt gedraaid, wijst de pijl naar de GND-pin; wanneer deze helemaal naar rechts wordt gedraaid, wijst de pijl naar de 3V3-pin. De middelste pin is de pin waaruit de Raspberry Pi Pico een waarde leest.

--- /task ---

Zorg ervoor dat de Raspberry Pi Pico **losgekoppeld** van de computer is.

--- task ---

Gebruik drie jumperdraden met stekkerbus en sluit er een aan op elke poot van de potentiometer. Je kunt de benen met wat isolatietape vastzetten als ze los voelen.

**Sluit** het andere uiteinde van elke jumperdraad aan op de Raspberry Pi Pico:
+ Verbind de pin met een kleine '1' met de **GND** pin tussen **GP21** en **GP22**
+ Verbind de middelste pin met de **GP26_A0** pin
+ Verbind de pin met een kleine '3' met de **3V3** pin

![Een diagram van een potentiometer die is aangesloten op een Raspberry Pi Pico met behulp van de GND, GP26_A0 en 3V3 pen.](images/pot-diagram.png)

--- /task ---

--- collapse ---

---
title: Hoe werkt een potentiometer?
---

Een **potentiometer** is een analoog ingangsonderdeel dat zijn weerstand verandert afhankelijk van de positie van het instelwiel. Een potentiometer heeft drie pinnen die moeten worden aangesloten op 3V3, een analoge pin en GND. De pin 3V3 levert voeding aan de potentiometer en de spanningswaarde van de analoge pin zal veranderen afhankelijk van de weerstand van de potentiometer.

--- /collapse ---

--- task ---

Sluit je Raspberry Pi Pico aan op je computer.

Maak in Thonny een nieuw bestand en voeg de volgende code toe aan `print` de waarde van de potentiometer.

--- code ---
---
language: python
filename: 
line_numbers: true
line_number_start: 1
line_highlights: 
---
from picozero import Pot # Pot is een afkorting voor Potentiometer
from time import sleep

instelwiel = Pot(0) # Aangesloten op pin A0 (GP26)

while True:
    print(instelwiel.value)
    sleep(0.1) # Vertraag de uitvoer

--- /code ---

De regel `sleep(0.1)` vertraagt de aflezing en het afdrukken van waarden van de potentiometer zodat Thonny de uitvoer kan bijhouden.

--- /task ---

--- task ---

**Test:** Voer je script uit en Thonny moet beginnen met het afdrukken van waarden naar de shell. Draai aan de potentiometer om de waardeverandering te zien.

![Een schermafdruk van getallen tussen 0 en 1 in de Thonny Shell.](images/potentiometer-shell.png)

--- /task ---

Het is vrij moeilijk om te zien wat er gebeurt als de waarden zo snel worden afgedrukt. Thonny heeft een plotter die je kunt gebruiken om de waarden van de potentiometer te visualiseren.

--- task ---

Kies in Thonny **view**->**plotter** en de plotter verschijnt naast de shell.

--- /task ---

--- task ---

**Test:** Voer je script uit en draai de potentiometer. Let op de waardeverandering in de plotter.

--- print-only ---

![Een schermafdruk van waarden die zijn geplot op een schaal van 0 tot 1.](images/thonny-plotter.png)

--- /print-only ---

--- no-print ---

![Een animatie van de plotter die in Thonny draait.](images/thonny-plotter.gif){:width="300px"}

--- /no-print ---

De waarde moet 0 (of dicht bij 0) zijn wanneer de potentiometer helemaal naar links wordt gedraaid en 1 (of dicht bij 1) wanneer deze helemaal naar rechts wordt gedraaid.

--- /task ---

--- task ---

**Fouten oplossen:**

De waarden zijn omgedraaid.
+ Verwissel de startdraden die zijn aangesloten op **GND** en **3V3**.

--- /task ---

