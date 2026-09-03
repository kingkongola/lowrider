# Systemaudit

**Current 2026-09-03.** Den här filen innehåller stabila system-/fysiska gates. Flyktiga priser och lager hör hemma i `PROCUREMENT.md`/`SOURCING.md`; faktisk kostnad i `COSTS.md`.

## Samlad bedömning

Grundarkitekturen håller:
- LowRider V4
- 650×1250 mm arbetsyta
- Ø30×1,5 mm rails
- StepperOnline 59 Ncm motorer
- **köpt Elecrow Jackpot3**
- HDR-60-24
- Omron NC endstops
- VEVOR 0700C
- fast NVR/HDR-box + rörlig controller

Ingen audit kräver ändrad maskingeometri.

## Mekanik — verifierat

- X-rör 816 mm ×2
- Y-rör 1505 mm
- strut 819, `front_wing_size=30`
- GT2 999 / 1705 / 1705 = 4409 mm
- 3 × GT2 16T, 5 mm bore, 10 mm belt
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

HDR sitter fast, controller rör sig:
- 3 m 20 AWG 2-core som marginal
- kapa efter full-travel dry-fit
- stor mjuk loop
- UL/PVC-kabeln är inte bevisad chain-flex; byt bara om verklig routing kräver snäv repetitiv böj
- dragavlasta före controllerkontakten

Före slutliga clips/remspänning ska följande vara samtidigt monterat och testat i alla fyra hörn + Z-extremer:
- 24 V
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

Garagegruppen 10 A är inte en blockerande gate. Gör sanity-check vid första samtidiga DeWalt + VEVOR-körningen. Utred först om säkringen faktiskt löser. Uppsäkra inte som workaround.

## Router

VEVOR 0700C är 220–240 V / 800 W. Marknadsföringstexten “6.5 A” används inte som EU-märkström.

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
4. Bord: racking/planhet/kantstöd.
5. VEVOR/Elaire: collet-säte + runout.
6. DeWalt: exakt typskylt före modellunika AUTO-data.
7. NVR/HDR: kapslings-dry-fit + terminalschema.
8. Full travel: alla rörliga kablar + vac-hose samtidigt.
9. Damm: behållare + statisk jordväg.
10. 230 V: PE/L/N/dragavlastning/NVR-test.

Checkout-gates är inte audit-gates och finns endast i `PROCUREMENT.md`.