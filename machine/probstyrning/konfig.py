"""Gör ett konfigurationsförslag för probstyrningen ur en riktig FluidNC config.yaml (D021).

Ändrar bara user_outputs: servot på analog0 (gpio.27) och CR Touchens stift på analog1 (gpio.26),
båda 50 Hz, och tar bort de gamla digitala utgångarna på samma pinnar. Allt annat lämnas orört.
Vägrar om filen inte har de väntade raderna, så att ingen ändring görs på fel antaganden.

Kör: python konfig.py INFIL UTFIL [--med-stopp]   (INFIL ska vara maskinens aktuella fil, läst samma dag)

--med-stopp lägger även in stoppslingan (D024) som control/estop_pin: gpio.39. Bara när stopplådan
är kopplad och bänkprovad: en öppen slinga betyder permanent larm, och utan slingan finns inget stopp.
Läggs in i maskinen först efter att Jackpots utgångsbygel är satt på 5 V och diffen är granskad.
"""
import sys
from pathlib import Path

ANDRINGAR = {
    "analog0_pin": "gpio.27", "analog1_pin": "gpio.26",
    "analog0_hz": "50", "analog1_hz": "50",
    "digital0_pin": "NO_PIN", "digital1_pin": "NO_PIN",
}


def andra(text: str) -> str:
    rader = text.splitlines()
    i0 = next((i for i, r in enumerate(rader) if r.rstrip() == "user_outputs:"), None)
    if i0 is None:
        raise SystemExit("hittar inte user_outputs:")
    i1 = next((i for i in range(i0 + 1, len(rader)) if rader[i] and not rader[i].startswith(" ")), len(rader))
    hittade = set()
    for i in range(i0 + 1, i1):
        nyckel = rader[i].strip().split(":")[0]
        if nyckel in ANDRINGAR:
            rader[i] = f"  {nyckel}: {ANDRINGAR[nyckel]}"
            hittade.add(nyckel)
    if hittade != set(ANDRINGAR):
        raise SystemExit(f"user_outputs saknar {sorted(set(ANDRINGAR) - hittade)}")
    ny = "\n".join(rader) + "\n"
    return ny


def med_stopp(text: str) -> str:
    rader = text.splitlines()
    i0 = next((i for i, r in enumerate(rader) if r.rstrip() == "control:"), None)
    if i0 is None:
        raise SystemExit("hittar inte control:")
    i = next((k for k in range(i0 + 1, len(rader)) if rader[k].strip().startswith("estop_pin:")), None)
    if i is None or rader[i].split(":", 1)[1].strip() != "NO_PIN":
        raise SystemExit("estop_pin saknas eller är redan satt; ändra inte på okänt underlag")
    if any("gpio.39" in r and not r.strip().startswith("#") for r in rader):
        raise SystemExit("gpio.39 används redan (t.ex. som toolsetter_pin); D024 ger den till stoppet")
    rader[i] = "  estop_pin: gpio.39"
    return "\n".join(rader) + "\n"


def _kontroll_gpio(ny: str) -> str:
    anv = [r for r in ny.splitlines() if ("gpio.26" in r or "gpio.27" in r) and not r.strip().startswith("#")]
    if len(anv) != 2:
        raise SystemExit(f"gpio.26/27 används på fler ställen än servo och stift: {anv}")
    return ny


if __name__ == "__main__":
    argv = [a for a in sys.argv[1:] if a != "--med-stopp"]
    if len(argv) != 2:
        raise SystemExit(__doc__)
    ut = _kontroll_gpio(andra(Path(argv[0]).read_text()))
    if "--med-stopp" in sys.argv:
        ut = med_stopp(ut)
    sys.argv[1:3] = argv
    Path(sys.argv[2]).write_text(ut)
    print("skrev", sys.argv[2])
