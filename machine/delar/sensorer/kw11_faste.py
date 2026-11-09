"""Utbytbar KW11-3Z-N-hållare, en enda printdel (antal 2).

Komponentmått är ännu *nominella*: 20×10×6.4 mm kropp och 8,5–9,5 mm
hålavstånd före leverans av QUARKZMAN-paketet. Hållaren skruvas på
servokassetten, aldrig på V1E:s original-Core. Lägesbekräftelse är INTE
ett mekaniskt stopp; rullspakens verkliga arbetspunkt kräver mätning.
"""
from __future__ import annotations

from build123d import Plane, Polygon, extrude
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/"nollpunkt"))
from fallarm import cy, k

# All geometri i ett lokalt X/Y/Z-system, millimeter. Platta i X/Z,
# extruderad mot +Y för plan FDM-utskrift på en sida.
PLATT_T=4.0
SKRUVBRYTARE_M2=2.7 # hålen på verklig KW11-kropp kontrolleras vid leverans
SKRUV_KASSETT_M3=3.4
X_BRYTARE=(8.0,17.0)    # 9.0 c-c nominellt; justerslits 8.5–9.5 och ±1
X_DOCK=30.0
Z_DOCK=(6.0,17.0)
Z_BRYTARE=11.5

def kw11_hallare():
    """En låg, fasad, individuellt lossbar brytarhållare.

    M2-slitsar över osäkert leverantörsmått; M3-slitsar ger ±2 mm justering
    relativt servokassettens stationära fästöra. Ingen ny Core-skruv.
    """
    outline=Plane.XZ*Polygon(
        (3,0),(32,0),(35,3),(35,20),
        (32,23),(3,23),(0,20),(0,3),align=None,
    )
    s=extrude(outline,amount=PLATT_T,dir=(0,1,0))
    # KW11: två M2-långhål orienterade längs X för olika hålavstånd.
    for x in X_BRYTARE:
        for dx in (-1.1,1.1):
            s-=cy(-0.5,PLATT_T+0.5,x+dx,Z_BRYTARE,SKRUVBRYTARE_M2)
        s-=k((x-1.1,x+1.1),(-0.5,PLATT_T+0.5),
             (Z_BRYTARE-SKRUVBRYTARE_M2/2,Z_BRYTARE+SKRUVBRYTARE_M2/2))
    # Fäste mot egen servokassett, två separata M3 med ±2 mm Z-justering.
    for z in Z_DOCK:
        for dz in (-2.0,2.0):
            s-=cy(-0.5,PLATT_T+0.5,X_DOCK,z+dz,SKRUV_KASSETT_M3)
        s-=k((X_DOCK-SKRUV_KASSETT_M3/2,X_DOCK+SKRUV_KASSETT_M3/2),
             (-0.5,PLATT_T+0.5),(z-2,z+2))
    # Integrerad lätt kabelavlastning vid kontaktändan: två hål för ett
    # smalt buntband; framdragen kabel får inte användas som dragstopp.
    for x in (5,11):
        s-=cy(-0.5,PLATT_T+0.5,x,19.5,2.0)
    return s
