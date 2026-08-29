# Procurement optimization

Syfte: optimera **hela bygget**, inte varje komponent isolerat.

Målet är lägsta vettiga totalpris inklusive artikelpris, frakt, moms/import, variant-/kvalitetsrisk och risken att behöva köpa om något.

Den här filen är den kanoniska orderöversikten. Daterade filer i `research/` är evidens/historik.

## Redan betalt

### HaWiWe — CLOSED
**165,50 € inklusive 8,00 € frakt**.

Täcker:
- aluminium XZ-plattor
- 4 × MGN12H 150 mm rails
- LR4 screw set
- Elaire/Makita-style 1/8" collet

## Låst geometri

- användbar yta: **650 × 1250 mm**
- rör: **816 / 816 / 1505 mm**
- strut: **819 mm**
- GT2: **999 / 1705 / 1705 mm**, totalt **4409 mm**
- minimum bord: **941 × 1563 mm**
- praktisk CNC-deck: cirka **1000 × 1620 mm**

## Aktuell optimerad ordergraf

### 1. Motonet — rör, lokal pickup
- 2 × `88-7123`
- Ø30×1,5 mm ×2 m
- observerat 189 kr/st = **378 kr**
- kontrollera OD/rakhet/bucklor före köp

### 2. LaskaKit — mekanik + lågspänningskabel
Behåll denna korg intakt:
- 6 × `LA190008E` smooth idlers
- 1 × `LA190032A` T8×8 400 mm rod
- 2 × `LA190033A` T8×8 brass nuts
- 2 × `LA190031` 5→8 couplers
- 1 × `LA190013C` 5 m / 10 mm fiberglass GT2 belt
- 10 m `LA150151A` endstop cable
- ~1 m UL2464 20 AWG **2-core** PSU-output cable
- board-side endstop connector/pigtail route efter om lämplig crimper finns

Aktuell korgklass: cirka **€49–55 levererat** beroende på connector-route.

### 3. StepperOnline Germany — motors only
- 1 × fempack `5-17HS19-2004S1`
- 59 Ncm / 83,55 oz-in / 2 A
- 1 m kabel
- Germany warehouse
- observerat ~€38–42 beroende storefront

Germany warehouse levererar till Sverige. Köp inga China-only delar i denna korg.

### 4. DigiKey — GLOBALT OPTIMERAD fri-frakt-korg

Detta ersätter tidigare HDR+Omron-only-korg samt separata 608/Wago/M20/Faston-köp.

Köp:
- 1 × Mean Well `HDR-60-24` / `1866-2249-ND`
- 10 × Omron `SS-3GL13PT` / `SW768-ND`
- **16 × `608-2RS-W/CHEVRONSRI2`** / `1995-1010-ND`
  - exact 8×22×7 mm, two contact seals
  - 14 installeras + 2 reserv
- 3 × genuine Wago `221-413`
- 2 × Altech `5309 720/SET`
  - M20×1.5, IP68, 5–12 mm kabel, locknut included
- 10 × TE Connectivity `3-350820-2`
  - Ultra-Fast 250 female
  - 6.35×0.8 mm
  - fully insulated, 14–16 AWG

Beräknad total med aktuella priser: **~622 kr inkl moms**.

DigiKey Sveriges fri-fraktgräns är **615 kr**, så denna korg ska ge fri frakt.

Detta tar bort behovet av:
- Tradera/Fyndiq/Kullager.se för 608
- Jula Wago-pack
- Jula M20 glands
- Biltema Faston-pack

Det är inte filler buying: alla rader behövs i bygget, med endast små reservmarginaler.

Se `research/2026-08-29-global-cart-optimization.md`.

### 5. VEVOR EU — router
- exact **VEVOR 0700C**
- SKU `YXKXBJ710W65AH7WLV2`
- product ID `010235793217`
- 800 W / 65 mm / 10k–30k rpm
- observerat **€83,99**

Provpassa redan köpt Elaire-collet och kontrollera runout efter ankomst.

### 6. Elecrow — Jackpot3
- exact `CQA240812C2`
- observerat **US$76,99**
- slutlig Sverige-frakt/VAT/import fortfarande checkout-gated

Jackpot2 ska inte återöppnas som default.

### 7. SUNLU — PLA
- ordinary PLA
- 6 × 1 kg normala spolar
- köp om Sverige-checkout håller ungefär **100–110 kr/kg levererat**

### 8. Sorotec — commissioning cutters
- 3 × `L1S.M.0317`
- 3,175 mm single-flute upcut
- cirka **€19,40 levererat** enligt senaste verifiering

Ingen lång plywoodfräs ännu.

### 9. GT2 16T — enda riktiga mekaniska orphan-raden

Need 3 exact:
- GT2 / 2 mm pitch
- 16T
- 5 mm bore
- 10 mm belt

Preferred exact Allegro:
- `GT2-16T-5B_10mm_K`
- dual grub screws
- raw price mycket låg

Köp om 3 st blir **≤150–180 kr levererat till Sverige**.

DigiKeys 16T-del är för 6 mm rem och är fel; den ska inte användas för att konsolidera.

### 10. KEDU KJD12 — separat säkerhetsdel

Ny stark EU-kandidat:
- CEM Elettromeccanica
- genuine **KEDU KJD12**
- bipolar
- emergency-stop mushroom/cover
- 15 A / 230 V
- IP54
- VDE/TUV
- 6.3×0.8 Faston
- **€14,90 inkl VAT** före Sverige-frakt

Om CEM:s Sverige-checkout ger en rimlig frakt och total klart under ~500 kr är den bättre än IKH-fallbacken (~482 kr) eftersom tillverkaren uttryckligen är KEDU.

### 11. Biltema — lokal elbox-korg
Efter DigiKey-konsolideringen återstår främst:
- `35-0065` IP65 4-module enclosure — 99,90 kr
- `46-3610` 3 m jordad 3G1,5 donor extension cord — 59,90 kr

Wago, M20 glands och Faston köps inte längre här.

### 12. Bord / deck / spoilboard

**180 cm är inte krav.**

Sök nu:
- **160–180 cm långt**
- helst 90–100 cm djupt
- stabilt/vridstyvt
- helst ≤700 kr

160×90 fungerar: vår ~1620 mm deck överhänger bara ~10 mm per kortände.

Se `TABLE.md`.

## Damm

Behåll befintlig plan:
- ägd DeWalt shop-vac
- printad dust shoe
- printad cyclone
- separat styv 15–30 l behållare
- testa befintlig 48 mm ×2,1 m slang först
- printa adaptrar
- slangbom/dragavlastning

## Småsaker / explicit inte köp

- **ingen Loctite/threadlocker ska köpas**; befintlig används
- stepper-extensioner först efter dry-fit; manualen gör 2–3 förlängningar sannolika men inte säkra på vår kompakta maskin
- ingen T-track/clamp-korg före verkligt behov
- ingen lång plywoodfräs före konkret jobb
- ingen extra 1/8" collet

## Nuvarande slutsats

Korgarna är nu optimerade på **hela levererade totalen**, inte per komponent.

Största vinsten är DigiKey-konsolideringen: den passerar fri-fraktgränsen med delar vi ändå behöver och eliminerar flera små separata köp.

Kvar som verkligt checkoutarbete:
1. Allegro 16T Sverige-total
2. StepperOnline Germany→Sweden-frakt
3. LaskaKit slutlig total + 2-core variant
4. Elecrow Jackpot3 landad kostnad
5. CEM genuine KEDU Sverige-frakt
6. SUNLU checkout

Ändra inte specifikationer bara för att minska antal paket.