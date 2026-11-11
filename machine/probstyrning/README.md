# Probstyrning: fällarm och CR Touch

**Status 2026-11-11:** byggt i programvara, **inget provat på maskinen**. Pinnar enligt D021: servot på `gpio.27` (M67 E0), CR Touchens stift på `gpio.26` (M67 E1), kontaktsignalen på `gpio.36` (probe). Verktygsknappen har ingen ingång (D024), så `G38` kan bara utlösas av CR Touchen.

| Fil | Vad |
| --- | --- |
| [installning.json](installning.json) | **Enda källan** till pulsvärden och mätparametrar |
| [makron.py](makron.py) | Gör FluidNC-makron ur källan, med självtest. Armens makron skapas först när armen är inställd |
| [makron/](makron/) | Genererade `.nc`-filer som laddas upp till Jackpot. Ändra aldrig för hand |
| [konfig.py](konfig.py) | Gör konfigurationsförslaget ur maskinens aktuella `config.yaml` |
| [config-forslag-probstyrning.yaml](config-forslag-probstyrning.yaml) | Förslaget gjort ur backupen 2026-11-05; görs om på maskinens aktuella fil före uppladdning |

## Så styrs armen

Ett servo försöker alltid nå den vinkel pulsen anger. Står ett hårt stopp i vägen trycker det med full kraft tills det blir varmt, och plaststoppet kan krypa. Därför gör `arm_ut` och `arm_in` så här:

1. Fräsen av och Z upp till säker höjd, stiftet indraget.
2. Mjuk ramp i 20 steg från det ena ändläget till det andra, sedan 30 µs (ca 3 grader) **förbi** stoppet så att armen säkert ligger an.
3. Kort vila, sedan **pulserna av** (`M67 E0 Q0`). Stoppet, och magneten i parkerat läge, bär armen. Servot står aldrig och trycker.

Armens läge bekräftas av kameran före jobb (beslut 0035, förslag 0036 i `cnc`). Makrona själva vet inte var armen står.

## Arbetsordning

1. **Servot utan pulser (2 min, ESP32-servoprovet).** Kör [servoprov.ino](../servoprov/servoprov.ino), skriv `1500`, vänta, skriv `x`. Försök vrida hornet för hand. **Går det lätt** är sekvensen ovan rätt. **Håller servot emot** fungerar avstängningen inte som tänkt; stoppa och rapportera. Logga i CALIBRATION.md.
2. **CR Touch på bänk.** Ställ LM2596 A på 5,1 V och mät **innan** något ansluts. Mata CR Touchen därifrån, styrsignalen från ESP32:n (`1500`, sedan `650` = ut, `1470` = in, `1780` = självtest, `2190` = larm av). Kontrollera att stiftet går ut och in, och mät kontaktsignalen med multimeter när stiftet trycks in: vilken spänning, och är den hög eller låg vid kontakt? Det avgör om `probe.pin` ska vara `gpio.36` eller `gpio.36:low`.
3. **Armens ändlägen på monterad arm (ESP32).** Ställ armen för hand mitt i rörelsen. Skriv `1500`, stega sedan med `+`/`-` (10 µs) mot utfällt läge tills armen precis ligger an mot stoppet och servot börjar brumma. Backa 10 µs: det är `utfalld_us`. Gör samma mot parkerat läge, där magneten ska ta. Skriv in värdena i `installning.json`, sätt `installd` till dagens datum, logga i CALIBRATION.md och kör `python makron.py`. Generatorn vägrar värden som inte ger rimlig rörelse.
4. **Jackpot.** Sätt bygeln för utgångarna på 5 V. Läs maskinens aktuella `config.yaml`, kör `python konfig.py aktuell.yaml forslag.yaml`, granska diffen (sex rader) och ladda upp. Ladda upp `makron/*.nc` till Jackpots lokala filer. Prova i konsolen: `M67 E1 Q3.235` (stift ut), `M67 E1 Q7.365` (in), sedan `arm_ut.nc` och `arm_in.nc` med fräsen avstängd.
5. **Mätning.** Först efter godkänt steg 4 och enligt [inkopplingsprovet](../delar/nollpunkt/INKOPPLING_OCH_PROV.md) steg 3: `mat_z.nc` över spill. Den söker snabbt nedåt högst 25 mm, lyfter 2 mm, fäller ut stiftet igen och mäter långsamt. Det långsamma värdet gäller. Avståndet mellan stiftets spets och fräsens spets mäts separat; utan det ger mätningen ingen nollpunkt.

## Inte verifierat

CR Touchens pulsvärden är BLTouch-protokollet. Signalens polaritet, servots beteende utan pulser, armens pulser och FluidNC 3.9.9:s `M67` på 50 Hz på just dessa pinnar är oprovade.
