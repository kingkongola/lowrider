# Decisions

Endast beslut som påverkar detta LowRider-bygge.

## D001 — LowRider V4
**Status:** beslutat / delar köpta

Bygg LowRider V4. Maskinvalet är avslutat. PrintNC och IndyMill är inte längre aktiva alternativ för detta bygge.

## D002 — Arbetsyta omkring 650 × 1250 mm
**Status:** preliminärt beslutat

Målet är att rymma ungefär en kvarts 1220 × 2440-skiva med praktisk marginal. Exakt slutmått ska verifieras i aktuell LR4-kalkylator innan storleksberoende material kapas eller beställs.

## D003 — Standardnära bygge först
**Status:** beslutat

Bygg maskinen korrekt och få den körklar innan eventuella modifieringar. Uppgradera först när en faktisk begränsning har visat sig.

## D004 — Bordet ska dimensioneras efter slutlig LR4-geometri
**Status:** beslutat

Yttermått, sarg och frigång bestäms först när slutlig arbetsyta och maskinens exakta footprint är verifierade. Bordet ska samtidigt planeras för god dammhantering och praktisk användning i ett garage där motorarbete också sker.

## D005 — Jackpot3 som styrkort
**Status:** beslutat förstahandsval

Jackpot3 väljs framför SKR Pro och äldre Jackpot-versioner om prisskillnaden inte är orimlig.

Skäl:
- V1E säljer Jackpot3 som aktuell standardlösning och den är förkonfigurerad för LowRider V4.
- 6 integrerade TMC2226-drivare, alltså inga separata stepper-drivers att köpa eller montera.
- FluidNC, Wi‑Fi och webbgränssnitt direkt på kortet.
- 7 ingångar och 4 valbara 5 V / linjenivå-utgångar.
- full PWM på 5 V-utgångarna; detta lämnar möjlighet till laser senare.
- USB‑C och integrerad RJ11/pendant-anslutning.

## D006 — VEVOR 0700C, 800 W, 65 mm som fräsmotor
**Status:** beslutat förstahandsval

Målmodell: **VEVOR 0700C, 800 W, 220–240 V / 50 Hz, 65 mm kropp, 10 000–30 000 rpm**.

Detta ersätter den tidigare 710 W VV-1B-220V-kandidaten.

Skäl:
- modellen heter uttryckligen **0700C** och VEVOR anger kompatibilitet med Makita 0700-bas.
- 65 mm kropp passar LR4:s Makita-format.
- VEVOR anger 6,35 mm och 8 mm spännhylsor som standard.
- en dokumenterad V1E-användare kör en **VEVOR 0700C (Makita 700-klon)** med en Makita-style/Sienci 1/8"-spännhylsa i VEVOR:s originalmutter och rapporterar mycket liten runout.
- den redan köpta HaWiWe-hylsan är en **Elaire Makita-style 1/8" / 3,175 mm** för Makita RT700/RT0700/RT0701-familjen. Det gör 0700C till det säkrare VEVOR-valet.

**Begränsning:** det finns fortfarande inget formellt datablad från VEVOR/Elaire som uttryckligen säger att just Elaire MRP-1250 passar VEVOR 0700C. Hylsan ska därför provpassas och runout kontrolleras innan riktig fräsning.

## D007 — Dammhantering ingår i grundbygget
**Status:** beslutat

CNC:n delar garage med motorarbete. Dammutsug är därför inte en senare bekvämlighetsuppgradering utan ett grundkrav före regelbunden fräsning i trä, MDF eller XPS.

Grundlösningen ska minst omfatta:
- LR4-dust shoe
- grovdammsugare/shop-vac
- cyklonavskiljare
- slangdragning/avlastning som inte belastar Z eller gantry
- möjlighet att begränsa och lätt städa den smutsiga CNC-zonen

## D008 — Laser senare
**Status:** uppskjutet

Laser är intressant men ska inte påverka grundbygget mer än valet av Jackpot3. Tidigast aktuellt 2027.

## D009 — Plasma inte i nuvarande scope
**Status:** bortprioriterat

Plasma ska inte styra bord, inköp eller byggordning nu. Fokus är att få en bra router-CNC körklar först.
