"""
Presentation helpers used only by figure scripts.
"""
from __future__ import annotations
import os
import numpy as np
import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt

METHODS = [
    "CLARE",
    "QE-ORP", "EARP", "IEBERP", "AUV-AoI", "ACRL",
    "RERA", "RLOR", "QTRU", "DAWPC-MAC", "AI-Classifier",
]

COLORS = {
    "CLARE":       "#FF0000",
    "QE-ORP":      "#0044CC",
    "EARP":        "#00A000",
    "IEBERP":      "#7A1FA2",
    "AUV-AoI":     "#FFC400",
    "ACRL":        "#00B3B3",
    "RERA":        "#FF1493",
    "RLOR":        "#FF6600",
    "QTRU":        "#8B0000",
    "DAWPC-MAC":   "#708090",
    "AI-Classifier":"#4B0082",
}

STYLES = {
    "CLARE":       "-",
    "QE-ORP":      (0, (6, 2)),
    "EARP":        (0, (4, 1, 1, 1)),
    "IEBERP":      (0, (7, 2, 2, 2)),
    "AUV-AoI":     (0, (2, 1)),
    "ACRL":        (0, (1, 1)),
    "RERA":        (0, (3, 1, 1, 1, 1, 1)),
    "RLOR":        (0, (5, 2, 1, 2)),
    "QTRU":        (0, (8, 3)),
    "DAWPC-MAC":   (0, (3, 1)),
    "AI-Classifier":(0, (6, 2, 2, 2, 2, 2)),
}

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif", "Times New Roman"],
    "font.weight": "bold", "axes.labelweight": "bold",
    "axes.titleweight": "bold", "axes.linewidth": 1.4,
    "pdf.fonttype": 42, "ps.fonttype": 42, "savefig.dpi": 600,
    "xtick.direction": "in", "ytick.direction": "in",
})


def save(fig, name):
    os.makedirs("figures", exist_ok=True)
    path = os.path.join("figures", name + ".pdf")
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("saved " + path)
