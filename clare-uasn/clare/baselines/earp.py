"""
EARP baseline (ref3):

    "Energy Efficient Routing for Underwater Sensor Network Using Eco-Aware
     Routing Protocol in Comparison with Opportunistic Routing Protocol"

Representative implementation: residual-energy-maximizing node selection.
"""
from clare.sim.protocol import Protocol


class EARPProtocol(Protocol):
    name = "EARP"

    def choose_forwarder(self, i_node, neighbours, params):
        cands = [j for j in neighbours if j.xyz[2] < i_node.xyz[2]]
        if not cands:
            return None
        j = max(cands, key=lambda n: n.E)
        return {"id": j.idx, "z": j.xyz[2], "E": j.E, "q": j.q,
                "E_Ntx": 1.5, "eta": j.eta, "_score": j.E}
