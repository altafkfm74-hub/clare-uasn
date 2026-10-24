"""Acoustic channel using PER from Eq. (15)."""
from __future__ import annotations
import numpy as np
from clare.core.link_model import rx_power, sinr, per_from_sinr


def link_per(x_tx, x_rx, P_tx=2.0, f_khz=18.0,
             N0=1e-15, B=10_000.0, I_w=0.0) -> float:
    d = float(np.linalg.norm(np.asarray(x_tx, float) - np.asarray(x_rx, float)))
    pr = rx_power(P_tx, d, f_khz)
    sn = sinr(pr, N0, B, I_w)
    return per_from_sinr(sn)
