from clare.env.world import default_world
from clare.sim.engine import simulate
from clare.baselines import BASELINES
from clare.baselines.clare_protocol import CLAREProtocol


def test_all_protocols_runnable():
    world = default_world(seed=0, n_nodes=8)
    for name, cls in BASELINES.items():
        r = simulate(protocol=cls(), world=world, duration_h=0.05, seed=0)
        assert 0.0 <= r.pdr <= 1.0
    r = simulate(protocol=CLAREProtocol(), world=world, duration_h=0.05, seed=0)
    assert 0.0 <= r.pdr <= 1.0
