"""Generate the gripper pinion profile as a DXF that imports cleanly into SOLIDWORKS.

The outline is ONE closed polyline (no gaps possible) plus one circle for the bore.
Geometry: standard full-depth involute spur gear.
  addendum = 1.0 * module, dedendum = 1.25 * module
  below the base circle the flank runs radially to the root circle
Usage: python gear_profile.py   ->  writes pinion_m1.25_z18.dxf
Requires: pip install ezdxf shapely
"""
import math

import ezdxf
from ezdxf import units
from shapely.geometry import Polygon

# ---- design inputs (docs/sizing.md) -------------------------------------
MODULE = 1.25          # mm
TEETH = 18
PRESSURE_ANGLE = 20.0  # deg
BORE_DIAMETER = 3.4    # mm, center hole for the horn screw
OUT_FILE = "pinion_m1.25_z18.dxf"

# ---- derived geometry -----------------------------------------------------
alpha = math.radians(PRESSURE_ANGLE)
r_pitch = MODULE * TEETH / 2               # 11.25 mm
r_base = r_pitch * math.cos(alpha)         # 10.571 mm
r_tip = r_pitch + MODULE                   # 12.50 mm
r_root = r_pitch - 1.25 * MODULE           # 9.6875 mm
pitch_angle = 2 * math.pi / TEETH


def inv(a):
    """Involute function."""
    return math.tan(a) - a


half_tooth_at_pitch = math.pi / (2 * TEETH)          # half the tooth angle at the pitch circle
phi_base = half_tooth_at_pitch + inv(alpha)          # half-angle at the base circle


def phi(r):
    """Angle from the tooth centerline to the flank at radius r (r >= base radius)."""
    return half_tooth_at_pitch + inv(alpha) - inv(math.acos(r_base / r))


N_FLANK, N_TIP, N_ROOT = 20, 6, 10
polar = []
for k in range(TEETH):
    c = k * pitch_angle
    polar.append((r_root, c - phi_base))                      # radial flank start
    for i in range(N_FLANK + 1):                              # involute, rising side
        r = r_base + (r_tip - r_base) * i / N_FLANK
        polar.append((r, c - phi(r)))
    a1, a2 = c - phi(r_tip), c + phi(r_tip)                   # tip arc
    for i in range(1, N_TIP):
        polar.append((r_tip, a1 + (a2 - a1) * i / N_TIP))
    for i in range(N_FLANK, -1, -1):                          # involute, falling side
        r = r_base + (r_tip - r_base) * i / N_FLANK
        polar.append((r, c + phi(r)))
    polar.append((r_root, c + phi_base))                      # radial flank end
    s, e = c + phi_base, c + pitch_angle - phi_base           # root arc to next tooth
    for i in range(1, N_ROOT):
        polar.append((r_root, s + (e - s) * i / N_ROOT))

points = [(r * math.cos(a), r * math.sin(a)) for r, a in polar]

# ---- checks before writing ------------------------------------------------
outline = Polygon(points)
radii = [math.hypot(x, y) for x, y in points]
assert outline.is_valid, "outline self-intersects"
assert abs(max(radii) - r_tip) < 1e-9 and abs(min(radii) - r_root) < 1e-9
print(f"pitch dia {2 * r_pitch:.3f} mm | outside dia {2 * r_tip:.3f} mm | "
      f"root dia {2 * r_root:.4f} mm | base dia {2 * r_base:.3f} mm")
print(f"tooth thickness at tip {2 * r_tip * phi(r_tip):.3f} mm | "
      f"{len(points)} outline points | closed, valid polygon")

# ---- write DXF (millimeters) ----------------------------------------------
doc = ezdxf.new("R2010")
doc.units = units.MM
msp = doc.modelspace()
msp.add_lwpolyline(points, close=True)
msp.add_circle((0, 0), BORE_DIAMETER / 2)
doc.saveas(OUT_FILE)
print(f"wrote {OUT_FILE}")
