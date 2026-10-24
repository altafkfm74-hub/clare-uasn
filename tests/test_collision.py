from clare.core import collision as C


def test_collision_condition():
    assert C.collision_condition(200, 300, [0, 0, 200], [0, 0, 300]) is True


def test_interference_free():
    assert C.interference_free(0.0, 2.0, 1500.0, 1500.0) is True


def test_measurement_set():
    assert C.measurement_set([0, 0, 100], [[0, 0, 50], [500, 0, 50]]) == [0]
