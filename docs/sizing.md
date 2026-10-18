# Sizing analysis

Equations use GitHub math ($...$).

## Inputs
Data: [analysis/data/](../analysis/data/)

Raw data: analysis/data/. Bottle mass 512 g. Egg design mass range 48–73 g; the heavy end (73 g) is used for sizing. Jaw opening: CAD 37–78 mm, stroke 41 mm (docs/spec.md).

## Assumptions
<!-- Friction coefficient and its source, safety factor, mechanism efficiency, servo voltage -->

- Friction coefficient: μ = 0.4 (design value) for a solid neoprene pad, about 1.5 mm thick, on the bottle label and on eggshell. No handbook lists these material pairs. The value is conservative: textbook static friction for rubber on concrete is 0.60–0.90 (Beer & Johnston table, reproduced in https://gcp-web.sjsu.edu/people/steven.vukazich/docs/95.8.1%20Friction%20.pdf), and rubbers generally show higher static friction than plastics (https://eprints.ums.edu.my/id/eprint/40836/1/ABSTRACT.pdf). Verified by tilt test once the pad material is in hand: bottle on a pad-covered board with its axis pointing downhill so it slides instead of rolling, egg lying lengthwise; μ = tan(angle at which sliding starts). If the measured μ is below 0.4, redo the sizing with the measured value.
- Safety factor on grip force: SF = 2.0, built from named sources that multiply:

  | Source | What it covers | Factor |
  |---|---|---|
  | Force-control error | Spec allows actual force 15% below the setpoint | 1/0.85 = 1.18 |
  | μ uncertainty | Contamination or a slicker spot; μ dropping 20% (0.4 to 0.32) | 1.25 |
  | Load jolts | Jolt when the support is removed, or a brisk hand lift (about 0.2 g extra) | 1.2 |
  | FSR calibration | Sensor reading up to 10% high | 1.11 |
  | Combined | 1.18 × 1.25 × 1.2 × 1.11 ≈ 1.96 | rounded to 2.0 |

  The tilt test and FSR calibration will replace the μ and calibration allowances with measured values. For the egg, the setpoint must also stay well below the shell's cracking force.
- Mechanism efficiency: η = 0.5 (design value). Covers friction in the printed gear mesh and rails, including rail friction from the bottle's weight hanging off the fingertips. To be measured after the build.
- Servo torque: use the datasheet stall torque at 4.8 V, even though the servo will run at 5–6 V, so the calculated torque errs on the safe side.
- Separation of margins: SF covers grip-force uncertainty, η covers drive losses, and the 25% torque margin covers servo uncertainty. None of them covers the same thing twice.

## Grip force

__

## Kinematics: jaw gap vs. servo angle

__

## Servo torque (worst case)

__

## Servo comparison
<!-- Stall torque at my voltage, converted to N·mm -->

__

## Margin
<!-- State what it is measured against -->

__

## Result

__
