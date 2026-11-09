"""Konsekvent montagegranskning av MODULÄR sensorenhet på befintlig Core.

Exakt BRep-intersektion mellan våra egna build123d-delar; AABB/samplad
ytavståndsscreening mot befintliga referens-STL. Det är inte ett
säkerhetsgodkännande, ej heller verklig uppmätning av maskinen.
"""
from __future__ import annotations

import io
import json
import math
import sys
import zipfile
from itertools import combinations
from pathlib import Path

import numpy as np
import trimesh
from build123d import Pos, Rot

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
from core_enhet import delar, Param, C, k, cz


def positionerade(d: Param = Param()):
    parts = delar(d)
    parts["pi_lada"] = Pos(d.pi_x, d.pi_y, d.pi_z) * parts["pi_lada"]
    parts["pi_lock"] = Pos(d.pi_x, d.pi_y, d.pi_z + 22.0) * parts["pi_lock"]
    return parts


def brep_intersektioner(parts: dict) -> list[dict]:
    """Alla oväntade överlapp. Förväntad skruvförbindning = ytberöring (0 mm³)."""
    found = []
    for (name1,a),(name2,b) in combinations(parts.items(),2):
        ab,bb = a.bounding_box(), b.bounding_box()
        lower = np.maximum(np.asarray(tuple(ab.min),dtype=float),np.asarray(tuple(bb.min),dtype=float))
        upper = np.minimum(np.asarray(tuple(ab.max),dtype=float),np.asarray(tuple(bb.max),dtype=float))
        overlap = upper-lower
        if (overlap <= 0.05).any():
            continue
        try:
            result=a.intersect(b)
            if result is None: # build123d returnerar None för tom BRep-skärning
                volume=0.0
            elif isinstance(result,list):
                volume = sum(float(s.volume) for s in result)
            else:
                volume=float(result.volume)
        except Exception as e:
            found.append({"par":[name1,name2],"status":"kan_inte_verifieras","fel":str(e)[:120]})
            continue
        if volume > .05:
            found.append({"par":[name1,name2],"status":"intrang",
                          "overlapp_mm3":round(volume,3),
                          "bbox_intersektion_mm":np.round(overlap,2).tolist()})
    return sorted(found,key=lambda v:-v.get("overlapp_mm3",0))


def _gemensam_volym(a,b) -> float:
    r=a.intersect(b)
    if r is None:
        return 0.0
    if isinstance(r,list):
        return sum(float(s.volume) for s in r)
    return float(r.volume)


def rorelse_svep(parts:dict, d:Param) -> dict:
    """Grov mätplansmodell: servorörelse 0..-90 grader, ingen rörelse i CNC.

    BlTouch-fästets kroppslängd är från datablad; connector, kabel,
    servohorn av metall och toleranser är EJ CAD-mätta.
    """
    # Smal BLTouch-kropp 11.5 x 5.8 mm och helt utfällt stift.
    # Att den rör vid undersidan av monteringsflänsen är avsiktligt.
    z_flans=d.bl_tip_z+d.bl_tip_from_flange
    body=k((C.XC-5.75,C.XC+5.75),(C.YC-2.9,C.YC+2.9),
           (z_flans-36.3,z_flans))
    pin=cz(d.bl_tip_z,z_flans-36.3,C.XC,C.YC,2.4)
    probe=body+pin
    # C.servo() är endast skalenlig skiss, METALLHORNET saknas.
    fixed={n:p for n,p in parts.items() if n!="bltouch_arm"}
    fixed["SPMS664_ritad"]=C.servo()
    unsafe=[]
    nearest={}
    for angle in range(-90,1,15):
        transform=(Pos(C.PX,0,C.PZ)*Rot(0,angle,0)
                   *Pos(-C.PX,0,-C.PZ))
        for moving_name,moving in [
            ("BLTouch_arm",transform*parts["bltouch_arm"]),
            ("BLTouch_kropp_mall",transform*probe)
        ]:
            mb=moving.bounding_box()
            for fixed_name,p in fixed.items():
                fb=p.bounding_box()
                lo=np.maximum(np.asarray(tuple(mb.min)),np.asarray(tuple(fb.min)))
                hi=np.minimum(np.asarray(tuple(mb.max)),np.asarray(tuple(fb.max)))
                sep=np.maximum(0,lo-hi)
                dist=float(np.linalg.norm(sep))
                key=moving_name+"--"+fixed_name
                nearest[key]=min(nearest.get(key,float("inf")),dist)
                if dist>0:
                    continue
                try:
                    vol=_gemensam_volym(moving,p)
                    if vol>0.05:
                        unsafe.append({"angle_deg":angle,"moving":moving_name,
                                       "fixed":fixed_name,"overlap_mm3":round(vol,2)})
                except Exception as e:
                    unsafe.append({"angle_deg":angle,"moving":moving_name,
                                   "fixed":fixed_name,"unverified":str(e)[:100]})
    return {"poses_deg":list(range(-90,1,15)),
            "CAD_collisions":unsafe,
            "min_bbox_separation_mm":{k:round(v,2) for k,v in nearest.items()},
            "BEGRANSNING":"Bara fast CAD och approx BLTouch kropp; inga servohorn, Omron-hävarmar, kablar, riktiga toleranser eller full Core-mesh som BRep" }


