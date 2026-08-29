# Sourcing plan — current 2026-08-29

Mål: bra kvalitet utan dumsnålhet, låg total kostnad inklusive frakt och så få beställningar som **ekonomiskt rimligt**.

**Temporalitet:** priser/lager ska omkontrolleras före köp. `PROCUREMENT.md` är kanonisk order-/kundvagnsöversikt; daterade filer under `research/` är evidens/historik.

## Låsta val

- Maskin: **LowRider V4**
- Arbetsyta: **650 × 1250 mm**
- CNC-deck: cirka **1000 × 1620 mm**
- Rails: **Ø30×1,5 mm stål** → 30 mm-printvariant
- Controller: **Jackpot3**
- Router: **VEVOR 0700C, 800 W, 65 mm**
- PSU: **Mean Well HDR-60-24**
- Endstops: **Omron SS-3GL13PT**, köp 10/installera 5
- Motorer: StepperOnline **`5-17HS19-2004S1`** fempack
- Dammutsug är ett grundkrav
- Laser väntar till tidigast 2027; plasma ingår inte i nuvarande scope

## Redan köpt och betalt — ska inte sourcas igen

HaWiWe, **165,50 € inklusive 8,00 € frakt**:
- Aluminium XZ plates, 6,0 mm
- 4 × MGN12H 150 mm linear rails
- LR4 screw set
- Elaire/Makita-style 1/8" (3,175 mm) collet

## Aktuella köpvägar

### Motonet — rör
- 2 × `88-7123`
- Ø30×1,5 mm ×2 m
- observerat 189 kr/st
- kontrollera OD/rakhet före betalning
- kapa 1505 / 816 / 816 mm

### LaskaKit — mekanik + lågspänningskablage
- 6 × `LA190008E` smooth idlers, 5 mm lagerhål, för 10 mm rem
- 1 × `LA190032A` Tr8×8 400 mm; V1E kräver 145 mm+, så kapa praktiskt cirka **150–160 mm ×2** efter assembly-check, inte automatiskt mitt itu
- 2 × `LA190033A` Tr8×8 brass nuts
- 2 × `LA190031` 5→8 couplers
- 1 × `LA190013C` 5 m, 10 mm fiberglass GT2 belt om lager
- **fallback:** 3 × 2 m samma 10 mm fiberglass-spec; varje 999/1705/1705-segment får en egen längd utan skarv
- 10 m `LA150151A` endstop cable
- **3 m** UL2464 20 AWG / ~0,52 mm² **2-core**, nominellt ~4,8 mm OD, för fast HDR-box → rörlig Jackpot; kapa efter full-travel dry-fit
- board connectors/pigtails efter crimperläge

UL2464-ledningen är inte dokumenterad som continuous-flex/drag-chain. Använd stor rörelseloop; byt kabeltyp om verklig routing kräver snäv repetitiv böj.

### StepperOnline Germany — motors only
- 1 × fempack `5-17HS19-2004S1`
- 59 Ncm, 2 A, 5 mm D-axel, 24 mm axel, 1 m fabrikskabel
- Germany warehouse
- köp inga China-only delar bara för falsk samfrakt

### DigiKey — konsoliderad komponentkorg
- 1 × Mean Well `HDR-60-24` / `1866-2249-ND`
- 10 × Omron `SS-3GL13PT` / `SW768-ND`
- 16 × exact 608-2RS 8×22×7 mm — 14 installeras + 2 reserv
- 3 × genuine Wago `221-413`
- 2 × M20×1,5 IP68 cable glands för 3G1,5 nät in/ut
- 10 × isolerade 6,35×0,8 mm Faston-hylsor som passar faktisk KJD12
- uppskattad merchandise-total omkring **622 kr inkl moms**

**Audit correction:** DigiKey anger fri Sverige-frakt vid 615 kr, men vi har inte verifierat om tröskeln bedöms före/efter moms. Fri frakt är därför **checkout-gated**; anta inte 0 kr frakt innan varukorgen faktiskt visar det.

Den fasta boxens 24 V-utgång behöver dessutom **egen mindre kabelgenomföring/dragavlastning**. Den valda 2-core-kabeln är nominellt ~4,8 mm OD, medan M20-glanden är dokumenterad för 5–12 mm; välj mindre gland efter verkligt mått.

Detta supersederar äldre HDR+Omron-only-korg och separat 608-orphan-spår.

