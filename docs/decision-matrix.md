# Decision matrix

Score each 1–5 (5 = best)

Force-control behavior replaces Gear-free, which double-counted Ease of modeling and Ease of printing and assembly.

| Criterion | Weight | Rack and pinion | Crank and links | Parallelogram four-bar |
|---|---|---|---|---|
| Ease of modeling | 20% | 4: pinion profile imported | 3: links stacked, rail on the servo axis | 5: plain bars and pins |
| Ease of printing and assembly | 20% | 3: rails and gear mesh to tune | 2: rails plus several pin joints | 5: pins only |
| Parallel jaw motion | 15% | 5: both jaws, centered | 4: centered only if the layout is exact | 2: one jaw, moves on an arc |
| Part count | 10% | 5: 3 unique parts | 3: 4 plus pins | 3: 4 plus pins |
| Torque needed | 15% | 5: lowest (worst case = average) | 3: about 1.6x | 2: highest |
| Force-control behavior | 20% | 5: constant ratio | 2: varies sharply near the stroke ends | 3: varies moderately |
| Weighted total | 100% | 4.40 | 2.75 | 3.50 |

## Decision and reason

Rack and pinion. Highest weighted total (4.40 vs. 3.50 and 2.75). Weights: modeling and printing 20% each (CAD due Monday; build risk over winter break), force-control behavior 20% (the core of the project), part count 10% (overlaps the ease rows). Sensitivity check: rack and pinion stays on top unless ease of modeling and printing together carry more than about 60% of the weight.
