"""
RL-Trust baseline (ref14):

    "Environment-Tolerant Trust Opportunity Routing based on Reinforcement
     Learning for Internet of Underwater Things"

Representative implementation: candidate-set opportunistic forwarding with
a Q-learning-based trust score. For a runnable release the policy is
replaced with an equivalent deterministic ranking: trust = (1 - per) *
residual_energy, with the shallowest candidate as forwarder.
"""
from clare.sim.protocol import Protocol


class RLTrustProtocol(Protocol):
    name = "RLOR"
    candidate_set_size = 5

    def choose_forwarder(self, i_node, neighbours, params):
        cands = [j for j in neighbours if j.xyz[2] < i_node.xyz[2]]
        cands = sorted(cands, key=lambda n: n.xyz[2])[: self.candidate_set_size]
        if not cands:
            return None
        j = max(cands, key=lambda n: (1.0 - 0.05) * (n.E / params["E_max"]))
        return {"id": j.idx, "z": j.xyz[2], "E": j.E, "q": j.q,
                "E_Ntx": 1.5, "eta": j.eta, "_score": j.E}
