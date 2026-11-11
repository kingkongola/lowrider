# Täckning: vad är kontrollerat?

Genererad av `tackning.py` ur `komponenter.yaml` och `system.yaml`. Ändra i YAML-filerna, inte här.

Varje ruta har den sämsta status som står i den. **Har kontroll** = A, S, F eller X: rutan har en definierad kontroll eller är inte relevant. F betyder ett **planerat** fysiskt prov; om det är utfört ägs av CHECKLIST.md. Nominella antaganden (N) och SAKNAS räknas inte.

| Matris | Storlek | A (automatisk kontroll) | S (simulerad/beräknad) | F (fysiskt prov) | N (nominellt antagande) | X (ej relevant) | SAKNAS (inte kontrollerat) | Har kontroll | Verifierat med bevis | Relevanta rutor |
|---|---|---|---|---|---|---|---|---|---|---|
| Komponenter | 38 × 11 | 61 | 76 | 71 | 97 | 113 | 0 | 77 % | 0 | 305 |
| Systemet | 25 × 9 | 23 | 109 | 40 | 20 | 33 | 0 | 91 % | 0 | 192 |

**Verifierat med bevis** räknar rutor med godkänd post i `resultat.yaml` (datum, metod, protokoll, ansvarig). Att en kontroll finns är inte detsamma som att den är utförd.

## Inte kontrollerat (0 rutor)

| Matris | Rad | Kolumn | Vad saknas |
|---|---|---|---|

## Komponenter

| | Mått verifierade | Print/tillverkning | Insättning, fri väg | Fastsättning, åtkomst och grepp | Elektrisk koppling och kabelväg | Frigång i drift | Last och vibration | Värme | Damm och spån | Service och byte | Funktionsprov |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Torn | A | F | X | F | X | A | F | F | F | S | F |
| Sidopanel | A | S | A | A | S | X | F | N | N | S | F |
| Arm | A | S | A | F | F | A | F | X | N | S | F |
| Skyddshylsa | A | S | A | F | X | A | N | X | N | S | F |
| Hornbygel | A | S | A | F | X | A | F | X | X | S | F |
| Distansbricka | A | S | A | A | X | X | N | X | X | X | X |
| LED-fäste | A | S | N | N | F | N | X | F | N | N | F |
| Pi Zero 2 WH | N | X | A | A | A | X | N | F | N | A | F |
| microSD | S | X | A | N | X | X | S | X | N | A | F |
| Camera Module 3 | A | X | S | A | S | X | N | N | F | S | F |
| CSI-kabel | N | X | S | N | S | X | N | X | X | S | F |
| ADXL345 | N | X | A | A | A | X | F | X | X | S | F |
| INMP441 | N | X | A | N | A | X | N | X | S | S | F |
| LM2596 A | N | X | A | N | S | X | N | A | X | S | F |
| LM2596 B | N | X | A | N | S | X | N | A | X | S | F |
| Servo SPMS664 | N | X | A | A | S | F | F | N | N | S | F |
| Servohorn | F | X | A | F | X | A | F | X | X | S | F |
| CR Touch | N | X | A | A | N | A | N | X | F | S | F |
| Magnet | N | X | A | N | X | X | F | N | N | N | F |
| Kopplingskort | N | S | A | N | S | X | N | N | X | S | F |
| Tornkabel 12 ledare | N | X | S | S | S | F | N | X | N | N | F |
| Y-kabel 8 ledare | N | X | N | N | S | F | N | X | N | N | F |
| Stopplåda | S | S | S | S | S | X | X | N | N | S | F |
| Pumpkort | S | S | S | S | S | X | X | N | X | N | F |
| Kontaktor, nödstopp, startknapp | N | X | S | S | S | X | X | N | N | N | F |
| HDR-60-24 nr 2 | N | X | S | N | S | X | X | N | N | N | F |
| COB-list | N | X | N | N | S | X | X | F | N | N | F |
| Jackpot-anslutningar | N | X | X | N | S | X | X | X | X | N | F |
| M5 tornet till maskinen | F | X | A | S | X | X | F | X | X | S | F |
| Självgängande M3 och M2.5 i PETG | A | N | A | F | X | X | N | X | X | N | F |
| Stoppdel nedre | A | S | A | A | X | A | F | X | N | S | F |
| Stoppdel övre | A | S | A | A | X | A | F | N | N | S | F |
| M3 stålskruv mot magneten | N | X | S | N | X | A | A | X | N | S | F |
| Servokabel och kontakt | N | X | S | N | S | X | N | X | X | S | F |
| CR Touch-kabel och kontakt | N | X | S | S | S | F | F | X | N | S | F |
| Kondensator 470-1000 µF | N | X | S | S | S | X | N | N | X | N | F |
| Verktygsfäste och Core (befintliga) | A | X | X | S | X | A | N | X | X | S | F |
| Dammsko och kjol (befintliga) | A | X | X | X | X | A | X | X | N | X | F |

## Systemet

| | Krav formulerat | Konstruktion finns | Automatisk kontroll | Simulering eller beräkning | Bänkprov | Prov på maskinen | Vad händer när det går fel | Ägande fil | Återställning efter fel |
|---|---|---|---|---|---|---|---|---|---|
| Tornets infästning på maskinen | S | S | A | A | X | F | F | S | F |
| Armens rörelse och ändlägen | S | S | A | A | F | F | N | S | S |
| Probmätning till nollpunkt | S | S | A | N | F | F | S | S | S |
| Kamerabild och kalibrering | S | S | A | S | F | F | S | S | S |
| Belysning | S | S | A | N | F | F | N | S | N |
| Armspärren | S | S | A | F | X | F | S | S | S |
| Vibrationsmätning | S | S | A | F | F | F | S | S | S |
| Ljudmätning | S | S | A | N | F | F | S | S | S |
| Matning, övervakning | S | S | X | S | F | F | S | S | S |
| Matning, maskin och servo | S | S | X | A | F | F | N | S | N |
| Jord och störningar | S | S | X | X | X | F | S | S | S |
| Stoppkedjan | S | S | A | S | F | F | S | S | S |
| Start efter stopp | S | S | A | X | F | F | S | S | S |
| FluidNC-konfiguration | S | S | A | X | X | F | N | S | S |
| Programvara på Pi:n | S | S | A | X | F | F | S | S | S |
| Programvara på datorn | S | S | A | X | X | F | A | S | S |
| Nätverk | S | S | X | X | F | N | S | S | N |
| Kabelföring genom rörelsen | S | S | X | S | X | F | N | S | N |
| Värme i tornet | S | S | X | A | F | F | N | S | N |
| Damm och spån | S | S | X | X | X | F | S | S | S |
| Underhåll | N | S | A | X | X | N | X | S | X |
| 230 V-säkerhet | S | S | X | X | X | F | S | S | S |
| Dokumentens samstämmighet | S | X | A | X | X | X | N | S | A |
| Probstiftet mot fräsens spets | S | S | A | N | X | F | S | S | S |
| Kamerafäste och optisk stabilitet | S | S | A | N | F | F | S | S | S |
