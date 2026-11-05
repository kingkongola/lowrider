"""Krock och bild för fallarm. Kräver trimesh, scipy, pillow, matplotlib. Sökvägar: CAD i /tmp/nollpunkt-prov0/cad."""
import numpy as np, trimesh, warnings, math, sys
warnings.filterwarnings('ignore')
from scipy.spatial import cKDTree
from PIL import Image, ImageDraw
import matplotlib;matplotlib.use('Agg');import matplotlib.pyplot as plt
A='/Users/bemca/dev/lowrider/machine/delar/nollpunkt/';D='/Users/bemca/dev/lowrider/machine/delar/';T='/tmp/nollpunkt-prov0/'
XC,YC=40.,40.;PX,PZ=30.6,37.1;OX,OZ=38.,85.;R,r,L=24.,14.,29.1;TH_UT=-177.;SP=-39.3
STIFT,KH,KD,SL=27.,28.,45.,23.
c=trimesh.load(T+'cad/Core.stl');v=c.vertices;core=trimesh.Trimesh(np.c_[v[:,0]-193.7,v[:,2]-92.5,-(v[:,1]-169.17)+94.75],c.faces,process=False)
def cyl(x,y,z0,z1,rr,sec=40):
    m=trimesh.creation.cylinder(radius=rr,height=z1-z0,sections=sec);m.apply_translation([x,y,(z0+z1)/2]);return m
def box(x,y,z):
    b=trimesh.creation.box(extents=[x[1]-x[0],y[1]-y[0],z[1]-z[0]]);b.apply_translation([sum(x)/2,sum(y)/2,sum(z)/2]);return b
M={'Core':core,'T':trimesh.load(D+'tool-mount-t-v1-makita.stl'),'B':trimesh.load(D+'tool-mount-b_makita.stl'),'Sko':trimesh.load(D+'dust_shoe_makita.stl'),'Kjol':trimesh.load(D+'dust_skirt_makita.stl')}
TR={k:cKDTree(trimesh.sample.sample_surface(m,150000,seed=1)[0]) for k,m in M.items()}
Sc=np.load(T+'scan_M.npy');TR['Skanning']=cKDTree(Sc)
F=trimesh.load(A+'fallarm_faste.stl');K=trimesh.load(A+'fallarm_kapa.stl');Ar=trimesh.load(A+'fallarm_arm.stl');St=trimesh.load(A+'fallarm_stag.stl');Ve=trimesh.load(A+'fallarm_vev.stl')
servo=trimesh.load(A+'fallarm_servo_bild.stl')
fast={'Fäste':F,'Kåpa':K,'Servo':servo}
for k,m in fast.items():TR[k]=cKDTree(trimesh.sample.sample_surface(m,60000,seed=2)[0])
prob=trimesh.util.concatenate([cyl(XC,YC,SP+STIFT,SP+STIFT+KH,KD/2),cyl(XC,YC,SP+STIFT+KH,SP+STIFT+KH+SL,3),cyl(XC,YC,SP+2,SP+STIFT,1.2),trimesh.creation.icosphere(radius=2,subdivisions=2).apply_translation([XC,YC,SP+2])])
def ry(deg):return trimesh.transformations.rotation_matrix(np.radians(deg),[0,1,0],[PX,0,PZ])
_C=[None]
def lage(u):
    """u=0 infälld, 1 nere. Löser fyrleden och följer samma gren från dödläget."""
    O=np.array([OX,OZ]);n=max(1,int(round(u*60)));C=None
    for i in range(n+1):
        uu_=u*i/n;th=TH_UT-90*uu_;A_=np.array([PX+r*math.cos(math.radians(th)),PZ+r*math.sin(math.radians(th))]);d=np.linalg.norm(A_-O)
        a=(R**2-L**2+d**2)/(2*d);h=math.sqrt(max(R**2-a**2,0));e=(A_-O)/d;nn=np.array([-e[1],e[0]])
        cs=[O+a*e+s_*h*nn for s_ in(1,-1)]
        if C is None:C=O+R*e if i==0 else cs[0]
        else:
            if i==1:
                C=max(cs,key=lambda q:q[0]) if GREN>0 else min(cs,key=lambda q:q[0])
            else:C=min(cs,key=lambda q:np.linalg.norm(q-C))
    return th,A_,C,O
def rorliga(u):
    th,A_,C,O=lage(u)
    arm=Ar.copy();pr=prob.copy()
    T_=ry(-90*(1-u));arm.apply_transform(T_);pr.apply_transform(T_)
    st=St.copy();ang=math.atan2(A_[1]-C[1],A_[0]-C[0]);st.apply_transform(trimesh.transformations.rotation_matrix(-ang,[0,1,0],[0,0,0]));st.apply_translation([C[0],64.6,C[1]])
    ve=Ve.copy();ang2=math.atan2(C[1]-O[1],C[0]-O[0]);ve.apply_transform(trimesh.transformations.rotation_matrix(-ang2,[0,1,0],[0,0,0]));ve.apply_translation([O[0],60.5,O[1]])
    return {'Arm':arm,'Prob':pr,'Stag':st,'Vev':ve},ang2
