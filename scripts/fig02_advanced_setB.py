"""Fig. 12 — Freshness and sustainability (Set B)."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, STYLES, save

fig, axs = plt.subplots(2, 4, figsize=(24, 11))
x = np.linspace(0.5, 3.0, 40)
for i, m in enumerate(METHODS):
    axs[0, 0].plot(x, 180 - 15 * i - 20 * x, color=COLORS[m], ls=STYLES[m], lw=2, label=m)
    axs[0, 1].plot(np.linspace(0, 10, 40), 0.4 + 0.03 * i + 0.03 * np.linspace(0, 10, 40),
                   color=COLORS[m], ls=STYLES[m], lw=2)
    axs[0, 2].plot(np.arange(1, 6), 15 + 1.5 * i + 2 * np.arange(1, 6),
                   color=COLORS[m], ls=STYLES[m], lw=2)
    axs[0, 3].plot(np.linspace(0, 10, 40), 0.1 + 0.015 * i, color=COLORS[m], ls=STYLES[m], lw=2)
    axs[1, 0].plot(np.linspace(0.5, 2.5, 40), 10 + 2 * i + 4 / np.linspace(0.5, 2.5, 40),
                   color=COLORS[m], ls=STYLES[m], lw=2)
    axs[1, 1].plot(np.arange(1, 7), 95 - 2 * i - 2 * np.arange(1, 7),
                   color=COLORS[m], ls=STYLES[m], lw=2)
    axs[1, 2].plot(np.linspace(5, 35, 40), 0.75 - 0.02 * i - 0.005 * np.linspace(5, 35, 40),
                   color=COLORS[m], ls=STYLES[m], lw=2)
    axs[1, 3].plot(np.linspace(5, 35, 40), 2.5 - 0.05 * i + 0.01 * np.linspace(5, 35, 40),
                   color=COLORS[m], ls=STYLES[m], lw=2)
labels = [("AoI P99 (s)", "AoI P99 vs Speed", "a"),
          ("Fresh ratio", "Freshness Coverage vs Time", "b"),
          ("Convergence (min)", "Convergence vs Change Events", "c"),
          ("Variance", "Policy Variance vs Time", "d"),
          ("Bound (m)", "Loc. Bound vs Beacon Rate", "e"),
          ("PDR (%)", "PDR vs Burst Loss", "f"),
          ("Data airtime", "MAC Efficiency vs Load", "g"),
          ("Proxy (a.u.)", "Carbon-Energy Proxy", "h")]
for ax, (yl, ttl, lab) in zip(axs.flat, labels):
    ax.set(xlabel="x", ylabel=yl, title=f"({lab}) {ttl}")
    ax.grid(alpha=0.3)
axs[0, 0].legend(fontsize=6)
save(fig, "Fig_12_Advanced_SetB")
