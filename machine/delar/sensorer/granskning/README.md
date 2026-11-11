# Granskningsmatriser – sidotorn v2

**Status:** Konstruktionen ar inte provprintad eller godkand for drift. Faststalld utifran `sidotorn.py`, `granska_sidotorn.py`, D020/D021/D022 (2026-11-11). Detta ar en **granskningsplan**, inte ett resultatprotokoll.

**Viktigt:** `granska_sidotorn.py` skriver diagnostiska avstand men har inga numeriska godkannandeassertioner; darfor klassas de som `S`, **inte `A`**. Inget `godkand` har markerats utan aterfunnet korbevis. `F` betyder definierat fysiskt prov, **inte att provet har gjorts**.

## Statuskoder

| Kod | Innebord |
|---|---|
| A | Automatisk grind med separat korbevis och resultat |
| S | Modell-/simuleringsdiagnostik; ej fysisk verifikation |
| F | Fysiskt prov specificerat; kan vara ej utfort |
| N | Nominellt antagande; inget verifierat bevis |
| X | Ej relevant med explicit motivering |
| SAKNAS | Kontrollmetod saknas; synligt tomrum |

`resultat` i JSON ar skilt fran kontrollmetod. Fysisk status byts till `godkand` endast tillsammans med reproducerbar evidens eller logg.

## 1. Komponentmatris – 32 objekttyper, 352 celler

| ID / objekt | Mått | Print | In | Fäste | El | Rör | Last | Värme | Damm | Service | Funk |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C01 Sidotorn och integrerad M5-bärplatta | S | F | F | S | X | F | F | F | F | F | F |
| C02 Fällarm | S | F | F | F | X | S | F | F | F | F | F |
| C03 BLTouch-skyddshylsa | S | F | F | F | X | S | F | F | F | F | F |
| C04 Sidopanel | S | F | F | S | X | F | F | F | F | F | F |
| C05 ADXL-distansbricka | S | F | F | F | X | F | F | F | F | F | F |
| C06 Spektrum SPMS664-servo | N | X | F | F | F | F | F | F | F | F | F |
| C07 Metallservohorn och splines | SAKNAS | X | F | F | X | F | F | F | F | F | F |
| C08 BLTouch (exakt revision ej verifierad) | N | X | F | F | F | F | F | F | F | F | F |
| C09 Raspberry Pi Camera Module 3 Standard | N | X | F | S | F | F | F | F | F | F | F |
| C10 Raspberry Pi Zero 2 WH | N | X | S | F | F | F | F | F | F | F | F |
| C11 ADXL345-modul | N | X | F | F | F | F | F | F | F | F | F |
| C12 LM2596 A, föreslagen 5,1 V | N | X | S | F | F | F | F | F | F | F | F |
| C13 LM2596 B, föreslagen 6,0 V | N | X | S | F | F | F | F | F | F | F | F |
| C14 Neodymmagnet Ø6×3 mm | S | X | F | F | X | F | F | F | F | F | F |
| C15 M3 stålskruv för parkeringsmagnet | N | X | F | F | X | F | F | F | F | F | F |
| C16 M5-bultar befintliga maskinfästen | N | X | F | F | X | F | F | F | F | F | F |
| C17 M3 servofäste | N | X | F | F | X | F | F | F | F | F | F |
| C18 M3×10 kameraklämmor | N | X | F | F | X | F | F | F | F | F | F |
| C19 M3×10 BLTouch-hylsa och arm | N | X | F | F | X | F | F | F | F | F | F |
| C20 M3×10 ADXL-fäste | N | X | F | F | X | F | F | F | F | F | F |
| C21 M3 panelskruvar | N | X | F | F | X | F | F | F | F | F | F |
| C22 CSI-flex 200 mm, 15↔22 poler | N | X | F | F | F | S | F | F | F | F | F |
| C23 Servokabel och kontakt | N | X | F | F | F | F | F | F | F | F | F |
| C24 BLTouch-kabel och kontakt | N | X | F | F | F | F | F | F | F | F | F |
| C25 Samlad kabelstam och bakre utgång | N | X | F | F | F | F | F | F | F | F | F |
| C26 Pi-matning från separat övervakningsdomän | SAKNAS | X | F | F | F | F | F | F | F | F | F |
| C27 Matningsskydd/säkring och jord-/returdragning | SAKNAS | X | F | F | F | F | F | F | F | F | F |
| C28 Servoavkoppling 470–1000 µF kandidat | N | X | F | F | F | F | F | F | F | F | F |
| C29 V1E verktygsfästen/Core (befintligt) | N | X | F | F | X | F | F | F | F | F | F |
| C30 Dammsko och kjol (befintliga) | N | X | F | F | X | F | F | F | F | F | F |
| C31 Jackpot3 GPIO och probegränssnitt | N | X | F | F | X | F | F | F | F | F | F |
| C32 COB-huvudbelysning på undre strut (extern) | N | X | F | F | X | F | F | F | F | F | F |


