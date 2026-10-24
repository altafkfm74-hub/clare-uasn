"""
Cross-layer forwarding score — Eqs. (19)-(23).

Default weights from Section IV-A of the paper:
    (wp, wr, we, wb, wc) = (0.30, 0.20, 0.18, 0.16, 0.16)
"""
from __future__ import annotations
from typing import Sequence
import numpy as np

DEFAULT_WEIGHTS = (0.30, 0.20, 0.18, 0.16, 0.16)


def depth_progress(z_i, z_j):
    """Eq. (19)."""
    return float(z_i - z_j)


def normalize_energy(E_j, E_max):
    """Eq. (20)."""
    return 0.0 if E_max <= 0 else float(min(max(E_j / E_max, 0.0), 1.0))


def normalize_buffer(q_j, Q_max):
    """Eq. (21)."""
    return 0.0 if Q_max <= 0 else float(min(max(q_j / Q_max, 0.0), 1.0))


def score(dz, E_Ntx, E_bar, q_bar, eta_j,
          weights: Sequence[float] = DEFAULT_WEIGHTS):
    """Eq. (22)."""
    w_p, w_r, w_e, w_b, w_c = weights
    return float(w_p * dz - w_r * E_Ntx
                 - w_e * (1.0 - E_bar)
                 - w_b * q_bar
                 - w_c * (1.0 - eta_j))


def select_forwarder(candidates, z_i, dz_max=100.0, N_tx_max=5.0,
                     E_max=1000.0, Q_max=50.0,
                     weights: Sequence[float] = DEFAULT_WEIGHTS):
    """Eq. (23)."""
    best, best_s = None, -np.inf
    for c in candidates:
        if c["z"] >= z_i:
            continue
        dz = depth_progress(z_i, c["z"]) / dz_max
        eN = min(max(c["E_Ntx"] / N_tx_max, 0.0), 1.0)
        E_bar = normalize_energy(c["E"], E_max)
        q_bar = normalize_buffer(c["q"], Q_max)
        s = score(dz, eN, E_bar, q_bar, c["eta"], weights)
        if s > best_s:
            best_s = s
            best = dict(c)
            best["_score"] = s
    return best
