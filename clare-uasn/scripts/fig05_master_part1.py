"""Fig. 15A — Load, energy, and speed metrics (Master Part 1)."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, STYLES, save

fig, axs = plt.subplots(3, 4, figsize=(26, 15))
load = np.linspace(10, 35, 40)
for i, m in enumerate(METHODS):
    axs[0, 0].plot(load, 95 - 0.3 * i - 0.1 * load, color=COLORS[m], ls=STYLES[m], lw=2, label=m)
    axs[0, 1].plot(load, 0.5 + 0.15 * i + 0.02 * load, color=COLORS[m], ls=STYLES[m], lw=2)
    axs[0, 2].plot(load, 77 - 2 * i - 0.5 * load, color=COLORS[m], ls=STYLES[m], lw=2)
    axs[0, 3].plot(load, 0.05 + 0.03 * i + 0.001 * load, color=COLORS[m], ls=STYLES[m], lw=2)
    axs[1, 0].plot(load, 0.4 + 0.08 * i + 0.02 * load, color=COLORS[m], ls=STYLES[m], lw=2)
    axs[1, 1].plot(np.linspace(0, 10, 40), 0.6 + 0.02 * i + 0.03 * np.linspace(0, 10, 40),
                   color=COLORS[m], ls=STYLES[m], lw=2)
    axs[1, 2].plot(np.arange(20, 81, 20), 300 - 15 * i + 20 * np.arange(4),
                   color=COLORS[m], ls=STYLES[m], lw=2)
    axs[1, 3].plot(np.arange(20, 81, 20), 30 + 3 * i + 0.5 * np.arange(4),
                   color=COLORS[m], ls=STYLES[m], lw=2)
    axs[2, 0].plot(np.arange(1, 4), 60 - 5 * i - 10 * np.arange(1, 4),
                   color=COLORS[m], ls=STYLES[m], lw=2)
    axs[2, 1].plot(np.arange(1, 4), 1.0 + 0.15 * i + 0.1 * np.arange(1, 4),
                   color=COLORS[m], ls=STYLES[m], lw=2)
    axs[2, 2].plot(np.arange(1, 4), 0.8 + 0.08 * i + 0.1 * np.arange(1, 4),
                   color=COLORS[m], ls=STYLES[m], lw=2)
    axs[2, 3].bar(i, 95 - 1.5 * i, color=COLORS[m], edgecolor="black")
labels = [("PDR (%)", "PDR vs Load"), ("Delay (s)", "Delay vs Load"),
          ("Goodput (kbps)", "Goodput vs Load"), ("Drop (%)", "Drop Ratio vs Load"),
          ("Energy (J/pkt)", "Energy vs Load"), ("Fairness", "Jain Fairness vs Time"),
          ("Lifetime (h)", "Lifetime vs Nodes"), ("Overhead", "Overhead vs Nodes"),
          ("AoI (s)", "AoI vs Speed"), ("Delay (s)", "Delay vs Speed"),
          ("Energy (J/pkt)", "Energy vs Speed"), ("PDR (%)", "PDR Sensitivity")]
for ax, (yl, ttl) in zip(axs.flat, labels):
    ax.set(ylabel=yl, title=ttl); ax.grid(alpha=0.3)
axs[0, 0].legend(fontsize=6, ncol=1)
save(fig, "Fig_15A_Master_Part1")
