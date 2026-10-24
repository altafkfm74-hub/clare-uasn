from clare.core import energy as E


def test_expected():
    assert abs(E.expected_transmissions(0.10) - 1 / 0.9) < 1e-9


def test_energy_per_packet():
    e = E.energy_per_packet(1.5, 2.0, 0.1, 0.75, 0.05, 1e-6)
    assert e > 0
