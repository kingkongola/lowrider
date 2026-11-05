"""Attrapp av proben V5/TP05C för provmontering, inte för mätning.
Mått ur annonsens ritning (ej uppmätt): kropp Ø33 x 21, skaft Ø6 x 20, stylus 26.
Kontakten är uppskattad ur annonsens foto: mäts och ändras vid leverans."""
from build123d import *
from pathlib import Path
UT = Path(__file__).parent
KROPP_D, KROPP_H = 33.0, 21.0
STIFT_L, SKAFT_L, SKAFT_D = 26.0, 20.0, 6.0
KONTAKT_UNDER_TOPP, KONTAKT_L, KONTAKT_D = 7.0, 25.0, 9.0
def del_kropp():
    """Står på överkanten med stylus uppåt, utskriftsläge."""
    k = Cylinder(KROPP_D/2, KROPP_H, align=(Align.CENTER, Align.CENTER, Align.MIN))
    k = chamfer(k.edges().group_by(Axis.Z)[-1], 1.5)
    k += Cylinder(4.5, 4, align=(Align.CENTER, Align.CENTER, Align.MIN)).moved(Location((0, 0, KROPP_H)))
    k += Cylinder(2.0, STIFT_L-2.5, align=(Align.CENTER, Align.CENTER, Align.MIN)).moved(Location((0, 0, KROPP_H)))   # Ø4, grövre än verkligt för att hålla
    k += Sphere(2.5).moved(Location((0, 0, KROPP_H+STIFT_L-2.5)))
    k -= Cylinder(3.1, 10, align=(Align.CENTER, Align.CENTER, Align.MIN)).moved(Location((0, 0, -0.5)))
    kontakt = Cylinder(KONTAKT_D/2, KONTAKT_L+KROPP_D/2, align=(Align.CENTER, Align.CENTER, Align.MIN))
    k += kontakt.moved(Location((0, 0, KONTAKT_UNDER_TOPP), (-90, 0, 0)))
    return k
def del_skaft():
    return Cylinder(SKAFT_D/2, SKAFT_L+9.5, align=(Align.CENTER, Align.CENTER, Align.MIN))
if __name__ == "__main__":
    for n, d in (("kropp", del_kropp()), ("skaft", del_skaft())):
        print(n, d.is_valid, len(d.solids()), round(d.volume/1000, 1), d.bounding_box().size)
        export_stl(d, str(UT/f"attrapp_{n}.stl"), tolerance=0.05, angular_tolerance=0.2)
