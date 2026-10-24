"""
QTRU baseline (ref19):

    "An intelligent Q-learning-based tree routing method in underwater
     acoustic sensor networks"

Representative implementation: Q-learning-based tree construction with a
four-term reward (depth, residual energy, transmission probability,
candidate set). At runtime, the forwarder is the neighbor with the best
reward score.
"""
from clare.sim.protocol import Protocol


class QTRUProtocol(Protocol):
    name = "QTRU"

    def choose_forwarder(self, i_node, neighbours, params):
        cands = [j for j in neighbours if j.xyz[2] < i_node.xyz[2]]
        if not cands:
            return None
        def reward(j):
            dz = (i_node.xyz[2] - j.xyz[2]) / 100.0
            e = j.E / params["E_max"]
            p_succ = 1.0 - 0.05
            candidate_set = min(len(cands), 5) / 5.0
            return 0.4 * dz + 0.3 * e + 0.2 * p_succ + 0.1 * candidate_set
        j = max(cands, key=reward)
        return {"id": j.idx, "z": j.xyz[2], "E": j.E, "q": j.q,
                "E_Ntx": 1.5, "eta": j.eta, "_score": reward(j)}
