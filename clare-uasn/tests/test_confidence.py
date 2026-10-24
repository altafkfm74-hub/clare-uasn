import numpy as np
from clare.core import confidence


def test_eta_bounds():
    P = np.eye(6)
    e = confidence.eta(P)
    assert 0.0 < e <= 1.0
