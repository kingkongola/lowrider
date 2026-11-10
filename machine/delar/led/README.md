# LED-fäste – HORISONTELL understrut, LowRider V4

**2026-11-10: korrigerad CAD-prototyp, ej fysiskt monterad.** Tidigare version (före commit `45695db`) är **FELAKTIG**, roterade strutplattan 90° och utgick från en vertikal kant. **Använd inte den äldre STL-/STEP-filen eller illustrationsbilden.** Den tidigare lokala CAD-exporten var av en annan konstruktion.

## Ursprung och verifierade mått

- V1E LowRider V4 har en **vertikal frontstrut och en horisontell understrut** (två olika plattor). Originalmontering: [V1E Beam Assembly](https://docs.v1e.com/lowrider/#beam-assembly), [V1E permanent strut-montage](https://docs.v1e.com/lowrider/#temp-to-custom-strut-plates).
- I **projektets egen** [`strut_plate.svg`](../../../strut_plate.svg) finns två rader med M5-hål på varje platta, **56,0 mm mellan raderna** och **160,2 mm mellan brace-positioner längs X**. För den första plattformen är två närliggande rader t.ex. y=-61,75 och y=-5,75 mm (center y=-33,75 mm). Motsvarande två rader finns på den andra plattformen. Dessa är **ritningsmått**; mät mot verklig montering om något avviker.
- CAD: X längs strutplattan, Y tvärs, Z upp, den **horisontella understrutens undersida = z=0**. Hålcentrum vid (x=0, y=±28) och borrning i z-led. M5-skruvarna är befintliga låsskruvar till **Brace**. Ingen U-klämma eller antagen lodrät 6 mm-kant används.

## CAD nu – Z-intrånget är en hård budget (2026-11-10)

**Den förra CAD-versionen ska inte printas:** dess pelare sänkte LED-ytorna till ungefär **21 mm under understrutplattans undersida**. Det var ett oacceptabelt onödigt intrång i arbetsvolymen.

Den aktuella [`tre_vinklar.py`](tre_vinklar.py) är **omarbetad till en lågprofil i build123d**:

- **Horisontell understrut** med undersida **Z=0**; LED-fästet och dess skruvbossar ligger enbart under detta plan.
- **Tre LED-banor**, 8 mm list på 10 mm breda hyllor. **En nedåt, två framåt**. Nya **provisoriska vinklar är 0°/15°/25°**, i stället för äldre 0°/25°/50°, eftersom låg Z-profil väger tyngre än den ännu oprövade branta vinkeln.
- **Nytt bärande stag 2026-11-10:** hyllan är fortsatt **1,6 mm tjock**, men varje lutad 15°/25°-bana får **ett sammanhängande 1,2 mm längsgående kantstag på baksidan** från den **lägre kanten** upp till en **0,9 mm tunn horisontell överdel** mot understrutplattan (Z=0). Överdelen och den lutande LED-hyllan bildar tillsammans en **triangulärt styvad profil** längs hela 154 mm-banan. Detta är mer relevant för styvhet i de långa ändarna än ett kort stag bara vid mittskruven. 0°-banan har också överdel men behöver inget högt kantstag. **LED:s nedre ljus-/limyta är helt fri.** 0,15 mm konstruktionsfrigång mot plattan gäller högsta punkt på lutad LED-hylla, medan överdelen ligger mot plattan. Inga extra fästdetaljer eller hål.
- **Tvärwebb 1,0 mm** tjock, med **lokal 2,2 mm förstärkning** vid de två befintliga M5/Brace-hålen (56,0 mm c/c); i stället för en heltäckande 3 mm tjock bas. Det reducerar påverkan på M5:s tillgängliga skruvlängd, men mutter/grepp måste fortfarande granskas.
- **Z-konsekvens efter förstärkning:** kantstaget ligger endast **ovanför LED-hyllans lägsta punkt** och överdelen mellan Z=-0,9 och 0. Den maximala modellen växer alltså **inte** nedåt. I lokalt CADQuery-baserat kontrollbygge av motsvarande geometri: **en vattentät kropp, min Z≈-5,74 mm, max Z=0**; det validerar inte att build123d-exporten fungerar eller att en print passar. Den fysiska kontrollen måste omfatta att överdelen får plats mot understrutten längs hela X (M5/Brace-fästena är fortsatt de enda skruvade fästpunkterna).
- Parametern `max_z_intrang_mm=6.2` är en **hård CAD-spärr**, kontrollerad innan geometri konstrueras och med verklig CAD-bounding box vid export. Det teoretiska intrånget vid `0/15/25` är cirka **5,83 mm** under plattans undersida. Befintliga skruvskallars/nuts utskjutande höjd kan redan vara större, men det får **inte antas** före faktisk kontroll.
- Med tidigare provvinkel **50°** och samma 10 mm hylla blir intrånget teoretiskt cirka **8,84 mm**, vilket nu **stoppas av kodens 6,2 mm-budget**. En mer framåtriktad bana ska vid verkligt behov placeras på en annan yta, inte bara hänga längre ned.
- Det finns fortfarande rundade ändhörn och diskret fasning: 1,2 mm radie på hylländar, 0,2 mm på långkanter, 0,7 mm på tvärwebb och 0,6 mm på M5-bossar. Plan LED-anliggningsyta kvarstår.
- Parametrarna för vinkel, hyllbredd, tjocklek, M5 c/c, Z-budget, framriktning och modullängd kan ändras.
- **Detta är prototypgeometri:** inga frigångar mot verklig brace, rör, Core/dammsko, skruvskallar eller material är ännu godkända. Förväxla inte mindre utstick med garanterad återställd användbar Z-arbetsvolym.

### Exportera och kontrollera

```bash
python -m pip install 'build123d==0.10.0'
python machine/delar/led/tre_vinklar.py --ut export/led
python machine/delar/led/tre_vinklar.py --vinklar 0 10 20 --max-z-intrang 6.2
```

[GitHub Actions: led-tre-vinklar](https://github.com/kingkongola/lowrider/actions/workflows/led-tre-vinklar.yml) bygger och kontrollerar STL/STEP när körning är tillgänglig. **Lokal CadQuery-kontroll av motsvarande lågprofilmodell** gav **en sluten solid, Z-min ≈ −5,74 mm** (fasningar/radier minskar utstick något), men den är **inte samma sak som verifierad build123d-CI**. Tidigare nedladdade STL/STEP avser **fel äldre version** och får inte användas. Repet är den kanoniska CAD-källan.

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
