# LED-fäste – HORISONTELL understrut, LowRider V4

**2026-11-10: korrigerad CAD-prototyp, ej fysiskt monterad.** Tidigare version (före commit `45695db`) är **FELAKTIG**, roterade strutplattan 90° och utgick från en vertikal kant. **Använd inte den äldre STL-/STEP-filen eller illustrationsbilden.** Den tidigare lokala CAD-exporten var av en annan konstruktion.

## Ursprung och verifierade mått

- V1E LowRider V4 har en **vertikal frontstrut och en horisontell understrut** (två olika plattor). Originalmontering: [V1E Beam Assembly](https://docs.v1e.com/lowrider/#beam-assembly), [V1E permanent strut-montage](https://docs.v1e.com/lowrider/#temp-to-custom-strut-plates).
- I **projektets egen** [`strut_plate.svg`](../../../strut_plate.svg) finns två rader med M5-hål på varje platta, **56,0 mm mellan raderna** och **160,2 mm mellan brace-positioner längs X**. För den första plattformen är två närliggande rader t.ex. y=-61,75 och y=-5,75 mm (center y=-33,75 mm). Motsvarande två rader finns på den andra plattformen. Dessa är **ritningsmått**; mät mot verklig montering om något avviker.
- CAD: X längs strutplattan, Y tvärs, Z upp, den **horisontella understrutens undersida = z=0**. Hålcentrum vid (x=0, y=±28) och borrning i z-led. M5-skruvarna är befintliga låsskruvar till **Brace**. Ingen U-klämma eller antagen lodrät 6 mm-kant används.

## CAD nu — 35° med cirka 6,6 mm nedstick (2026-11-10)

**Aktuell parametrisk build123d-källa:** [`tre_vinklar.py`](tre_vinklar.py). Uppdaterade provvinklar är **0°/15°/35°**, fortfarande **en nedåt och två framåt**. 35° ersätter 30° efter användarens godkännande av cirka 6,6 mm för fästet. Den visuella och mekaniska lösningen är **inte fysiskt godkänd**.

- Strutundersidans plan definieras som **Z=0**. Fästet ligger under den horisontella plattan. **Två befintliga M5/Brace-hål 56 mm c/c**, med 1,0 mm tunn central monteringswebb och 2,2 mm lokal förstärkning vid M5. Ingen 90°-vänd klämma eller ny fästborrning.
- **8 mm COB** limmas på **9 mm breda**, 1,6 mm tjocka hyllor med 0,5 mm marginal per sida. Små radier/fasningar används på yttre hörn; LED-ytans plana bredd och verklig tejpadhesion ska kontrolleras.
- Längsgående **kantstag 1,2 mm** går på baksidan av de lutade 15°- och 35°-hyllorna, från nedre kanten upp mot **0,9 mm tunn överyta** i kontakt med understruten. 0°-hyllan har också överdel. Stagen ökar inte utsticket under LED-hyllans lägsta punkt i CAD, men faktisk passning och styvhet återstår.
- **Hård CAD-gräns `max_z_intrang_mm=6.65`:** 35° med 9 mm hylla ger **6,62 mm teoretisk yttergräns**, avrundat cirka 6,6 mm. Gränsen gäller **bara fästet**. LED-remsans och tejpens tjocklek, lödpunkter, eventuellt uppstickande skruvskallar eller verkliga maskinens kollisionsvolym ingår inte. Den gamla 30°-modellen gav lokalt cirka 5,94 mm, men siffran kan **inte** återanvändas som uppmätt värde för 35°.
- Parametrar för vinkel, hyllbredd, stag, M5 pitch, centrumavstånd, Z-gräns och modullängd är ändringsbara. En 10 mm hylla skulle vid 35° ge cirka **7,20 mm** och stoppas av gränsen.
- Ett segment är **154 mm** och M5-stationerna är **160,2 mm** från varandra. Behov av anpassade ändmoduler och antal moduler kontrolleras på verklig maskin.
- **Ogiltig gammal CAD:** första 90°-felet, följande ~21 mm nedhängande modell och äldre 0°/15°/25° eller 0°/15°/30° som standard. Ingen tidigare uppladdad STL/STEP ska antas motsvara aktuell källkod.

### Export / kontroll

```bash
python -m pip install 'build123d==0.10.0'
python machine/delar/led/tre_vinklar.py --ut export/led
python machine/delar/led/tre_vinklar.py --vinklar 0 15 35 --max-z-intrang 6.65
```

[GitHub Actions](https://github.com/kingkongola/lowrider/actions/workflows/led-tre-vinklar.yml) är uppdaterad med **Z-gräns 6,65 mm**, korrekt 35°/9 mm-variant och test att 10 mm vid 35° underkänns. **Ingen CI-körning har kontrollerats i detta dokument**. Vattentät/sammanhängande build123d-STL, M5-skruvlängd, plats för Brace, printbarhet, lys-/kylprov och hela XYZ-svepet återstår att verifiera.

## Kabeldragning — monteringsplan, ännu ej borrad

1. Tre LED-remsor får **varsin lödd +24 V- och GND-ledning** och ansluts **parallellt** i en skyddad förgrening med gemensam säkrad 24 V-matning; aldrig i serie. Tre ungefär 0,8 m remsor ger uppgivet cirka **24 W / 1 A totalt**.
2. Löd- och kappositioner väljs efter verklig Brimeti-remsspecifikation, lägg krympslang/isolering och **mekanisk dragavlastning** på varje remsa, så att flexkortets kopparpads inte bär kabelns rörelser.
3. Försök först ta ledningarna **runt befintlig öppning eller plattkant**. Om det inte blir skyddat och prydligt: planera **en gemensam kabelgenomföring** genom den horisontella understrutplattan, inte ett hål per remsa. **Hålcentrum och diameter är medvetet inte låsta** (4–5 mm är en tänkbar storleksordning, beroende på verklig kabel och genomföringsskydd).
4. Markera föreslaget hål på den faktiskt monterade plattan, **kontrollera båda sidor** så att det inte skär M5/Brace-låsning, rör, fästöron eller bärande smala bryggor. Ingen borrning innan sådan kontroll och kallt XYZ-svep. Avgrada och använd genomföringsskydd, samt dragavlasta vid plattan.
5. Låt kabeln följa redan planerad balk-/rörelsekabelväg med korrekt böjradie och säkring. **Håll lågspännings-LED åtskilt från 230 V**. Fastställ längd först efter komplett rörelseprov. Se [CABLE_ROUTING.md](../../../CABLE_ROUTING.md).
6. **CAD efter verklig torrpassning:** lägg in kabelöppning/notch och separat clips/dragavlastning som parametrar *om det behövs*. Ingen borrposition är någonsin härledd ur enbart SVG.

## Spärrar före riktig montering

1. Kontrollera visuellt underplattans orientering, vilka låsskruvar som är tillgängliga och om M5-skallarna kan dras åt med fästet på plats. Verifiera yttre avstånd till X-rör, Core, dammsko, motorer och full XYZ-rörelse. Glöm inte skruvarna som ställer maskinens heal/toe.
2. Kontrollera **skruvlängd och låsning** när den nya 2,2 mm tjocka lokala bossen placeras under skruvskallarna.
3. Provprinta **ett** segment i PETG, kontrollera passning mot original-Brace och kör en kall full-svep/kollisionstest före elanslutning.
   Kontrollera även att **kantstaget inte skymmer 8 mm LED-ytan**, att det tunna överlocket ligger an mot understruten och att det **inte bärs endast av en tunn punktkontakt** vid den centrala tvärwebben. Testa försiktigt böjning av fria ändarna; dimensionera om om de kan vibrera eller deformeras synbart.
4. Testa BRIMETI på faktisk PETG-yta med övervakad temperatur vid full 24 V/10 W/m, minst under en längre körning. Tejp direkt på PETG har sämre termisk ledning än aluminium. Vid för hög temperatur eller opålitlig tejp: ändra lösning. Ingen aluminiumprofil är ett krav för **första provet**, men termisk lämplighet är ännu inte bevisad.
5. Kontrollera kamera/reflexer/skuggor och riktning. Vinklarna är justerbara provvärden, inte beslutade slutvinklar.

**Originalkonstruktionens mekanik är inte fysiskt avläst i denna körning.** `strut_plate.svg` och V1E:s montage har kontrollerats; original-Brace-3D-geometri har inte importeras till CAD. Kalla därför inte denna lösning print-/driftklar ännu.
