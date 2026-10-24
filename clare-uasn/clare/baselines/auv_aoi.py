"""
Multi-AUV-assisted AoI-energy collection baseline (ref6):

    "Joint optimization of AoI and energy for AUV-assisted data collection
     in underwater acoustic sensor networks"

Representative implementation: AUV collects from nodes with the oldest
last-update time; routing locally uses depth progress only, so that the
AUV contact is the freshness driver.
"""
from clare.sim.protocol import Protocol


class AUVAoIProtocol(Protocol):
    name = "AUV-AoI"

    def choose_forwarder(self, i_node, neighbours, params):
        cands = [j for j in neighbours if j.xyz[2] < i_node.xyz[2]]
        if not cands:
            return None
        # prefer shallower nodes (toward AUV collection points)
        j = min(cands, key=lambda n: n.xyz[2])
        return {"id": j.idx, "z": j.xyz[2], "E": j.E, "q": j.q,
                "E_Ntx": 1.5, "eta": j.eta, "_score": -j.xyz[2]}
