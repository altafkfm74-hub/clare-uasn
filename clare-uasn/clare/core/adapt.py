"""
Online adaptation of confidence threshold tau and low-confidence penalty alpha.

Described in Section III-H and Fig. 1(h):

    tau_{t+1} = tau_t + mu_tau * d PDR / d tau

The penalty alpha follows the same scheme. Weights of the composite score
are NOT adapted here; they are fixed in forwarder.DEFAULT_WEIGHTS.
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class AdaptiveParams:
    tau: float = 0.5
    alpha: float = 0.7
    mu_tau: float = 0.02
    mu_alpha: float = 0.02
    tau_min: float = 0.2
    tau_max: float = 0.9
    alpha_min: float = 0.3
    alpha_max: float = 1.0


def step(param: AdaptiveParams, dPDR_dtau: float, dPDR_dalpha: float) -> AdaptiveParams:
    """Gradient-ascent update for tau and alpha (Section III-H)."""
    param.tau = float(max(param.tau_min,
                          min(param.tau_max, param.tau + param.mu_tau * dPDR_dtau)))
    param.alpha = float(max(param.alpha_min,
                            min(param.alpha_max, param.alpha + param.mu_alpha * dPDR_dalpha)))
    return param


def apply_alpha(eta_j: float, alpha: float, tau: float) -> float:
    """
    Confidence-weighted routing term.

    If eta_j >= tau, use eta_j as the effective confidence;
    if eta_j < tau, down-weight it by alpha.
    """
    return float(eta_j if eta_j >= tau else alpha * eta_j)