def referens_stl():
    """Referenser är existerande originalfiler, inte våra framtagna ur fantasin."""
    source=ROOT/"machine"/"delar"
    o={}
    for key, filename in [
        ("tool_mount_t","tool-mount-t-v1-makita.stl"),
        ("tool_mount_b","tool-mount-b_makita.stl"),
        ("dammsko","dust_shoe_makita.stl"),
        ("kjol","dust_skirt_makita.stl")
    ]:
        file=source/filename
        if file.exists():
            o[key]=trimesh.load(file,force="mesh")
    servomodell=source/"nollpunkt"/"fallarm_C_servo_bild.stl"
    if servomodell.exists():
        o["SPMS664_referens"]=trimesh.load(servomodell,force="mesh")
    archive=source/"nollpunkt"/"nollpunkt-overlamning-codex.zip"
    if archive.exists():
        with zipfile.ZipFile(archive) as f:
            matches=[s for s in f.namelist() if s.endswith("/Core.stl")]
            if len(matches)==1:
                m=trimesh.load(io.BytesIO(f.read(matches[0])),file_type="stl",force="mesh")
                v=m.vertices
                # Samma M-konvertering som projektets befintliga kontroll_c.py.
                m.vertices=np.column_stack([v[:,0]-193.7,v[:,2]-92.5,
                                            -(v[:,1]-169.17)+94.75])
                o["befintlig_core"]=m
    return o


def ekran(avstand: float, antal: int):
    # Screening, INTE certifierat minavstånd: heltäckande mesh-intersektion
    # eller krävande maskinmätning återstår innan säker rörelse får ske.
    return round(float(avstand),2)


def granska(ut:Path):
    from scipy.spatial import cKDTree
    d=Param()
    parts=positionerade(d)
    intrusion=brep_intersektioner(parts)
    sweep=rorelse_svep(parts,d)
    referenser=referens_stl()
    sampled_refs={}
    for name,m in referenser.items():
        if not m.is_empty and len(m.faces):
            pts,_=trimesh.sample.sample_surface(m,min(30000,max(6000,len(m.faces)//5)),seed=3)
            sampled_refs[name]=cKDTree(pts)
    work={}
    for name,part in parts.items():
        vertices=np.asarray(tuple(part.bounding_box().min),dtype=float),np.asarray(tuple(part.bounding_box().max),dtype=float)
        lo,hi=vertices
        # Dyrt att provköra hela BRep-intersektionen mot tessellerade original.
        # Tätt sampling av våra STL gör detta till ett grovt varnande mått.
        try:
            tri=part.tessellate(0.2)[0]
            own=np.asarray([v.to_tuple() for v in tri],dtype=float)
        except Exception:
            own=np.empty((0,3),dtype=float)
        perref={}
        for ref,mesh in referenser.items():
            mi=mesh.bounds
            sep=np.maximum(0,np.maximum(lo-mi[1],mi[0]-hi))
            aabb_separation=round(float(np.linalg.norm(sep)),2)
            if aabb_separation>8:
                continue
            if len(own):
                dist=float(sampled_refs[ref].query(own,k=1,workers=-1)[0].min())
            else:
                dist=None
            perref[ref]={"aabb_min_separation_mm":aabb_separation,
                         "samplad_ytnarhet_mm":round(dist,2) if dist is not None else None,
                         "metod":"ej exakt kollisionskontroll"}
        if perref:
            work[name]=perref
    result={"schema":1,"status":"KONSTRUKTIONSGRANSKNING_EJ_SAKERT_FOR_PRINT_MONTERING",
            "interna_kollisioner":intrusion,
            "servoprob_rorelsesvep":sweep,
            "referenser":list(referenser.keys()),
            "externa_narhetsvarningar":work,
            "obekraftat":["Core- och motorfästets koordinattransform kommer från äldre kontroll_c.py",
                          "marginaler till servohornets METALL och 2 Omron-brytare",
                          "full rörelsebana 0..90 grader för BLTouch-probe och flexkabel",
                          "verklig dammsko, portpassning, skruvskallar, belysning",
                          "elektriska ledningsnivåer, kabelkrokningar, serviceloop"],
            "modulprincip":"separat rygg+skruvade moduler; befintlig Core oförändrad"}
    ut.parent.mkdir(parents=True,exist_ok=True)
    ut.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return result


if __name__=="__main__":
    if len(sys.argv)!=2:
        raise SystemExit("usage: granska_montage.py output.json")
    result=granska(Path(sys.argv[1]))
    # Intersektionerna är kvalitetsavvikelser och ska inte döljas i rapporten,
    # men rapport genereras även vid fynd för konstruktionsiteration.
    if result["interna_kollisioner"] or result["servoprob_rorelsesvep"]["CAD_collisions"]:
        raise SystemExit("CAD: överlapp i moduler eller servo-svep; granska rapporten före utskrift")
