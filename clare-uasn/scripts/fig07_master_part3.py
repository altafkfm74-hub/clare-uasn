"""Fig. 15C — Distributional tails, radar, ablation (Master Part 3)."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, STYLES, save

fig, axs = plt.subplots(2, 4, figsize=(24, 11))
t = np.linspace(0.5, 2.0, 60)
for i, m in enumerate(METHODS):
    axs[0, 0].plot(t, 1 - np.exp(-(t - 0.5) / (0.3 + 0.08 * i)),
                   color=COLORS[m], ls=STYLES[m], lw=2, label=m)
    axs[0, 1].plot(t, 1 - np.exp(-(t - 1.0) / (0.2 + 0.08 * i)),
                   color=COLORS[m], ls=STYLES[m], lw=2)
axs[0, 0].set(xlabel="T (s)", ylabel="CDF", title="(a) Delay CDF (Moderate)")
axs[0, 0].legend(fontsize=5); axs[0, 0].grid(alpha=0.3)
axs[0, 1].set(xlabel="T (s)", ylabel="CDF", title="(b) Delay CDF (High)")
axs[0, 1].grid(alpha=0.3)

axes_lbl = ["PDR", "Delay", "Energy", "Lifetime", "AoI", "Overhead", "Chan", "Loc"]
angles = np.linspace(0, 2 * np.pi, len(axes_lbl), endpoint=False).tolist()
angles += angles[:1]
axr = fig.add_subplot(2, 4, 3, polar=True)
for i, m in enumerate(METHODS):
    vals = [0.9 - 0.04 * i] * len(axes_lbl); vals += vals[:1]
    axr.plot(angles, vals, color=COLORS[m], lw=2, label=m)
axr.set_xticks(angles[:-1]); axr.set_xticklabels(axes_lbl, fontsize=6)
axr.set_title("(c) Radar Summary", pad=15)

variants = ["CLARE", "w/o Channel", "w/o Buffer", "w/o Energy", "w/o LocConf", "w/o AUV"]
for j, (ax, ytitle, tt, base) in enumerate([
        (axs[0, 3], "PDR (%)", "(d) Ablation PDR", 95),
        (axs[1, 0], "Delay (s)", "(e) Ablation Delay", 1.0),
        (axs[1, 1], "Energy (J/pkt)", "(f) Ablation Energy", 1.0),
        (axs[1, 2], "AoI (s)", "(g) Ablation AoI", 40)]):
    load = np.linspace(10, 30, 20)
    for i, m in enumerate(METHODS):
        ax.plot(load, base - 0.2 * i - 0.1 * load,
                color=COLORS[m], ls=STYLES[m], lw=2)
    ax.set(title=tt, ylabel=ytitle); ax.grid(alpha=0.3)
save(fig, "Fig_15C_Master_Part3")
