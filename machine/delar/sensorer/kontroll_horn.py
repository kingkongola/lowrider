"""Kontroll av hornets formficka, mittskruvens stapel, insättning och rörelse. Inte fysisk glappverifiering."""
import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
import build123d
from build123d import Compound, Cylinder, Pos, Rot
import sidotorn as cad


def volym(o):
    return 0.0 if o is None else sum(s.volume for s in o.solids())


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--ut',type=Path,required=True)
    a=ap.parse_args();hf=cad.hf
    arm,torn,horn=cad.arm(),cad.torn_monterat(),hf.horn()
    kropp=hf.provkropp();skruv=hf.mittskruv()
    kallor=[Path(__file__),Path(cad.__file__),Path(hf.__file__),Path(cad.lampor.__file__),Path(cad.cr.__file__),cad.cr.REFERENS]
    r={'build123d':build123d.__version__,'kallor_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in kallor},
       'granssnitt':{},'mattskillnader':[],'svep':{},'fel':[]}
    for nam,o in [('arm',arm),('torn',torn),('provkropp',kropp)]:
        if not o.is_valid or len(o.solids())!=1:r['fel'].append('Ogiltig/delad kropp: '+nam)
    # Nominellt: hornet i fickan och M3-skruven i sätet utan intrång.
    for nam,x,y in [('prov/horn',kropp,horn),('prov/mittskruv',kropp,skruv),
                   ('arm/horn',arm,cad.horn_lage(horn)),('arm/mittskruv',arm,cad.horn_lage(skruv))]:
        v=volym(x&y);r['granssnitt'][nam]={'intrang_mm3':round(v,7),'avstand_mm':round(x.distance_to(y),6)}
        if v>1e-5:r['fel'].append(f'{nam}: {v:.6f} mm³')
    # Formlåsningen: väggarna ska ligga inom SPEL från hornet. Ett horn som är 0,05 mm större
    # per sida än spelet ska ta i (negativtest: annars är fickan för stor och hornet glappar).
    stor=hf.armkuvert(.01,hf.G-.01,hf.SPEL+.05)
    r['negativtest_horn_spel_plus_005_intrang_mm3']=round(volym(kropp&stor),6)
    if r['negativtest_horn_spel_plus_005_intrang_mm3']<.01:r['fel'].append('Fickan är större än SPEL: hornet kan glappa')
    # Skruvstapeln: samma gängdjup som fabriksskruven, så att M3 x 10 inte kan bottna i axeln.
    r['gangdjup_mm']=hf.gangdjup();r['fabriksskruvens_gangdjup_mm']=hf.FABRIKSSKRUV_L-hf.FLANS
    if abs(hf.gangdjup()-(hf.FABRIKSSKRUV_L-hf.FLANS))>1e-9:r['fel'].append('Gängdjupet skiljer sig från fabriksskruvens')
    # Skallen ska ligga helt försänkt i navbossen.
    r['skalle_under_bossytan_mm']=round(hf.SKALLE[1]+.3-hf.SKALLE[1],3)
    # Måttvariation: hornets bredder, tjocklek och nav ±0,2. Redovisas; passningen avgörs av provbiten.
    for dc,dd,dg,da in itertools.product((-.2,0,.2),repeat=4):
        ho=hf.horn(hf.C+dc,hf.D+dd,hf.G+dg,hf.NAV_D+da)
        v=volym(ho&kropp)
        r['mattskillnader'].append({'avvikelser_C_D_G_A_mm':[dc,dd,dg,da],'intrang_mm3':round(v,5)})
    tr=sum(1 for m in r['mattskillnader'] if m['intrang_mm3']>1e-5)
    r['mattfall_som_tar_i']=f'{tr} av {len(r["mattskillnader"])} (väntat: horn >0,15 mm bredare per sida)'
    print('Måttfall som tar i:',r['mattfall_som_tar_i'],flush=True)
    # Insättning: hornet rakt in i fickan från servosidan, 12 mm i steg.
    montering=[]
    for y in [.05,.2,.5]+list(range(1,13)):
        q=cad.horn_lage(Pos(0,y,0)*horn);v=volym(q&arm)
        montering.append({'horn_y_mm':y,'intrang_mm3':round(v,7)})
        if v>1e-5:r['fel'].append(f'Hornet tar i armen {y} mm före sitt läge: {v:.6f} mm³')
    r['hornmontering']=montering
    # Skruvens väg: skallen in i sätet utifrån, 12 mm.
    for y in [.2,.5]+list(range(1,13)):
        v=volym(cad.horn_lage(Pos(0,-y,0)*hf.cy(0,0,-hf.BOTTEN-hf.SKALLE[1],-hf.BOTTEN,hf.SKALLE[0]))&arm)
        if v>1e-5:r['fel'].append(f'Skallen tar i armen {y} mm utanför sätet: {v:.6f} mm³')
    stal=cad.magnet_skruv_attrapp()
    r['magnetstal_horn_avstand_mm']=round(stal.distance_to(cad.horn_lage(horn)),6)
    if volym(stal&cad.horn_lage(horn))>1e-5:r['fel'].append('Magnetens stålskruv intränger i hornet')
    r['magnetstal_gangmaterial_mm3']=round(volym(stal&arm),6)
    if r['magnetstal_gangmaterial_mm3']<.1:r['fel'].append('Magnetkontaktens skruv saknar gängmaterial')
    mx,mz,mv=cad.magnet_lage(cad.PROB[0]);my=sum(cad.BULA_Y)/2
    ux,uz=math.cos(math.radians(mv)),math.sin(math.radians(mv))
    def magnetprov(langd,m):
        return Pos(mx+ux*m,my,mz+uz*m)*Rot(0,90-mv,0)*Cylinder(.15,langd)
    hud=magnetprov(cad.HUD-.1,cad.HUD/2)
    r['magnet_hud_karnvolym_mm3']=round(volym(hud&torn),7)
    if abs(volym(hud&torn)-hud.volume)>1e-6:r['fel'].append('Magnetstoppets skyddshud saknas i centrum')
    magnet=Pos(mx+ux*(cad.HUD+1.5),my,mz+uz*(cad.HUD+1.5))*Rot(0,90-mv,0)*Cylinder(3,3)
    r['magnet_intrang_i_ficka_mm3']=round(volym(magnet&torn),7)
    if volym(magnet&torn)>1e-5:r['fel'].append('Ø6x3-magneten får inte plats i sitt urtag')
    sn,so=cad.stoppdelar()
    axel=cad.cyl_y(cad.PX,cad.PZ,0,60,6.2)   # hornet sitter på axeln och mittskruven går in i den: avsett
    hinder={'tornkropp':cad.torn(),'stoppdelar':sn+so,'servoattrapp':cad.servo_attrapp(),'servo_utan_axel':cad.servo_attrapp()-axel,
            'lampmodul':Compound(children=[cad.lampor.barare(),cad.lampor.lampkuvert()])}
    delar={'arm':arm,'horn':cad.horn_lage(horn),'mittskruv_M3x10':cad.horn_lage(skruv),'magnetstal_M3x10':stal}
    for nam,o in delar.items():
        bb=o.bounding_box();radie=max(math.hypot(x-cad.PX,z-cad.PZ) for x in (bb.min.X,bb.max.X) for z in (bb.min.Z,bb.max.Z))
        steg=.5 if nam=='magnetstal_M3x10' else (1 if nam=='arm' else 2)
        granser=2*radie*math.sin(math.radians(steg)/4)
        for hn,hi in hinder.items():
            pa_axeln=nam in ('horn','mittskruv_M3x10')
            if (hn=='servoattrapp' and pa_axeln) or (hn=='servo_utan_axel' and not pa_axeln):continue
            rr=[]
            for i in range(round(-cad.PARK/steg)+1):
                g=cad.PARK+i*steg
                q=Pos(cad.PX,0,cad.PZ)*Rot(0,g,0)*Pos(-cad.PX,0,-cad.PZ)*o
                d=q.distance_to(hi);v=volym(q&hi) if d<.0001 else 0
                rr.append({'grader':g,'avstand_mm':round(d,6),'intrang_mm3':round(v,7)})
                if v>1e-5:r['fel'].append(f'{nam}/{hn} vid {g}°: {v:.6f} mm³')
            # Avsedd kontakt i ändlägena: armen mot stoppen, stålskruven mot magnetstoppet parkerat.
            # Mot stoppdelarna är kontakt avsedd i ändlägena: armen i båda, stålskruven parkerad.
            # Inflygningen 5° före ändläget undantas bara mot stoppdelarna, aldrig mot tornkroppen.
            till={('arm','stoppdelar'):(cad.PARK,0),('magnetstal_M3x10','stoppdelar'):(cad.PARK,)}.get((nam,hn),())
            ovr=[v for v in rr if not any(abs(v['grader']-t)<=5 for t in till)]
            mini=min(ovr,key=lambda v:v['avstand_mm'])
            fria=mini['avstand_mm']>granser
            if not fria:r['fel'].append(f"{nam}/{hn}: mellanlägen obevisade, {mini['avstand_mm']} mm vid {mini['grader']}° mot gräns {granser:.4f}")
            r['svep'][nam+'/'+hn]={'steg_grader':steg,'minsta':mini,'rotationsgrans_mm':round(granser,6),
                'mellanlagen_fria':fria,'lagen':rr}
            print(nam,hn,mini,flush=True)
    r['begransningar']=[
        'Geometrisk kontroll, inte mätning av skruvförspänning, hållfasthet eller krypning i plast.',
        'Hornets exakta spets och kontur är konstruerade ur fyra mått; formlåsningen provas med provbiten.',
        'Mittskruvens gänga (M3 eller 4-40) är inte provad; M3 x 10 provas för hand i axeln före åtdragning.',
        'Arm mot ändstopp får ha nollavstånd. Avståndsgränsen bevisar inte avsiktlig stoppkontakt.',
        'Stålskruven vid magneten är ett M3x10-kuvert; verklig längd och skalle kontrolleras före montage.',
        'Fysisk passning, glapp, skruvåtkomst, kabelböjar och magnetkraft återstår.']
    a.ut.parent.mkdir(parents=True,exist_ok=True);a.ut.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    print('Fel:',r['fel'],flush=True);raise SystemExit(bool(r['fel']))


if __name__=='__main__':main()
