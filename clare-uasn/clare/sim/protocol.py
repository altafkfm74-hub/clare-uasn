"""Protocol interface and CLARE reference protocol."""
from __future__ import annotations
from clare.core import forwarder, confidence, adapt


class Protocol:
    name = "base"

    def update_eta(self, node, cov):
        node.eta = confidence.eta(cov)

    def choose_forwarder(self, i_node, neighbours, params):
        adaptive = params.get("adaptive")
        cands = []
        for j in neighbours:
            eta_eff = j.eta
            if adaptive is not None:
                eta_eff = adapt.apply_alpha(j.eta, adaptive.alpha, adaptive.tau)
            cands.append({"id": j.idx, "z": j.xyz[2], "E": j.E, "q": j.q,
                          "E_Ntx": 1.5, "eta": eta_eff})
        return forwarder.select_forwarder(
            cands, z_i=i_node.xyz[2],
            dz_max=params["dz_max"], N_tx_max=params["N_tx_max"],
            E_max=params["E_max"], Q_max=params["Q_max"],
            weights=params["weights"],
        )


class CLAREProtocol(Protocol):
    name = "CLARE"

    def choose_forwarder(self, i_node, neighbours, params):
        return super().choose_forwarder(i_node, neighbours, params)
