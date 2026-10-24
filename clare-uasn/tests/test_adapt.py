from clare.core import adapt


def test_adaptive_step():
    p = adapt.AdaptiveParams()
    tau0 = p.tau
    adapt.step(p, dPDR_dtau=1.0, dPDR_dalpha=0.0)
    assert p.tau > tau0


def test_apply_alpha():
    assert adapt.apply_alpha(0.8, alpha=0.5, tau=0.5) == 0.8
    assert adapt.apply_alpha(0.2, alpha=0.5, tau=0.5) == 0.1
