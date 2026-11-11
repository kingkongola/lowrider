# Täckning: vad är kontrollerat?

Genererad av `tackning.py` ur `komponenter.yaml` och `system.yaml`. Ändra i YAML-filerna, inte här.

Varje ruta har den sämsta status som står i den. **Har kontroll** = A, S, F eller X: rutan har en definierad kontroll eller är inte relevant. F betyder ett **planerat** fysiskt prov; om det är utfört ägs av CHECKLIST.md. Nominella antaganden (N) och SAKNAS räknas inte.

| Matris | Storlek | A (automatisk kontroll) | S (simulerad/beräknad) | F (fysiskt prov) | N (nominellt antagande) | X (ej relevant) | SAKNAS (inte kontrollerat) | Har kontroll |
|---|---|---|---|---|---|---|---|---|
| Komponenter | 30 × 11 | 47 | 58 | 59 | 80 | 86 | 0 | 76 % |
| Systemet | 23 × 8 | 20 | 84 | 36 | 13 | 31 | 0 | 93 % |

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

## Systemet

| | Krav formulerat | Konstruktion finns | Automatisk kontroll | Simulering eller beräkning | Bänkprov | Prov på maskinen | Vad händer när det går fel | Ägande fil |
|---|---|---|---|---|---|---|---|---|
| Tornets infästning på maskinen | S | S | A | A | X | F | F | S |
| Armens rörelse och ändlägen | S | S | A | A | F | F | N | S |
| Probmätning till nollpunkt | S | S | A | N | F | F | S | S |
| Kamerabild och kalibrering | S | S | A | S | F | F | S | S |
| Belysning | S | S | A | N | F | F | N | S |
| Armspärren | S | S | A | F | X | F | S | S |
| Vibrationsmätning | S | S | A | F | F | F | S | S |
| Ljudmätning | S | S | A | N | F | F | S | S |
| Matning, övervakning | S | S | X | S | F | F | S | S |
| Matning, maskin och servo | S | S | X | A | F | F | N | S |
| Jord och störningar | S | S | X | X | X | F | S | S |
| Stoppkedjan | S | S | A | S | F | F | S | S |
| Start efter stopp | S | S | A | X | F | F | S | S |
| FluidNC-konfiguration | S | S | A | X | X | F | N | S |
| Programvara på Pi:n | S | S | A | X | F | F | S | S |
| Programvara på datorn | S | S | A | X | X | F | A | S |
| Nätverk | S | S | X | X | F | N | S | S |
| Kabelföring genom rörelsen | S | S | X | S | X | F | N | S |
| Värme i tornet | S | S | X | A | F | F | N | S |
| Damm och spån | S | S | X | X | X | F | S | S |
| Underhåll | N | S | A | X | X | N | X | S |
| 230 V-säkerhet | S | S | X | X | X | F | S | S |
| Dokumentens samstämmighet | S | X | A | X | X | X | N | S |
