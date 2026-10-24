"""
Recursive Bayesian localization — Eqs. (3)-(19) of the CLARE manuscript.

Equations implemented
---------------------
Eq. (3)  : ToA ranging       t~ = d / c(k) + n
Eq. (4)  : Sound-speed model c(k) = c0 + delta_c(k)
Eq. (5)  : Aggregated noise  t~ = d / c0 + nu
Eq. (6)  : State             s = [x, v]
Eq. (7)  : State prediction
Eq. (8)  : Covariance prediction
Eq. (9)  : Kalman gain
Eq. (10) : State update
Eq. (11) : Covariance update
Eq. (18) : Multi-AUV fusion  s += K * sum(t~ - t_hat)
"""
from __future__ import annotations
import numpy as np


def toa_measurement(distance, c0, delta_c=0.0, noise_std=0.0, rng=None):
    """Eq. (3) with sound-speed model Eq. (4)."""
    t = distance / (c0 + delta_c)
    if noise_std > 0.0 and rng is not None:
        t += rng.normal(0.0, noise_std)
    return float(t)


def F_Q(dt, sigma_w2, dim=3):
    """Eq. (7)-(8): state transition and process-noise matrices."""
    I = np.eye(dim)
    F = np.block([[I, dt * I], [np.zeros((dim, dim)), I]])
    Q = sigma_w2 * np.block([[(dt ** 3) / 3.0 * I, (dt ** 2) / 2.0 * I],
                             [(dt ** 2) / 2.0 * I, dt * I]])
    return F, Q


def ekf_predict(state, cov, F, Q):
    """Eqs. (7)-(8)."""
    return F @ state, F @ cov @ F.T + Q


def kalman_gain(cov_pred, H, R):
    """Eq. (9)."""
    S = H @ cov_pred @ H.T + R
    return np.linalg.solve(S, (cov_pred @ H.T).T).T


def ekf_update(state_pred, cov_pred, innovation, H, R):
    """Eqs. (10)-(11)."""
    K = kalman_gain(cov_pred, H, R)
    s = state_pred + K @ innovation
    I = np.eye(cov_pred.shape[0])
    P = (I - K @ H) @ cov_pred
    return s, 0.5 * (P + P.T)


def toa_jacobian(x_node, x_anchor, c0, dim=3):
    """Observation Jacobian H for ToA."""
    d = x_node - x_anchor
    r = max(np.linalg.norm(d), 1e-9)
    H = np.zeros((1, 2 * dim))
    H[0, :dim] = (d / r) / c0
    return H


def multi_auv_fusion(state_pred, K, innovations):
    """Eq. (18): multi-AUV measurement fusion."""
    total = np.zeros_like(state_pred)
    for e in innovations:
        total += e
    return state_pred + K @ total
