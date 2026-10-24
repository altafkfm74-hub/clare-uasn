"""
clare.baselines — ten reference protocols.

    qe_orp        : QoS-aware energy-optimized cooperative opportunistic routing
    earp          : Eco-aware routing protocol (EARP)
    ieberg        : Improved energy-based efficient routing (IEBERP)
    auv_aoi       : Multi-AUV-assisted AoI-energy data collection
    acrl          : AUV clustering + RL (FCM + Firefly + Q-learning)
    rera          : Reliable energy-efficient routing + AUV outlier detection
    rl_trust      : RL trust opportunistic routing (RLOR)
    qtru          : Q-learning tree routing (QTRU)
    dawpc_mac     : Deep Q-Learning MAC with power control (DAWPC-MAC)
    ai_classifier : AI-driven adaptive communication classifier

    clare_protocol : reference CLARE wrapper (not a baseline)

All baselines share the same Protocol interface. To use a specific one,
import it directly, e.g.:

    from clare.baselines.qtru import QTRUProtocol
    from clare.baselines.eedbr_alias import EEDBRProtocol  # not present here
"""
from clare.baselines.clare_protocol import CLAREProtocol
from clare.baselines.qe_orp        import QEORPProtocol
from clare.baselines.earp          import EARPProtocol
from clare.baselines.ieberg        import IEBERPProtocol
from clare.baselines.auv_aoi       import AUVAoIProtocol
from clare.baselines.acrl          import ACRLProtocol
from clare.baselines.rera          import RERAProtocol
from clare.baselines.rl_trust      import RLTrustProtocol
from clare.baselines.qtru          import QTRUProtocol
from clare.baselines.dawpc_mac     import DAWPCMACProtocol
from clare.baselines.ai_classifier import AIClassifierProtocol

BASELINES = {
    "QE-ORP":       QEORPProtocol,
    "EARP":         EARPProtocol,
    "IEBERP":       IEBERPProtocol,
    "AUV-AoI":      AUVAoIProtocol,
    "ACRL":         ACRLProtocol,
    "RERA":         RERAProtocol,
    "RLOR":         RLTrustProtocol,
    "QTRU":         QTRUProtocol,
    "DAWPC-MAC":    DAWPCMACProtocol,
    "AI-Classifier":AIClassifierProtocol,
}
__all__ = ["CLAREProtocol"] + list(BASELINES.values()) + ["BASELINES"]
