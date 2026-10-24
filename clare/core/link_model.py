"""
Acoustic link quality — Eqs. (13)-(16).

    P_r(k) = P_t(k) G(d, f)                       (13)
    gamma(k) = P_r / (N0 B + I)                   (14)
    p_err(k) = Q(sqrt(2 gamma))                   (15)
    p_err(k) = 1 - N_succ / N_tx                  (16)
"""
from __future__ import annotations
from math import erf, sqrt


def path_gain(distance, frequency_khz, absorption_db_per_khz=0.0):
    """G(d, f) for Eq. (13)."""
    if distance <= 0:
        raise ValueError("distance must be positive")
    spreading = 1.0 / (distance ** 2)
    A = absorption_db_per_khz * frequency_khz
    return float(spreading * 10.0 ** (-A * distance / 10.0))


def rx_power(P_tx, distance, frequency_khz, absorption_db_per_khz=0.0):
    """Eq. (13)."""
    return float(P_tx * path_gain(distance, frequency_khz, absorption_db_per_khz))


def sinr(P_rx, N0, bandwidth_hz, interference_w=0.0):
    """Eq. (14)."""
    return float(P_rx / max(N0 * bandwidth_hz + interference_w, 1e-30))


def per_from_sinr(sinr_linear):
    """Eq. (15): p_err(gamma) = Q(sqrt(2 gamma))."""
    try:
        x = max(sinr_linear, 0.0)
        return float(0.5 * (1 - erf(sqrt(2.0 * x) / sqrt(2.0))))
    except Exception:
        return 1.0


def per_from_ack(n_success, n_tx, eps=1e-9):
    """Eq. (16)."""
    if n_tx <= 0:
        return 0.0
    p = 1.0 - n_success / max(n_tx, eps)
    return float(min(max(p, 0.0), 1.0))
