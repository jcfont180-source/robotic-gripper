"""Generate the finger-rack body outline as a DXF that imports cleanly into SOLIDWORKS.

Part frame (sketch on the Front Plane):
  X = 0 at the finger's inner face (the pad sits on the +X side of it)
  Y = 0 at the pinion axis height in the assembly
The rack runs along +X above the pinion, teeth pointing down (-Y).
The outline is ONE closed polyline: rack body + 10 straight-sided involute rack teeth.
Usage: python rack_profile.py  ->  writes finger_rack_profile.dxf
Requires: pip install ezdxf shapely
"""
import math

import ezdxf
from ezdxf import units
from shapely.geometry import Polygon

# ---- design inputs (docs/sizing.md) -------------------------------------
MODULE = 1.25
PRESSURE_ANGLE = 20.0      # deg
PINION_PITCH_RADIUS = 11.25
BACKLASH_OFFSET = 0.15     # rack pitch line moved 0.15 mm away from the pinion
N_TEETH = 10
TEETH_START_X = 11.5       # mm from the finger's inner face (10 mm from the pad surface)
BODY_LEFT_X = -8.0         # back of the 8 mm finger
BODY_RIGHT_X = 52.0
BODY_TOP_Y = 21.0
OUT_FILE = "finger_rack_profile.dxf"

# ---- derived geometry -----------------------------------------------------
t = math.tan(math.radians(PRESSURE_ANGLE))
pitch = math.pi * MODULE                         # 3.927 mm
y_pitch = PINION_PITCH_RADIUS + BACKLASH_OFFSET  # 11.40 mm
y_tip = y_pitch - MODULE                         # 10.15 mm (tooth tips, toward pinion)
y_root = y_pitch + 1.25 * MODULE                 # 12.9625 mm
s = pitch / 2                                    # tooth thickness at the pitch line
half_root = s / 2 + (y_root - y_pitch) * t       # half tooth width at the root line
half_tip = s / 2 - (y_pitch - y_tip) * t         # half tooth width at the tip

pts = [(BODY_LEFT_X, BODY_TOP_Y), (BODY_RIGHT_X, BODY_TOP_Y), (BODY_RIGHT_X, y_root)]
for k in reversed(range(N_TEETH)):               # walk the bottom edge right to left
    xc = TEETH_START_X + (k + 0.5) * pitch
    pts += [(xc + half_root, y_root), (xc + half_tip, y_tip),
            (xc - half_tip, y_tip), (xc - half_root, y_root)]
pts.append((BODY_LEFT_X, y_root))

# ---- checks ---------------------------------------------------------------
poly = Polygon(pts)
assert poly.is_valid, "outline self-intersects"
print(f"pitch {pitch:.4f} mm | pitch line Y {y_pitch:.4f} | tip Y {y_tip:.4f} | root Y {y_root:.4f}")
print(f"tooth width: tip {2 * half_tip:.4f} mm, root {2 * half_root:.4f} mm, "
      f"root land {pitch - 2 * half_root:.4f} mm")
print(f"teeth span X {TEETH_START_X + 0.5 * pitch - half_root:.3f} to "
      f"{TEETH_START_X + (N_TEETH - 0.5) * pitch + half_root:.3f} mm | {len(pts)} points, closed, valid")

# ---- write DXF (millimeters) ----------------------------------------------
doc = ezdxf.new("R2010")
doc.units = units.MM
doc.modelspace().add_lwpolyline(pts, close=True)
doc.saveas(OUT_FILE)
print(f"wrote {OUT_FILE}")
