# LED-fäste – HORISONTELL understrut, LowRider V4

**2026-11-10: korrigerad CAD-prototyp, ej fysiskt monterad.** Tidigare version (före commit `45695db`) är **FELAKTIG**, roterade strutplattan 90° och utgick från en vertikal kant. **Använd inte den äldre STL-/STEP-filen eller illustrationsbilden.** Den tidigare lokala CAD-exporten var av en annan konstruktion.

## Ursprung och verifierade mått

- V1E LowRider V4 har en **vertikal frontstrut och en horisontell understrut** (två olika plattor). Originalmontering: [V1E Beam Assembly](https://docs.v1e.com/lowrider/#beam-assembly), [V1E permanent strut-montage](https://docs.v1e.com/lowrider/#temp-to-custom-strut-plates).
- I **projektets egen** [`strut_plate.svg`](../../../strut_plate.svg) finns två rader med M5-hål på varje platta, **56,0 mm mellan raderna** och **160,2 mm mellan brace-positioner längs X**. För den första plattformen är två närliggande rader t.ex. y=-61,75 och y=-5,75 mm (center y=-33,75 mm). Motsvarande två rader finns på den andra plattformen. Dessa är **ritningsmått**; mät mot verklig montering om något avviker.
- CAD: X längs strutplattan, Y tvärs, Z upp, den **horisontella understrutens undersida = z=0**. Hålcentrum vid (x=0, y=±28) och borrning i z-led. M5-skruvarna är befintliga låsskruvar till **Brace**. Ingen U-klämma eller antagen lodrät 6 mm-kant används.

## CAD nu

[`tre_vinklar.py`](tre_vinklar.py) i **build123d** skapar ett provfäste som sitter **under den horisontella bottenplattan** med två befintliga M5-hål på samma brace-station.

- **Tre långa hyllor** för **8 mm COB**: en rakt ned (0°) och två framåt (25° och 50° initialt).
- Hyllorna är 10 mm breda och 154 mm långa med smal ryggförstyvning på den icke lysande sidan.
- Gemensam tvärgående adapter 78 mm längs Y, 18 mm längs X och 3 mm tjock, med **två genomgående Ø5,4 mm** M5-hål (56 mm c-c).
- Alla mått (LED-bredd, vinklar, framriktning, M5-avstånd och längd) är parametrar; `--fram-sida -1` vänder strålriktningen. Vid annan vald monteringsstation måste geometrin speglas i rätt Y-riktning.
- Installera inte fästet genom att bara återanvända befintliga 30 mm låsskruvar utan att kontrollera **grepp-/gängingrepp**: fästets 3 mm byggmått kan kräva längre M5. Spänn inte om Brace på måfå – maskinens riktning/kalibrering kan påverkas.
- 154 mm är ett segment, inte ett bevisat komplett montage: hålstationspitch är 160,2 mm och ändstationerna ligger nära plattans ändar. **Full täckning och eventuella kortare ändmoduler behöver dimensioneras och prova på riktiga maskinen**. Prova en mittstation först.

## Exportera

```bash
python -m pip install 'build123d==0.10.0'
python machine/delar/led/tre_vinklar.py --ut export/led
python machine/delar/led/tre_vinklar.py --vinklar 0 20 45 --led-bredd 8.2 --m5-pitch 56
```

GitHub Actions: [led-tre-vinklar.yml](https://github.com/kingkongola/lowrider/actions/workflows/led-tre-vinklar.yml). Exporterar STL/STEP och kontrollerar vattentät mesh/antal solider; **CI-status och fysisk verklig passning är inte verifierade här**. En lokal motsvarande **CadQuery**-modell är exporterad och kontrollerad som en sluten solid, men den ersätter inte verifiering av build123d-exporten.

## Spärrar före riktig montering

1. Kontrollera visuellt underplattans orientering, vilka låsskruvar som är tillgängliga och om M5-skallarna kan dras åt med fästet på plats. Verifiera yttre avstånd till X-rör, Core, dammsko, motorer och full XYZ-rörelse. Glöm inte skruvarna som ställer maskinens heal/toe.
2. Kontrollera **skruvlängd och låsning** om den 3 mm tjocka adaptern ska placeras under skruvskallarna.
3. Provprinta **ett** segment i PETG, kontrollera passning mot original-Brace och kör en kall full-svep/kollisionstest före elanslutning.
4. Testa BRIMETI på faktisk PETG-yta med övervakad temperatur vid full 24 V/10 W/m, minst under en längre körning. Tejp direkt på PETG har sämre termisk ledning än aluminium. Vid för hög temperatur eller opålitlig tejp: ändra lösning. Ingen aluminiumprofil är ett krav för **första provet**, men termisk lämplighet är ännu inte bevisad.
5. Kontrollera kamera/reflexer/skuggor och riktning. Vinklarna är justerbara provvärden, inte beslutade slutvinklar.

**Originalkonstruktionens mekanik är inte fysiskt avläst i denna körning.** `strut_plate.svg` och V1E:s montage har kontrollerats; original-Brace-3D-geometri har inte importeras till CAD. Kalla därför inte denna lösning print-/driftklar ännu.
