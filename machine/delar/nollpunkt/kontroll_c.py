"""Krock och bild för version C."""
import numpy as np, trimesh, warnings, math
warnings.filterwarnings('ignore')
from scipy.spatial import cKDTree
from PIL import Image, ImageDraw
import matplotlib;matplotlib.use('Agg');import matplotlib.pyplot as plt
A='/Users/bemca/dev/lowrider/machine/delar/nollpunkt/';D='/Users/bemca/dev/lowrider/machine/delar/';T='/tmp/nollpunkt-prov0/'
XC,YC=61.,34.;PX,PZ=45.,43.6;SP=-39.3;ST,KH,KD,SL=26.,21.,33.,20.;K_UT,K_L,K_D=7.,25.,9.
c=trimesh.load(T+'cad/Core.stl');v=c.vertices;core=trimesh.Trimesh(np.c_[v[:,0]-193.7,v[:,2]-92.5,-(v[:,1]-169.17)+94.75],c.faces,process=False)
def cyl(x,y,z0,z1,rr,sec=40):
    m=trimesh.creation.cylinder(radius=rr,height=z1-z0,sections=sec);m.apply_translation([x,y,(z0+z1)/2]);return m
M={'Core':core,'T':trimesh.load(D+'tool-mount-t-v1-makita.stl'),'B':trimesh.load(D+'tool-mount-b_makita.stl'),'Sko':trimesh.load(D+'dust_shoe_makita.stl'),'Kjol':trimesh.load(D+'dust_skirt_makita.stl')}
TR={k:cKDTree(trimesh.sample.sample_surface(m,150000,seed=1)[0]) for k,m in M.items()}
TR['Skanning']=cKDTree(np.load(T+'scan_M.npy'))
F=trimesh.load(A+'fallarm_C_faste.stl');K=trimesh.load(A+'fallarm_C_kapa.stl');Ar=trimesh.load(A+'fallarm_C_arm.stl');servo=trimesh.load(A+'fallarm_C_servo_bild.stl')
fast={'Fäste':F,'Kåpa':K,'Servo':servo}
for k,m in fast.items():TR[k]=cKDTree(trimesh.sample.sample_surface(m,60000,seed=2)[0])
kontakt=trimesh.creation.cylinder(radius=K_D/2,height=K_L+KD/2,sections=24);kontakt.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2,[1,0,0]));kontakt.apply_translation([XC,YC-(K_L+KD/2)/2,SP+ST+KH-K_UT])
prob=trimesh.util.concatenate([cyl(XC,YC,SP+ST,SP+ST+KH,KD/2),cyl(XC,YC,SP+ST+KH,SP+ST+KH+SL,3),cyl(XC,YC,SP+2,SP+ST,1.2),trimesh.creation.icosphere(radius=2,subdivisions=2).apply_translation([XC,YC,SP+2]),kontakt])
def ry(deg):return trimesh.transformations.rotation_matrix(np.radians(deg),[0,1,0],[PX,0,PZ])
res={}
for u in np.linspace(0,1,13):
    Tm=ry(-90*(1-u))
    for n,m in (('Arm',Ar),('Prob',prob)):
        P=trimesh.transformations.transform_points(trimesh.sample.sample_surface(m,6000,seed=3)[0],Tm)
        for k,t in TR.items():
            res[(n,k)]=min(res.get((n,k),99),float(t.query(P)[0].min()))
print('minsta avstånd under hela svängen (mm); Arm mot Servo ligger an via servoarmen')
for n in('Prob','Arm'):print(n,' '.join(f"{k} {res[(n,k)]:.1f}" for k in TR))
for k,m in fast.items():
    P=trimesh.sample.sample_surface(m,8000,seed=4)[0];print(k,' '.join(f"{q} {TR[q].query(P)[0].min():.1f}" for q in('Core','T','B','Sko','Kjol','Skanning')))
allt=trimesh.util.concatenate([F,K,servo,Ar.copy().apply_transform(ry(-90)),prob.copy().apply_transform(ry(-90))]);print('y max infälld',allt.bounds[1,1].round(1),'y min',allt.bounds[0,1].round(1),'x max',allt.bounds[1,0].round(1),'z min',allt.bounds[0,2].round(1))
# knappen: fri sträcka längs raka vägen
B=np.array([19.2,15.3,40.]);d=np.array([.78,.62,0]);S=trimesh.sample.sample_surface(allt,200000,seed=5)[0];tt=cKDTree(S)
for t in range(5,80,5):
    print('knappväg',t,'mm: fritt',round(float(tt.query(B+d*t)[0]),1),end=' ; ')
print()
V={'snett':np.array([.85,.5,.3]),'sida':np.array([0,1,.0])}
fr=[('c',core,(150,158,168)),('t',M['T'],(214,190,110)),('b',M['B'],(214,190,110)),('s',M['Sko'],(226,214,170)),('f',cyl(0,0,75,175,32.5,48),(70,120,135)),('h',cyl(0,0,14.7,31,9),(120,120,125)),('v',cyl(0,0,-15.3,14.7,1.6),(50,50,55))]
def render(parts,view,xl,yl,S=5):
    d=V[view];d=d/np.linalg.norm(d);up=np.array([0,0,1.]);rr=np.cross(up,d);rr/=np.linalg.norm(rr);uu=np.cross(d,rr)
    w,h=int((xl[1]-xl[0])*S),int((yl[1]-yl[0])*S);im=Image.new('RGB',(w,h),(255,255,255));dr=ImageDraw.Draw(im)
    Lg=np.array([.5,.3,.8]);Lg=Lg/np.linalg.norm(Lg);tr=[];cs=[]
    for n,m,col in parts:
        kk=(m.face_normals@d)>0;tr.append(m.triangles[kk]);cs.append(np.outer(.45+.55*np.clip(m.face_normals[kk]@Lg,0,1),col))
    Tt=np.vstack(tr);C=np.vstack(cs);o=np.argsort((Tt@d).mean(1));X=(Tt@rr-xl[0])*S;Y=(yl[1]-Tt@uu)*S
    for i in o:dr.polygon([(X[i,0],Y[i,0]),(X[i,1],Y[i,1]),(X[i,2],Y[i,2])],fill=tuple(C[i].astype(int)))
    return np.asarray(im)
fig,ax=plt.subplots(2,2,figsize=(15,14));BL=(58,68,80);OR=(232,120,30)
for j,(u,t) in enumerate(((0,'INFÄLLD under fräsning'),(1,'NERE när nollan mäts'))):
    Tm=ry(-90*(1-u));par=fr+[('fä',F,BL),('se',servo,(30,30,34)),('ar',Ar.copy().apply_transform(Tm),OR),('pr',prob.copy().apply_transform(Tm),(60,60,66)),('ka',K,OR)]
    for i,(vw,xl,yl) in enumerate((('snett',(-85,150),(-70,140)),('sida',(-145,85),(-60,150)))):
        ax[i][j].imshow(render(par,vw,xl,yl),extent=[*xl,*yl]);ax[i][j].axis('off');ax[i][j].set_title(t+' — '+('snett' if vw=='snett' else 'från sidan'),fontsize=11)
fig.suptitle('Version C: armen direkt på servots axel. Studie, ej provad. Prob V5 Ø33 med kontakt mot -y.',fontsize=14);fig.tight_layout();fig.savefig(T+'fallarm_C.png',dpi=120)
