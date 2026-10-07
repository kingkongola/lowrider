// Genererar g-kod för FluidNC ur V1E:s strut_plate.svg (LowRider V4, strut_length=819, num_braces=6).
// Körning: NODE_PATH=<mapp med node_modules/clipper-lib> node gen_strut_gcode.js ../../strut_plate.svg
// SVG-x (plattans längd) -> maskin-Y, SVG-y -> maskin-X. Origo (G54 X0 Y0) = nedre vänstra hörnet av plattområdet.
const fs = require('fs');
const ClipperLib = require('clipper-lib');

const svg = fs.readFileSync(process.argv[2], 'utf8');
const OUT = process.argv[3] || '.';

const TOOL_D = 3.175, R = TOOL_D / 2;
const SAFE_Z = 5;
const PASS_Z = [-2.1, -4.2, -6.3];          // 6,00 mm MDF + 0,3 mm in i offerskivan
const TAB_TOP = -4.5;                        // 1,5 mm MDF kvar i tabs
const TAB_W = 4, N_TABS = 6;
const F_CUT = 1500, F_PLUNGE = 300, F_HELIX = 700;
const HELIX_STEP = 1.05;
const HOLE_D = 5.3;

// ---- parsa SVG ----
const d = [...svg.matchAll(/<path d="([\s\S]*?)"/g)].map(m => m[1]).join(' ');
const subs = d.split(/(?=M )/).filter(s => s.trim()).map(s =>
  [...s.matchAll(/(-?[\d.e+-]+),(-?[\d.e+-]+)/g)].map(m => [+m[1], +m[2]]));
const minY = Math.min(...subs.flat().map(p => p[1]));
const minX = Math.min(...subs.flat().map(p => p[0]));
const tf = ([x, y]) => [y - minY, x - minX];          // [maskin-X, maskin-Y]
const polys = subs.map(s => s.map(tf));

const area = p => p.reduce((a, q, i) => { const r = p[(i + 1) % p.length]; return a + (q[0] * r[1] - r[0] * q[1]); }, 0) / 2;
const outers = polys.filter(p => p.length > 100);
const holes = polys.filter(p => p.length <= 100).map(p => {
  const xs = p.map(a => a[0]), ys = p.map(a => a[1]);
  return [(Math.min(...xs) + Math.max(...xs)) / 2, (Math.min(...ys) + Math.max(...ys)) / 2];
});
holes.sort((a, b) => a[1] - b[1] || a[0] - b[0]);

// ---- offset ytterkontur utåt med verktygsradien ----
const S = 1000;
function offsetOuter(p) {
  const path = p.map(([x, y]) => ({ X: Math.round(x * S), Y: Math.round(y * S) }));
  const co = new ClipperLib.ClipperOffset(2, 0.05 * S);
  co.AddPath(path, ClipperLib.JoinType.jtMiter, ClipperLib.EndType.etClosedPolygon);
  const sol = new ClipperLib.Paths();
  co.Execute(sol, R * S);
  if (sol.length !== 1) throw new Error('offset gav ' + sol.length + ' banor');
  let q = sol[0].map(a => [a.X / S, a.Y / S]);
  if (area(q) < 0) q.reverse();                       // CCW runt delen = medfräs (CW-spindel)
  return simplify(q, 0.01);
}
function simplify(p, tol) {                           // ta bort nästan kollinjära punkter
  const out = [p[0]];
  for (let i = 1; i < p.length; i++) {
    const a = out[out.length - 1], b = p[i], c = p[(i + 1) % p.length];
    const dist = Math.abs((c[0] - a[0]) * (a[1] - b[1]) - (a[0] - b[0]) * (c[1] - a[1])) / (Math.hypot(c[0] - a[0], c[1] - a[1]) || 1);
    if (dist > tol || Math.hypot(b[0] - a[0], b[1] - a[1]) > 5) out.push(b);
  }
  return out;
}

