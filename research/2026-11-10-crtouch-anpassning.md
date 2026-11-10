---
research_date: 2026-11-10
scope: CR Touch-kit, mekanisk referens och anpassning till LowRiderns fällarm
status: recommendation-ready
decision_state: CR Touch tillgänglig enligt användaren; CAD anpassad från tredjepartsreferens, fysisk verifiering återstår
price_basis: inga priser eller nya köp undersökta
region: Sweden / EU
sources_checked:
  - Creality originalmanual och produktdata
  - Jonathan Harper E34M1 CAD och licens
  - TH3D sensor-side anslutningsguide
  - V1 Engineering Jackpot3-dokumentation
supersedes: null
---

# CR Touch på LowRiderns servofällarm

Detta är daterad källevidens och konstruktionsunderlag. Tillgång ägs av [PROCUREMENT.md](../PROCUREMENT.md), komponenter av [BOM.md](../BOM.md), konstruktion av [sidotorn.py](../machine/delar/sensorer/sidotorn.py), fysisk provstatus av [CHECKLIST.md](../CHECKLIST.md). CR Touch används som lokal Z-probe på fällarmen; ingen Ender-firmware eller ändring av maskinens homing följer av detta.

## Vad standardkitet innehåller

[Crealitys originalmanual](https://cdn.creality.com/product-detial/us/cr-touch-auto-leveling-kit/08582340baaa0bb280d3d5e6863163f2.pdf) visar en CR Touch, en fempolig kabel, tre metallbeslag för Ender/CR-skrivare, två M3×6, två M3×8, tre buntband och manualen. [Crealitys butikssida](https://www.creality3dofficial.com/products/creality-cr-touch) anger samma huvuddelar men fyra buntband. Räkna därför inte det exakta buntbandsantalet som fysiskt verifierat. Ingen kabellängd antas från en annan kitvariant.

För LowRider används sensorn och originalkabeln. De tre skrivarspecifika metallbeslagen ersätter inte vår fällarm och ingår inte i dess CAD. Skruvarna kan användas enligt nedan efter fysisk kontroll. Detta är kitets dokumenterade standardinnehåll, inte inventering av användarens öppnade kartong.

## Tillverkaruppgifter kontra CAD-referens

[Creality](https://www.crealitycloud.com/product/upgrade-kit/cr-touch-609f2c75c9e6ecdd6918fcec) anger **27 × 17,5 × 39,3 mm**, **6 mm stiftslag**, **5 V**, effekt under 1 W och repeterbarhetsstandardavvikelse högst 0,04 mm. Det sista är en produktspecifikation, inte uppmätt noggrannhet hos vår maskin.

Den läsbara referensen kommer från [Jonathan Harpers E34M1](https://github.com/jon-harper/E34M1/blob/2080145fc3bdac97037eeb46cb69e17a2cbef690/CAD/abl/abl_cr_touch.step), komponent `CR-Touch_Mockup_v1`. Ursprung/licens finns i [referenskatalogen](../machine/delar/sensorer/referenser/README.md). Det är tredjeparts-CAD, inte en verifierad tillverkningsritning. Användarens kompletterande [Printables STEP-referens](https://www.printables.com/model/390312) var inte läsbar via de använda webbverktygen och används därför inte som outtalad måttkälla.

Ur E34M1-referensen: 18 mm hålavstånd, Ø3,2 mm fästhål, 1,9 mm flänstjocklek och 37 mm från flänsens ovansida till kroppens nederkant. Maximal flänsbredd är 27,2 mm; kroppen nedanför skuldran är cirka 16,2 mm bred. Djupet är 17,5 mm. Stiftet är centrerat mellan hålen i X men förskjutet 2,25 mm från hålraden i Y.

Referensens utfällda spets ligger 46 mm under flänsens ovansida. Det skiljer sig från enkel addition av Crealitys 39,3 mm och 6 mm. Modellen skalas inte för att tvinga ihop uppgifterna: 46 mm används konservativt i kollisionskontrollen, och den absoluta stiftgeometrin ska mätas före probning.

## Utförd CAD-anpassning

- BLTouch-lådan ersätts av referensmodellens separata kropp och stift. Proben vrids 180° runt sin egen Z-axel så att dess kropp/kontakt ligger bort från armens rygg; stiftförskjutningen blir +2,25 mm i monteringsramens Y.
- Servoaxel, probens hålrad, nominell −150°-rörelse, kamera, torn och magnetprincip behålls. Probfoten breddas och får en öppning framåt för kontaktens reserverade utrymme, 12 × 10,5 × 10 mm. Det är ett konstruktionskuvert, inte en uppmätt kontakt.
- Armens kabelspår breddas till 6 × 2,2 mm. Den verkliga femledarkabelns böjar och slinga vid servoaxeln måste fortfarande provas; ett stelt kontaktkuvert är ingen modell av en flexibel kabel.
- Ny avsmalnande hylsa ersätter den gamla 13,8 mm-öppningen. Huvudkaviteten har nominellt 0,6 mm spel per sida mot referensens kroppsmått. Skruvunderläggen har separat sidospel och verktygsöppningar. Stiftänden är öppen.
- M3-frigång i hylsan är Ø3,4 mm: önskad frigång Ø3,25 + 0,15 mm diametertillägg enligt användarens erfarenhetsvärde. Armens Ø2,6 mm pilothål avser gängning i plast och provas separat; modellen skalas inte globalt.
- Skruvstapel med skydd: 2 mm hylsöra + 1,9 mm referensfläns + 4,1 mm ingrepp i 4,5 mm armfot med M3×8. Utan hylsa ger M3×6 samma nominella ingrepp. Faktisk skruvskalle och flänstjocklek måste jämföras vid provmontage.
- Referensens egna Ø5,5 mm M3-skruvhuvuden överlappar dess sensorattrapp cirka 0,08681 mm³ vardera, maximalt cirka 0,05 mm i sidled. Samma lilla avvikelse finns i vår skruvstapel med samma huvudmodell; den får inte redovisas som verifierad fysisk passning. Kontrollskriptet kräver att vår stapel inte försämrar originalets avvikelse och redovisar den som öppen referensfråga. Hylsans verktygsöppningar har inte denna överlappning med skruvmodellen.
- Magnetens plastbula kortas 0,5 mm i sin längdriktning för att ligga innanför armens sidplan. Skruvhuvudet ska nå magneten utan att plastbulan först tar i stoppet. Nominellt parkeringsläge ändras inte.

## El och fysisk verifiering

CR Touch kräver nominellt 5 V enligt Creality. Matningsplanen ändras därför till 5,0 V för Pi/prob; servot behåller egen 6,0 V-regulator. Ingen regulator har ställts eller kopplats om genom dokumentändringen.

[TH3D:s sensor-side guide](https://tickets.th3dstudio.com/help-guides/article/crtouch-sensor-pinout-%E2%80%93-sensor-side) skiljer servo/styrning, ZStop/kontakt, matning och två jordledare. Använd funktionsnamn och kontrollera den faktiska kabeln; färger och Creality-moderkortets IN/OUT-etiketter är inte en tillräcklig kopplingsanvisning. [Jackpot3:s dokumentation](https://docs.v1e.com/electronics/jackpot3/) beskriver 5 V-PWM-utgångar och de skyddade ingångarna. D021:s GPIO-plan behålls, men faktisk anslutning och startbeteende är ännu inte provade.

Första fysiska kontrollen är den lilla plattan [crtouch-passning.json](../print/crtouch-passning.json): prov av armfoten och hylsan i samma geometri som slutdelarna. Kontrollera kortets/kontaktens passning, skruvåtkomst, flänsens anliggning och fritt stift. Monterad rörelse, verkliga kablar, servohornets infästning och elektriska signaler återstår efter detta. Mätresultat förs endast i [CALIBRATION.md](../CALIBRATION.md).
