## Ce que tu vas faire

Fabriquer un cœur battant en papier avec une LED pulsante et un cadran pour régler la fréquence cardiaque.

--- no-print ---

![Une image animée montrant un cœur en origami rouge avec une LED rouge clignotante à l'intérieur des plis.](images/heartbeat.gif){:width="400px"}

---/no-print ---

--- print-only ---

![Une image montrant un cœur en origami rouge avec une LED rouge clignotante à l'intérieur des plis.](images/heart-static.png)

--- /print-only ---

[[[flashing-light-warning]]]

Tu vas devoir :
+ Utiliser un potentiomètre (cadran) pour modifier la fréquence cardiaque
+ Créer un effet de pulsation avec une LED
+ Alimenter ton Raspberry Pi Pico loin de ton ordinateur

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Une <span style="color: #0faeb0">entrée analogique</span> donne plage de valeurs, plutôt qu'un simple 0 ou 1 (on ou off). Un <span style="color: #0faeb0">potentiomètre </span> est un composant d'entrée analogique qui a un cadran que tu tournes pour augmenter ou diminuer les valeurs. Le Raspberry Pi Pico possède des broches d'entrée analogiques qui te permettent de lire des valeurs analogiques et de les utiliser dans ton code. 
</p>

Pour mener à bien ce projet, tu auras besoin de :

**Matériel**

Tu peux acheter tout le matériel requis pour ce projet et les autres projets du parcours à partir de la [boutique en ligne Pimoroni](https://shop.pimoroni.com/products/pico-intro-kit?variant=39893512945747){:target='_blank'} et [boutique en ligne Kitronik](https://kitronik.co.uk/products/5343-raspberry-pi-foundation-pico-pathway-pack){:target='_blank'}

+ Un Raspberry Pi Pico avec des broches soudées dessus
+ Un câble de données USB A vers micro USB
+ Une LED rouge avec une résistance attachée aux fils de connexion avec des connecteurs prises
+ Un potentiomètre (cadran)
+ 3 x fils de liaison prise-prise
+ Une feuille de papier, rouge si tu en as une
+ Du ruban adhésif ou du ruban adhésif de toile (duct tape)
+ En option, une LED bleue, une résistance et plus de fils de liaison

[[[pin-socket-jumper-wires]]]

**Logiciel**

+ Thonny : ce projet peut être réalisé à l'aide de l'éditeur Thonny Python, qui peut être installé sur un ordinateur Linux, Windows ou Mac

[[[thonny-install]]]

[[[change-theme-thonny]]]

--- no-print ---

--- task ---

Regarde la vidéo du rythme cardiaque contrôlé par un potentiomètre. Que se passe-t-il lorsque le cadran est tourné à gauche et à droite ?

<video width="640" height="360" controls>
<source src="images/beating-heart.mp4" type="video/mp4">
Ton navigateur ne prend pas en charge la vidéo WebM, essaye FireFox ou Chrome
</video>

--- /task ---

--- /no-print ---
