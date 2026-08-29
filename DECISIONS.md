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
- strut-input: **819 mm**
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
**Status:** beslutat huvudspår / audit-korrigerat

Första bordslösningen ska vara ett styvt begagnat mat-/konferens-/kontorsbord, **160–180 cm långt och helst 90–100 cm djupt**, med befintlig strukturell skiva kvar.

Ovanpå monteras en avtagbar ~1000×1620 mm CNC-deck i första hand av 11 mm OSB eller ungefär 12 mm konstruktionsplywood. Separat ~12 mm MDF används som löstagbar spoilboard.

På ett 90 cm djupt bord överhänger en 1000 mm deck cirka 50 mm per långsida. Där ska LR4:s rail/wheel/belt-clip-zon få verkligt lokalt stöd och säker infästning; använd blockning/list eller genomgående infästning om befintlig bordsskiva inte bär kanten.

Prisregler:
- 0–400 kr: starkt köp om geometri + rackingtest passerar
- 400–700 kr: normal Pareto-zon
- 700–1000 kr: endast tydligt högkvalitativt/styvt kommersiellt underrede
- >1000 kr: normalt vänta

Ingen torsionsbox, specialsvetsad ram, höj-/sänkbart skrivbord eller hjulsystem före första körningen utan konkret behov.

## D005 — Jackpot3 som styrkort
**Status:** beslutat förstahandsval

Jackpot3 väljs framför SKR Pro och äldre Jackpot-versioner om prisskillnaden inte är orimlig.

Skäl:
- aktuell V1E-standardlösning för LR4
- 6 integrerade TMC2226-drivare
- FluidNC, Wi‑Fi och webbgränssnitt
- öppna 2,54 mm stepperheaders
- full PWM på 5 V-utgångarna; möjlighet till laser senare

Elecrow-kortet kräver flashning. V1E:s vid byggtillfället aktuellt testade FluidNC + rätt LR4-config ska laddas innan driven rörelse/homing.

## D006 — VEVOR 0700C, 800 W, 65 mm som fräsmotor
**Status:** beslutat förstahandsval / fysisk verifiering återstår

Målmodell: **VEVOR 0700C, 800 W, 220–240 V / 50 Hz, 65 mm kropp, 10 000–30 000 rpm**.

Den redan köpta HaWiWe-hylsan är en Elaire Makita-style 1/8" / 3,175 mm för Makita RT700/RT0700/RT0701-familjen.

**Gate:** inget formellt VEVOR/Elaire-datablad verifierar exakt MRP-1250 + VEVOR 0700C. Hylsan ska provpassas och runout kontrolleras innan riktig fräsning. Tool mount ska vara Makita/65 mm-varianten.

## D007 — Dammhantering ingår i grundbygget
**Status:** beslutat

CNC:n delar garage med motorarbete. Dammutsug är ett grundkrav före regelbunden fräsning i trä, MDF eller XPS.

Grundlösningen:
- LR4 dust shoe för Makita/65 mm
- befintlig DeWalt shop-vac
- cyklonavskiljare, printad först
- separat styv uppsamlingsbehållare
- slangdragning/avlastning som inte belastar Core/Z
- möjlighet att begränsa och lätt städa CNC-zonen

Stockslangen är inte verifierat antistatisk. Statisk jordväg till definierad PE-punkt eller groundable hose ska vara löst före XPS/reguljär dammig drift.

## D008 — Laser senare
**Status:** uppskjutet

Laser är intressant men ska inte påverka grundbygget mer än valet av Jackpot3. Tidigast aktuellt 2027.

## D009 — Plasma inte i nuvarande scope
**Status:** bortprioriterat

Plasma ska inte styra bord, inköp eller byggordning nu. Fokus är router-CNC först.

## D010 — Mean Well HDR-60-24 + exact Omron + DigiKey-konsolidering
**Status:** beslutat förstahandskorg

24 V-nätaggregat: **Mean Well HDR-60-24, 24 V / 2,5 A / 60 W**.

