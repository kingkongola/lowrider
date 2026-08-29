---
researched_at: 2026-08-29
last_updated_at: 2026-08-29
scope: machine mains power, emergency stop / NVR, controller PSU interaction
status: researched-not-ordered
confidence: high-on-architecture-medium-on-final-supplier
machine_target: LowRider V4, ~650x1250 mm usable area
constraints:
  - dust-prone garage
  - VEVOR 0700C router ~800 W
  - Jackpot3 controller at 24 VDC
  - prefer low complexity and low delivered cost
  - machine stop should stop both router and motion
sources_checked:
  - V1 Engineering Jackpot3 docs
  - V1 Engineering 24 V PSU page
  - E-Switch KJD17 datasheet
  - Farnell Sweden
  - DigiKey Sweden
  - ABB emergency-stop catalog / Swedish distributors
  - Kew Online KJD17-D2 reference
observed_prices_are_time_sensitive: true
---

# Research: machine power + stop architecture

This slice covers the 230 V machine-power architecture and stop behavior. It does **not** yet lock a full enclosure/BOM.

## Electrical facts from V1E

Jackpot3 accepts **9–24 VDC** and needs at least about **19 W**. V1E normally uses **24 V / 2.5 A / 60 W or larger** for LowRider.

Sources:
- https://docs.v1e.com/electronics/jackpot3/
- https://www.v1e.com/products/24v-power-supply

## Design goal

A useful machine stop should remove energy from both:
1. the 24 V motion controller / steppers, and
2. the 230 V router.

Stopping only Jackpot3 while the router remains powered is not the preferred architecture.

## KJD17 family — exact variant distinction matters

E-Switch KJD17 part-number coding shows:
- function `1` = normal Off-On NVR
- function `2` = Off-On **with remote trip**
- 230 V / 50 Hz is the correct voltage-frequency code for Sweden

Therefore:
- `KJD17-21413-112` = guarded normal NVR Off-On
- `KJD17-22413-112` = guarded NVR Off-On **with remote trip**

Both are 230 VAC, 16 A, DPST, IP54-class industrial switches with no-volt-release behavior.

Current Swedish price references:
- Farnell `KJD17-22413-112`: **134.04 SEK ex VAT** (~167.55 incl VAT)
- DigiKey Sweden `KJD17-22413-112`: **169.45 SEK incl VAT**

Sources:
- E-Switch KJD17 datasheet: https://www.diverseelectronics.com/upload/documents/KJD17.pdf
- Farnell: https://se.farnell.com/e-switch/kjd17-22413-112/pb-switch-dpst-16a-230v-panel/dp/4051018
- DigiKey: https://www.digikey.se/en/products/detail/e-switch/KJD17-22413-112/16019184

## Important safety correction: remote trip is NOT automatically a true E-stop

The `KJD17-22413-112` remote-trip/A1 input is useful for guard/interlock circuits. It can drop the NVR coil.

However, do **not** assume that placing a mushroom only in the A1/remote-trip loop is equivalent to a true upstream emergency disconnect. Community wiring discussions point out a failure mode: depending on wiring, holding START can energize the load even when the remote-trip loop is open. A welded/failed KJD17 contact is another reason not to treat the A1 loop as the sole emergency power isolation.

So:
- remote trip = useful interlock capability
- remote trip alone = **not our final machine E-stop strategy**

Reference discussion:
- https://www.model-engineer.co.uk/forums/topic/e-stop-wiring/

## Load margin

Approximate nominal running load:
- VEVOR 0700C router ~800 W => ~3.5 A at 230 V
- 24 V / 60–100 W controller PSU => <0.5 A mains-side nominal

Total nominal load is comfortably below a 16 A KJD17 main-switch rating.

## Architecture A — KJD17 NVR as machine ON/OFF, plus proper upstream E-stop

This is the technically clean modular architecture:

`wall -> emergency disconnect -> KJD17 NVR -> switched router + controller PSU`

Benefits:
- emergency device removes power before the NVR and load
- NVR prevents automatic restart after power restoration
- router and controller are both de-energized
- KJD17 can still use its remote-trip input later for guard/interlock logic

