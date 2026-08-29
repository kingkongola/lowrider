# Decisions

Endast beslut som påverkar detta LowRider-bygge.

## D001 — LowRider V4
**Status:** beslutat / delar köpta

Bygg LowRider V4. Maskinvalet är avslutat. PrintNC och IndyMill är inte längre aktiva alternativ för detta bygge.

## D002 — Arbetsyta 650 × 1250 mm
**Status:** beslutat / geometri verifierad

Användbar arbetsyta låses till **650 × 1250 mm** med de köpta 6,0 mm HaWiWe XZ-plattorna.

Aktuell V1E-kalkylator ger:
- 2 × X-rör: **816 mm**
- 1 × Y-rör: **1505 mm**
- strut: **819 mm**
- X-rem: **999 mm**
- Y-remmar: **1705 mm ×2**
- total GT2: **4409 mm**, alltså räcker 5 m
- minimum bord: **941 × 1563 mm**
- praktisk CNC-deck: cirka **1000 × 1620 mm**

Storleken rymmer en nominell kvarts 1220×2440-skiva (610×1220) med marginal utan onödigt garagefotavtryck.

## D003 — Standardnära bygge först
**Status:** beslutat

Bygg maskinen korrekt och få den körklar innan eventuella modifieringar. Uppgradera först när en faktisk begränsning har visat sig.

## D004 — Begagnat bord + avtagbar CNC-deck
**Status:** beslutat huvudspår

Första bordslösningen ska vara ett styvt begagnat mat-/konferens-/kontorsbord, helst **180×90 eller 180×100 cm**, med befintlig strukturell skiva kvar.

Ovanpå monteras en **avtagbar ~1000×1620 mm CNC-deck** i i första hand 11 mm OSB eller ungefär 12 mm konstruktionsplywood, beroende på det faktiska bordets top. Deck skruvas/bultas, inte limmas. Separat ~12 mm MDF används som löstagbar spoilboard.

Prisregler:
- 0–400 kr: starkt köp om geometri + rackingtest passerar
- 400–700 kr: normal Pareto-zon
- 700–1000 kr: endast tydligt högkvalitativt/styvt kommersiellt underrede
- >1000 kr: normalt vänta

Ingen torsionsbox, specialsvetsad ram, höj-/sänkbart skrivbord eller hjulsystem ska byggas/köpas före första körningen utan ett konkret behov.

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

Skäl:
- modellen heter uttryckligen **0700C** och VEVOR anger kompatibilitet med Makita 0700-bas.
- 65 mm kropp passar LR4:s Makita-format.
- VEVOR anger 6,35 mm och 8 mm spännhylsor som standard.
- dokumenterat V1E-fall finns med VEVOR 0700C + Makita-style 1/8"-hylsa och låg rapporterad runout.
- den redan köpta HaWiWe-hylsan är en Elaire Makita-style 1/8" / 3,175 mm för Makita RT700/RT0700/RT0701-familjen.

**Begränsning:** inget formellt VEVOR/Elaire-datablad säger uttryckligen att just Elaire MRP-1250 passar VEVOR 0700C. Hylsan ska därför provpassas och runout kontrolleras innan riktig fräsning.

## D007 — Dammhantering ingår i grundbygget
**Status:** beslutat

CNC:n delar garage med motorarbete. Dammutsug är därför inte en senare bekvämlighetsuppgradering utan ett grundkrav före regelbunden fräsning i trä, MDF eller XPS.

Grundlösningen ska minst omfatta:
- LR4-dust shoe
- befintlig DeWalt shop-vac
- cyklonavskiljare, printad först
- separat styv uppsamlingsbehållare
- slangdragning/avlastning som inte belastar Z eller gantry
- möjlighet att begränsa och lätt städa den smutsiga CNC-zonen

## D008 — Laser senare
**Status:** uppskjutet

Laser är intressant men ska inte påverka grundbygget mer än valet av Jackpot3. Tidigast aktuellt 2027.

## D009 — Plasma inte i nuvarande scope
**Status:** bortprioriterat

Plasma ska inte styra bord, inköp eller byggordning nu. Fokus är att få en bra router-CNC körklar först. Den avtagbara CNC-decken gör att underredet inte behöver låsas permanent till routertoppen.

## D010 — Mean Well HDR-60-24 + exact Omron från DigiKey
**Status:** beslutat förstahandskorg

24 V-nätaggregat låses till **Mean Well HDR-60-24, 24 V / 2,5 A / 60 W** i DIN-format.

Endstops låses till **Omron SS-3GL13PT**. Köp 10, installera 5 och behåll 5 reserv. Koppla NC, COM + NC.

Nuvarande inköpsväg är DigiKey för HDR + Omron i samma korg. Detta **supersederar den äldre provisoriska GST60A24-P1J-riktningen**.

Lågspännings-/endstopkabel läggs i den redan planerade LaskaKit-korgen; StepperOnline ska fortsatt vara motors-only.