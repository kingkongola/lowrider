# Jackpot3 I/O – kartläggning inför sensorarm och BLTouch

**2026-11-08. Underlag, inte inkopplingsorder.** Inga nya GPIO har konfigurerats. Informationen om vad maskinen **redan använder** kommer från [aktuell `machine/AKTIV`](../../AKTIV) → [`config-2026-11-05-z800.yaml`](../../config-2026-11-05-z800.yaml). Kortets generella egenskaper kommer från [V1E Jackpot3-dokumentationen](https://docs.v1e.com/electronics/jackpot3/). Skillnaden mellan *pinne upptagen i YAML*, *på PCB tillgänglig* och *lämplig för en funktion* får inte suddas ut.

## Det som redan är reserverat

| Gränssnitt i aktiv FluidNC-konfiguration | GPIO | Användning |
| --- | --- | --- |
| X limit | `gpio.25` | X-ändläge |
| Y motor0 / motor1 limits | `gpio.33` / `gpio.35` | Y-autosquare |
| Z motor0 / motor1 limits | `gpio.32` / `gpio.34` | Z-autosquare |
| `probe.pin` | `gpio.36:low` | Dagens prob/touchplate |
| `probe.toolsetter_pin` | `NO_PIN` | Ännu inte konfigurerad |
| `user_inputs.digital0..7` | `NO_PIN` | Ingen extra användaringång konfigurerad |
| `user_outputs.digital0..3` | `gpio.26 / 27 / 0 / 2` | Reserverade i YAML, faktisk användning inte genomgången |
| `user_outputs.analog0..3` | `NO_PIN` | Ingen PWM-utgång är konfigurerad |
| `uart1` | `gpio.16` / `gpio.4` | Befintlig TMC-UART |
| `i2so`, SPI, SD | Flera andra | Ändra inte utan analys av maskindrift |

V1E dokumenterar **sju dedikerade skyddade ingångar** på Jackpot3. Med fem befintliga maskinändlägen + en probe-ingång är i praktiken **sex upptagna**. `gpio.39` är dokumenterad som input-only och verkar inte användas i denna YAML, men dess åtkomlighet på **just din installation** och anslutningstyp är inte verifierad.

### Det nya sensorbygget behöver

- Två separata digitala läsningar: **arm infälld** respektive **arm utfälld** (Omron `SS-3GL13PT` × 2).
- En digital triggersignal från **BLTouch**.
- En *annan* probe-/toolsetter-ingång om den planerade fasta verktygslängdsknappen ska kunna finnas samtidigt.
- En styrbar servo-PWM till **Spektrum SPMS664** och en **separat** styrsignal till BLTouch-stiftet.
- Rätt matningsspänning, jordning, kabelskydd och mekaniska säkra ändstopp.

**Därmed räcker inte ”en återstående vanlig sensorport” för två armkontakter + separat toolsetter.** Vi måste pröva expansion/modulport eller RJ11 (och hur FluidNC stöder avläsningen), inte plocka en befintlig Y/Z-limit och förstöra autosquare.

## Möjliga anslutningsvägar (inte låsta)

1. V1E anger att **`gpio.12` och `gpio.15` är delade mellan RJ11 och modulporten**. Modulporten har även `gpio.13` och `gpio.14` enligt dokumentationen. De är bara **potentiella resurser** tills mekanik, elektrisk nivå, skydd, uppstartsfunktion och firmwarefunktion kontrollerats.
2. Kortet har fyra väljbara **5 V/24 V-utgångar**; full PWM anges i 5 V-läge och enklare PWM i 24 V-läge. Detta är **inte** bevis att samtliga kan styra både BLTouch och SPMS664 med lämpliga pulser och ström. **`gpio.26` kan pulsera vid uppstart** enligt V1E; märk som olämplig kandidat för ett rörligt servo eller probe-stift tills uppstartsrisken är eliminerad.
3. `gpio.0` och `gpio.2` finns i befintlig utgångskonfiguration. Ändra dem inte förrän uppstart, elektriska anslutningar och aktuella användningar har utretts.
4. V1E anger att de dedikerade switch-ingångarna är aktiva lågt med **10 kΩ pull-up**. Den planerade COM–NO-logiken kan därför provas som en logisk kandidat, men slutligt val kräver fysisk kabel-/kortkontroll och en fungerande felmodell för öppna/fastnade kontakter.
5. Befintlig `probe.pin = gpio.36:low` kan inte godtyckligt användas som två separata samtidiga probsignaler. Vi måste verifiera stöd för en dedikerad `toolsetter_pin` i **installerad FluidNC 3.9.9** före inkoppling.

## Princip att låsa när vi har full pinout

- **Inget nytt kort som reflex:** undersök först dokumenterade expansions-/modulporten på redan köpt Jackpot3.
- **Inga antagna pinnar:** märk varje kandidat med fysiskt kortstift, elektrisk kompatibilitet, bootbeteende och verifierat FluidNC-stöd.
- **Poka-yoke:** ett saknat, motsägande eller ofärskt ändläge tillåter inte probning; styrsignaler till servo/BLTouch får aldrig skickas av ljud-/kameraanalys.
- **En ändring i taget:** behåll den senast bekräftade maskinkonfigurationen orörd. Ny konfigurationsfil får först vara ett separat granskningsförslag och kräver godkännande för varje riktig rörelse.

**Status:** logisk resurssammanställning gjord; **ingen** fysisk pinout verifierad och **ingen** spänningssatt mätning eller kabeldragning gjord. Fortsätt med ren mjukvarusimulering och besluta om fysisk IO-topologi innan CAD-fästet tillverkas.

Se [projektjournalen](https://github.com/kingkongola/cnc/blob/main/docs/PROJEKTJOURNAL_SENSORER.md) för motiv, beslut och nästa steg.