En rad ar **en komponentmatris**: de 11 stegen och individuella kontrollinstruktioner ligger i `komponentmatris.json` under `komponenter[].kontroller`. Antal i JSON anger kopior/fastelement. `bltouch.stl` och `kabel.stl` ar **attrapper**, inte utskrifter; faktiska utskrifter ar `torn`, `arm`, `kapa`, `sidopanel`, `bricka` (bricka x2).

## 2. Systemmatris – 16 funktioner, 128 celler

| ID / objekt | Krav | CAD | Auto | Beräk | Bänk | Maskin | Fel | Åter |
|---|---|---|---|---|---|---|---|---|
| S01 Mekaniskt montage på befintlig Core | N | S | SAKNAS | S | F | F | N | F |
| S02 Servorörelse 0 till −150 grader | N | S | SAKNAS | S | F | F | N | F |
| S03 Magnetisk parkering utan matning | N | S | SAKNAS | S | F | F | N | F |
| S04 BLTouch probegeometri och fräsfrigång | N | S | SAKNAS | S | F | F | N | F |
| S05 Kamerabild, täckning och koordinatkalibrering | N | S | SAKNAS | S | F | F | N | F |
| S06 Kamerainfästning/optisk stabilitet | N | S | SAKNAS | S | F | F | N | F |
| S07 CSI 200 mm-kabel och serviceväg | N | S | SAKNAS | S | F | F | N | F |
| S08 Pi Zero 2 WH, SD och åtkomst | N | S | SAKNAS | S | F | F | N | F |
| S09 Separat kraftdomän och säkra 5,1/6,0 V | N | S | SAKNAS | S | F | F | N | F |
| S10 Jackpot3/probe-I/O och startlogik | N | S | SAKNAS | S | F | F | N | F |
| S11 ADXL processövervakning och vibration | N | S | SAKNAS | S | F | F | N | F |
| S12 Kabelstam, dragavlastning, skav och EMC | N | S | SAKNAS | S | F | F | N | F |
| S13 Värme, passiv ventilation, damm och material | N | S | SAKNAS | S | F | F | N | F |
| S14 Tornets printbarhet, hållfasthet och service | N | S | SAKNAS | S | F | F | N | F |
| S15 LED- och kamerabelysningsgränssnitt | N | S | SAKNAS | S | F | F | N | F |
| S16 Maskinsäkerhet vid avbrott, service och omstart | N | S | SAKNAS | S | F | F | N | F |


Varje ruta har en metod, ett forvantat kontrollmoment och plats for bevis, inte bara en bokstav. Alla 0 markerade godkannanden avser verkligt korbevis (just nu inga). JSON-filerna ar sanningskalla, tabellerna ar lasvy.

## Prioriterade blockerare (P0)

1. **Servo/parkering:** metallhorn, verklig stoppgeometri, lossdragskraft och beteende utan strom.
2. **Proben:** verklig BLTouch-revision, stift/kontakt, hela svepet med kjol och korrekt G38-logik.
3. **Kamera och kablar:** kortets verkliga anlaggning, bildtackning/kalibrering, 200 mm CSI-flexens tva vikningar, SD-korts-/skruvverktygsatkomst.
4. **Matning:** D022 motsager det aldre utkastet med Pi driven fran brytna maskin-24 V. Matningskalla, sakerhet och bakmatning maste projekteras innan inkoppling.
5. **Verktygshuvud:** verklig Core, skruvlanger, dammsko/borst, Z-granser, spanskador, varme och vibrationsprov.
6. **Automatik:** `granska_sidotorn.py` behover maskinella testorakler/asertioner och testfixtures innan en gron CI-korning betyder geometriskt godkand.

D020 ersatter KW11 i aktuellt system. KW11 och `core_enhet.py` finns som historiska alternativ men far inte ateranvandas som bevis for sidotornet.

## Korning

```sh
python3 machine/delar/sensorer/granskning/kontrollera_matriser.py
python3 machine/delar/sensorer/granskning/kontrollera_matriser.py --strict
```

Standardkommandot validerar matrisernas struktur, unika ID, fulla celler, kanda statusar och att verkliga STL-exportnamn stammer med print-/attrapplistorna. `--strict` kraver verifierade prov pa alla relevanta celler och forvantas **misslyckas** tills konstruktionen ar granskat godkand. Kontroll av datorlogik ar inte fysiskt prov.
