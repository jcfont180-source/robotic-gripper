# Robotic gripper

## Project rules
- Project: two-finger gripper designed for 3D printing. An Arduino Mega 2560
  will sense grip force with an FSR and control it with a servo. Mechanism:
  decided in docs/ (decision matrix coming).
- Roles: I own the spec, the calculations, and every design decision. You
  write code to my spec. Never invent or change a spec number; if one is
  missing, ask me.
- Source of truth for requirements: the Spec table in README.md.
- Units: N, mm, N·mm for torque, g for mass.
- Wiring: servo signal on pin 9; servo power from the bench supply, never the
  Arduino 5V pin; supply negative tied to Arduino GND.
