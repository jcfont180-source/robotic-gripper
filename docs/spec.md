# Spec

## Payload
- **Target:** Hold a 512 g sealed water bottle (Ø 65.3 mm at grip height) for 30 s without slipping
- **Test setup:** Bottle sealed, full, dry, room temperature. Gripped on the label at 120 mm from the base (label checked: does not twist). The jaws close horizontally on the side of the bottle. Gripper clamped to the table edge. Bottle rests on a stack of books between the jaws; the jaws close, the books are slid out, and the timer starts.
- **Instrument:** Tape measure (1 mm marks); marker line on the bottle level with the top edge of one jaw
- **Trials:** 10
- **Pass criterion:** Marker line moves less than 2 mm after 30 s, in all 10 trials
- **Reason:** Ø 65.3 mm = measured circumference 205 mm / π. 30 s is well beyond a normal pick-and-place hold and long enough for slow slip to appear. 10 trials catch a gripper that only works most of the time. The 2 mm threshold is twice the tape's 1 mm resolution.

## Fragile handling
- **Target:** Hold a raw egg within the design range for 10 s without cracking or dropping it
- **Test setup:** Test object: USDA Grade A Large raw egg. Design range: width 41–48 mm, mass 48–73 g, from a sample of 5 eggs (analysis/data/egg_sample.csv). The test egg is weighed, measured, and logged before testing; an egg outside the design range is noted in the results. Same rig as Payload. The egg stands upright in an egg cup on the book stack; the jaws close at the egg force setpoint, the stack is slid out, the egg is held 10 s, the stack is slid back, and the jaws open. Towel underneath.
- **Instrument:** Phone flashlight shone through the shell (crack check); tape measure (1 mm marks) and marker line (movement)
- **Trials:** 10, all on the same egg; if it cracks, log the trial number
- **Pass criterion:** No crack visible under the flashlight after each trial, and the marker line moves less than 2 mm
- **Reason:** Design ranges are the sample mean ± 3 standard deviations, rounded outward (width: mean 44.8 mm, s ≈ 1.0 mm; mass: mean 60.4 g, s ≈ 4.1 g). The sample is small, so every test egg is measured and logged. Cracks happen at peak force during closing, so a 10 s hold is enough to show a stable grip. Using one egg for all 10 trials is the harder test, since damage accumulates.

## Force control
- **Target:** Steady-state force within ±15% of the setpoint at 3 setpoints (egg, bottle, and one midway; values set in docs/sizing.md), with peak force during closing no more than 20% above the setpoint
- **Test setup:** Same rig as Payload and Fragile handling. The egg setpoint is tested on the egg; the bottle and midway setpoints on the bottle. Each trial: close to the setpoint, hold 10 s, open. Force is logged to Python at 50 Hz.
- **Instrument:** FSR in one finger pad, calibrated against known weights (calibration error reported separately); Arduino logging to Python
- **Trials:** 5 per setpoint (15 total)
- **Pass criterion:** In every trial, the mean force over the last 5 s is within ±15% of the setpoint, and the peak force is at most 1.2 × the setpoint
- **Reason:** ±15% leaves room for FSR hysteresis and drift and for the servo's step size; revisit once the FSR is chosen. The peak limit protects the egg, which reacts to peak force, not the average. 50 Hz logging catches the peak during closing. Tracking error is measured with the calibrated FSR, so the calibration error is reported alongside it.

## Jaw opening
- **Target:** 37 to 78 mm (stroke 41 mm)
- **Test setup:** Gripper clamped, no load. Command full closed and measure the gap between the jaw pad faces; command full open and measure again.
- **Instrument:** Tape measure (1 mm marks)
- **Trials:** 3 readings at each end, averaged
- **Pass criterion:** Mean full-closed opening ≤ 37 mm and mean full-open opening ≥ 78 mm
- **Reason:** Min = smallest design egg (41 mm) − 2 mm build tolerance (allowed difference between the printed jaw opening and the CAD model, checked on the first print) − 2 mm for pad compression and squeeze travel. Max = bottle width (65.3 mm) + 5 mm approach clearance per side + 2 mm build tolerance, rounded up.

## Durability
- **Target:** 1000 full open/close cycles without failure
- **Test setup:** Gripper clamped, no load. The Arduino cycles the jaws between full open and full closed and counts cycles. Servo on the bench supply with its current limit set.
- **Instrument:** Arduino cycle counter; tape measure (1 mm marks) for jaw opening before and after; visual inspection
- **Trials:** 1 run
- **Pass criterion:** All 1000 cycles complete with no cracked parts, no slipping or skipping in the drive, and no binding; full-open and full-closed jaw openings within 2 mm of their pre-test values
- **Reason:** Testing, development, and demos use a few hundred cycles, so 1000 gives roughly 2–3× margin and runs in about half an hour.