GREN=int(sys.argv[2]) if len(sys.argv)>2 else 1
print('vevvinkel');sw=[lage(u) for u in(0,1)]
a0=math.degrees(math.atan2(*(sw[0][2]-sw[0][3])[::-1]));a1=math.degrees(math.atan2(*(sw[1][2]-sw[1][3])[::-1]));print('infälld',round(a0,1),'nere',round(a1,1),'svep',round(abs((a1-a0+180)%360-180),1))
print('minsta avstånd (mm); under ~1 = tar i eller ligger an')
res={}
for u in np.linspace(0,1,11):
    mv,_=rorliga(u)
    for n,m in mv.items():
        P=trimesh.sample.sample_surface(m,6000,seed=3)[0]
        for k,t in TR.items():
            if (n,k) in (('Stag','Fäste'),): pass
            d=float(t.query(P)[0].min());res[(n,k)]=min(res.get((n,k),99),d)
for n in('Prob','Arm','Stag','Vev'):print(n,' '.join(f"{k} {res[(n,k)]:.1f}" for k in TR))
for k,m in fast.items():
    P=trimesh.sample.sample_surface(m,8000,seed=4)[0];print(k,' '.join(f"{q} {TR[q].query(P)[0].min():.1f}" for q in('Core','T','B','Sko','Kjol','Skanning')))
for n,u in (('nere',1),('infälld',0)):
    mv,_=rorliga(u);bb=mv['Prob'].bounds;print(n,'prob',bb.round(1).tolist(),'spets')
if len(sys.argv)>1:
    V={'snett':np.array([.85,.5,.3]),'sida':np.array([0,1,.0]),'fram':np.array([1,0,.0])}
    fr=[('c',core,(150,158,168)),('t',M['T'],(214,190,110)),('b',M['B'],(214,190,110)),('s',M['Sko'],(226,214,170)),('k',M['Kjol'],(170,165,140)),('f',cyl(0,0,75,175,32.5,48),(70,120,135)),('h',cyl(0,0,14.7,31,9),(120,120,125)),('v',cyl(0,0,-15.3,14.7,1.6),(50,50,55))]
    def render(parts,view,xl,yl,S=4):
        d=V[view];d=d/np.linalg.norm(d);up=np.array([0,0,1.]);rr=np.cross(up,d);rr/=np.linalg.norm(rr);uu=np.cross(d,rr)
        w,h=int((xl[1]-xl[0])*S),int((yl[1]-yl[0])*S);im=Image.new('RGB',(w,h),(255,255,255));dr=ImageDraw.Draw(im)
        Lg=np.array([.5,.3,.8]);Lg=Lg/np.linalg.norm(Lg);tr=[];cs=[]
        for n,m,col in parts:
            kk=(m.face_normals@d)>0;tr.append(m.triangles[kk]);cs.append(np.outer(.45+.55*np.clip(m.face_normals[kk]@Lg,0,1),col))
        Tt=np.vstack(tr);C=np.vstack(cs);o=np.argsort((Tt@d).mean(1));X=(Tt@rr-xl[0])*S;Y=(yl[1]-Tt@uu)*S
        for i in o:dr.polygon([(X[i,0],Y[i,0]),(X[i,1],Y[i,1]),(X[i,2],Y[i,2])],fill=tuple(C[i].astype(int)))
        return np.asarray(im).astype(float)
    BL=(58,68,80);OR=(232,120,30)
    fig,ax=plt.subplots(2,2,figsize=(15,14))
    for j,(u,t) in enumerate(((0,'INFÄLLD under fräsning'),(1,'NERE när nollan mäts'))):
        mv,_=rorliga(u)
        par=fr+[('fä',F,BL),('se',servo,(30,30,34)),('ar',mv['Arm'],OR),('st',mv['Stag'],(240,240,240)),('ve',mv['Vev'],(240,240,240)),('pr',mv['Prob'],(60,60,66))]
        for i,(vw,xl,yl) in enumerate((('snett',(-70,150),(-70,130)),('sida',(-125,90),(-60,150)))):
            b=render(par+[('ka',K,(232,120,30))],vw,xl,yl,S=6)
            ax[i][j].imshow(b.astype(np.uint8),extent=[*xl,*yl]);ax[i][j].axis('off');ax[i][j].set_title(t+' — '+('snett' if vw=='snett' else 'från sidan'),fontsize=11)
            if vw=='sida':
                for z,cc,lb in ((-15.3,'#a00','fräs 30 mm utstick -15'),(-39.3,'#c0f','probspets -39'),(24,'g','kjol 24')):
                    ax[i][j].axhline(z,c=cc,lw=.8,ls=':');ax[i][j].text(xl[0]+2,z+1,lb,color=cc,fontsize=9)
    fig.suptitle('Fällarm v4: formgiven studie, inget utanför Core längs balken, ej provad. Svart kropp = plats för proben (Ø45).',fontsize=14);fig.tight_layout();fig.savefig(T+'fallarm_bild.png',dpi=120)
