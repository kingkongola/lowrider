import math
S = 6  # px per mm
W, H = 1500, 1000
o = []
def L(x1,y1,x2,y2,c="#222",w=2,d=""):
    o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}"/>')
def R(x,y,w,h,f="none",c="#222",sw=2): o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{f}" stroke="{c}" stroke-width="{sw}"/>')
def C(x,y,r,f="none",c="#222",sw=2): o.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{f}" stroke="{c}" stroke-width="{sw}"/>')
def T(x,y,t,s=20,a="start",c="#222",b=False):
    fw = 'font-weight="bold"' if b else ''
    o.append(f'<text x="{x}" y="{y}" font-size="{s}" text-anchor="{a}" fill="{c}" font-family="Helvetica" {fw}>{t}</text>')
def mat(x1,y1,x2,y2,t,off=0,vert=False):
    if vert:
        L(x1,y1,x1,y2,"#c0392b",1.5); L(x1-6,y1,x1+6,y1,"#c0392b",1.5); L(x1-6,y2,x1+6,y2,"#c0392b",1.5)
        T(x1-10,(y1+y2)/2+7,t,18,"end","#c0392b")
    else:
        L(x1,y1,x2,y1,"#c0392b",1.5); L(x1,y1-6,x1,y1+6,"#c0392b",1.5); L(x2,y1-6,x2,y1+6,"#c0392b",1.5)
        T((x1+x2)/2,y1-8,t,18,"middle","#c0392b")

o.append(f'<rect width="{W}" height="{H}" fill="#fbf8f2"/>')
T(40,50,"3D-taster (kinematisk) – genomskärning och ovanifrån, skala 6:1",28,b=True)

# ---- genomskärning, mittlinje x=380
cx = 560; top = 140  # överkant skaft
shank = 30; cap = 6; body = 34; floor = 5
y_cap = top + shank*S; y_body = y_cap + cap*S; y_floor_top = y_body + (body-floor)*S; y_bot = y_body + body*S
R(cx-3*S, top, 6*S, shank*S, "#c9ccd1")                       # skaft
T(cx+3*S+12, top+60, "skaft Ø6 stål → i chucken", 18)
R(cx-18*S, y_cap, 36*S, cap*S, "#f3d9a4")                      # lock
R(cx-18*S, y_body, 3*S, body*S, "#f3d9a4"); R(cx+15*S, y_body, 3*S, body*S, "#f3d9a4")   # väggar
R(cx-18*S, y_floor_top, 15*S-5*S+0, floor*S, "#f3d9a4")         # golv vänster
R(cx+5*S, y_floor_top, 13*S, floor*S, "#f3d9a4")                # golv höger
T(cx-18*S-130, y_body+130, "utskrivet hus", 18, "end")
# kulor på golvet (r=11), stift vilar på dem
ball_r = 2.5; bx = cx + 11*S; by = y_floor_top - ball_r*S
C(bx, by, ball_r*S, "#9aa3ad"); C(cx-11*S, by, ball_r*S, "#9aa3ad")
pin_y = by - ball_r*S - 1.5*S + 4
hub_top = pin_y - 3*S
R(cx-7*S, hub_top, 14*S, 6*S, "#bfe3c0")                       # nav (plast)
R(cx+7*S, pin_y-1.5*S, 7.5*S, 3*S, "#7f8c8d")                  # stift höger
R(cx-14.5*S, pin_y-1.5*S, 7.5*S, 3*S, "#7f8c8d")               # stift vänster (i snittet)
# fjäder
sy0, sy1 = y_body, hub_top
n=8
pts=" ".join(f"{cx+(-4 if i%2 else 4)*S},{sy0+(sy1-sy0)*i/n}" for i in range(n+1))
o.append(f'<polyline points="{pts}" fill="none" stroke="#2c3e50" stroke-width="3"/>')
T(cx-30*S, sy0+40, "fjäder (t.ex. ur kulspetspenna)", 18, "end")
# mätspets
R(cx-1.5*S, hub_top+6*S, 3*S, (y_bot-hub_top-6*S)+20*S, "#7f8c8d")
tip_y = y_bot + 20*S + 2*S
C(cx, tip_y, 2*S, "#c0392b")
T(cx+40, tip_y-20, "mätspets Ø3 med kula Ø4", 18)
# etiketter
L(bx+ball_r*S, by, cx+260, by+40, "#555", 1); T(cx+265, by+46, "6 stålkulor Ø5 (2 per stift)", 18)
L(cx+14*S, pin_y, cx+260, pin_y-50, "#555", 1); T(cx+265, pin_y-44, "3 stålstift Ø3 (120° isär)", 18)
L(cx-7*S, hub_top+3*S, cx-30*S, hub_top+80, "#555", 1); T(cx-30*S-5, hub_top+86, "nav i plast (isolerar!)", 18, "end")
L(cx+18*S, y_body+40, cx+260, y_body+10, "#555", 1); T(cx+265, y_body+16, "2 sladdar ut → probe-ingång", 18)
# mått
mat(cx-18*S, y_cap-20, cx+18*S, 0, "Ø36 mm")
mat(cx-18*S-40, y_cap, 0, y_bot, "40 mm", vert=True)
mat(cx-18*S-40, y_bot, 0, tip_y+2*S, "~22 mm", vert=True)

# ---- ovanifrån
ux, uy = 1230, 330
C(ux, uy, 18*S, "#f3d9a4"); C(ux, uy, 15*S, "#fbf8f2")
C(ux, uy, 7*S, "#bfe3c0")
for k in range(3):
    a = math.radians(90 + 120*k)
    ex, ey = ux + 14.5*S*math.cos(a), uy - 14.5*S*math.sin(a)
    L(ux + 7*S*math.cos(a), uy - 7*S*math.sin(a), ex, ey, "#7f8c8d", 3*S)
    for s in (-1, 1):
        px = ux + 11*S*math.cos(a) + s*2.6*S*math.sin(a)
        py = uy - 11*S*math.sin(a) + s*2.6*S*math.cos(a)
        C(px, py, ball_r*S, "#9aa3ad")
C(ux, uy, 1.5*S, "#c0392b")
T(ux, uy+18*S+40, "ovanifrån: varje stift ligger i en ”ränna” mellan 2 kulor", 18, "middle")
T(ux, uy+18*S+64, "→ delen hamnar på exakt samma ställe varje gång", 18, "middle")

# ---- elschema
ey = 880
T(60, ey, "Kretsen (i serie, sluten i vila = NC):", 20, b=True)
xs = [80, 180, 300, 420, 520, 640, 740]
labels = ["in", "kula", "stift 1", "kula", "kula", "stift 2", "…"]
for i in range(len(xs)-1):
    L(xs[i]+20, ey+50, xs[i+1]-20, ey+50, "#222", 2)
for x, t in zip(xs, labels):
    T(x, ey+56, t, 16, "middle")
T(800, ey+20, "Rör spetsen något → ett stift lyfts från en kula → kretsen bryts → maskinen stannar.", 18)
T(800, ey+50, "Navet MÅSTE vara i plast: i metall kortsluts stiften och en lyft märks inte.", 18, c="#c0392b")
T(800, ey+80, "Starta ALDRIG KATSU med tastern i chucken (sladden).", 18, c="#c0392b")
open(__import__("pathlib").Path(__file__).with_name("taster.svg"),"w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'+"".join(o)+"</svg>")
