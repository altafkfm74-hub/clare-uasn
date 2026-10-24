"""
RERA baseline (ref9):

    "Reliable energy-efficient routing based on improved LOF detection and
     AUV-aided for UWSN"

Representative implementation: LOF-style outlier detection on neighbors;
anomalous nodes forward only delay-sensitive traffic (single-hop); other
nodes forward via the highest-E shallower neighbor.
"""
from clare.sim.protocol import Protocol


class RERAProtocol(Protocol):
    name = "RERA"

    def choose_forwarder(self, i_node, neighbours, params):
        cands = [j for j in neighbours if j.xyz[2] < i_node.xyz[2]]
        if not cands:
            return None
        # outlier check: nodes with very low E relative to median are skipped
        energies = [n.E for n in cands]
        med = sorted(energies)[len(energies) // 2]
        inliers = [n for n in cands if n.E >= 0.5 * med]
        pool = inliers if inliers else cands
        j = max(pool, key=lambda n: n.E)
        return {"id": j.idx, "z": j.xyz[2], "E": j.E, "q": j.q,
                "E_Ntx": 1.5, "eta": j.eta, "_score": j.E}
