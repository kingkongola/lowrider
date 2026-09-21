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
- praktisk maskinbredd runt 941 mm minimum

## D003 — Standardnära bygge först
**Status:** låst

Få standardmaskinen körklar innan modifieringar. Uppgraderingar kräver ett visat behov.

## D004 — Begagnat styvt bord som direkt maskinbas
**Status:** låst

**Uppdaterat 2026-09-19:** begagnad **180×100 cm bordsskiva köpt för 300 kr**. Den används direkt som strukturell maskinbas om underredet är styvt. Kontrollera underredet före montering och bygg/förstärk endast om behov finns.

Den köpta skivan rymmer 941×1563 mm minimumfootprint utan den tidigare planerade kantbreddningen för ett 90 cm-bord. Köp inte hel extra OSB/ply-deck utan verifierat behov.

Separat löstagbar ~12 mm MDF används som spoilboard över arbetszonen.

## D005 — Jackpot2 som tekniskt router-first-val
**Status:** superseded av D015

Jackpot2 var det tekniskt billigaste rimliga valet för router-only eftersom snabb laser-PWM inte behövs. Detta är fortfarande en korrekt funktionsbedömning men är inte längre aktiv köpväg.

## D006 — Router: KATSU 101750
**Status:** köpt 2026-09-03

KATSU `101750`, 220–240 V / 710 W / variabelt varvtal / cirka 65 mm kropp, Makita RT0700-familjens formfaktor. Köpt via Amazon.se. Köpt HaWiWe/Elaire Makita-style 1/8" collet ska provpassas och runout verifieras före riktig fräsning.

VEVOR `0700C` är blacklistad/replaced och ska inte köpas.

## D007 — Dammhantering i grundbygget
**Status:** låst

LR4 dust shoe + befintlig DeWalt shop-vac + cyklon + separat uppsamlingsbehållare + slangavlastning. Statisk jordväg ska vara löst före regelbunden MDF/trä/XPS-körning.

## D008 — Laser senare
**Status:** uppskjutet

Laser tidigast 2027 och får inte överoptimera grundbygget.

## D009 — Plasma utanför nuvarande bygge
**Status:** låst

Plasma styr inte bord, controller, el eller inköp i nuvarande bygge. Först byggs och driftsätts en vanlig router-LR4.

En eventuell modulär plasmavariant är ett separat framtida projekt, tidigast nästa vinter. Ingen plasma-framtidssäkring ska få komplicera eller fördyra version 1.

## D010 — Mean Well + Omron + DigiKey-konsolidering
**Status:** låst

- Mean Well `HDR-60-24`, 24 V / 2,5 A / 60 W.
- 10 × Omron `SS-3GL13PT`, 5 installerade + 5 reserv, NC via COM+NC.
- DigiKey samlar även 16 × 608-2RS, Wago, nätgenomföringar, Faston och lågspänningskablar enligt `PROCUREMENT.md`.

## D011 — Ø30 mm rails
**Status:** låst

Alla diameterberoende printar = 30 mm. Permanenta struts: `strut_length=819`, `front_wing_size=30`.

## D012 — Fast elbox + rörlig controller
**Status:** superseded av D016

Tidigare plan: NVR + HDR fasta på bordet, Jackpot3 på rörlig balk och lång rörlig 24 V-kabel. Omprövat eftersom V1E:s balkmonterade aggregat ger kortare 24 V-rutt utan att eliminera rörlig 230 V-kabel till fräsen.

## D016 — Tillbaka till V1E:s placering av 24 V-aggregatet
**Status:** beslutad plan; fysisk och elsäker monteringskontroll återstår

NVR/maskinstopp sitter fast och åtkomligt på bordet. Jackpot3 samt Mean Well HDR-60-24 planeras på rörlig balk enligt V1E:s princip. Mean Well-aggregatet är inte identiskt med V1E:s exempel: verifiera lämplig kapsling/beröringsskydd, infästning, skyddsjord och dragavlastning innan 230 V ansluts. Ingen oskyddad nätspänningsplint på balken. Använd inte den långa 24 V-slingan från det gamla förslaget utan ett konkret monteringsbehov. Kontrollera fräskabel, aggregatets matning, motor/endstop och dammsugarslang samtidigt genom hela rörelseområdet. Den redan köpta 3 m 20 AWG-kabeln finns i BOM, men behöver inte användas i denna rutt.

## D013 — NVR/maskinstopp
**Status:** låst

Kravet är 230 V NVR/no-voltage-release med lämplig märkström, tydlig lättåtkomlig stoppfunktion och dokumenterad terminalkoppling. Exakt KEDU-proveniens är inte ett projektkrav. Funktionen kallas NVR/maskinstopp, inte verifierad safety-rated E-stop.

## D014 — Commissioning-dependencies
**Status:** låst

Inventera data-USB-C och FAT32 microSD innan köp. T8 400 mm kapas efter fysisk assembly-check, praktiskt mål ~150–160 mm ×2, inte automatiskt i halvor. Endstops är home/auto-square, inte runtime hard limits.

## D015 — Jackpot3 från Elecrow
**Status:** **köpt 2026-09-03**

Controller är **Elecrow Jackpot3 `CQA240812C2`**.

- checkout: controller 69,44 € efter rabatt + DDP Economy 14,11 € = 83,55 €
- faktisk bankdebitering: **937 kr**
- DDP valdes för att undvika separat tull-/transportörshantering
- beslutet är nu stängt; Jackpot2-fallbacken är inte längre aktiv

Laser är fortfarande uppskjuten och var inte skälet till köpet.
