"""
AI-Classifier baseline (ref27):

    "AI-Driven Adaptive Communications for Energy-Efficient Underwater
     Acoustic Sensor Networks"

Representative implementation: lightweight on-node classifier that
adapts transmission parameters; network layer remains depth-only.
"""
from clare.baselines.dawpc_mac import DAWPCMACProtocol as _Base


class AIClassifierProtocol(_Base):
    name = "AI-Classifier"
