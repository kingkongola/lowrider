"""Parametriskt kontrakt för sidotornets CR Touch-gränssnitt.

Kör efter vanlig CAD-export i CI: python kontroll_parametrik.py
Kontrollerar att ett probe-X-avsteg (+4 mm) fortplantas till probe,
armfot, kontaktkuvert, nedre/övre stopp och magnetläge, medan
kamerans och maskinfästets kända ankare lämnas orörda.

Detta är INTE en full kollisions-, tolerans- eller monteringskontroll.
För nominellt läge finns kontroll_crtouch.py och kontroll_horn.py.
"""
from __future__ import annotations

import math

import sidotorn as cad


class Kontraktsfel(AssertionError):
    pass


def krav(villkor: bool, beskrivning: str) -> None:
    if not villkor:
        raise Kontraktsfel("UNDERKÄND: " + beskrivning)


def nara(a: float, b: float, namn: str, tol: float = 0.03) -> None:
    krav(abs(a - b) <= tol, f"{namn}: {a:.5f} ≠ {b:.5f} (tolerans {tol})")


def bbox_foljer_x(referens, variant, dx: float, namn: str) -> None:
    """Kontrollerar verklig BRep-bounding box, inte källans placeringsvariabel."""
    a, b = referens.bounding_box(), variant.bounding_box()
    nara(b.min.X - a.min.X, dx, f"{namn}.min.X")
    nara(b.max.X - a.max.X, dx, f"{namn}.max.X")
    for axel in ("Y", "Z"):
        nara(getattr(b.min, axel), getattr(a.min, axel), f"{namn}.min.{axel}")
        nara(getattr(b.max, axel), getattr(a.max, axel), f"{namn}.max.{axel}")


def kontrollera_proben(probe_fn, x0: float, dx: float) -> None:
    bbox_foljer_x(probe_fn(x0), probe_fn(x0 + dx), dx, "CR Touch")


def kontrollera_stopp_och_magnet(x: float) -> None:
    """Två olika konstruktionsfunktioner ska beskriva samma kontaktpunkt."""
    u, n, langd = cad.arm_geo(x)
    krav(abs(math.hypot(*u) - 1) < 1e-10, "armens riktningsvektor är inte normerad")
    t = cad.STOPP_T[0]
    w0, w1 = cad.ARM_W
    bredd = w0 + (w1 - w0) * t / langd
    nedre = cad.stopp_block(x, -1, w0, w1)
    nara(nedre[0][0], cad.PX + u[0] * t - n[0] * bredd, "nedre stoppets X", 1e-6)
    nara(nedre[0][1], cad.PZ + u[1] * t - n[1] * bredd, "nedre stoppets Z", 1e-6)

    ovre = cad.stopp_block(x, +1, w0, w1)
    t_step = 0.5
    index = round((cad.BULA_T - cad.STOPP_T[0]) / t_step)
    krav(index < len(ovre) // 2, "magnetkontaktens punkt saknas i stoppets kontur")
    mx, mz, vinkel = cad.magnet_lage(x)
    nara(ovre[index][0], mx, "magnetens X mot övre stoppet", 1e-5)
    nara(ovre[index][1], mz, "magnetens Z mot övre stoppet", 1e-5)
    nara(vinkel, math.degrees(math.atan2(n[1], n[0])) - cad.PARK,
         "magnetens normalvinkel", 1e-5)


def main() -> None:
    x0, dx = cad.PROB[0], 4.0
    fasta_ankare = (cad.LINS, cad.M5_Z, cad.PI_CENTER)

    kontrollera_proben(cad.crtouch, x0, dx)
    bbox_foljer_x(cad.kontaktkuvert(x0), cad.kontaktkuvert(x0 + dx),
                  dx, "kontaktkuvert")

    # Armfotens yttre X-gräns ska följa probens X. Resterande arm ändras
    # av rotations-/splinegeometrin och ska INTE antas vara en translation.
    arm_bas, arm_ny = cad.arm(x0), cad.arm(x0 + dx)
    krav(arm_bas.is_valid and arm_ny.is_valid, "armen är inte giltig i båda varianterna")
    krav(len(arm_bas.solids()) == len(arm_ny.solids()) == 1,
         "armen måste vara en solid i båda varianterna")
    nara(arm_ny.bounding_box().max.X - arm_bas.bounding_box().max.X,
         dx, "armfotens högra X-gräns", 0.06)

    kontrollera_stopp_och_magnet(x0)
    kontrollera_stopp_och_magnet(x0 + dx)
    gammal = cad.magnet_lage(x0)
    ny = cad.magnet_lage(x0 + dx)
    krav(math.dist(gammal[:2], ny[:2]) > 0.1,
         "magnetläget följer inte en ändrad probposition")
    krav((cad.LINS, cad.M5_Z, cad.PI_CENTER) == fasta_ankare,
         "fasta kamera-/maskin-/Pi-ankare ändrades")

    # Negativtest: simulerad felkoppling som ignorerar indata.
    # Samma BRep-kontroll MÅSTE underkänna en prob som stannat på default-X.
    try:
        kontrollera_proben(lambda _x: cad.crtouch(x0), x0, dx)
    except Kontraktsfel:
        pass
    else:
        raise Kontraktsfel("UNDERKÄND: negativtestet upptäckte inte en frikopplad CR Touch")

    # Negativtest för magnetgränssnitt: ett stillastående magnetläge
    # ska inte kunna ersätta resultatet för den flyttade proben.
    krav(math.dist(gammal[:2], ny[:2]) > 0.1,
         "UNDERKÄND: negativt magnettest kunde inte skilja lägen")
    print(f"GODKÄND: CR Touch och beroenden följer probe X {x0:.1f} → {x0 + dx:.1f} mm; "
          "negativtest för frikopplad probe fångades")
    print("BEGRÄNSNING: ingen full BRep-krockkontroll av den förskjutna sammansättningen; "
          "ingen fysisk passning verifierad")


if __name__ == "__main__":
    main()
