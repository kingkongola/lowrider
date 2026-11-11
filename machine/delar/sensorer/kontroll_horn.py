"""Kontroll av hornfickans klämväg, skruvar och rörelse. Inte fysisk glappverifiering."""
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
    arm,torn,bygel,horn=cad.arm(),cad.torn_monterat(),hf.bygel(),hf.horn()
    kropp=hf.provkropp()
    kallor=[Path(__file__),Path(cad.__file__),Path(hf.__file__),Path(cad.lampor.__file__),Path(cad.cr.__file__),cad.cr.REFERENS]
    r={'build123d':build123d.__version__,'kallor_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in kallor},
       'granssnitt':{},'mattskillnader':[],'svep':{},'fel':[]}
    for nam,o in [('arm',arm),('torn',torn),('bygel',bygel),('provkropp',kropp)]:
        if not o.is_valid or len(o.solids())!=1:r['fel'].append('Ogiltig/delad kropp: '+nam)
    for nam,x,y in [('prov/horn',kropp,horn),('prov/bygel',kropp,bygel),('horn/bygel',horn,bygel),
                   ('arm/horn',arm,cad.horn_lage(horn)),('arm/bygel',arm,cad.horn_lage(bygel)),('bygel/skruvar',bygel,hf.skruvar())]:
        v=volym(x&y);r['granssnitt'][nam]={'intrang_mm3':round(v,7),'avstand_mm':round(x.distance_to(y),6)}
        if v>1e-5:r['fel'].append(f'{nam}: {v:.6f} mm³')
    # Oberoende ±0,2 mm avvikelse i respektive bredd och tjocklek.
    # Navdiametern varierar också ±0,2. De fasta stöden bestämmer sättningen;
    # bygeln förskjuts i y tills dess sneda yta når hornets övre kant.
    mn=(hf.C-hf.D)/2/(hf.F-hf.E);h0=hf.h(0)
    for dc,dd,dg,da in itertools.product((-.2,0,.2),repeat=4):
        c,d,g,diam=hf.C+dc,hf.D+dd,hf.G+dg,hf.NAV_D+da
        ma=(c-d)/2/(hf.F-hf.E);phi=math.atan(mn)-math.atan(ma)
        dx=(diam-hf.NAV_D)/2
        dn=-h0+hf.h(0,c,d)*math.sqrt(1+mn*mn)/math.sqrt(1+ma*ma)+mn*dx
        mp=-ma
        slope=(math.sin(phi)+mp*math.cos(phi))/(math.cos(phi)-mp*math.sin(phi))
        intercept=hf.h(0,c,d)/(math.cos(phi)-mp*math.sin(phi))+dn-slope*dx
        q=dg+max(slope*t+intercept-hf.h(t) for t in (16.2,17.8))
        ho=Pos(dx,0,dn)*Rot(0,-math.degrees(phi),0)*hf.horn(c,d,g,diam)
        ka=Pos(0,q,0)*bygel
        iv={n:round(volym(x&y),7) for n,x,y in [('horn/kropp',ho,kropp),('horn/bygel',ho,ka),('bygel/kropp',ka,kropp)]}
        spets=hf.SKRUVSATE+q-hf.SKRUV_L
        rad={'avvikelser_C_D_G_A_mm':[dc,dd,dg,da],'bygel_y_mm':round(q,6),
             'navcentrum_x_z_mm':[round(dx,6),round(dn,6)],'intrang_mm3':iv,
             'skruvgrepp_mm':round(-spets,6),'till_halbotten_mm':round(spets-hf.PILOT_BOTTEN,6)}
        r['mattskillnader'].append(rad)
        if any(v>1e-5 for v in iv.values()) or spets<=hf.PILOT_BOTTEN or -spets<4:
            r['fel'].append('Klämfall: '+str(rad))
    # Kontrollera att intrångstestet reagerar när bygeln sänks för långt.
    r['avsiktligt_fel_bygel_02_mm_for_lag_intrang_mm3']=round(volym((Pos(0,-.2,0)*bygel)&horn),6)
    if r['avsiktligt_fel_bygel_02_mm_for_lag_intrang_mm3']<.01:r['fel'].append('Kontrollen upptäcker inte för låg bygel')
    print('Klämfall',len(r['mattskillnader']),'fel',len(r['fel']),flush=True)
    montering=[]
    for y,n in [(.5,6-i*.5) for i in range(13)]+[(.5-i*.1,0) for i in range(1,6)]:
        q=cad.horn_lage(Pos(0,y,n)*horn);v=volym(q&arm)
        montering.append({'horn_y_n_mm':[round(y,4),round(n,4)],'intrang_mm3':round(v,7)})
        if v>1e-5:r['fel'].append(f'Monteringsintrång {y}/{n}: {v:.6f} mm³')
    r['hornmontering_stickprov']=montering
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
    heads=Compound(children=[hf.cy(x,z,hf.SKRUVSATE,hf.SKRUVSATE+3,5.5) for x,z in hf.SKRUVAR])
    if volym(cad.horn_lage(heads)&arm)>1e-5:r['fel'].append('Bygelns skruvskallar intränger i armen')
    sn,so=cad.stoppdelar()
    hinder={'tornkropp':cad.torn(),'stoppdelar':sn+so,'servoattrapp':cad.servo_attrapp(),
            'lampmodul':Compound(children=[cad.lampor.barare(),cad.lampor.lampkuvert()])}
    delar={'arm':arm,'bygel':cad.horn_lage(bygel),'bygel_M3x10':cad.horn_lage(hf.skruvar()),'magnetstal_M3x10':stal}
    for nam,o in delar.items():
        bb=o.bounding_box();radie=max(math.hypot(x-cad.PX,z-cad.PZ) for x in (bb.min.X,bb.max.X) for z in (bb.min.Z,bb.max.Z))
        steg=.5 if nam=='magnetstal_M3x10' else (1 if nam=='arm' else 2)
        granser=2*radie*math.sin(math.radians(steg)/4)
        for hn,hi in hinder.items():
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
        'Geometriskt klämprov, inte mätning av skruvförspänning, friktion, hållfasthet eller krypning i plast.',
        'M3-gängan formar sig i Ø2,6-pilot: skruvskaftets nominella intrång i pilotväggen är avsiktligt.',
        'Hornets exakta spets, navets tandning och servoattrappens läge måste provpassas.',
        'Arm mot ändstopp får ha nollavstånd. Avståndsgränsen bevisar inte avsiktlig stoppkontakt.',
        'Stålskruven vid magneten är ett M3x10-kuvert; verklig längd och skalle kontrolleras före montage.',
        'Fysisk passning, glapp, skruvåtkomst, kabelböjar och magnetkraft återstår.']
    a.ut.parent.mkdir(parents=True,exist_ok=True);a.ut.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    print('Fel:',r['fel'],flush=True);raise SystemExit(bool(r['fel']))


if __name__=='__main__':main()
