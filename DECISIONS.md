# Decisions

Endast beslut som påverkar detta LowRider-bygge.

## D001 — LowRider V4
**Status:** beslutat / delar köpta

Bygg LowRider V4. Maskinvalet är avslutat.

## D002 — Arbetsyta omkring 650 × 1200 mm
**Status:** preliminärt beslutat

Exakt slutmått ska verifieras i aktuell LR4-kalkylator innan storleksberoende material kapas eller beställs.

## D003 — Standardnära bygge först
**Status:** beslutat

Bygg maskinen korrekt och få den körklar innan eventuella modifieringar. Uppgradera först när en faktisk begränsning har visat sig.

## D004 — Bordet ska dimensioneras efter slutlig LR4-geometri
**Status:** beslutat

Yttermått, sarg och frigång bestäms först när slutlig arbetsyta och maskinens exakta footprint är verifierade.

## D005 — Jackpot3 som styrkort
**Status:** beslutat förstahandsval

Jackpot3 väljs framför SKR Pro och äldre Jackpot-versioner om prisskillnaden inte är orimlig.

Skäl:
- V1E säljer Jackpot3 som aktuell standardlösning och den är förkonfigurerad för LowRider V4.
- 6 integrerade TMC2226-drivare, alltså inga separata stepper-drivers att köpa eller montera.
- FluidNC, Wi‑Fi och webbgränssnitt direkt på kortet.
- 7 ingångar och 4 valbara 5 V / linjenivå-utgångar.
- full PWM på 5 V-utgångarna; Jackpot2 saknar snabb PWM och är därför främst ett budgetalternativ om laser inte är aktuellt.
- USB‑C och integrerad RJ11/pendant-anslutning.

Jackpot1 är inte förstahandsval för nybygge eftersom det kräver separata TMC2209-drivare och separat ESP32-modul. Jackpot2 är acceptabelt om det hittas tydligt billigare, men V1E märker det som ett mer nischat/budgetalternativ och Jackpot3 är den aktuella huvudversionen.

## D006 — VEVOR 710 W, 65 mm Makita-klon som fräsmotor
**Status:** beslutat förstahandsval

Målmodell: **VEVOR VV-1B-220V, 710 W, 65 mm kropp, 13 000–33 000 rpm, fast bas**.

Skäl:
- 65 mm kropp passar LR4:s vanliga Makita-format.
- variabel hastighet och soft-start.
- 710 W är i rätt klass för LR4 och långt billigare än Makita.
- VEVOR EU hade den på ca 42,90 € vid research 29/8 2026.
- den billiga 1-bas-versionen räcker för CNC; dyrare plunge/tilt/offset-baser ger ingen nytta när motorn sitter permanent i LR4.

**Viktig osäkerhet:** VEVOR anger medföljande spännhylsor 1/4", 6 mm och 8 mm. Det finns inget verifierat underlag att den redan köpta Makita 3,175 mm-spännhylsan passar VEVOR-motorn. Kontrollera faktisk mutter/kon-geometri innan den används. Köp inte ytterligare 1/8"-lösning förrän detta är verifierat.
