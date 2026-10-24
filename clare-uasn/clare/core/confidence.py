"""
Localization confidence abstraction — Eq. (12).

    eta_i(k) = 1 / (1 + tr(P_i(k)))

Bound is guaranteed in (0, 1] for any finite covariance.
"""
from __future__ import annotations
import numpy as np


def eta(P, eps=1e-12):
    """Eq. (12)."""
    return float(1.0 / (1.0 + np.trace(P) + eps))


def eta_batch(P_list):
    return np.array([eta(P) for P in P_list])
