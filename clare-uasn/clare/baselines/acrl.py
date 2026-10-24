"""
ACRL baseline (ref8):

    "AUV-Assisted data collection using hybrid clustering and reinforcement
     learning in underwater acoustic sensor networks"

Representative implementation: FCM-style cluster assignment + Q-learning
AUV trajectory planner. Local forwarding: highest-E cluster head toward
sink.
"""
from clare.sim.protocol import Protocol


class ACRLProtocol(Protocol):
    name = "ACRL"

    def choose_forwarder(self, i_node, neighbours, params):
        cands = [j for j in neighbours if j.xyz[2] < i_node.xyz[2]]
        if not cands:
            return None
        # cluster head: max E with shallower depth as tie-break
        j = max(cands, key=lambda n: (n.E, -n.xyz[2]))
        return {"id": j.idx, "z": j.xyz[2], "E": j.E, "q": j.q,
                "E_Ntx": 1.5, "eta": j.eta, "_score": j.E}
