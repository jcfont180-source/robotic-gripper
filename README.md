# Force-Controlled Robotic Gripper

<!-- Lead with a visual: CAD screenshot now, demo GIF later -->

A two-finger gripper designed for 3D printing, in which an Arduino senses and controls grip force. Every requirement below has a number and a test method.

**Status (Oct 2026):** spec, sizing analysis, and CAD in progress. Printing, force sensing, and testing planned for winter break.

## Spec

| Requirement | Target | Test method | Result |
|---|---|---|---|
| Payload | Hold a 512 g sealed water bottle (Ø 65.3 mm at grip height) for 30 s without slipping | Clamped gripper, books slid out; marker-line slip < 2 mm; 10 trials | |
| Fragile handling | Hold a raw egg within the design range for 10 s without cracking or dropping it | Same rig, one egg upright in a cup; flashlight crack check and slip < 2 mm; 10 trials | |
| Force control | Steady-state force within ±15% of the setpoint at 3 setpoints (egg, bottle, and one midway; values set in docs/sizing.md), with peak force during closing no more than 20% above the setpoint | FSR logged at 50 Hz; last-5 s mean within ±15%, peak ≤ 1.2 × setpoint; 5 trials × 3 setpoints | |
| Jaw opening | 37–78 mm in CAD; printed: ≤ 39 mm closed, ≥ 76 mm open | Tape measure between pad faces at full open and full closed; 3 readings each | |
| Durability | 1000 full open/close cycles without failure | Unloaded Arduino cycle test; no damage, openings within 2 mm of pre-test values | |

## Mechanism choice
<!-- Sketches and decision matrix -->

## Sizing analysis
<!-- Grip force, safety factor, servo torque and margin -->

## Repo layout
- `cad/`: SOLIDWORKS files plus STEP and STL exports
- `analysis/`: calculations
  - `analysis/data/`: raw measurements (CSV)
- `firmware/`: Arduino code
- `docs/`: decision matrix, screenshots, build log
  - `docs/spec.md`: full requirements (target, test setup, instrument, trials, pass criterion, reason)
  - `docs/decision-matrix.md`: mechanism decision matrix
  - `docs/sizing.md`: sizing analysis
  - `docs/images/`: CAD screenshots
