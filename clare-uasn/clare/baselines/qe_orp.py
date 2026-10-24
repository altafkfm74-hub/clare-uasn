"""
QE-ORP baseline (ref4 in the paper):

    "QoS-Aware and Energy-Optimized Cooperative Opportunistic Routing Protocol
     for Underwater Wireless Sensor Networks in Water Resource Management"

Representative implementation: depth + residual energy + link state, with
single-path partner selection. Weight vector normalized to 3 terms.
"""
from clare.sim.protocol import Protocol
import numpy as np


class QEORPProtocol(Protocol):
    name = "QE-ORP"
    w_depth = 0.5
    w_energy = 0.3
    w_link = 0.2

    def choose_forwarder(self, i_node, neighbours, params):
        best, best_s = None, -np.inf
        for j in neighbours:
            if j.xyz[2] >= i_node.xyz[2]:
                continue
            dz = i_node.xyz[2] - j.xyz[2]
            e_bar = j.E / params["E_max"]
            # link state approximated by 1 - per
            per = 0.05  # nominal; real impl uses ACK ratio
            link = 1.0 - per
            s = (self.w_depth * dz
                 + self.w_energy * e_bar
                 + self.w_link * link)
            if s > best_s:
                best_s = s
                best = {"id": j.idx, "z": j.xyz[2], "E": j.E, "q": j.q,
                        "E_Ntx": 1.5, "eta": j.eta, "_score": s}
        return best