Downside: a genuinely rated E-stop that can safely interrupt the full mains load adds cost.

## ABB certified mushroom candidate

ABB `CE3T-10R-02`, part `1SFA619500R1051`:
- 30 mm red mushroom
- twist release
- **2 NC**
- complete compact device
- IP66/IP67/IP69K front rating
- conforms to EN/IEC 60947-5-5 / EN ISO 13850 family requirements in ABB catalog

Swedish observed pricing:
- CS MegaStore: **283 SEK incl VAT + 49 SEK shipping = ~332 SEK delivered**
- RS Sweden: **333.42 SEK incl VAT**, free shipping threshold 500 SEK
- price aggregators have shown from ~233 SEK

Important: this device is ideal as a safety control contact device, but final current-utilization rating must be respected. Do not blindly run router load through a safety contact merely because the catalog says 24–300 V. If used with KJD17, safest industrial pattern is to use the E-stop to de-energize a properly rated switching element rather than rely on an underspecified pilot-device contact for router current.

Sources:
- ABB catalog: https://library.e.abb.com/public/12123c6f16c142d198fe63610e88bf5e/1SFC151007C0201_RevE3_Pilot%20devices%20catalog%20-%202025-04-03.pdf
- CS MegaStore: https://www.csmegastore.se/i/1502612/przycisk-bezpiecze%C5%84stwa-grzybkowy-30mm-2r-0-1z-2r-24-300-v-czerwony-ce3t-10r-02-1sfa619500r1051
- RS: https://se.rs-online.com/web/p/emergency-stop-push-buttons/2255897

## Architecture B — complete KJD17-D2 NVR + mushroom station

This remains the most attractive **single-box** concept found.

Known `KJD17-D2` complete station reference:
- 220–240 V
- 16 A NVR start/stop
- separate emergency-stop mushroom
- 2 NC emergency contacts stated as 12 A / 250 V
- complete ~80×115×90 mm enclosure
- reference price **£15.90** before Sweden shipping/import handling

If an EU seller with credible component provenance and sensible delivered price is found, this could beat a DIY KJD17 + separate certified mushroom + contactor arrangement on both cost and simplicity.

Source:
- https://www.kewonline.net/store/product/a-nvr-no-volt-release-stopstart-emergency-stop-switch-kjd17-d2

## Architecture C — KJD17 only, no mushroom

A guarded KJD17 gives:
- green START
- red STOP
- NVR/no-restart protection
- 16 A DPST main switching

For initial bench testing this is materially safer than a normal toggle switch, but it is **not the same physical human-factor safety as a large latching mushroom**.

Do not call this a finished E-stop solution.

## PSU implication

This research strengthens the preference for an external Mean Well brick if the price premium stays modest.

### External brick path

Using `GST60A24-P1J`:

`switched 230 V -> router plug + 24 V brick plug -> Jackpot3`

Pros:
- no open 230 V PSU terminals inside CNC electronics
- simpler mains enclosure
- easier separation of mains and low-voltage wiring
- simpler service/replacement

### Open PSU path

`LRS-100-24` remains cheap and electrically excellent, but requires a proper mains enclosure around its exposed terminals.

**Current rule:** prefer `GST60A24-P1J` if its delivered total is within roughly **100–150 SEK** of the complete safely-enclosed `LRS-100-24` solution.

## Current decision state

Locked principles:
- machine ON/OFF should use NVR/no-volt-release behavior
- router and controller should share the same machine-level power shutdown path
- do not use a cheap marketplace mushroom as the only safety component
- do not treat KJD17 remote-trip/A1 as a standalone true E-stop

Leading product for machine ON/OFF:
- **E-Switch `KJD17-22413-112`** because remote trip costs little and gives useful future interlock capability

Still open:
- cheapest credible way to add a proper large emergency mushroom that really removes machine power
- whether a complete KJD17-D2-like station can be sourced economically inside the EU
- exact enclosure/outlet arrangement

## Next research action

Small next slice:
1. search EU/Sweden for complete **NVR + mushroom + enclosure** stations rated >=10 A / 230 V
2. compare delivered price against DIY `KJD17-22413-112 + certified mushroom + switching element`
3. only then lock machine-power hardware
