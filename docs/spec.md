# Spec

## Payload
- **Target:** Hold a 512 g sealed water bottle (Ø 65.3 mm at grip height) for 30 s without slipping
- **Test setup:** Bottle sealed, full, dry, room temperature. Gripped on the label at 120 mm from the base (label checked: does not twist). Gripper approaches from the side. Gripper clamped to the table edge. Bottle rests on a stack of books between the jaws; the jaws close, the books are slid out, and the timer starts.
- **Instrument:** Tape measure (1 mm marks); marker line on the bottle level with the top edge of one jaw
- **Trials:** 10
- **Pass criterion:** Marker line moves less than 2 mm after 30 s, in all 10 trials
- **Reason:** Ø 65.3 mm = measured circumference 205 mm / π. 30 s is well beyond a normal pick-and-place hold and long enough for slow slip to appear. 10 trials catch a gripper that only works most of the time. The 2 mm threshold is twice the tape's 1 mm resolution.

## Fragile handling
- **Target:** Hold a raw egg within the design range for 10 s without cracking or dropping it
- **Test setup:** Test object: USDA Grade A Large raw egg. Design range: width 41–48 mm, mass 48–73 g, from a sample of 5 eggs (analysis/data/egg_sample.csv). Each test egg is weighed, measured, and logged before its trial; eggs outside the design range are noted in the results. Same rig as Payload. The egg stands upright in an egg cup on the book stack; the jaws close at the egg force setpoint, the stack is slid out, the egg is held 10 s, the stack is slid back, and the jaws open. Towel underneath.
- **Instrument:** Phone flashlight shone through the shell (crack check); tape measure (1 mm marks) and marker line (movement)
- **Trials:** 10, all on the same egg; if it cracks, log the trial number
- **Pass criterion:** No crack visible under the flashlight after each trial, and the marker line moves less than 2 mm
- **Reason:** Design ranges are the sample mean ± 3 standard deviations, rounded outward (width: mean 44.8 mm, s ≈ 1.0 mm; mass: mean 60.4 g, s ≈ 4.1 g). The sample is small, so every test egg is measured and logged. Cracks happen at peak force during closing, so a 10 s hold is enough to show a stable grip. Using one egg for all 10 trials is the harder test, since damage accumulates.

## Force control
- **Target:** Within ±__% of setpoint at __ setpoints
- **Test setup:** __
- **Instrument:** __
- **Trials:** __
- **Pass criterion:** __
- **Reason:** __

## Jaw opening
- **Target:** 37 to 78 mm (stroke 41 mm)
- **Test setup:** __
- **Instrument:** __
- **Trials:** __
- **Pass criterion:** __
- **Reason:** Min = smallest design egg (41 mm) − 2 mm build tolerance (allowed difference between the printed jaw opening and the CAD model, checked on the first print) − 2 mm for pad compression and squeeze travel. Max = bottle width (65.3 mm) + 5 mm approach clearance per side + 2 mm build tolerance, rounded up.

## Durability
- **Target:** __ open/close cycles
- **Test setup:** __
- **Instrument:** __
- **Trials:** __
- **Pass criterion:** __
- **Reason:** __
