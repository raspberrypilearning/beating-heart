## Du kommer göra

Ett Raspberry Pi Pico-projekt för att göra ett hjärta i papper som slår, med en pulserande lysdiod och en ratt för att justera pulsen.

--- no-print ---

![En animerad bild som visar ett rött origamihjärta med en pulserande röd lysdiod inuti.](images/heartbeat.gif){:width="400px"}

--- /no-print ---

--- print-only ---

![En bild som visar ett rött origamihjärta med en pulserande röd lysdiod inuti.](images/heart-static.png)

--- /print-only ---

[[[flashing-light-warning]]]

Du kommer att:
+ Använd en potentiometer (ratt) för att ändra hjärtfrekvensen
+ Skapa en pulserande effekt med en lysdiod
+ Driva din Raspberry Pi Pico utan dator

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
En <span style="color: #0faeb0">analog ingång</span> ger ett intervall av värden, snarare än bara en 0 eller 1 (på eller av). En <span style="color: #0faeb0">potentiometer</span> är en analog ingångskomponent som har en ratt som du vrider på för att öka eller minska värden. Raspberry Pi Pico har analoga ingångsstift som låter dig läsa analoga värden och använda dem i din kod. 
</p>

För att slutföra detta projekt behöver du:

**Hårdvara**

Du kan köpa all nödvändig hårdvara för det här projektet och de andra projekten på den här vägen från t.ex. [Pimoroni webbutik.](https://shop.pimoroni.com/products/pico-intro-kit?variant=39893512945747){:target='_blank'} och [Kitronik webbutik.](https://kitronik.co.uk/products/5343-raspberry-pi-foundation-pico-pathway-pack){:target='_blank'}

+ En Raspberry Pi Pico med pålödda stift
+ En data USB A till mikro USB-kabel
+ En röd lysdiod med ett motstånd anslutet till bygelkablar med uttagskontakter
+ En potentiometer (ratt)
+ 3 x uttag-uttag byglingskablar
+ Ett pappersark, rött om du har det
+ Tejp
+ Som tillval, en blå lysdiod, motstånd och fler bygelkablar

[[[pin-socket-jumper-wires]]]

**Programvara**

+ Thonny – detta projekt kan slutföras med Thonny Python-redigeraren, som kan installeras på en Linux-, Windows- eller Mac-dator

[[[thonny-install]]]

[[[change-theme-thonny]]]

--- no-print ---

--- task ---

Titta på videon av hjärtslag som styrs av en potentiometer. Vad händer när ratten vrids åt vänster och höger?

<video width="640" height="360" controls>
<source src="images/beating-heart.mp4" type="video/mp4">
Din webbläsare stöder inte WebM-video, prova FireFox eller Chrome
</video>

--- /task ---

--- /no-print ---
