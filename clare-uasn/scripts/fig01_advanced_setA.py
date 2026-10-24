"""Fig. 11 — Advanced stability metrics (Set A)."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, STYLES, save

fig, axs = plt.subplots(2, 4, figsize=(24, 11))
load = np.linspace(5, 35, 60)
for i, m in enumerate(METHODS):
    axs[0, 0].plot(load, 0.15 + 0.02 * i + 0.01 * load,
                   color=COLORS[m], ls=STYLES[m], lw=2, label=m)
    axs[0, 1].plot(load, 0.5 + 0.1 * i + 0.05 * load, color=COLORS[m], ls=STYLES[m], lw=2)
    axs[0, 2].plot(load, 50 + 5 * i + 1.0 * load, color=COLORS[m], ls=STYLES[m], lw=2)
    axs[0, 3].plot(load, 250 - 3 * i - 0.5 * load, color=COLORS[m], ls=STYLES[m], lw=2)
    axs[1, 0].plot(load, 1.6 - 0.02 * i, color=COLORS[m], ls=STYLES[m], lw=2)
    axs[1, 1].plot(load, 0.5 - 0.01 * i, color=COLORS[m], ls=STYLES[m], lw=2)
    axs[1, 2].plot(load, 0.1 + 0.02 * i, color=COLORS[m], ls=STYLES[m], lw=2)
    axs[1, 3].plot(load, 200 - 3 * i, color=COLORS[m], ls=STYLES[m], lw=2)
labels = [("Jitter (s)", "Delay Jitter vs Load", "a"),
          ("P95 (s)", "P95 Delay vs Load", "b"),
          ("Queue (%)", "Queue Occupancy vs Load", "c"),
          ("bits/J", "Energy Efficiency vs Load", "d"),
          ("bps/Hz", "Spectral Eff. vs SNR", "e"),
          ("Outage", "Link Outage vs SNR", "f"),
          ("Ctrl/Data", "Ctrl/Data Airtime vs Nodes", "g"),
          ("T90 (s)", "T90 Delivery Time vs Nodes", "h")]
for ax, (yl, ttl, lab) in zip(axs.flat, labels):
    ax.set(xlabel="x", ylabel=yl, title=f"({lab}) {ttl}")
    ax.grid(alpha=0.3)
axs[0, 0].legend(fontsize=6, ncol=1)
save(fig, "Fig_11_Advanced_SetA")
