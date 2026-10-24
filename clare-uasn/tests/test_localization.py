import numpy as np
from clare.core import localization as L


def test_toa():
    t = L.toa_measurement(1500.0, 1500.0, 10.0)
    assert abs(t - 1500.0 / 1510.0) < 1e-9


def test_ekf_dims():
    F, Q = L.F_Q(0.5, 1e-3, dim=3)
    s, P = L.ekf_predict(np.zeros(6), np.eye(6), F, Q)
    K = L.kalman_gain(P, np.eye(1, 6), np.eye(1))
    assert K.shape == (6, 1)
