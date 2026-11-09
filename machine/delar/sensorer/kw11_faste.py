"""Utbytbar KW11-3Z-N-hållare, en enda printdel (antal 2).

Amazonbilden från 2026-11-09 anger 20 mm längd, Ø5 mm rulle,
ungefär 20 mm rullspak, 4 mm terminaler och '16 mm' vertikalt.
Bilden saknar uttryckligt centrumavstånd. Vanliga KW11-3Z säljs som
20×10.2×6.4 mm kropp med 9–9.5 mm centrumavstånd. CAD-mallen
är därför NOMINELL och INTE en verifierad QUARKZMAN-måttritning. Hållaren skruvas på
servokassetten, aldrig på V1E:s original-Core. Lägesbekräftelse är INTE
ett mekaniskt stopp; rullspakens verkliga arbetspunkt kräver mätning.
"""
from __future__ import annotations

from build123d import Plane, Polygon, extrude
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/"nollpunkt"))
from fallarm import cy, k, prisma_xz

# All geometri i ett lokalt X/Y/Z-system, millimeter. Platta i X/Z,
# extruderad mot +Y för plan FDM-utskrift på en sida.
PLATT_T=4.0
SKRUVBRYTARE_M2=2.7 # hålen på verklig KW11-kropp kontrolleras vid leverans
SKRUV_KASSETT_M3=3.4
X_BRYTARE=(8.0,17.5)   # 9.5 c-c nominal från liknande KW11, två breda slitsar
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


# Separat referensATTRAPP till 3D-montage, exporteras ALDRIG som print-STL.
# Kroppens höjd är antagen från vanliga KW11-3Z (inte säljbildens
# inkonsekvent proportionerade '16 mm'). Frigång till rullspaken är
# dessutom försedd med marginal, men manövervägen är EJ känd.
KW11_MALL = {
    "body_mm": [20.0, 6.4, 10.2],    # längd, tjocklek, höjd
    "roller_d_mm": 5.0,             # QUARKZMAN-bild
    "lever_span_mm": 20.0,         # QUARKZMAN-bild, ej slaglängd
    "terminal_length_mm": 4.0,     # QUARKZMAN-bild
    "nominal_pitch_mm": 9.5,       # ANNAN KW11-3Z variant
    "mount_pitch_verified": False,
    "switch_actuation_point_verified": False,
}

def kw11_atrapper():
    """CAD-referenser för kropp, hävarm, rulle och tre metallterminaler.

    Passar visuellt med kw11_hallare i dess lokala X/Z-ram. Kroppens
    M2-borrcentrum är visuellt inlagt, inte en fysisk mätning.
    Komponenterna hålls isär för att inte förväxlas med printkroppar.
    """
    x0=2.5
    z0=Z_BRYTARE-4.2
    y0=PLATT_T+0.1
    body=k((x0,x0+20.0),(y0,y0+6.4),(z0,z0+10.2))
    for x in X_BRYTARE:
        body-=cy(y0-0.2,y0+6.6,x,Z_BRYTARE,2.35)
    upper=z0+10.2
    # Tunn böjd hävarm; antagen FRIGÅNGSENVELOPP, ej pressningsrörelse.
    lever=prisma_xz([(x0+1.7,upper+2.3),
                      (x0+17.6,upper+0.4),
                      (x0+17.6,upper+1.1),
                      (x0+1.7,upper+3.0)],y0+2.7,y0+3.6)
    roller=cy(y0+1.2,y0+5.2,x0+2.0,upper+4.1,5.0)
    terminals=[]
    for x in (x0+3.1,x0+10.2,x0+17.5):
        terminals.append(k((x-0.3,x+0.3),
                           (y0+2.5,y0+3.3),(z0-4,z0+0.5)))
    return {"hus":body,"havararm":lever,"rulle":roller,
            **{f"terminal_{i+1}":p for i,p in enumerate(terminals)}}
