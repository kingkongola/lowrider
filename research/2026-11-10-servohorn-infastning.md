---
research_date: 2026-11-10
scope: Servohornets infästning, måttavvikelser och befintliga fästelement
status: recommendation-ready
decision_state: ersatt 2026-11-11 av formficka + M3×10 genom armen (DECISIONS.md, D020-tillägg); kilbygeln utgick
price_basis: observerade SEK inklusive moms; inget köpt; frakt ej fastställd
region: Sweden / EU
sources_checked:
  - användarens mätningar och tillgång
  - Bossard BN610 och BN272 datablad
  - Electrokit produktsidor och köpvillkor
supersedes: null
---

# Servohornets infästning

Mätvärden ägs endast av [CALIBRATION.md](../CALIBRATION.md#2026-11-10--servohornets-nav-första-måtten), konstruktionen av [CAD-underlaget](../machine/delar/sensorer/README.md#hornet-formficka-och-mittskruv-m3--10-omgjort-2026-11-11). Användaren vill ha en glappfri, servicebar infästning. Klämning var ett förslag, inte ett låst metodkrav. M2 saknas och ett separat köp med frakt avvisades.

| Metod | Bedömning |
| --- | --- |
| Två genomgående M2 i de två yttre originalhålen | Kompakt och utan uppborrning, men kräver skruv/mutter som saknas. Inte aktuellt som separat fraktköp. |
| Två M3 i samma hål efter uppborrning | Hålavståndet är 4,3 mm medan vanliga M3-insexskallar är Ø5,5 mm. Två skallar ryms inte bredvid varandra i samma plan. Kräver ytterligare ändring, inte bara borrning. |
| M3-bygel utanför hornet | Aktuellt CAD-val: två printdelar och befintliga M3-typer, utan uppborrning eller nya muttrar. Pilothål och klämväg måste verifieras fysiskt. |

Bygeln använder sned kontakt mot hornets kant. Botten och sidostöd tar upp rörelse, ett bakre navanslag ger längdläget. Sättningen och skruvstapeln prövas geometriskt vid måttvariationer. Det bevisar inte friktion, långtidshållning eller att fysisk montering är glappfri.

## Fästelement och daterat prisexempel

- Bossards [BN610-datablad](https://www.electrokit.com/upload/quick/ef/7d/8095_41036142.pdf) och [BN272-datablad](https://xonstorage.blob.core.windows.net/pdf/bossard_1000454_xonlink.pdf) ger referensmått för insexskruvar. M3-skallen modelleras som Ø5,5 × 3 mm. Verkliga skruvar ska jämföras före montage.
- Electrokit [M2×8, 41036134](https://www.electrokit.com/insexskruv-mc6s-m2x8-rostfri-a2): 10 st för 13,50 kr. [M2-muttrar, 41013901](https://www.electrokit.com/mutter-m2): 25 st för 12,50 kr. De minsta listade kvantiteterna blir tillsammans 26 kr före frakt. [Frakten fastställs i kassan](https://www.electrokit.com/villkor-konsument). Inget av detta är beställt eller debiterat.

Den nya M3-bygeln är vald utifrån användarens tillgångs- och fraktkrav, inte utifrån ett påstående att M2-förband i sig är olämpliga.
