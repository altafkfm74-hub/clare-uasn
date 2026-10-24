"""
Multi-AUV coordination equations — Eqs. (1)-(8).

    Eq. (1) : Collision avoidance |z_m - z_n| >= dz_min  OR
              ||x_m - x_n||_2 >= R_safe
    Eq. (2) : Beacon schedule     t_m = t0 + m * dT_slot
    Eq. (3) : Interference-free   |t_m - t_n| >= tau_max + guard
    Eq. (4) : Proximity trigger   d_mn < R_safe
    Eq. (5) : Collision bound     P_coll <= 1 - exp(-int lambda P_fail)
    Eq. (6) : Measurement set     B_i = {m : ||x_i - x_A_m|| <= R_beacon}
    Eq. (7) : Multi-AUV fusion (defined in localization.multi_auv_fusion)
    Eq. (8) : Mean coverage       bar_M = mean E[|B_i|]
"""
from __future__ import annotations
import numpy as np

DZ_MIN = 50.0
R_SAFE = 50.0
DT_SLOT = 2.0
DELTA_GUARD = 0.5
R_BEACON = 300.0


def collision_condition(z_m, z_n, x_m, x_n, dz_min=DZ_MIN, R_safe=R_SAFE):
    """Eq. (1)."""
    if abs(z_m - z_n) >= dz_min:
        return True
    dx = np.asarray(x_m, float) - np.asarray(x_n, float)
    return bool(np.linalg.norm(dx) >= R_safe)


def beacon_slot(t0, m_index, dt_slot=DT_SLOT):
    """Eq. (2)."""
    return float(t0 + m_index * dt_slot)


def interference_free(t_m, t_n, d_max, c0, delta_guard=DELTA_GUARD):
    """Eq. (3)."""
    return bool(abs(t_m - t_n) >= d_max / c0 + delta_guard)


def proximity(x_m, x_n, R_safe=R_SAFE):
    """Eq. (4)."""
    return bool(np.linalg.norm(np.asarray(x_m, float) - np.asarray(x_n, float)) < R_safe)


def collision_probability_bound(lambda_enc, P_fail, T):
    """Eq. (5)."""
    return float(1.0 - np.exp(-lambda_enc * P_fail * T))


def measurement_set(x_i, auv_positions, R_beacon=R_BEACON):
    """Eq. (6)."""
    p = np.asarray(x_i, float)
    return [m for m, xa in enumerate(auv_positions)
            if np.linalg.norm(p - np.asarray(xa, float)) <= R_beacon]


def mean_coverage(coverage_sets):
    """Eq. (8)."""
    if not coverage_sets:
        return 0.0
    return float(np.mean([len(s) for s in coverage_sets]))
