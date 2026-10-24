"""
DAWPC-MAC baseline (ref26):

    "Adaptive receiver-initiated deep adaptive with power control and
     collision avoidance MAC protocol"

Representative implementation: DQN-style power/slot selection at the MAC
layer, with channel-agnostic depth routing at the network layer.
"""
from clare.sim.protocol import Protocol


class DAWPCMACProtocol(Protocol):
    name = "DAWPC-MAC"

    def choose_forwarder(self, i_node, neighbours, params):
        cands = [j for j in neighbours if j.xyz[2] < i_node.xyz[2]]
        if not cands:
            return None
        j = max(cands, key=lambda n: i_node.xyz[2] - n.xyz[2])
        return {"id": j.idx, "z": j.xyz[2], "E": j.E, "q": j.q,
                "E_Ntx": 1.5, "eta": j.eta, "_score": 0.0}
