# Research: motors, PSU and Z couplers — 2026-08-29

This is one deliberately small procurement slice. Scope: **5 steppers + 24 V PSU + 2× 5→8 mm Z couplers only**.

## 1. Motors — lock candidate

### Recommended

**StepperOnline `5-17HS19-2004S1`**

Observed 2026-08-29:
- €38.13 / 5-pack
- 59 Ncm / 83.55 oz-in
- 2.0 A
- 1.8°
- 42×42×48 mm
- 5 mm D-shaft
- 24 mm shaft length
- 1 m cable
- Germany warehouse selectable

This remains the preferred LowRider V4 motor candidate. It closely matches the V1E ~84 oz-in class and the savings from the 55 Ncm E-series alternative are too small to justify deviating.

Source: https://www.stepperonline.nl/5st-nema-17-bipolair-59ncm-83-55oz-in-2a-42x48mm-4-draden-met-1m-kabel-aansluiting-5-17hs19-2004s1

### Rejected budget alternative

`5-17HE19-2004S`, 55 Ncm / 77.88 oz-in. Previously observed about €11.5 cheaper for all five. Not enough saving to justify the lower torque / deviation from the known LR4 class.

## 2. PSU — do NOT bundle with StepperOnline just for convenience

The cheap StepperOnline PSU options checked earlier are not naturally part of the Germany motor shipment. Therefore optimize PSU independently.

### Option A — Mean Well `LRS-100-24`

Observed Swedish/EU pricing 2026-08-29:
- DigiKey: 142.60 SEK ex VAT / 178.25 SEK incl VAT, 3814 in stock
- RS Sweden: 162.21 SEK ex VAT / 202.76 SEK incl VAT, in stock; free delivery only above 750 SEK
- Lampornu: 233.75 SEK incl VAT

Specs:
- 24 V
- 4.5 A
- 108 W
- chassis/open-terminal PSU

Pros:
- very cheap for a genuine Mean Well
- large current margin
- common, well documented

Cons:
- mains terminals are exposed and must be enclosed correctly
- may create a separate shipping charge if bought alone

Sources:
- https://www.digikey.se/sv/products/detail/mean-well-usa-inc/LRS-100-24/7705008
- https://se.rs-online.com/web/p/switchade-nataggregat/1065846

### Option B — Mean Well `GST60A24-P1J`

Observed pricing 2026-08-29:
- Mouser listing: ~176.81 SEK shown, but EU consumer-order restriction warning on the page
- DigiKey: ~224.63 SEK incl VAT in current listing, stock situation less attractive than LRS
- Starelec Sweden: 370 SEK incl VAT, immediately available
- Farnell: 269.35 SEK ex VAT, free standard delivery stated on product page, but final consumer checkout still needs confirmation

Specs:
- 24 V
- 2.5 A
- 60 W
- external Class-I desktop brick
- IEC C14 mains inlet
- 5.5×2.1 mm DC plug

Pros:
- no exposed mains terminals at the CNC controller
- clean and garage-friendly installation
- 60 W / 2.5 A is in the right LR4 power class

Cons:
- typically ~50–200 SEK more than LRS-100-24 once realistic consumer channel / shipping is considered
- mains lead may be separate

Sources:
- https://www.digikey.se/en/products/detail/mean-well-usa-inc/GST60A24-P1J/7703715
- https://starelec.se/product/krosskraftk%C3%A4lla-24vdc-2-5a-60w-gst60a24-p1j

### Current PSU decision

**Do not buy yet.**

The technically cheapest good choice is `LRS-100-24`; the cleaner installation choice is `GST60A24-P1J`.

Procurement rule for final checkout:
- choose GST60A24-P1J if its delivered premium over LRS-100-24 is roughly <=100 SEK
- otherwise choose LRS-100-24 and put it in a proper enclosed electrical box

This avoids paying several hundred SEK merely for the desktop form factor.

## 3. Z couplers — 2× 5 mm → 8 mm flexible

Technical target:
- flexible/beam coupling
- 5 mm motor shaft → 8 mm leadscrew
- around 18–20 mm OD / ~25 mm long is normal

StepperOnline `ST-FC04` is exactly correct mechanically:
- 5→8 mm
- 18×25 mm
- aluminum flexible beam coupling
- current global listing around $1.27 each

However, it is not worth creating a separate China shipment for two tiny couplers.

Source: https://www.omc-stepperonline.com/5mm-8mm-flexible-coupling-18x25mm-cnc-stepper-motor-shaft-coupler-st-fc04

### Current coupler decision

**Specification locked; supplier not locked.**

Buy 2× generic 5→8 mm flexible couplers in the same future commodity cart as T8/GT2/bearings if the price premium is modest. A few tens of SEK extra is preferable to another parcel.

## Small-cart conclusion

For this slice:

1. **Motor order is basically ready:** StepperOnline Germany `5-17HS19-2004S1` 5-pack.
2. **PSU remains a two-candidate price/installation decision:** LRS-100-24 vs GST60A24-P1J.
3. **Coupler dimensions are locked, supplier intentionally deferred** so they can be bundled with the mechanical commodity order.

No other parts should be added to the StepperOnline motor order unless they are confirmed to ship from the same EU/Germany warehouse and actually reduce delivered total cost.