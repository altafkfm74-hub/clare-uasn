# CLARE — Cross-Layer AUV-assisted Reliable and Energy-efficient Routing
#         for Underwater Acoustic Sensor Networks

Reference implementation of the method and **ten baseline protocols** described in:

> A. Hussain, S. Li,
> "CLARE: Jointly Optimized Multi-AUV-Assisted Localization Confidence and
> Cross-Layer Routing for Energy-Efficient Underwater Sensor Networks,"
> 2026.

## Repository layout

| Part | Module            | Purpose                                                                             |
|------|-------------------|-------------------------------------------------------------------------------------|
| I    | `clare.core`      | Every equation of Section III (EKF, confidence, link, energy, score, collision, adapt) |
| II   | `clare.env`       | World, four AUV trajectories, seabed sensors, acoustic channel, ARQ                |
| III  | `clare.sim`       | Packet-level event-driven simulator + metrics + beacon scheduler + drift           |
| IV   | `clare.baselines` | Ten baseline protocols (QE-ORP, EARP, IEBERP, AUV-AoI, ACRL, RERA, RLOR, QTRU, DAWPC-MAC, AIClassifier) |
| V    | `scripts/`        | One script per Section IV figure                                                    |

## Install

```bash
pip install -r requirements.txt
```

## 30-second demo

```python
from clare.env.world import default_world
from clare.sim.engine import simulate
from clare.baselines.clare_protocol import CLAREProtocol

world = default_world(seed=0, n_nodes=30)
r = simulate(protocol=CLAREProtocol(), world=world, duration_h=0.5, seed=0)
print(f"PDR={r.pdr:.3f}  delay={r.mean_delay_s:.2f}s  E/bit={r.energy_per_bit_nj:.0f} nJ")
```

## Reproduce any figure

```bash
python scripts/fig01_advanced_setA.py
```

## Tests

```bash
pytest tests/ -q
```

## License

MIT — see `LICENSE`.
