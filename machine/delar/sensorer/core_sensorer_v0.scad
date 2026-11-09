// ARKIVERAD STUDIE (2026-11-09): ersatt av core_enhet.py i build123d.
// EJ gällande ritning, EJ printa BLTouch-armen eller använda dessa STL för montage.
// Se machine/delar/sensorer/README.md och grön build123d-CI för gällande delar.
// LowRider V4 test-passnings-CAD. Alla mått mm. Ingen kollisionsverifiering.
// Extrahera STL med: openscad -o pi_bas.stl -D 'part="pi_bas"' core_sensorer_v0.scad
// Delar: pi_bas, pi_lock, kamera, bltouch_mattjigg, bltouch_arm.
// OBS! BLTouch-armen är endast preliminär, ingen rörelse eller G38 godkänd!
part = "pi_bas";
$fn=48;

// Zero 2 WH: 65x30 PCB, 58x23 monteringshål.
// Camera Module 3 Standard: ~25x24 PCB, linshöjd ~11.5.
// BLTouch-hålplan och fysisk spetsposition MÅSTE kontrolleras på levererad del.
case_x=80; case_y=46; case_h=22; case_floor=2.5; wall=2;
pi_span_x=58; pi_span_y=23; pi_screw_d=2.8;
lid_x=35.25; lid_y=18.5;
cam_plate=35; cam_t=3;
servo_px=45; servo_py=23.5; servo_pz=43.6;
probe_x=61; probe_y=34;
target_tip_z=-39.3; // Gammal C-probs mål, EJ verifierat för BLTouch.
flange_tip_mm=36.3; // Preliminär passningsparameter, mät levererad probe.
probe_flange_z=target_tip_z+flange_tip_mm;
bl_pitch=18; bl_hole=3.4;

module slot(len,d,h){
  hull(){translate([-len/2+d/2,0,0]) cylinder(d=d,h=h);
         translate([len/2-d/2,0,0]) cylinder(d=d,h=h);}
}
module pi_bas(){
 difference(){
  union(){
   difference(){
    translate([-case_x/2,-case_y/2,0]) cube([case_x,case_y,case_h]);
    translate([-case_x/2+wall,-case_y/2+wall,case_floor])
      cube([case_x-2*wall,case_y-2*wall,case_h]);
   }
   for (xx=[-1,1],yy=[-1,1]){
    translate([xx*lid_x,yy*lid_y,case_floor]) cylinder(d=6.5,h=case_h-case_floor);
    translate([xx*pi_span_x/2,yy*pi_span_y/2,case_floor]) cylinder(d=5.8,h=4.5);
   }
   for(xx=[-22,22])
    translate([xx,case_y/2+3,case_floor/2])
       cube([17,8,case_floor],center=true);
  }
  for(xx=[-1,1],yy=[-1,1]){
   translate([xx*lid_x,yy*lid_y,case_floor]) cylinder(d=2.6,h=case_h+1);
   translate([xx*pi_span_x/2,yy*pi_span_y/2,-1])
      cylinder(d=pi_screw_d,h=case_h+2);
  }
  // Generösa kabelfönster: verklig portorientering kontrolleras vid provpassning.
  translate([-32,-case_y/2-1,6]) cube([64,wall+2,13]);
  translate([-case_x/2-1,-11,6]) cube([wall+2,22,13]);
  translate([case_x/2-wall-1,-13,6]) cube([wall+3,26,13]);
  for(xx=[-22,22]) translate([xx,case_y/2+4,-1]) slot(10,3.4,case_floor+3);
  // Passiva öppningar, ingen fläkt behövs som startkrav.
  for(xx=[-24,-12,0,12,24])
    translate([xx-2.5,case_y/2-wall-1,12]) cube([5,wall+2,5]);
 }
}
module pi_lock(){
 difference(){
  union(){
   translate([-case_x/2,-case_y/2,0]) cube([case_x,case_y,2.5]);
   translate([-case_x/2+wall+.35,-case_y/2+wall+.35,2.5])
    difference(){
     cube([case_x-2*(wall+.35),case_y-2*(wall+.35),1.8]);
     translate([2,2,-1])
      cube([case_x-2*(wall+2.35),case_y-2*(wall+2.35),4]);
    }
  }
  for(xx=[-1,1],yy=[-1,1])
   translate([xx*lid_x,yy*lid_y,-1]) cylinder(d=3.3,h=7);
 }
}
module kamera(){
 // Öppen optisk platta, justerspår i stället för ogrundad exakt hålbild.
 difference(){
  union(){
   translate([-cam_plate/2,-cam_plate/2,0]) cube([cam_plate,cam_plate,cam_t]);
   translate([cam_plate/2,-12,0]) cube([12,24,cam_t]);
   for(xx=[-14.5,14.5],yy=[-14.5,14.5])
      translate([xx,yy,cam_t]) cylinder(d=4,h=1);
  }
  translate([0,0,-1]) cylinder(d=20,h=cam_t+3);
  for(xx=[-11,11],yy=[-8,8])
    translate([xx,yy,-1]) rotate([0,0,90]) slot(8,2.3,cam_t+3);
  for(yy=[-8,8])
    translate([cam_plate/2+6,yy,-1]) cylinder(d=3.4,h=cam_t+3);
 }
}
module bltouch_mattjigg(){
 difference(){
  translate([-16,-14,0]) cube([32,28,4]);
  for(yy=[-bl_pitch/2,bl_pitch/2])
   translate([0,yy,-1]) cylinder(d=bl_hole,h=6);
  translate([0,0,-1]) cylinder(d=10,h=6);
 }
}
module bltouch_arm(){
 // Ersätter gamla Ø33-klämman i koncept C med lodrät BLTouch.
 // Jämför alltid servohorn, kåpa, omgivande Core och båda stopplägena.
 difference(){
  union(){
   translate([servo_px,servo_py,servo_pz]) rotate([90,0,0])
     cylinder(d=18,h=5,center=true);
   hull(){
    translate([servo_px,servo_py,servo_pz]) rotate([90,0,0])
     cylinder(d=16,h=5,center=true);
    translate([probe_x,servo_py,probe_flange_z+3]) rotate([90,0,0])
     cylinder(d=13,h=5,center=true);
   }
   translate([probe_x-13,probe_y-16,probe_flange_z]) cube([26,32,4]);
   hull(){
    translate([probe_x,servo_py,probe_flange_z+3]) sphere(d=6);
    translate([probe_x,probe_y,probe_flange_z+3]) sphere(d=6);
   }
  }
  translate([servo_px,servo_py,servo_pz]) rotate([90,0,0])
    cylinder(d=7.5,h=12,center=true);
  for(zz=[servo_pz-7,servo_pz+7])
    translate([servo_px,servo_py,zz]) rotate([90,0,0])
      cylinder(d=2.4,h=12,center=true);
  for(yy=[probe_y-bl_pitch/2,probe_y+bl_pitch/2])
    translate([probe_x,yy,probe_flange_z-1]) cylinder(d=bl_hole,h=7);
  translate([probe_x,probe_y,probe_flange_z-1]) cylinder(d=10,h=7);
 }
}
if(part=="pi_bas") pi_bas();
else if(part=="pi_lock") pi_lock();
else if(part=="kamera") kamera();
else if(part=="bltouch_mattjigg") bltouch_mattjigg();
else if(part=="bltouch_arm") bltouch_arm();
else assert(false,str("Unknown part: ",part));