Endstops: **Omron SS-3GL13PT**. Köp 10, installera 5 och behåll 5 reserv. Koppla NC, COM + NC.

DigiKey-korgen konsoliderar även 16 × 608-2RS, Wago, M20 nätgenomföringar och Faston enligt `PROCUREMENT.md`.

**Auditgräns:** DigiKey anger fri frakt vid 615 kr men vår ~622 kr är en inkl-momsuppskattning. Fri frakt räknas inte som säker förrän checkout visar den.

## D011 — Ø30 mm rails låser printvariant och strut-wing
**Status:** beslutat / audit-fynd

Motonet Ø30×1,5 mm är railspåret.

Konsekvenser:
- alla diameterberoende LR4-printar ska vara **30 mm-varianten**
- permanenta struts genereras med `strut_length=819`
- `front_wing_size=30`
- generatorns avsiktliga ~0,5 mm reduktion ska inte kompenseras manuellt

## D012 — Fast elbox + rörlig maskin gör kabelrörelse till konstruktionskrav
**Status:** beslutat / audit-korrigering

KJD12 + HDR-60-24 sitter i en **fast box på bordet**. Jackpot3 sitter separat på den **rörliga beam/YZ_Min-sidan**.

Tidigare antagande om ~1 m 24 V-kabel är borttaget.

- köp 3 m 20 AWG 2-core som längdmarginal
- kapa/terminera efter full-travel dry-fit
- 24 V-utgången får egen kabelgenomföring/dragavlastning
- routerkabel, 24 V, stepper/endstopkablar och vac-hose testas tillsammans vid alla rörelseextremer innan slutlig kabelinfästning
- Jackpot-boxen hålls separat och luftig; den ska inte stoppas in i 230 V-boxen
- UL2464/PVC-rutten ska ha stor rörelseloop; krävs snäv repetitiv böj används continuous-flex-kabel i stället

## D013 — KJD12 är NVR/maskinstopp, inte påstått safety-rated E-stop
**Status:** beslutat terminologi/säkerhetsgräns

KJD12 är verifierad som elektromagnetisk start/stop med no-voltage release/underspänningsutlösning, och varianter finns med röd emergency-stop-kåpa.

Vi har inte verifierat att den valda varianten uppfyller en specifik safety-rated E-stop-kategori/standard. Repot ska därför kalla den **KJD12 NVR/maskinstopp med röd stoppkåpa**.

Den ska:
- vara direkt nåbar från normal operatörsplats
- väljas efter exakt 230 V/50 Hz-variant, märkdata, terminalschema och mekaniska mått
- dry-fittas i kapslingen innan håltagning

## D014 — Commissioning-dependencies är del av BOM, inte eftertanke
**Status:** beslutat / andra auditpasset

Andra inköpsauditens huvudfynd är att en komplett komponentlista inte räcker om maskinen ändå inte kan flashas, köras eller verifieras.

Därför gäller:
- Elecrow Jackpot3 kräver **data-kapabel USB-C** för flashing; inventera först
- Jackpot3 behöver ett lämpligt **microSD >2 GB, FAT32, helst Class 4/6** för den föredragna G-code-filvägen; inventera först, köp bara om det saknas
- endstops är i standardkonfiguration **home/auto-square-sensorer**, inte runtime hard limits/kollisionsskydd
- printer-gate före full sats: minst 200×200×190 mm byggvolym, skew-kontroll, `Z_Stub`/`Z_Nut` testfit och bridge-preview
- 400 mm T8-stång kapas inte automatiskt i halvor; praktiskt mål är cirka 150–160 mm ×2 efter fysisk kontroll, V1E minimum 145 mm
- om 5 m GT2-rullen saknas är 3×2 m samma 10 mm fiberglass-spec en ren fallback utan skarvar

Princip: **en rad är inte godkänd bara för att delen i sig är rätt; dess monterings-, kabel-, konfigurations- och commissioning-gränssnitt måste också vara täckta.**