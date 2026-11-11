"""Genererar FluidNC-makron för fällarm och CR Touch ur installning.json.

Varför en generator: pulsvärdena finns på ett enda ställe. Makrona kan inte få olika värden,
och armens makron skapas inte alls förrän armens pulser är inställda på monterad arm.

Kanaler (D021): M67 E0 = fällservo (gpio.27), M67 E1 = CR Touchens stift (gpio.26).
M67 tar pulsens andel av perioden i procent: vid 50 Hz är 1500 µs = 7,5 %. Q0 stänger av pulserna.

Kör: python makron.py            skriver makron/*.nc och visar vad som saknas
     python makron.py --kontroll  kör självtesterna utan att skriva filer
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

HAR = Path(__file__).parent
SERVO_MIN_US, SERVO_MAX_US = 500, 2500      # bänkprovets gränser (CALIBRATION.md 2026-11-10)


def q(us: float, hz: int) -> str:
    """Pulslängd i µs till M67:s Q i procent, fyra decimaler (0,0005 % = 0,1 µs)."""
    return f"{us * hz / 10000:.4f}"


def huvud(namn: str, syfte: str) -> list[str]:
    return [f"({namn}: {syfte})", "(Genererad av machine/probstyrning/makron.py ur installning.json. Ändra inte för hand.)"]


def kontrollera(c: dict) -> list[str]:
    fel = []
    s = c["stift"]
    for k in ("ut_us", "in_us", "sjalvtest_us", "larm_av_us"):
        if not 500 <= s[k] <= 2500:
            fel.append(f"stift.{k} utanför 500-2500 µs")
    a = c["arm"]
    if a["installd"]:
        for k in ("parkerad_us", "utfalld_us"):
            v = a[k]
            if not isinstance(v, (int, float)) or not SERVO_MIN_US <= v <= SERVO_MAX_US:
                fel.append(f"arm.{k} saknas eller utanför {SERVO_MIN_US}-{SERVO_MAX_US} µs")
        if not fel and abs(a["utfalld_us"] - a["parkerad_us"]) < 800:
            fel.append("armens två lägen ligger under 800 µs isär; 150 grader kräver mer, kontrollera mätningen")
        if not 0 <= a["forbi_stopp_us"] <= 60:
            fel.append("arm.forbi_stopp_us ska vara 0-60 µs (högst ca 5 grader in i stoppet)")
    m = c["matning"]
    if not 0 < m["max_ned_mm"] <= 40:
        fel.append("matning.max_ned_mm ska vara 0-40 mm")
    if not 0 < m["langsam_mm_min"] <= m["snabb_mm_min"] <= 300:
        fel.append("matningshastigheterna ska vara 0 < långsam <= snabb <= 300 mm/min")
    return fel


def ramp(fran: float, till: float, c: dict) -> list[str]:
    a, hz = c["arm"], c["pwm_hz"]
    n = a["ramp_steg"]
    ut = []
    for i in range(1, n + 1):
        ut.append(f"M67 E0 Q{q(fran + (till - fran) * i / n, hz)}")
        ut.append(f"G4 P{a['ramp_paus_s']}")
    return ut


def stift(lage: str, c: dict) -> list[str]:
    return [f"M67 E1 Q{q(c['stift'][lage], c['pwm_hz'])}", f"G4 P{c['stift']['vanta_s']}"]


def sakert(c: dict) -> list[str]:
    return ["M5 (fräsen av)", "G90", f"G53 G0 Z{c['saker_z_mpos']:.3f} (upp till säker höjd i maskinkoordinater)"]


def arm_till(mal: str, c: dict) -> list[str]:
    """Rampa mjukt till ändläget, tryck lätt förbi in i stoppet, vila och stäng av pulserna.

    Servot får aldrig stå och trycka mot stoppet: efter vilan är pulserna av, och stoppet
    (och magneten i parkerat läge) bär armen. Rampen startar i motsatt ändläge, eftersom
    det är där armen står när makrot körs; spärr och kamera bekräftar läget.
    """
    a = c["arm"]
    fran_us = a["parkerad_us"] if mal == "utfalld_us" else a["utfalld_us"]
    till_us = a[mal]
    riktning = 1 if till_us > fran_us else -1
    return [f"M67 E0 Q{q(fran_us, c['pwm_hz'])} (håll startläget)", "G4 P0.2",
            *ramp(fran_us, till_us + riktning * a["forbi_stopp_us"], c),
            f"G4 P{a['vila_vid_stopp_s']}", "M67 E0 Q0 (pulserna av: stoppet bär armen)"]


def generera(c: dict) -> dict[str, list[str]]:
    m = {
        "stift_ut.nc": huvud("stift_ut", "fäll ut CR Touchens stift") + stift("ut_us", c),
        "stift_in.nc": huvud("stift_in", "dra in CR Touchens stift") + stift("in_us", c),
        "crtouch_sjalvtest.nc": huvud("crtouch_sjalvtest", "stiftet går ut och in tio gånger, sedan indraget")
        + stift("sjalvtest_us", c) + ["G4 P8"] + stift("in_us", c),
        "crtouch_larm_av.nc": huvud("crtouch_larm_av", "släpp CR Touchens larm (blinkande), sedan indraget")
        + stift("larm_av_us", c) + stift("in_us", c),
    }
    if c["arm"]["installd"]:
        mt = c["matning"]
        m["arm_ut.nc"] = huvud("arm_ut", "fäll ut proben från parkerat läge") + sakert(c) + stift("in_us", c) + arm_till("utfalld_us", c)
        m["arm_in.nc"] = huvud("arm_in", "parkera proben mot magneten") + sakert(c) + stift("in_us", c) + arm_till("parkerad_us", c)
        m["mat_z.nc"] = (huvud("mat_z", "mät materialets ovansida under proben; läs PRB i konsolen")
            + ["(Kör först efter godkänt funktionsprov, INKOPPLING_OCH_PROV.md steg 3. Kör över materialet, inte över en kant.)"]
            + sakert(c) + stift("in_us", c) + arm_till("utfalld_us", c) + stift("ut_us", c)
            + ["G91", f"G38.2 Z-{mt['max_ned_mm']:.2f} F{mt['snabb_mm_min']} (snabb sökning; larm om inget hittas)",
               f"G0 Z{mt['lyft_mm']:.2f}", "(stiftet drogs in av sig självt vid kontakt; fäll ut igen)"] + stift("ut_us", c)
            + [f"G38.2 Z-{mt['lyft_mm'] + 1:.2f} F{mt['langsam_mm_min']} (långsam mätning, detta värde gäller)",
               f"G0 Z{mt['lyft_mm']:.2f}", "G90"] + stift("in_us", c) + sakert(c) + arm_till("parkerad_us", c))
    return m


def sjalvtest() -> None:
    c = json.loads((HAR / "installning.json").read_text())
    assert q(1500, 50) == "7.5000" and q(647, 50) == "3.2350"
    assert not kontrollera(c), kontrollera(c)
    assert "arm_ut.nc" not in generera(c), "armmakron får inte skapas innan armen är inställd"
    p = json.loads(json.dumps(c))
    p["arm"].update(installd="test", parkerad_us=2300, utfalld_us=700)
    assert not kontrollera(p), kontrollera(p)
    g = generera(p)
    ut = "\n".join(g["arm_ut.nc"])
    assert "M5" in ut and "G53 G0 Z" in ut and ut.rstrip().endswith("M67 E0 Q0 (pulserna av: stoppet bär armen)")
    assert f"Q{q(670, 50)}" in ut, "utfällt ska tryckas 30 µs förbi stoppet"
    assert f"Q{q(2330, 50)}" in "\n".join(g["arm_in.nc"]), "parkerat ska tryckas 30 µs förbi stoppet åt andra hållet"
    mz = "\n".join(g["mat_z.nc"])
    assert mz.index("G38.2") > mz.index("M67 E1 Q3.2350"), "stiftet ut före mätning"
    andra = mz.index("G38.2", mz.index("G38.2") + 1)
    assert mz.rindex("M67 E1 Q3.2350", 0, andra) > mz.index("G38.2"), "stiftet fälls ut igen före den långsamma mätningen"
    assert mz.rstrip().endswith("M67 E0 Q0 (pulserna av: stoppet bär armen)"), "mätningen slutar med parkerad arm"
    for fel in ({"parkerad_us": 2300, "utfalld_us": 2000}, {"parkerad_us": 2600, "utfalld_us": 700}, {"forbi_stopp_us": 200}):
        p2 = json.loads(json.dumps(p)); p2["arm"].update(fel)
        assert kontrollera(p2), f"felaktig inställning släpptes igenom: {fel}"
    print("GODKÄND: makron.py självtest")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kontroll", action="store_true")
    a = ap.parse_args()
    sjalvtest()
    if a.kontroll:
        return
    c = json.loads((HAR / "installning.json").read_text())
    fel = kontrollera(c)
    if fel:
        raise SystemExit("UNDERKÄND installning.json: " + "; ".join(fel))
    ut = HAR / "makron"
    ut.mkdir(exist_ok=True)
    for f in ut.glob("*.nc"):
        f.unlink()
    for namn, rader in generera(c).items():
        (ut / namn).write_text("\n".join(rader) + "\n")
        print("skrev", namn)
    if not c["arm"]["installd"]:
        print("armens makron (arm_ut, arm_in, mat_z) skapas när armens pulser är inställda, se README steg 3")


if __name__ == "__main__":
    main()
