# Systemaudit

**Current 2026-09-19.** Den här filen innehåller stabila system-/fysiska gates. Flyktiga priser och lager hör hemma i `PROCUREMENT.md`/`SOURCING.md`; faktisk kostnad i `COSTS.md`.

## Samlad bedömning

Grundarkitekturen håller:
- LowRider V4
- 650×1250 mm arbetsyta
- Ø30×1,5 mm rails
- StepperOnline 59 Ncm motorer
- **köpt Elecrow Jackpot3**
- HDR-60-24
- Omron NC endstops
- KATSU 101750
- fast NVR/maskinstopp + rörlig Jackpot3 och planerat balkmonterat HDR-60-24; korrekt kapsling och infästning återstår

Ingen audit kräver ändrad maskingeometri.

## Mekanik — verifierat

- X-rör 816 mm ×2
- Y-rör 1505 mm
- strut 819, `front_wing_size=30`
- GT2 999 / 1705 / 1705 = 4409 mm
- 3 × GT2 16T, 5 mm bore, 10 mm belt — köpta, ej mottagna 2026-09-19
- 6 × smooth idler, 5 mm hole, 10 mm belt
- 14 × 608-2RS installeras + 2 reserv
- T8×8, 4-start, 8 mm lead
- T8 400 mm kapas efter assembly-check; ~150–160 mm ×2 praktiskt mål

## Print — verifierat

P1S 256³ är tillräcklig. Före full sats:
- senaste LR4-filer
- alla diameterberoende delar = 30 mm
- tool mount = Makita/65 mm
- `Z_Stub` + `Z_Nut` testfit
- slicer-preview av bridges/unsupported geometry

## Controller/elektronik

**Elecrow Jackpot3 `CQA240812C2` är köpt 2026-09-03 enligt D015.** Inköpsvalet är stängt. Före driven rörelse:
- kontrollera kortet vid leverans
- flasha V1E:s då aktuellt testade FluidNC/LR4-config
- kontrollera motorutgångar
- kontrollera varje endstopstatus
- börja jogga 1 mm i taget
- inventera data-USB-C + FAT32 microSD

Endstops är home/auto-square och **inte runtime hard limits**.

## 24 V och kabelrörelse

Aktuell plan enligt D016: HDR-60-24 och Jackpot3 följer balken, med kort 24 V-matning mellan dem. Den tidigare långa rörliga 24 V-rutten är inte längre grundlösningen.
- verifiera balkens infästning, beröringsskydd/kapsling av 230 V-plintar, skyddsjordning och dragavlastning för vårt specifika DIN-aggregat
- förlägg nätmatningen till aggregatet säkert tillsammans med fräskabeln enligt fysisk full-travel-kontroll
- den redan köpta 3 m 20 AWG-kabeln är reserv/längdmarginal, inte något som måste installeras

Före slutliga clips/remspänning ska följande vara samtidigt monterat och testat i alla fyra hörn + Z-extremer:
- nätmatning till HDR samt kort 24 V-rutt
- routerkabel
- motor/endstopkablar
- vac-hose

Inget får sträckas, kinka, bära kontaktlast eller falla in i rörelsezonen.

## 230 V

- NVR/maskinstopp ska vara direkt nåbar.
- exakt terminalschema för levererad NVR ska följas.
- PE är kontinuerlig/oswitchad.
- inga åtkomliga spänningsförande delar med boxen stängd.
- PE-kontinuitet + kontroll mot L/N före energisering.
- verifiera no-restart med router frånkopplad.
- kapsling väljs efter fysisk dry-fit, inte på katalogmått.

Garagegruppen 10 A är inte en blockerande gate. Gör sanity-check vid första samtidiga DeWalt + KATSU-körningen. Utred först om säkringen faktiskt löser. Uppsäkra inte som workaround.

## Router

KATSU 101750, 220–240 V / 710 W, är köpt router. Den äldre VEVOR 0700C är ersatt och ska inte köpas.

Fysisk gate:
- provpassa köpt Elaire/Makita-style 1/8" collet
- korrekt säte
- runout innan riktig fräsning

## Damm

Före regelbunden MDF/trä/XPS:
- fungerande dust shoe/cyclone
- behållaren vakuumtestad
- slangen avlastad från gantry/Z
- definierad statisk jordväg/groundable lösning verifierad

HDR-60-24 är inte jordpunkt.

## Fysiska gates som blockerar slutgodkännande

1. HaWiWe: transportskada + fyra produktgrupper + M3×10/XZ/MGN-passning.
2. Jackpot3: transportskada/korrekt kort vid leverans.
3. Motonet-rör: verklig OD/rakhet före kapning.
4. Köpt 180×100-bordsskiva: racking/planhet/underrede och rail-/belt-layout; ingen 90 cm-kantbreddning.
5. KATSU/Elaire: collet-säte + runout.
6. DeWalt: exakt typskylt före modellunika AUTO-data.
7. NVR/HDR: kapslings-dry-fit + terminalschema.
8. Full travel: alla rörliga kablar + vac-hose samtidigt.
9. Damm: behållare + statisk jordväg.
10. 230 V: PE/L/N/dragavlastning/NVR-test.

Checkout-gates är inte audit-gates och finns endast i `PROCUREMENT.md`.