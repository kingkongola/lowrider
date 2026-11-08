# Sensorarm och två prober – inkopplings- och provgrind

**Upprättad 2026-11-08. Status: skrivbordsgranskad, EJ fysiskt provad.** Det här är en checklista för arbete vid LowRider, inte ett godkänt elschema, tillåtelse att röra maskinen eller instruktion att skriva till den aktiva FluidNC-konfigurationen.

Utgångspunkt: [I/O-inventering](JACKPOT3_IO.md), [armens två ändlägen](ANDLAGEN.md), [projektjournalen](https://github.com/kingkongola/cnc/blob/main/docs/PROJEKTJOURNAL_SENSORER.md). **Senaste aktiva konfigurationen** bestäms av [`machine/AKTIV`](../../AKTIV). Inga delar från sensorköpet rapporterade mottagna.

## Beslut och vad som återstår

- **Beslut S-09:** mekaniskt åtskilda vilolägen, **ingen elektrisk mux**. Två probe-ingångar kan vara anslutna till FluidNC samtidigt, men [firmware behandlar endera som G38-trigger](https://github.com/bdring/fluidnc-wiki-content/blob/main/config/probe.md).
- **BLTouch:** servoarmen SPMS664 fälls till egen hård stoppunkt; brytare *utfälld* bekräftar läget. Stiftet manövreras separat. Avläst armvinkel och beordrat stiftläge är inte samma sak som kontakt.
- **Verktygslängdsknapp:** fällarmen parkerad och stiftet indraget; knappen aktiveras **endast** av fräsens faktiska beröring.
- **Omron-brytare:** två exemplar SS-3GL13PT ur tidigare DigiKey-order. Antal kvar, skick, COM/NO/NC och mekanisk frigång kräver kontroll.
- **Samma G38:** inget softwarekommando väljer aktiv probe. En framgångsrik `[PRB:...:1]` ensam visar **inte** om det var BLTouch eller toolsetter som triggade.

## Dokumenterade resurser – kandidater, inte pin-tilldelning

| Funktion | Konfiguration idag | Möjlig kandidat att utreda | Blockerande verifiering |
| --- | --- | --- | --- |
| Yttre prob / befintlig touchplate | `probe.pin=gpio.36:low` | Behåll befintlig för prov tills ny BLTouch-strategi är klar | Spänning/utgångsläge på faktisk BLTouch, konflikter med befintlig platta |
| Fast verktygslängdsknapp | `toolsetter_pin=NO_PIN` | `gpio.39` är nämnd som input-only / sjunde skyddad port | Tillgänglig kontakt, revision och faktiskt fritt stift |
| Omron infälld/utfälld | `user_inputs.digital*=NO_PIN` | Modulport `gpio.13`/`gpio.14` om RJ11 ska kunna reserveras för pendant | Elektrisk skyddsnivå, verklig mappning och konfigurerad M66-läsning |
| Armservo SPMS664 | Ingen servo/PWM konfigurerad | Någon *verifierad* 5 V PWM-kapabel utgång | Tillgänglighet, 50 Hz, pulsområde, separat servomatning och **bootrörelse** |
| BLTouch-styrsignal | Ingen separat PWM konfigurerad | En separat verifierad signalväg | Exakt BLTouch-variant, pulskommandon, logikspänning, startup och larm |

V1E listar **7 dedikerade ingångar, fyra utgångar, RJ11 och modulport**, samt att `gpio.12`/`gpio.15` delas mellan RJ11 och modulport. `gpio.26` kan ge en **uppstartspuls**. [V1E Jackpot3](https://docs.v1e.com/electronics/jackpot3/). I dagens fil används fem ändlägesingångar och en probe; **rör inte** Y-/Z-autosquare. Ny kandidatpinne ska alltid verifieras elektriskt, fysiskt och i exakt firmwareversion **innan** den skrivs i en ny, separat configfil.

## Grind A – med strömmen frånkopplad (ingen maskinrörelse)

- [ ] Inventera faktiskt modell-/revisionsnummer på BLTouch, Pi-kamera, mikrobrytare, kretskort och servot. Notera antal reservbrytare.
- [ ] Bekräfta med multimeter vilka anslutningar på **varje** Omron är COM, NO respektive NC och hur de växlar när hävarmen trycks.
- [ ] Testa två mekaniska ändstoppslägen utan att låta brytarna vara de hårda stopparna. Kontrollera frigång över hela Z-rörelsen, dammsko, fräs, kabelkedja och infällning vid strömbortfall.
- [ ] Fotografera **Jackpot3:s verkliga revision**, sjunde skyddade ingången, modulport, RJ11 och utgångarnas spänningsval innan någon kontakt kopplas. De finns inte verifierade i repot.
- [ ] Märk kablar/probfunktion; håll 5 V matning och 3,3 V logik åtskilda enligt **verkligt** datablad för respektive kort/revision. Inga antagna 5 V-säkra ESP32-portar.

## Grind B – strömsatt I/O-bänktest utan inkopplad fräs/motorrörelse

- [ ] Ta kopia av faktisk `config.yaml` från kortet och kontrollera den mot [`machine/AKTIV`](../../AKTIV), utan att ersätta fungerande konfiguration.
- [ ] Med var **och en** ingång individuellt och säkert inkopplad: avläs **rått** läge. Verifiera polaritet, öppen kontakt, sluten kontakt, ledningsbrott och båda Omron-kontakter samtidigt. Inga M66-test kan utföras innan nya `user_inputs` konfigurerats i en **separat testkonfiguration**.
- [ ] Kontrollera faktiskt stöd för `user_inputs.digital0..7` via [FluidNC `M66`](https://github.com/bdring/fluidnc-wiki-content/blob/main/config/user_inputs.md), och för `probe.toolsetter_pin` via [?]-status och [probe-dokumentationen](https://github.com/bdring/fluidnc-wiki-content/blob/main/config/probe.md). Detta är läsning av signal, **inte en säkerhetsfunktion**.
- [ ] Verifiera läge och pulstålighet för **SPMS664** och **BLTouch** separat med korrekt matning och utan mekanisk last. Särskilt på-/avslag, omstart och eventuell ofrivillig rörelse. [FluidNC RC-servo](https://github.com/bdring/fluidnc-wiki-content/blob/main/config/rc_servo.md) beskriver att servot kan gå till startposition vid aktivering.
- [ ] Observera att `probe.check_mode_start` enligt [aktuell FluidNC-dokumentation](https://github.com/bdring/fluidnc-wiki-content/blob/main/config/probe.md) handlar om **Check Mode**, inte en garanterad fysisk förkontroll vid riktig G38.
- [ ] Mät eller belägg faktisk signalkvalitet, kontaktstuds och timeout; först därefter bestäm `stabil_ms` och tidsfrister i programadapter.

## Grind C – isolerad fysisk mätning, uttryckligt godkännande krävs

- [ ] Från kända mekaniska vilolägen: visa att **ingen** av proberna är aktiv före G38.
- [ ] Verifiera att endast vald prob kan nå sitt kontaktläge under mätningen: först BLTouch med toolsetter orörd, sedan toolsetter med BLTouch indragen. Först under kontrollerat tillstånd utan risk för fräskollision.
- [ ] Utmana avsiktligt med förväntade fel (frånkopplad signalkabel, fast stift, frånvarande/extra kontakt, matningsbortfall). Börja med stillastående test; gör **inga** avsiktliga felinjektioner under obevakad maskinrörelse.
- [ ] Kontrollera hur `[PRB:...:1]`/larm rapporteras; att signalen går att läsa efter G38 är inte ett bevis på vilken probe som utlöste mätningen **vid kontakttidpunkten**.
- [ ] Komplettera uppmätt osäkerhet, stiftets verkliga repeterbarhet, mätkontaktens kontaktpunkt och verktygslängdsoffset i [`CALIBRATION.md`](../../../CALIBRATION.md) – inte i projektjournalen.

## Stoppvillkor

Om **inaktiv** prob kan trigga G38, om stiftet fastnar, om ändlägen inte kan bekräftas, eller om servot rör sig osäkert vid boot: **automatisk probing är blockerad**. Ompröva mekanik eller elektrisk separering i nytt beslut. Softwaretest + `M66`-pollning gör inte denna risk säker.

**Maskinstatus efter detta dokument:** ingen fysisk anslutning, matning, firmwareändring, kalibrering eller rörelse utförd av assistenten. Alla tre grindarna är ännu öppna.
