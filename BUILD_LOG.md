# Build log

## 2026-08-29 — initial design/procurement pass

- Privat GitHub-repo skapat för LowRider V4-bygget.
- Maskinvalet avslutat: LowRider V4.
- HaWiWe-order lagd och betald: 165,50 € inklusive 8,00 € frakt.
- Arbetsytan låst till 650 × 1250 mm.
- Exakt geometri: rör 816 / 816 / 1505 mm, strut 819, GT2 999 / 1705 / 1705 mm, minimum bord 941 × 1563 mm, deck ~1000×1620 mm.

## 2026-08-29 — oberoende system-/fysisk audit

- 24 V-rutten korrigerades till 3 m marginal + full-travel dry-fit.
- alla diameterberoende prints = 30 mm; strut `819` + `front_wing_size=30`.
- 90 cm bord godkändes med explicit kantstöd.
- KJD12 benämns NVR/maskinstopp, inte safety-rated E-stop.
- statisk jordning blev gate.

## 2026-08-30 — commissioning-audit

- T8 400 mm kapas efter assembly-check; ~150–160 mm ×2.
- microSD + data-USB-C inventeras före köp.
- endstops = home/auto-square, inte runtime hard limits.

## 2026-08-30 — sourcingoptimering

- DigiKey absorberade lågspänningskablar för att undvika separat order.
- PLA-behovet korrigerades till cirka 2,7 kg → köp 3 kg, inte 6 kg.

## 2026-09-03 — HaWiWe skickat + full repo reconciliation

- HaWiWe har skickat den redan betalda ordern.
- En tydlig kanonisk hierarki infördes: `PROCUREMENT.md` är enda ordermatrisen; BOM innehåller specs/kvantiteter; sourcing innehåller evidens; audit innehåller fysiska gates.
- Clas Ohlson KJD12 230 V/10 A verifierades till 299 kr som enkel NVR-kandidat.

## 2026-09-03 — verkliga kostnader + Jackpot3 köpt

- HaWiWe faktisk bankdebitering: **1 853 kr**.
- Jackpot3 `CQA240812C2` köpt från Elecrow: **937 kr** faktiskt debiterat.
- `COSTS.md` skapades som kanonisk ledger; SEK-debitering är facit framåt.

## 2026-09-03 — mekanik och commodity sourcing

- LaskaKit-order: 6 idlers, T8×8 400 mm, 2 kopplingar, 5 m GT2 10 mm; **444 kr** faktiskt debiterat.
- eBay/POWGE: 3 × 16T / 5 mm / 10 mm drive pulley; **72 kr** faktiskt debiterat.
- DigiKey: PSU, endstops, lager och el/lågspänningssmådelar; **986,98 kr** faktiskt debiterat.
- Amazon: 5 × STEPPERONLINE `17HS19-2004S1` samt KATSU `101750` beställda.

## 2026-09-05 — HKGY01 T8×8-muttrar annulleras

- eBay-säljaren meddelade out of stock och bad köparen annullera.
- **67 kr** ligger kvar i kostnadsloggen tills återbetalningen verifierats.

## 2026-09-05 — T8×8-muttrar ersättningsköpta via Amazon

- Amazon.se/euroharry: 4 × flänsad T8-mässingsmutter, Ø8 mm, 2 mm pitch, 4-start, 8 mm lead.
- Visat orderpris: **101,76 kr**.

## 2026-09-06 — 3 kg PLA köpt från PrintOnion

- **3 kg PLA 1,75 mm** köpt från PrintOnion för **426 kr**.
- Filamentbehovet för basbygget är stängt.
- Bordstrategin förenklades: ett styvt 180×90-bord använder sin egen skiva som maskinbas; ingen full extra deck som standard.

## 2026-09-07 — Motonet-rör köpta

- **2 stålrör** för LR4 köpta på Motonet för **340 kr totalt**.
- Planerad spec är `88-7123`, Ø30×1,5×2000 mm.
- Rörsourcingen är stängd; **kapa inte ännu**.
- Före kapning ska faktisk OD, rakhet och längd verifieras. Därefter målkapning: **1505 / 816 / 816 mm**.
- Verifierat faktiskt debiterat projektbelopp var då **5 125,98 kr**; aktiv committed cost exklusive HKGY01-annulleringen **6 389,11 kr**.

## 2026-09-09 — DigiKey-paket mottaget

- DigiKey-paketet hämtat/mottaget.
- Ordern innehåller PSU, endstops, 608-lager, Wago, glands, Faston, lågspänningskablage och board-pigtails enligt BOM.
- Leveransstatus ändrad till **RECEIVED**.
- Nästa gate är att räkna av innehållet mot BOM före montering; mottaget betyder ännu inte att varje del är fysisk-verifierad.

## 2026-09-10 — T8×8-mässingsmuttrar mottagna

- Amazon.se/euroharry-paketet med **4 × flänsad T8-mässingsmutter** mottaget i postlådan.
- Spec enligt beställningen: Ø8 mm, 2 mm pitch, 4-start, 8 mm lead.
- 2 används i LR4 och 2 blir reserv.
- Leveransstatus ändrad till **RECEIVED**.

## 2026-09-10 — alla hittills lagda köp debiterade

- Användaren bekräftade att **samtliga hittills lagda inköp är debiterade**.
- Amazon-orderna flyttades därför från väntande/committed till faktiskt betalt i `COSTS.md`.
- Debiterade Amazon-belopp enligt tidigare dokumenterade SEK-orderbelopp: motorer **608,37 kr**, KATSU **620,00 kr**, euroharry T8-muttrar **101,76 kr**.
- **Brutto faktiskt debiterat hittills: 6 456,11 kr.**
- **Aktiv faktisk projektkostnad exklusive HKGY01-order som väntar återbetalning: 6 389,11 kr.**
