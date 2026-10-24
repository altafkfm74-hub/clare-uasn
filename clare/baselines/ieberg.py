"""
IEBERP baseline (ref4):

    "Improved Energy-Based Efficient Routing Protocol for Underwater Wireless
     Sensor Networks"

Representative implementation: DUCS-style clustering + strata adaptation.
Nodes join the nearest cluster head (highest-E neighbor); forwarding goes
via cluster head toward the sink.
"""
from clare.sim.protocol import Protocol


class IEBERPProtocol(Protocol):
    name = "IEBERP"

    def choose_forwarder(self, i_node, neighbours, params):
        cands = [j for j in neighbours if j.xyz[2] < i_node.xyz[2]]
        if not cands:
            return None
        # cluster head selection: highest-E neighbor; break ties by depth
        j = max(cands, key=lambda n: (n.E, -n.xyz[2]))
        return {"id": j.idx, "z": j.xyz[2], "E": j.E, "q": j.q,
                "E_Ntx": 1.5, "eta": j.eta, "_score": j.E}
