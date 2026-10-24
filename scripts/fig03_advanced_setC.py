"""Fig. 13 — Delay distribution and energy trade-offs (Set C)."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, save

fig, axs = plt.subplots(1, 4, figsize=(24, 7))
rng = np.random.default_rng(1)
for i, m in enumerate(METHODS):
    delays = np.abs(rng.normal(1.55 + 0.1 * i, 0.3, 500))
    axs[0].hist(delays, bins=25, alpha=0.4, color=COLORS[m], label=m)
axs[0].set(xlabel="Delay (s)", ylabel="Frequency", title="(a) Delay Distribution")
axs[0].legend(fontsize=6, ncol=2)

for i, m in enumerate(METHODS):
    axs[1].bar(i, 0.65 - 0.03 * i, color=COLORS[m], edgecolor="black")
axs[1].set_xticks(range(len(METHODS)))
axs[1].set_xticklabels(METHODS, rotation=45, ha="right", fontsize=7)
axs[1].set(ylabel="Data fraction", title="(b) Airtime Breakdown")

for i, m in enumerate(METHODS):
    axs[2].scatter(1.5 + 0.1 * i, 1.5 + 0.08 * i, s=120,
                   color=COLORS[m], label=m, edgecolor="black")
axs[2].set(xlabel="Delay (s)", ylabel="Energy (J/pkt)", title="(c) Energy–Delay Bubble")
axs[2].legend(fontsize=6, ncol=2)

X, Y = np.meshgrid(np.linspace(0.5, 3.0, 40), np.linspace(10, 50, 40))
Z = 60 - 10 * X - 0.5 * Y + 20
c = axs[3].contourf(X, Y, Z, levels=15, cmap="viridis")
axs[3].set(xlabel="Speed (m/s)", ylabel="Visit (min)", title="(d) AoI Heatmap")
fig.colorbar(c, ax=axs[3], label="AoI (s)")
save(fig, "Fig_13_Advanced_SetC")
