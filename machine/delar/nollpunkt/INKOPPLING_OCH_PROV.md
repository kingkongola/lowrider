# Sensorenhet — förfarande för inkoppling och funktionsprov

**Konsoliderat 2026-11-10.** Detta beskriver hur framtida prov ska utföras. Aktuell genomförandestatus ägs av [CHECKLIST.md](../../../CHECKLIST.md), resultat av [CALIBRATION.md](../../../CALIBRATION.md). Här finns inga parallella statuskryss.

Förutsättningar och valda anslutningar finns i [kopplingsunderlaget](../sensorer/KOPPLING_CORE_V0.md). Inga armbrytare ingår. Dagens godkända prov av det lösa servots rörelseomfång behöver inte upprepas som en öppen konstruktionsfråga.

## 1. Passning med strömmen frånkopplad

Den tillgängliga proben är CR Touch Auto Leveling Kit; aktuell CAD bygger ännu på BLTouch. Kontrollera CR Touch-exemplarets kropp, hålbild, stift och kontakt samt servoarmens infästning, kamerakort och skruvåtkomst mot senaste CAD. För armen för hand genom använd rörelse och kontrollera fräs, dammsko, kabel och stopp även över relevant Z-rörelse. Prova magnetparkeringen separat; stoppens last får inte ligga på elektronik eller kablar.

## 2. Matning och signaler utan maskinrörelse

1. Verifiera först CR Touchens dokumenterade matning, kontaktens ledarordning och signaler; anta inte BLTouch-kompatibilitet från utseende eller kabelfärger. Ställ och mät de två regulatorerna utan ansluten elektronik. Kontrollera polaritet och Jackpot-utgångarnas spänningsbygel enligt kopplingsunderlaget.
2. Läs och spara faktiskt laddad `config.yaml`. Jämför med [machine/AKTIV](../../AKTIV) och skapa ett separat komplett konfigurationsförslag för sensoranslutningen. Undvik dubbelallokerade utgångar.
3. Prova servostyrningen från den avsedda Jackpot-utgången. Ställ de monterade armpositionerna och prova uppstart, avstängning och magnetens hållning vid strömbortfall. Det fristående ESP32-provet bevisar inte Jackpot-styrningen.
4. Prova CR Touch-stiftets styrning och läs dess kontaktsignal separat efter verifierad anslutning. Kontrollera polaritet, indraget/utfällt stift, larm och störningar. Prova fasta verktygsknappen separat om den är monterad.
5. Kontrollera att endera probe-ingången kan avsluta samma G38-logik. Kontrollera startspärr för redan aktiv probe och entydiga vilolägen innan något mätkommando med rörelse föreslås.
6. Starta Pi/kamera och ta riktiga bilder med känt fokus. Lär in armens parkeringsmärke och prova att oklar bild, uteblivet svar och fel armläge hindrar jobbstart. Utan inlärning är spärren ännu inte aktiv i dagens kod.

## 3. Kontrollerad fysisk mätning

Först efter godkänd mekanik och signalprov: visa planerad mätsekvens och inhämta uttryckligt godkännande till maskinrörelsen. Båda proberna ska vara inaktiva före start, och endast avsedd prob får kunna nå kontakt under provet. Börja utan fräskollision och logga kontaktpunkt, repeterbarhet och offset i mätloggen.

Avbryt vid okänt armläge, fast stift, oväntad kontakt, matningsbortfall eller rörelse vid uppstart som inte är under kontroll. En läst status efter en mätning bevisar inte vilken givare som utlöste kontakten. Kameraspärren är ingen säkerhetsfunktion eller ersättning för maskinens stopp.
