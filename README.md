# Force-Controlled Robotic Gripper

<!-- Lead with a visual: CAD screenshot now, demo GIF later -->

A two-finger gripper designed for 3D printing, in which an Arduino senses and controls grip force. Every requirement below has a number and a test method.

**Status (Oct 2026):** spec, sizing analysis, and CAD in progress. Printing, force sensing, and testing planned for winter break.

## Spec

| Requirement | Target | Test method | Result |
|---|---|---|---|
| Payload | Hold a 512 g sealed water bottle (Ø__ mm) for __ s, no slip | | |
| Fragile handling | Raw egg, no cracks | | |
| Force control | Within ±__% of setpoint at __ setpoints | | |
| Jaw opening | __ to __ mm | | |
| Durability | __ open/close cycles | | |

## Mechanism choice
<!-- Sketches and decision matrix -->

## Sizing analysis
<!-- Grip force, safety factor, servo torque and margin -->

## Repo layout
- `cad/`: SOLIDWORKS files plus STEP and STL exports
- `analysis/`: calculations
- `firmware/`: Arduino code
- `docs/`: decision matrix, screenshots, build log
