"""Node drift integration for Eq. (2)."""
from __future__ import annotations
import numpy as np


def drift_step(x, v, dt, rng=None, sigma_w2=0.0):
    """Eq. (2): x(k+1) = x(k) + v dt + w."""
    x_new = x + v * dt
    if rng is not None and sigma_w2 > 0.0:
        x_new = x_new + rng.normal(0.0, np.sqrt(sigma_w2 * dt), size=x.shape)
    return x_new