### VEVOR EU — router
- exakt **0700C**
- SKU `YXKXBJ710W65AH7WLV2`
- product ID `010235793217`
- 800 W / 65 mm / 10 000–30 000 rpm
- 65 mm-kroppen matchar Makita-formatets LR4-mount
- provpassa redan köpt Elaire-collet och kontrollera runout efter ankomst

### Elecrow — Jackpot3
- exact `CQA240812C2`
- måste flashas/konfigureras för LR4 efter leverans
- paketet listar board + fem 2-ledarpluggar + sex heatsinks; **microSD listas inte**
- inventera FAT32 microSD >2 GB, helst Class 4/6; köp enkelt 4–32 GB bara om det saknas
- inventera/verifiera data-kapabel USB-C för flashing
- Sverige-frakt/VAT/import avgörs i checkout

### SUNLU — PLA
- ordinary PLA
- LR4 behöver omkring 2,7 kg inklusive tool mount + board box
- bulkplanen är 6 × 1 kg normala spolar om checkout håller ungefär 100–110 kr/kg levererat
- före full print-sats: verifiera minst 200×200×190 mm byggvolym, printer skew och `Z_Stub`/`Z_Nut`-testfit

### Sorotec — första frässtål
- 3 × `L1S.M.0317`
- 3,175 mm single-flute upcut, 9 mm spiral/skärlängd
- commissioning + 5–6 mm strut-material
- lång plywoodfräs väntar tills ett verkligt 18–19 mm genomskärningsjobb finns

### Orphan: GT2 16T
- 3 × exact GT2 / 16T / 5 mm bore / 10 mm belt
- preferred Allegro `GT2-16T-5B_10mm_K`
- köp om Sverige-totalen är rimlig; byt säljare, inte spec, om frakten är dålig

### KJD12 / el
- genuin KEDU KJD12, 2-polig NVR/no-restart med röd stoppkåpa
- **terminologi:** NVR/maskinstopp; safety-rated E-stop-status är inte verifierad
- aktuell genuin kandidat är märkt för tillräcklig strömklass; verifiera ändå exakt variant, terminalschema och märkdata
- Biltema `35-0065` IP65 4-moduls kapsling förstahandsval efter fysisk dry-fit; `35-0067` större fallback
- 3 m jordad 3G1,5 donor extension lead är kandidat, men faktisk in+ut-längd kontrolleras mot bord/eluttag/DeWalt innan den kapas
- KJD12 ska placeras så stoppet är direkt nåbart från normal operatörsplats

## Bord / underrede

Huvudspår:
- begagnat styvt **160–180 cm långt**, helst 90–100 cm djupt
- helst <=700 kr
- behåll befintlig skiva
- skruva/bulta avtagbar ~1000×1620 OSB/ply CNC-deck ovanpå
- separat ~12 mm MDF-spoilboard
- på 90 cm-bord: verifiera/bygg lokalt stöd och säker infästning under deckens ~50 mm långsidesöverhäng där LR4 rail/wheels/belt clips arbetar

Se `TABLE.md` och `AUDIT.md`.

## Ska inte köpas ännu

- stepper-extensioner före dry-fit av motorernas befintliga 1 m-ledningar; 2–3 kan behövas enligt V1E-layouten
- router-förlängningskabel före full-travel dry-fit
- microSD eller USB-C innan befintligt lager hemma inventerats
- Jackpot-fläkt före verkligt kylbehov
- extra 1/8"-spännhylsa
- lång plywoodfräs före konkret jobb
- T-track / insert-grid / vacuum-table före verkligt behov
- ny grovdammsugare eller ny slang innan befintlig DeWalt-lösning testats
- laserutrustning före 2027
- prestandauppgraderingar innan standardmaskinen fungerar

## Nästa sourcingarbete

Ingen bred komponentjakt behövs nu.

Återstår främst:
1. verifiera 16T-checkout
2. verifiera slutliga checkout-totaler på låsta huvudkorgar, särskilt DigiKey faktisk frakt
3. LaskaKit: välj 5 m-rulle eller 3×2 m fallback efter lager + exakt 2-core 20 AWG-variant
4. välj mindre LV-kabelgenomföring efter verklig ~4,8 mm kabel-OD
5. kontrollera Motonet-rören fysiskt
6. hitta/inspektera ett faktiskt 160–180 × helst 90–100 cm bord
7. ändra bara produktval om pris, lager, kompatibilitet eller fysisk dry-fit ger ett konkret problem