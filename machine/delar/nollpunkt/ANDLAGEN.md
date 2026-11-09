# Ändlägesgivare till BLTouch-fällarm (designbeslut 2026-11-08)

[Gemensam projektjournal för sensorutbyggnaden](https://github.com/kingkongola/cnc/blob/main/docs/PROJEKTJOURNAL_SENSORER.md). [I/O-kartläggning och resurskonflikter](JACKPOT3_IO.md).

## Vald princip – ännu ej fysisk verifierad

Använd **två mikrobrytare** på servoarmens mekaniska ändlägen:
- **Infälld**: bekräftar parkerat läge, där verktyg och dammsko ska vara fria.
- **Utfälld**: bekräftar armens mätläge mot ett separat hårt mekaniskt stopp.

Ändlägesbrytarna är **enbart återkoppling**. De är inte avsedda att bära upp armen eller ersätta hårda stopp, och ingen av dem är ett certifierat säkerhetsdon. En servo som beordrats till ett läge har inte därmed bekräftat det.

**Beslutad brytare 2026-11-09:** användaren har **köpt 10 × QUARKZMAN KW11-3Z-N med rullspak, 1NO/1NC, på Amazon.se**, visat pris 92,94 kr, Prime-frakt 0 kr, **väntad leverans lördag 2026-11-14**. Två används här; de andra är reserv till **sensorenheten**. **Omron SS-3GL13PT (10 tidigare köpta) hålls i reserv till själva LowRidern**, används inte för den nya armen.

**Viktigt om CAD:** vanligt KW11-3Z-hus är cirka 20×10×6,4 mm, men hålavstånd för snarlika återförsäljarvarianter anges både **8,5 och 9,5 mm**. Därför används **justerbara separata fästen**, inte en låst hålbild för levererad QUARKZMAN. Mikrobrytarens manöverkraft, rullspaksväg, ledaranslutning, exakta höjd och elektriska kontaktklass kontrolleras vid leverans. Brytarna är **lägesindikatorer**, inte stopp eller skyddsklassade maskinsäkerhetsdon. Påstådd "waterproof" i annons är ingen verifierad IP-klass.

### Mekanisk princip

- Fäst brytarna på **stationär servoram** och låt **rörlig arm** påverka respektive hävarm strax innan den når separat mekaniskt stopp. Brytaren får inte vara ett rörelsestopp.
- Lägg dem utanför spånflöde och dammsko, med kabelavlastning. Kontrollera hela rörelsen, inklusive de två Z-ändlägena och strömavbrott.
- Ställbar aktiveringspunkt genom slits/håljustering i fästet, inte genom att böja hävarmen på chans.
- Uppdatera verklig CAD från BLTouchs levererade geometri. Befintlig `fallarm_c.py` avser en **annan tidigare probmodell Ø33** och är endast koncept, **inte** en färdig BLTouch-montering.

### Monterings-CAD för de inköpta KW11-brytarna

[**kw11_faste.py**](../sensorer/kw11_faste.py) definierar **en** fasad brytarhållare som printas **två gånger**. Hållarna monteras på **separata öron som tillhör den utbytbara servokassetten**, inte original-Core eller kamerafästet. M2-hålen är slitsade för ett nominellt hålavstånd på **8,5–9,5 mm**, M3-dockarna har ±2 mm justering. [**Grön CAD/STEP/STL/GLB**](https://github.com/kingkongola/lowrider/actions/runs/42616662416) verifierar endast att de printade delarna inte går in i andra *modellerade* delar.

**Öppet och blockerande:** Om den levererade KW11-3Z-N passar i slitsarna, verklig rullspakslängd, **kammarna som påverkar respektive spak**, de två separata hårdstoppen och de elektriska anslutningarnas avlastning. Ingen kontakt med rullspaken eller säker brytarsekvens har påståtts verifierad. Det befintliga servoarmssvepet testar inte spakens utstick.

### Elektrisk princip (beslutad logik; pinval öppet)

- Kandidat: **COM–NO**, slutet endast när respektive hävarm är aktiverad i sitt ändläge. Med korrekt pull-up ger kabelbrott öppen krets = inte bekräftat ändläge. Kortslutning är fortfarande möjlig; den motverkas delvis av att sekvensen kräver **öppen → sluten** kontakt på rätt givare.
- Verifiera elektrisk spänning och logik mot den valda ingången före inkoppling. **Inga GPIO är reserverade eller konfigurerade ännu.** Aktuellt `machine/config-2026-11-05-z800.yaml` har `user_inputs.digital0..7=NO_PIN`, `probe.pin=gpio.36:low`. Detta säger inte att godtyckliga fysiska GPIO finns på kortets kontaktlist.
- Två ändlägesingångar, BLTouch trigger och BLTouch styrsignal samt SPMS664-kommando är **separata signalbehov**. Inventera faktiska pinnar och stöd i FluidNC innan ett `config.yaml`-förslag tas fram.
- Inget trådlöst eller mjukvarubaserat nödstopp kan härledas ur denna lösning.

### Programkontrakt

Kanonisk beteendemodell: [`cnc/src/cnc/probmodell.py`](https://github.com/kingkongola/cnc/blob/main/src/cnc/probmodell.py).

Första observationen ska bekräfta **infälld aktiv, utfälld inaktiv**. Före BLTouch måste infälld kontakt släppa och utfälld kontakt aktiveras. Efter mätning ska stiftet dras in, därefter ska utfälld kontakt släppa och infälld kontakt bli aktiv. Om båda kontakter är aktiva samtidigt eller ingen når förväntat läge före timeout -> fel och **ingen vidare automatisk rörelse**.

Läsningar ska vara avstudsade och tidsgränser ska finnas i den framtida **hårdvaruadaptern**. Kärnan modellerar bara redan kvalificerade observationer. Vid uppstart efter strömavbrott är läget *okänt* tills en korrekt läsning görs. Testa med lossad brytarkabel och simulerad kortslutning.

### Nästa fysiska kontroll

1. När Amazon-paketet kommer **2026-11-14 (beräknat)**: mät och prova två nya `KW11-3Z-N` med multimeter (COM–NO/NC, spakväg och tillslag). **Rör inte Omron-reserven.**
2. Placera dem på ett verkligt servofäste med plats för kabel och metalliska/styva stopp; mät hur långt hävarmen ska tryckas.
3. Bestäm BLTouch-stiftets och armens frigång först när den levererade probens geometri är verifierad.
4. Kartlägg Jackpot3:s anslutningar och FluidNC:s ingångsfunktioner. **Ingen konfigurationsändring eller rörelse före detta.**
