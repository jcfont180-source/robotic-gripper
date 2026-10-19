# CAD

- Pinion: module 1.25 mm, 18 teeth, 20° pressure angle, 8 mm face width (docs/sizing.md).
- Finger-rack: one part printed twice; the second copy is the same part rotated 180° about the pinion axis. The neoprene pad is a separate body and is not printed.
- Base plate: 100 × 54 × 6 mm, two dovetail grooves with 0.2 mm sliding clearance, Ø24 mm horn hole (placeholder until the MG996R horn is measured). The servo mount comes later from the real servo's dimensions.
- The pinion and rack tooth profiles are computed from the involute equations by the scripts in cad/scripts/, using the numbers in docs/sizing.md, because SOLIDWORKS's built-in gear tool draws approximate tooth shapes. The rack's pitch line is offset 0.15 mm for backlash.
