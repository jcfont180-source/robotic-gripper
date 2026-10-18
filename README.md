# Force-Controlled Robotic Gripper

<!-- Lead with a visual: CAD screenshot now, demo GIF later -->

A two-finger gripper designed for 3D printing, in which an Arduino senses and controls grip force. Every requirement below has a number and a test method.

**Status (Oct 2026):** spec, sizing analysis, and CAD in progress. Printing, force sensing, and testing planned for winter break.

## Spec

| Requirement | Target | Test method | Result |
|---|---|---|---|
| Payload | Hold a 512 g sealed water bottle (Ø 65.3 mm at grip height) for __ s, no slip | | |
| Fragile handling | Raw egg, no cracks | | |
| Force control | Within ±__% of setpoint at __ setpoints | | |
| Jaw opening | 37 to 78 mm | | |
| Durability | __ open/close cycles | | |

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