// ---- g-kod ----
const f = v => (Math.round(v * 1000) / 1000).toString();
function build(zOff, title) {
  const L = [];
  const z = v => f(v + zOff);
  L.push(`; ${title}`);
  L.push('; LowRider V4 - strutplattor ur 6,00 mm MDF. Genererad av gen_strut_gcode.js ur strut_plate.svg');
  L.push('; Verktyg: 3,175 mm 2-flute upcut. Z0 = MDF-ytan. XY0 = nedre vänstra hörnet av plattområdet (X ca 0..179, Y ca 0..819).');
  L.push(`; Djup ${PASS_Z.map(a => -a).join("/")} mm, ${N_TABS} tabs/platta (${TAB_W} mm breda, 1,5 mm MDF kvar)`);
  if (zOff) L.push(`; LUFTKÖRNING: alla Z förskjutna +${zOff} mm. Fräsen ska INTE vara igång.`);
  L.push('G21 G90 G17 G54 G94');
  L.push(`G0 Z${z(SAFE_Z)}`);
  L.push(zOff ? '(MSG, LUFTKORNING - sakerstall att Z0 ar satt pa MDF-ytan)' : '(MSG, Starta KATSU manuellt, ratt 3, vanta tills full fart, tryck Cycle Start)');
  L.push('M0');
  // hål
  const Rh = HOLE_D / 2 - R;
  L.push('; --- 24 hål Ø5,3 (spiral, CW = medfräs) ---');
  holes.forEach(([cx, cy], i) => {
    L.push(`; hål ${i + 1}`);
    L.push(`G0 X${f(cx + Rh)} Y${f(cy)}`);
    L.push(`G0 Z${z(1)}`);
    L.push(`G1 Z${z(0)} F${F_PLUNGE}`);
    let zc = 0;
    while (zc > PASS_Z[2] + 1e-6) {
      zc = Math.max(zc - HELIX_STEP, PASS_Z[2]);
      L.push(`G2 X${f(cx + Rh)} Y${f(cy)} Z${z(zc)} I${f(-Rh)} J0 F${F_HELIX}`);
    }
    L.push(`G2 X${f(cx + Rh)} Y${f(cy)} I${f(-Rh)} J0 F${F_HELIX}`);
    L.push(`G0 Z${z(SAFE_Z)}`);
  });
  // ytterkonturer
  outers.forEach((o, k) => {
    const p = offsetOuter(o);
    const tabs = pickTabs(p);
    L.push(`; --- ytterkontur ${k === 0 ? 'främre plattan' : 'bottenplattan'}: ${p.length} punkter, tabs vid ${tabs.map(t => f(t.mid)).join(', ')} mm längs banan ---`);
    // starta i hörnpunkt 0, plungea utanför delen
    L.push(`G0 X${f(p[0][0])} Y${f(p[0][1])}`);
    L.push(`G0 Z${z(1)}`);
    PASS_Z.forEach((zp, pi) => {
      const last = pi === PASS_Z.length - 1;
      L.push(`; pass ${pi + 1}: Z${zp}`);
      L.push(`G1 Z${z(zp)} F${F_PLUNGE}`);
      L.push(`G1 F${F_CUT}`);
      emitLoop(L, p, last ? tabs : [], zp, z);
    });
    L.push(`G0 Z${z(SAFE_Z)}`);
  });
  L.push(`G0 Z${z(SAFE_Z)}`);
  L.push('G0 X0 Y0');
  L.push('M2');
  return L.join('\n') + '\n';
}

// tabs: väljer N_TABS långa raka kanter jämnt fördelade, tab i mitten
function segs(p) {
  const out = []; let s = 0;
  for (let i = 0; i < p.length; i++) {
    const a = p[i], b = p[(i + 1) % p.length], len = Math.hypot(b[0] - a[0], b[1] - a[1]);
    out.push({ i, a, b, len, s0: s }); s += len;
  }
  return { out, total: s };
}
function pickTabs(p) {
  const { out } = segs(p);
  const cand = out.filter(g => g.len > 100);
  const tabs = [];
  for (let k = 0; k < N_TABS; k++) {
    const g = cand[Math.floor((k + 0.5) * cand.length / N_TABS)];
    const mid = g.s0 + g.len / 2;
    tabs.push({ s0: mid - TAB_W / 2, s1: mid + TAB_W / 2, mid });
  }
  return tabs;
}
function emitLoop(L, p, tabs, zp, z) {
  const { out } = segs(p);
  const pt = (g, t) => [g.a[0] + (g.b[0] - g.a[0]) * t / g.len, g.a[1] + (g.b[1] - g.a[1]) * t / g.len];
  let up = false;
  const go = (xy, zz) => L.push(`G1 X${f(xy[0])} Y${f(xy[1])}`);
  for (const g of out) {
    const here = tabs.filter(t => t.s1 > g.s0 && t.s0 < g.s0 + g.len);
    let cur = 0;
    for (const t of here) {
      const a = Math.max(t.s0 - g.s0, 0), b = Math.min(t.s1 - g.s0, g.len);
      if (a > cur) go(pt(g, a));                       // fram till tabstart på djup
      if (a >= 0 && !up) { L.push(`G1 Z${z(TAB_TOP)} F${F_PLUNGE}`); L.push(`G1 F${F_CUT}`); up = true; }
      go(pt(g, b));
      L.push(`G1 Z${z(zp)} F${F_PLUNGE}`); L.push(`G1 F${F_CUT}`); up = false;
      cur = b;
    }
    go(g.b);
  }
}

// ---- skriv ut ----
fs.writeFileSync(`${OUT}/strut_plates.nc`, build(0, 'STRUTPLATTOR - SKARP KORNING'));
fs.writeFileSync(`${OUT}/strut_plates_AIR.nc`, build(20, 'STRUTPLATTOR - LUFTKORNING (Z +20 mm)'));

// kontroll
const allp = outers.map(offsetOuter).flat();
const bx = [Math.min(...allp.map(a => a[0])), Math.max(...allp.map(a => a[0]))];
const by = [Math.min(...allp.map(a => a[1])), Math.max(...allp.map(a => a[1]))];
console.log('banans utsträckning X', bx.map(f), 'Y', by.map(f), '| hål', holes.length, '| ytterkonturer', outers.length);
