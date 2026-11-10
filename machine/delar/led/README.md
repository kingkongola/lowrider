# LowRider V4 — trevinklat 8 mm COB-fäste

**Status 2026-11-10:** parametrisk **CAD-prototyp**, ännu inte printad, mätt eller termiskt verifierad. Ingen aluminiumprofil krävs för att prova konstruktionen. Huvudfil: [`tre_vinklar.py`](tre_vinklar.py). CAD:n använder **build123d**, samma bibliotek som sensorenheten. [GitHub Actions (STEP/STL)](https://github.com/kingkongola/lowrider/actions/workflows/led-tre-vinklar.yml). Prototypens STEP/STL från separat CadQuery-kontroll har en sammanhängande, sluten solid, men **build123d-körning och fysisk passning är inte kontrollerade i detta dokument**.

## Grundval

- 3 × BRIMETI COB-remsor, **8 mm breda**, 24 V, 4000 K, 10 W/m uppgivet. Exakt CRI och verkliga termiska data ännu inte verifierade.
- En remsa lyser **rakt ned** (0°); två **framåt** (25°/50° som **provvinklar**, inte låst optisk slutvinkel).
- Stödet är 10 mm brett per remsa (parameter `led_bredd+2*marginal`); remsorna tejpas på 155 mm långa 3D-printade hyllor.
- 5 separata moduler, ungefär 155 mm var och **160,2 mm centrumdelning**; de fyra gliporna på 5,2 mm kan LED-listens flexibla kretskort brygga, om faktisk kap-/böjbarhet tillåter.
- **Befintliga strutskruvar lämnas helt orörda.** Varje modul har två U-klämmor som förs upp på en vertikal struts **nederkant** och fixeras försiktigt med M3-skruv i plast (ej gängat i MDF).
- Enligt [repo-filen `strut_plate.svg`](../../../strut_plate.svg) har nederkanten raka sektioner från ca X18,25–159,95 mm följt av pitch 160,2 mm. Den första modulens centrum sätts till X89,1 mm. Dess klämmor ryms ungefär X27,1–43,1 mm och X135,1–151,1 mm, alltså i raka sektioner; M5-hålen ligger ca 16,55 mm över nederkanten, medan klämman når 13 mm. Detta gäller just originalgeometrin i SVG och förutsätter att aktuell strut är orienterad som ritad.
- Konstruktionen antar **6 mm MDF/hardboard** enligt BOM. Om verklig tjocklek skiljer: ändra `strut_tjocklek`.

## Ändra och exportera

```bash
python -m pip install 'build123d==0.10.0'
python machine/delar/led/tre_vinklar.py --ut export/led
python machine/delar/led/tre_vinklar.py --ut export/led --led-bredd 8.2 --strut-tjocklek 6.2 --vinklar 0 20 45
```

Exporten ger **en** modul som STEP och STL. Print den fem gånger först efter passningsprov. `--fram-sida -1` speglar de riktade remsorna åt andra sidan. `Param` i koden tillåter anpassning av modullängd, fästavstånd, spel, M3-förborrning, placeringspitch och ledvinklar.

## Verifiera innan montering

1. **En testmodul**, PETG snarare än PLA. M3-skruvarna är tryckskruvar; prova verklig skruvdiameter/grepp och dra inte så hårt att MDF skadas. Kontrollera att båda U-klämmorna når rak nederkant mellan strutens urtag och att inga skruvhuvuden, rör eller strut-inlägg kolliderar.
2. Kontrollera att den **8 mm** breda LED-remsan har tillräcklig böjbarhet, att lödpunkter och kapmärken hamnar rätt och att tejpen fäster på PETG. Inget skarpt böj runt läppen.
3. Tänd bara en kort provbit med **verifierad 24 V-matning** och övervaka temperatur vid fullt ljus under längre pass. Den jämförbara Maxel COF 10 W/m anger att dess egen list inte kräver extern kylning, **men det bevisar inte BRIMETI:s värmeegenskaper**. PETG är inte kylfläns. Vid för hög temperatur/tejp som släpper: ompröva metallflatlist/profil innan full längd används.
4. Kontrollera ljusriktning, skuggor/reflexer med kameran, tillgänglighet under dammsko och hela X/Y/Z-svepet. Om optiken inte fungerar justera de **tre vinkelparametrarna**, inte improvisera med frigången.
5. Innan full installation: separat säkrad LED-matning. 3 × 0,8 m ≈ **24 W** vid tillverkarens 10 W/m. Försök inte belasta maskinens 60 W Mean Well med hela LED-rullen utan separat effektbudget.

**Ingen STL är godkänd för drift före provprint, temperaturtest och frigångskontroll.** Övrig effekt-/stopparkitektur: [`machine/EL_BELYSNING_OCH_STOPP.md`](../../EL_BELYSNING_OCH_STOPP.md).
