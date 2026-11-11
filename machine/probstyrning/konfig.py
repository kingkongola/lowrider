"""Gör ett konfigurationsförslag för probstyrningen ur en riktig FluidNC config.yaml (D021).

Ändrar bara user_outputs: servot på analog0 (gpio.27) och CR Touchens stift på analog1 (gpio.26),
båda 50 Hz, och tar bort de gamla digitala utgångarna på samma pinnar. Allt annat lämnas orört.
Vägrar om filen inte har de väntade raderna, så att ingen ändring görs på fel antaganden.

Kör: python konfig.py INFIL UTFIL     (INFIL ska vara maskinens aktuella fil, läst samma dag)
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
    anv = [r for r in ny.splitlines() if ("gpio.26" in r or "gpio.27" in r) and not r.strip().startswith("#")]
    if len(anv) != 2:
        raise SystemExit(f"gpio.26/27 används på fler ställen än servo och stift: {anv}")
    return ny


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    ut = andra(Path(sys.argv[1]).read_text())
    Path(sys.argv[2]).write_text(ut)
    print("skrev", sys.argv[2])
