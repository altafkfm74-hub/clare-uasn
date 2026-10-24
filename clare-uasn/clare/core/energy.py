"""
Retransmission-aware energy — Eqs. (17)-(18) and (24)-(25).

    E[N_tx](k) = 1 / (1 - p_err)                 (17)
    E_i->j(k)  = E[N_tx] (Ptx Tdata + Prx Tack + Ec)
                + Pidle Tidle
                + Nctrl (Ptx Tctrl + Prx Tctrl)    (18)
    E_i(k+1)   = E_i(k) - E_i->j(k)              (24)
    q_i(k+1)   = min{Qmax, q_i(k) + a_i - s_i}   (25)
"""
from __future__ import annotations


def expected_transmissions(p_err, cap=1e6):
    """Eq. (17)."""
    p = min(max(float(p_err), 0.0), 1.0 - 1e-12)
    return float(min(1.0 / (1.0 - p), cap))


def energy_per_packet(E_Ntx, P_tx, T_data, P_rx, T_ack, E_c,
                     P_idle=0.0, T_idle=0.0, N_ctrl=0, T_ctrl=0.0):
    """Eq. (18)."""
    data_term = E_Ntx * (P_tx * T_data + P_rx * T_ack + E_c)
    idle_term = P_idle * T_idle
    ctrl_term = N_ctrl * (P_tx * T_ctrl + P_rx * T_ctrl)
    return float(data_term + idle_term + ctrl_term)


def update_energy(E_i, E_consumed):
    """Eq. (24)."""
    return float(max(E_i - E_consumed, 0.0))


def update_buffer(q_i, arrivals, service, Q_max):
    """Eq. (25)."""
    return float(min(max(q_i + arrivals - service, 0.0), Q_max))
