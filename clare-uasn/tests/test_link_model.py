from clare.core import link_model as L


def test_per_ack():
    p = L.per_from_ack(90, 100)
    assert abs(p - 0.10) < 1e-9


def test_per_sinr():
    assert L.per_from_sinr(0.0) == 0.5
    assert L.per_from_sinr(10.0) < 0.001
