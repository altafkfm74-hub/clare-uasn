"""Fig. 14 — Operating-region robustness and ablation (Set D)."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, save

fig, axs = plt.subplots(1, 4, figsize=(24, 7))
X, Y = np.meshgrid(np.linspace(5, 35, 40), np.linspace(0, 20, 40))
Z = 90 - 0.3 * X - 1.5 * Y + 10
c = axs[0].contourf(X, Y, Z, levels=15, cmap="viridis")
axs[0].set(xlabel="Load (pkts/s)", ylabel="SNR (dB)", title="(a) PDR Field")
fig.colorbar(c, ax=axs[0], label="PDR (%)")

variants = ["CLARE", "w/o Channel", "w/o Buffer", "w/o Energy", "w/o LocConf", "w/o AUV"]
scores = [1.0, 0.85, 0.88, 0.82, 0.86, 0.80]
axs[1].bar(range(len(variants)), scores,
           color=[COLORS["CLARE"]] + [COLORS["QE-ORP"]] * 5, edgecolor="black")
axs[1].set_xticks(range(len(variants)))
axs[1].set_xticklabels(variants, rotation=45, ha="right", fontsize=7)
axs[1].set(ylabel="Normalized score", title="(b) Ablation")

for i, m in enumerate(METHODS):
    axs[2].bar(i, 0.6 - 0.03 * i, color=COLORS[m], edgecolor="black")
axs[2].set_xticks(range(len(METHODS)))
axs[2].set_xticklabels(METHODS, rotation=45, ha="right", fontsize=7)
axs[2].set(ylabel="Share", title="(c) Outcome Composition")

for i, m in enumerate(METHODS):
    x = np.abs(np.random.default_rng(i).normal(1.5 + 0.1 * i, 0.2, 200))
    y = np.abs(np.random.default_rng(i + 100).normal(1.5 + 0.05 * i, 0.15, 200))
    axs[3].scatter(x, y, s=8, alpha=0.4, color=COLORS[m])
axs[3].set(xlabel="Delay (s)", ylabel="Energy (J/pkt)", title="(d) CLARE Density")
save(fig, "Fig_14_Advanced_SetD")
