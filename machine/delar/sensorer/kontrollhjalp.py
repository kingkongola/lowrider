"""Gemensam krockberäkning för CAD-kontrollerna. Felar stängt: om beräkningsmotorn inte kan ge ett
resultat stoppas kontrollen, i stället för att felet räknas som "ingen krock" (granskning issue #2).

Kör: python kontrollhjalp.py   (självtest: ett fel i booleanen måste ge UNDERKÄND, inte 0)
"""


class BerakningsFel(SystemExit):
    pass


def krock(a, b, namn=""):
    """Skärningsvolym i mm³. Ett undantag eller ett resultat utan volym är ett fel, aldrig 0."""
    try:
        s = a & b
    except Exception as e:
        raise BerakningsFel(f"UNDERKÄND: kollisionsberäkningen misslyckades ({namn}): {e}") from e
    if s is None:
        raise BerakningsFel(f"UNDERKÄND: kollisionsberäkningen gav inget resultat ({namn})")
    v = getattr(s, "volume", None)
    if v is None:
        raise BerakningsFel(f"UNDERKÄND: resultatet saknar volym ({namn})")
    return float(v)


if __name__ == "__main__":
    class Trasig:
        def __and__(self, _):
            raise RuntimeError("injicerat fel")
    try:
        krock(Trasig(), Trasig(), "självtest")
    except BerakningsFel:
        print("GODKÄND: ett fel i beräkningen stoppar kontrollen")
    else:
        raise SystemExit("UNDERKÄND: ett fel i beräkningen räknades som ingen krock")
