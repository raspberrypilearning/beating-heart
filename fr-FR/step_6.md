## Rends-le portable

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Donne vie à ton cœur avec une LED battement de cœur intégré. Tu peux alimenter ton Raspberry Pi Pico loin de l'ordinateur avec une alimentation USB ou une batterie. Lorsque tu allumes le Pico, il exécute un fichier appelé "main.py". 
</div>
<div>
![Une image montrant un cœur en origami rouge avec une LED rouge clignotante à l'intérieur des plis.](images/heart-static.png){:width="300px"}
</div>
</div>

### Exécute automatiquement ton programme de cœur battant à l'aide de main.py

--- task ---

Utilise le menu **Fichier** pour enregistrer ton code sur ton appareil Raspberry Pi Pico, en utilisant l'option **Enregistrer sous...**.

![Le menu Fichier dans Thonny affiché, avec l'option Enregistrer sous en surbrillance.](images/file_menu.png)

--- /task ---

--- task ---

Choisis d'enregistrer ton code sur ton Raspberry Pi Pico.

![Possibilité de choisir d'enregistrer sur l'ordinateur ou sur le Pico affiché.](images/save_to_pico.png)

--- /task ---

--- task ---

Appel ton fichier `main.py` pour qu'il s'exécute automatiquement lorsque ton Pico est alimenté par une alimentation externe, non connectée à ton ordinateur.

![L'option de menu Enregistrer, avec main.py choisi comme nom de fichier.](images/main.png)

--- /task ---

--- task ---

S'il est enregistré sous `main.py` sur le Raspberry Pi Pico, le programme se chargera lorsque l'appareil est alimenté par une alimentation externe, telle qu'une batterie.

--- /task ---

### Alimente ton cœur battant à l'aide d'une alimentation USB

Le Raspberry Pi Pico nécessite une alimentation capable de délivrer un minimum de 1,8V et un maximum de 5,5V.

La plupart des transformateurs micro USB peuvent alimenter ton Raspberry Pi Pico dans cette gamme. Par exemple, le transformateur micro USB officiel Raspberry Pi fournit jusqu'à 2,5 A de courant à 5,1 V.

![Alimentation électrique Raspberry Pi officielle illustrée du côté de la fiche.](images/transformer.png)

Une batterie avec un câble USB vers micro USB peut également alimenter un Raspberry Pi Pico. Cette batterie fournit jusqu'à 2,1 A de courant à 5 V.

![Une batterie générique montrant le côté et les spécifications techniques.](images/battery_pack.png)

--- task ---

Déconnecte ton Raspberry Pi Pico de ton ordinateur.

--- /task ---

--- task ---

Connecte le Raspberry Pi Pico à ton transformateur ou à ta batterie.

![Un micro-USB étant connecté au Raspberry Pi Pico.](images/connect-micro-usb.gif)

--- /task ---

--- task ---

**Test :** Allume ton alimentation USB ou ta batterie.

Tu devrais pouvoir tourner le potentiomètre pour régler la vitesse du rythme cardiaque.

<video width="640" height="360" controls>
<source src="images/beating-heart.mp4" type="video/mp4">
Ton navigateur ne prend pas en charge la vidéo WebM, essaye FireFox ou Chrome
</video>

--- /task ---

--- task ---

**Déboguer:**

--- collapse ---
---
title: La LED ne s'allume pas
---

+ Ta batterie fonctionne-t-elle ? La batterie est-elle allumée ? Tu peux tester un autre appareil alimenté par USB pour t'en assurer.

+ As-tu enregistré le fichier sous `main.py`? Rebranche ton Pico sur ton ordinateur et enregistre à nouveau le fichier. Vérifie attentivement le nom du fichier et l'extension `.py`.

--- /collapse ---

--- /task ---


