# Cost ledger

Kanonisk regel: **faktiskt debiterat SEK-belopp vinner** för projektkostnad. Leverantörens EUR/USD-belopp sparas bara för avstämning. Ej lagda order räknas inte som spenderat.

## Budgetram

Den ursprungliga LowRider-bedömningen var **cirka 7 000–9 000 kr totalt**. I den bredare PrintNC/LowRider-jämförelsen användes **8 000–12 000 kr** som yttersta totalram, inte som målkostnad.

Praktiskt mål för detta bygge: håll färdig standardnära LR4 nära **9 000 kr** om det går utan att kompromissa bort rätt delar eller säker el.

## Faktiskt betalt

| Datum | Leverantör | Innehåll | Ordervaluta | Faktiskt debiterat |
|---|---|---|---:|---:|
| 2026-08-29 | HaWiWe | XZ-plattor 6 mm + 4× MGN12H + LR4 screw set + Elaire/Makita 1/8" collet | 165,50 € inkl 8,00 € frakt | **1 853 kr** |
| 2026-09-03 | Elecrow | Jackpot3 `CQA240812C2` + DDP Economy | 83,55 € totalt | **937 kr** |
| 2026-09-03 | eBay / POWGE Synchronous Belts and Pulleys | 3 × 2GT/GT2 drive pulley, 16T, 5 mm bore, för 10 mm belt | eBay-listning visade US$5.99, fri frakt, importavgifter inkluderade | **72 kr** |
| 2026-09-03 | LaskaKit | 6 × smooth GT2-idler + T8×8 400 mm + 2 × 5→8-koppling + 5 m GT2 10 mm glasfiber; **mässingsmuttrar ingår inte** | 39,68 € inkl 8,93 € GLS Sweden | **444 kr** |
| 2026-09-03 | eBay / HKGY01 | 2 × flänsad T8×8 mässingsmutter, 2 mm pitch / 4-start / 8 mm lead — **annullering väntar efter out-of-stock-besked** | listning visade US$4.34 + US$1.00 frakt, `Includes import fees` | **67 kr** |
| 2026-09-03 | DigiKey | HDR-60-24 + 10 Omron endstops + 16×608-2RS + Wago + kabelgenomföringar + TE Faston + 13 m kablage + 3× Molex 2-poliga pigtails | 789,58 kr varor + 197,40 kr moms, fri UPS DDP | **986,98 kr** |
| 2026-09-03 | Amazon.se | 5 × STEPPERONLINE `17HS19-2004S1`, 59 Ncm / 84 oz-in, 2 A | SEK | **608,37 kr** |
| 2026-09-03 | Amazon.se / AIM Tools Ltd | KATSU `101750`, 220–240 V, 710 W, ~65 mm Makita-formfaktor | SEK | **620,00 kr** |
| 2026-09-05 | Amazon.se / euroharry | 4 × flänsad T8-mässingsmutter, Ø8 mm / 2 mm pitch / 4-start / 8 mm lead; 2 används + 2 reserv | SEK | **101,76 kr** |
| 2026-09-06 | PrintOnion | 3 kg PLA 1,75 mm för LR4-printarna | SEK | **426 kr** |
| 2026-09-07 | Motonet | 2 × stålrör för LR4, planerad spec Ø30×1,5×2000 mm | SEK | **340 kr** |

**Verifierat faktiskt debiterat hittills: 6 456,11 kr.**

Användaren bekräftade 2026-09-10 att **samtliga hittills lagda inköp är debiterade**. För Amazon-orderna används de redan dokumenterade SEK-orderbeloppen ovan eftersom inga avvikande debiteringsbelopp har rapporterats.

## Väntande återbetalning

- **67 kr — eBay / HKGY01.** Säljaren uppgav 2026-09-05 att T8×8-muttrarna var slut och bad köparen annullera. Annulleringsbegäran är skickad och återbetalningen är ännu inte verifierad.
- Tills återbetalningen är bekräftad ligger 67 kr kvar i brutto faktiskt debiterat ovan.

**Aktiv faktisk projektkostnad exklusive HKGY01-order som annulleras: 6 389,11 kr.**

Elecrow-avstämning: controller 69,44 € efter rabatt + DDP Economy 14,11 € = 83,55 €.

eBay-remhjul: faktisk SEK-debitering **72 kr** är facit oavsett listningens visade ungefärliga SEK-/USD-belopp. Annonsen angav fri frakt och `Includes import fees`.

LaskaKit-avstämning: varor **30,75 €** + GLS Sweden **8,93 €** = **39,68 €**. De två T8×8-mässingsmuttrarna var otillgängliga och ingår därför inte i ordern eller kostnaden.

eBay T8×8-muttrar: vald variant **T8 × 8 mm**, **2 Pcs**, quantity 1. Faktisk debitering **67 kr**. Ordern är på väg att annulleras på säljarens begäran p.g.a. out of stock; bokför inte någon återbetalning förrän den faktiskt är verifierad.

Amazon-orderna: användaren bekräftade 2026-09-10 att motorer, KATSU-router och euroharry T8-muttrar är debiterade. Inga avvikande SEK-belopp rapporterades, därför används orderbeloppen **608,37 + 620,00 + 101,76 = 1 330,13 kr** som debiterade värden.

PrintOnion PLA: **3 kg för 426 kr**, köpt 2026-09-06. Detta ersätter den tidigare 3DJake-baseline på 559 kr landat.

Motonet-rör: **2 st för totalt 340 kr**, köpta 2026-09-07. Planerad spec är Ø30×1,5×2000 mm; kapa först efter fysisk kontroll/mätning.

DigiKey-avstämning: delsumma **789,58 kr**, frakt **0 kr**, svensk VAT **197,40 kr**, total **986,98 kr**. Fraktmetod: **UPS Worldwide Saver, DDP**.

## Kvarvarande köp — ej spenderat ännu

Aktuella estimat finns i `PROCUREMENT.md`. Kärnmekanik, elektronik, router, PLA och rör är nu köpta/beställda och debiterade. Kvar är främst bord/spoilboard, strutmaterial, senare NVR/kapsling/elmaterial, commissioning-fräs och dammhantering.

## Kostnadsdisciplin

- använd faktisk SEK-debitering som facit
- behåll leverantörens valuta för felsökning/retur
- frakt, moms, DDP och avgifter ingår i faktisk projektkostnad
- gamla snapshots får inte räknas som spenderat
- annullerad order ligger kvar som debiterad tills återbetalningen verifierats
- budgeten inkluderar de delar som behövs för en körklar standardmaskin; senare laser/plasma/T-track/vacuum-table räknas som separata uppgraderingar
