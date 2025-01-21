## डायल से मान पढ़ें

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
एक potentiometer (डायल) आपको मानों की एक श्रेणी प्रदान करने की अनुमति देता है। Thonny plotter आपको उन मूल्यों को प्रदर्शित करने की अनुमति देता है ताकि आप डायल को मोड़ने का प्रभाव देख सकें।
</div>
<div>
![Thoneny में चलने वाले plotter का एक एनीमेशन।](images/thony-plotter.gif){:width="300px"}
</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Raspberry Pi Pico में तीन <span style="color: #0feb0">एनालॉग इनपुट पिन</span> हैं जिनका उपयोग एनालॉग इनपुट घटकों जैसे एक potentometer से मानों को पढ़ने के लिए किया जा सकता है। इन पिन को A0, A1, और A2 के रूप में लेबल किया गया है। Raspberry Pi Pico इन पिन का उपयोग करके वोल्टएज को 0 से 3.3V तक पढ़ सकता है।</p>

--- task ---

अपने potentiometer को देखें। ऊपर दिए गए डायल पर ध्यान दें जो आपको इसे घड़ी की दिशा में और घड़ी की उल्टी दिशा में करने की अनुमति देता है।

आप यह भी ध्यान देंगे कि आपके potiometer में **तीन** पिन हैं।

इस आरेख के समान ही अपने potentometer को पकड़ें:

![डायल को घड़ी की दिशा में घुमाया जा रहा है और तीन लेग्स: GND, A, और 3V3 दिखाता हुआ एक पोटेंशियल का चित्रण।](images/potentiometer-illustration.png){:width="300px"}

जब potiometer को बाईं ओर मोड़ दिया जाता है, तो तीर GND पिन को इंगित करता है; जब इसे दाईं ओर मोड़ दिया जाता है, तो तीर 3V3 पिन को इंगित करता है। मध्य पिन वह पिन है जिससे Raspberry Pi Pico एक मूल्य पढ़ता है।

--- /task ---

सुनिश्चित करें कि आपका Raspberry Pi Pico आपके कंप्यूटर से **unpixed** है।

--- task ---

तीन सॉकेट-सॉकेट जम्पर तारों का उपयोग करें और एक को संभाव्यमापी के प्रत्येक पैर से जोड़ें। आप पैरों को कुछ विद्युत टेप से सुरक्षित करना चाह सकते हैं यदि वे ढीली महसूस करते हैं।

**Connect** प्रत्येक jumper तार का दूसरा सिरा Raspberry Pi Pico:
+ **GP21** और **GP22** के बीच छोटे '1' लेबल वाली पिन को **GND** से कनेक्ट करें
+ बीच की पिन को **GP26_A0** पिन से कनेक्ट करें
+ छोटे '3' के साथ लेबल किए गए पिन को **3V3** पिन से कनेक्ट करें

![एक aspberry Pi Pico से जुड़े एक potentometer का एक आरेख जो जीडबल्यूडी, जीपी26_A0, और 3V3 पिन का उपयोग करता है।](images/pot-diagram.png)

--- /task ---

--- collapse ---

---
title: एक potentiometer कैसे काम करता है?
---

एक **potentiometer** एक एनालॉग इनपुट घटक है जो डायल की स्थिति के आधार पर अपने प्रतिरोध को बदल देता है। एक pinotiometer में तीन पिन होते हैं जिन्हें 3V3, एक एनालॉग पिन, और GND से कनेक्ट करने की आवश्यकता होती है। 3V3 पिन (3V3 pin) potentiometer को शक्ति प्रदान करता है और एनालॉग पिन से वोल्टेज रीडिंग potentiometer के प्रतिरोध के आधार पर बदल जाएगी।

--- /collapse ---

--- task ---

अपने Raspberry Pi Pico को अपने कंप्यूटर में प्लग करें।

Thonny में, एक नई फ़ाइल बनाएं और potentometer से मान `print` में निम्नलिखित कोड जोड़ें।

--- code ---
---
language: python filename: line_numbers: true line_number_start: 1
line_highlights:
---
from picozero import Pot # Pot is short for Potentiometer from time import sleep

dial = Pot(0) # Connected to pin A0 (GP26)

while True: print(dial.value) sleep(0.1) # Slow down the output

--- /code ---

`स्लीप(0.1)` लाइन, potentiometer से मूल्यों के पठन और मुद्रण को धीमा कर देती है ताकि Thonny आउटपुट के साथ बने रह सके।

--- /task ---

--- task ---

**परीक्षण:** अपनी स्क्रिप्ट चलाएँ और Thonny को शैल के लिए मानों को प्रिंट करना शुरू कर देना चाहिए। मान परिवर्तन देखने के लिए potentometer घुमाएँ।

![Thony Shell में 0 और 1 के बीच संख्याओं का स्क्रीनशॉट।](images/potentiometer-shell.png)

--- /task ---

जब मान इतनी तेज़ी से मुद्रित हो रहे हों, तो क्या हो रहा है यह देखना बहुत कठिन है। Thoneny में एक plotter है जिसका उपयोग आप इसके बजाय potentometer से मानों को देखने के लिए कर सकते हैं।

--- task ---

Thoneny में, **view**-&#062 चुनें;**Pltter** और plotter खोल के आगे दिखाई देंगे।

--- /task ---

--- task ---

**test:** अपनी स्क्रिप्ट चलाएं और potiometer को घुमाएं। plotter में मूल्य परिवर्तन देखें।

--- print-only ---

![0 से 1 तक के पैमाने पर प्लॉट किए गए मानों का स्क्रीनशॉट।](images/thonny-plotter.png)

--- /print-only ---

--- no-print ---

![Thoneny में चलने वाले plotter का एक एनीमेशन।](images/thonny-plotter.gif){:width="300px"}

--- /no-print ---

मान 0 होना चाहिए (या 0 के करीब) जब potentometer बाएं और 1 (या 1 के करीब) की तरफ मोड़ दिया जाता है जब यह दाएं के सभी रास्ते में बदल जाता है।

--- /task ---

--- task ---

**डीबग:**

मान गलत तरीके हैं।
+ **GND** और **3V3** से जुड़े जम्पर तारों को स्वैप करें।

--- /task ---

