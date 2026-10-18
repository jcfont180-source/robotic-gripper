## 2026-10-18 - Project start: spec, sizing analysis, and core CAD sprint

- Payload object: Deer Park water bottle, 512 g (511.2 g on a second scale as a cross-check), sealed and full. Grip at 120 mm from base, on the label (does not twist). Side approach.
- First bottle measurements (125 mm grip height, 215 mm circumference) were measuring errors and were redone.
- Egg: spec written around the USDA Grade A Large class instead of specific eggs. 5-egg sample measured for circumference and mass on Scale B in a bowl (eggs rolled off Scale A). Length not recorded; width sets the jaw range and mass sets the grip force.
- Scale B (Etekcity, Max 5 kg, d = 1 g) displayed one decimal place despite its 1 g label; masses recorded as displayed and treated as ±1 g.
- Set egg design range (41–48 mm, 48–73 g) and jaw opening (37–78 mm, stroke 41 mm).
- Mechanism: decision matrix in progress.
- Derived numbers (bottle diameter, egg design ranges, jaw opening) independently recomputed from the raw CSVs; all match.
- Payload and fragile handling rows set.
- Force control and durability rows set; every spec row now has a number and a test method. Setpoint values come from the sizing analysis.
- Jaw opening split into a CAD target (37–78 mm, includes 2 mm print allowance) and printed acceptance limits (≤ 39 mm closed, ≥ 76 mm open).
