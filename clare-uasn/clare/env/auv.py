"""
Four AUV trajectory classes matching Table II of the CLARE manuscript.

    AUV1 — raster scan  (200-300 m, central/right)
    AUV2 — loiter orbit (100-200 m, middle network)
    AUV3 — spiral sweep (150-350 m, left region)
    AUV4 — perimeter patrol (200-250 m, boundary)
"""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np


@dataclass
class AUVSpec:
    name: str
    x_center: float
    z_band: tuple
    trajectory: str


AUV_FLEET = [
    AUVSpec("AUV1", 700.0, (200, 300), "raster"),
    AUVSpec("AUV2", 500.0, (100, 200), "orbit"),
    AUVSpec("AUV3", 300.0, (150, 350), "spiral"),
    AUVSpec("AUV4", 500.0, (200, 250), "patrol"),
]


def position_at(spec: AUVSpec, t: float, W: float = 1000.0, H: float = 1000.0) -> tuple:
    """Return (x, y, z) of AUV at time t seconds."""
    zc = 0.5 * (spec.z_band[0] + spec.z_band[1])
    phase = (t / 300.0) % 1.0
    if spec.trajectory == "raster":
        x = spec.x_center - 200 + 400 * phase
        y = H / 2 + 250 * np.sin(2 * np.pi * 4 * phase)
    elif spec.trajectory == "orbit":
        a = 2 * np.pi * phase
        x = 500 + 300 * np.cos(a)
        y = 500 + 300 * np.sin(a)
    elif spec.trajectory == "spiral":
        a = 4 * np.pi * phase
        r = 100 + 250 * phase
        x = spec.x_center + r * np.cos(a)
        y = 500 + r * 0.6 * np.sin(a)
        z_lo, z_hi = spec.z_band
        zc = z_lo + phase * (z_hi - z_lo)
    else:  # patrol
        a = 2 * np.pi * phase
        x = 500 + 400 * np.cos(a)
        y = 500 + 400 * np.sin(a)
    x = float(np.clip(x, 20, W - 20))
    y = float(np.clip(y, 20, H - 20))
    return x, y, float(zc)
