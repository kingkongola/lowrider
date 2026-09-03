# Decisions

Endast beslut som påverkar den LowRider V4 som faktiskt byggs. Nyare beslut supersederar äldre när det anges uttryckligen.

## D001 — LowRider V4
**Status:** låst

Bygg LowRider V4. PrintNC och IndyMill är inte aktiva alternativ.

## D002 — Arbetsyta 650 × 1250 mm
**Status:** låst

Geometri:
- X-rör 816 mm ×2
- Y-rör 1505 mm
- Ø30×1,5 mm
- strut-input 819 mm
- `front_wing_size=30`
- GT2 999 / 1705 / 1705 mm = 4409 mm
- minimum bord 941 × 1563 mm
- praktisk deck ~1000×1620 mm

## D003 — Standardnära bygge först
**Status:** låst

Få standardmaskinen körklar innan modifieringar. Uppgraderingar kräver ett visat behov.

## D004 — Begagnat bord + avtagbar deck
**Status:** låst

Styvt begagnat bord 160–180 cm långt, helst 90–100 cm djupt och helst ≤700 kr. Befintlig bordsskiva behålls. Ovanpå: avtagbar ~1000×1620 structural deck + löstagbar ~12 mm MDF-spoilboard. 90 cm bord kräver verkligt stöd/infästning under decköverhänget i LR4:s kantzon.

## D005 — Jackpot2 som tekniskt router-first-val
**Status:** **superseded för inköp av D015**

Jackpot2 var det tekniskt billigaste rimliga valet för router-only eftersom snabb laser-PWM inte behövs. Detta är fortfarande en korrekt funktionsbedömning men inte längre aktiv köpväg.

## D006 — VEVOR 0700C
**Status:** låst

VEVOR 0700C, 220–240 V / 50 Hz, 800 W, 65 mm kropp, 10 000–30 000 rpm. Köpt HaWiWe/Elaire Makita-style 1/8" collet ska provpassas och runout verifieras före riktig fräsning.

## D007 — Dammhantering i grundbygget
**Status:** låst

LR4 dust shoe + befintlig DeWalt shop-vac + cyklon + separat uppsamlingsbehållare + slangavlastning. Statisk jordväg ska vara löst före regelbunden MDF/trä/XPS-körning.

## D008 — Laser senare
**Status:** uppskjutet

Laser tidigast 2027 och får inte överoptimera grundbygget.

## D009 — Plasma utanför scope
**Status:** låst

Plasma styr inte bord, controller eller inköp i nuvarande bygge.

## D010 — Mean Well + Omron + DigiKey-konsolidering
**Status:** låst

- Mean Well `HDR-60-24`, 24 V / 2,5 A / 60 W.
- 10 × Omron `SS-3GL13PT`, 5 installerade + 5 reserv, NC via COM+NC.
- DigiKey samlar även 16 × 608-2RS, Wago, nätgenomföringar, Faston och lågspänningskablar enligt `PROCUREMENT.md`.

## D011 — Ø30 mm rails
**Status:** låst

Alla diameterberoende printar = 30 mm. Permanenta struts: `strut_length=819`, `front_wing_size=30`.

## D012 — Fast elbox + rörlig controller
**Status:** låst

NVR + HDR sitter fast på bordet. Jackpot sitter på rörlig beam/YZ_Min-sida. Köp 3 m 20 AWG 2-core som längdmarginal; kapa efter full-travel dry-fit. Routerkabel, 24 V, motor/endstop och vac-hose provas samtidigt i alla rörelseextremer.

## D013 — NVR/maskinstopp
**Status:** låst

Kravet är 230 V NVR/no-voltage-release med lämplig märkström, tydlig lättåtkomlig stoppfunktion och dokumenterad terminalkoppling. Exakt KEDU-proveniens är inte ett projektkrav. Funktionen kallas NVR/maskinstopp, inte verifierad safety-rated E-stop.

## D014 — Commissioning-dependencies
**Status:** låst

Inventera data-USB-C och FAT32 microSD innan köp. T8 400 mm kapas efter fysisk assembly-check, praktiskt mål ~150–160 mm ×2, inte automatiskt i halvor. Endstops är home/auto-square, inte runtime hard limits.

## D015 — Elecrow Jackpot3 är aktiv controller-köpväg
**Status:** låst 2026-09-03 på sourcinggrund

Aktivt köp är **Elecrow Jackpot3 `CQA240812C2`**.

Skäl:
- Elecrow visar $76,99 och uttryckligen **In stock**.
- V1E:s egna Jackpot2/Jackpot3-sidor ger motsägelsefull butikstatus (sold-out-markering samtidigt som add-to-cart visas), så tillgängligheten är inte tillräckligt robust för projektplanen.
- V1E hänvisar internationella Jackpot3-kunder till Elecrow som direktare köpväg.
- skillnaden mot Jackpot2 är ett sourcingbeslut, inte ett nytt funktionskrav; laser är fortfarande uppskjuten.

Fallback: om V1E Jackpot2 vid faktisk checkout går att köpa och **landar klart billigare** än Elecrow utan leveransfördröjning får köpet gå tillbaka till Jackpot2. Annars ska bygget inte fördröjas för att spara den nominella artikelprisskillnaden.