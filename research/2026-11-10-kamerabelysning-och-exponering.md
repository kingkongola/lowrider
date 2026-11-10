---
research_date: 2026-11-10
scope: Kamerabelysning för sidotornet, 24 V, G4 och stillbildsexponering
status: exploring
decision_state: Ingen lampa vald eller beställd; jämnt ljus och verkligt bildprov före dimensionering för maximalt ljusflöde
price_basis: Observerade webpriser 2026-11-10; frakt och checkout ej kontrollerade
region: Sverige/EU
sources_checked:
  - Electrokit EKM021b, tillverkarens produktsida
  - Malmbergs Pro 9975354, tillverkarens produktblad
  - Velltra, köpväg för Malmbergs 9975354
  - NauticLED G4-Pro10-WW-SP, tillverkarens produktsida
  - iDEAL LED SCOB-24-3mm-3K-4W, tillverkarens produktsida
  - Raspberry Pi, officiell kameradokumentation
  - Lokal sidotorn.py och cnc/src/cnc/pikamera.py
supersedes: null
---

# Kamerabelysning och exponering — underlag, inte inköpsbeslut

Aktuell konstruktion ägs av `machine/delar/sensorer/sidotorn.py`, belysningskraven av [KAMERA_ANHALL.md](../machine/KAMERA_ANHALL.md). Denna fil bevarar daterad jämförelse, inte leveransstatus eller en alternativ BOM.

## Källbelagda kandidater

| Kandidat | Verifierad specifikation | Begränsning för sidotornet |
| --- | --- | --- |
| [Electrokit EKM021b, 41024239](https://www.electrokit.com/led-ring-for-raspberry-pi-kamera-vita-leds) | Kameramodul med 12 vita LED, 5 V, 190 mA, 25 × 24 × 2,6 mm, 6500 K. Tillverkaren anger kompatibilitet med Camera Module 3. Separat EN-signal krävs. | Ljusflöde i lumen inte publicerat. Ska inte anslutas till 17/24 V. Kräver kontroll av infästning, kontakt, linsfrigång och verklig matningsspänning mot vår CAD. |
| [Malmbergs Pro 9975354](https://malmbergsprod.blob.core.windows.net/web/products/9975354/pdf/MS-9975354.pdf) | COB-list: 24 V DC, 10 W/m, 1220 lm/m, 4000 K, Ra90, 8 mm bred, kapbar var 50 mm. | Minsta bit är för stor för nuvarande LED-spår. Separat hållare eller omritad plats krävs. |
| [NauticLED G4-Pro10-WW-SP](https://www.nauticled.com/shop/nauticled-g4-pro10-ww-sp-482) | G4, reglerad ingång 10–35 V DC, 1,6 W, 170 lm, 2700 K, 120° spridning, Ø30 mm. | Klarar nominellt både 17 och 24 V. Sockel och lampkropp kräver större hållare; ingen passning mot vår modell verifierad. Sidans sammanfattning och tabell anger olika CRI-gränser, därför används inget precist CRI-värde här. |
| [iDEAL LED SCOB-24-3mm-3K-4W](https://idealled.com.au/product/cob-high-performance-24v-3mm-4w-led-striplight/) | 24 V, 4 W/m, 340 lm/m, 3000 K, 3 × 1,6 mm, kapbar var 20 mm. | Även denna minsta bit är längre än nuvarande spår. Australisk leverantör, ingen svensk köpväg kontrollerad. Inte prioriterad för snabbt bygge. |

**Observerade köpdata:** Electrokit visade 149 kr inkl. moms och lagerförd vara med angiven 1–3 vardagars leverans. [Velltra](https://www.velltra.se/product/led-strip-cob-10w-m-24vdc-1220lm-m-4000k-ip20-5m-malmbergs-9975354) visade 389 kr för 5 m Malmbergs-list och angav normalt 2–5 vardagar; sidan visar även bevakningsfunktion, så lagersaldo ska inte betraktas som verifierat. Frakt och leverans till användarens adress har inte kontrollerats.

## Beräkningar och slutsatser, inte uppmätt resultat

- Två 50 mm-bitar Malmbergs-list ger nominellt sammanlagt **1 W, cirka 42 mA vid 24 V och 122 lm före eventuellt ljusspridande lock**. Beräknat från tillverkarens per-meter-värden; ljus på materialet är inte mätt.
- Kameralampans inmatade effekt är **0,95 W** från 5 V × 0,190 A. Detta bevisar inte att ljusflödet motsvarar 1 W av en annan lampa.
- Högre matningsspänning betyder inte automatiskt mer ljus. En lampas specificerade spänningsområde måste följas. En vanlig 12 V G4 är inte automatiskt lämplig för 17 eller 24 V; G4 är sockeln, inte en spänningsklass.
- De nuvarande CAD-spåren är preliminära. Ingen kandidat ovan är en verifierad direkt ersättning utan monteringskontroll.

## Stillbilder och tidsåtgång

Användaren påpekade att längre slutartid kan ersätta behovet av mycket starkt ljus eftersom maskinen står still för varje bild. **Det är en giltig provstrategi, inte ännu ett uppmätt belysningsbehov.** Längre exponering samlar mer ljus, men kräver att både maskin och kamera har slutat vibrera. Ojämna skuggor och blänk behöver fortfarande hanteras med ljusets placering.

[Raspberry Pi:s dokumentation](https://www.raspberrypi.com/documentation/accessories/camera-software.html#capture-long-exposures) beskriver manuell exponering och hur automatiken annars kan kräva flera bildrutor för att ställa in sig. Lokal `pikamera.py` låser fokus och sparar verklig exponering/förstärkning i metadata, men har ännu ingen färdig manuell exponeringsserie eller integrerad maskinskanning. Engångsvägen väntar 0,8 s efter kamerastart; återkommande start/stopp ska inte förväxlas med själva exponeringstiden.

Illustration för **50 bilder**, en räknad exponering per bild:

| Exponering per bild | Summan av exponeringstiderna |
| --- | ---: |
| 1/100 s = 10 ms | 0,5 s |
| 1/10 s = 100 ms | 5 s |
| 1/2 s = 500 ms | 25 s |

Detta är bara exponeringens tidsbidrag. Förflyttning, vibrationsavklingning, sensorutläsning, kamerans bildbuffring, överföring och bildbehandling tillkommer. Total skanningstid är inte mätt. Prova befintligt ljus och några exponeringstider med känt fokus innan lampstorlek eller minsta lumenantal låses.
