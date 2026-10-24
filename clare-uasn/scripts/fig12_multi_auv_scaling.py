"""Fig. 20 — Sensitivity to fleet size."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import save

fig, axs = plt.subplots(2, 4, figsize=(24, 11))
M = np.arange(1, 9)
for i, (tt, yl, formula) in enumerate([
        ("(a) PDR", "PDR (%)", lambda x: 90 + 8 * (1 - np.exp(-(x - 1) / 1.5))),
        ("(b) Delay", "Delay (s)", lambda x: 1.7 - 0.8 * (1 - np.exp(-(x - 1) / 1.5))),
        ("(c) AoI", "AoI (s)", lambda x: 62 - 38 * (1 - np.exp(-(x - 1) / 1.5))),
        ("(d) Energy", "E/bit (J/pkt)", lambda x: 1.8 - 0.6 * (1 - np.exp(-(x - 1) / 1.5)))]):
    ax = axs[0, i]
    ax.plot(M, [formula(m) for m in M], color="red", marker="o", lw=2, label="CLARE")
    ax.plot(M, [formula(m) * 0.95 for m in M], color="blue", marker="s", lw=2, ls="--", label="Routing-only")
    ax.set(xlabel="# AUVs", ylabel=yl, title=tt); ax.grid(alpha=0.3); ax.legend(fontsize=6)

for i, (tt, yl, formula) in enumerate([
        ("(e) RMSE", "RMSE (m)", lambda x: 20 - 10 * (1 - np.exp(-(x - 1) / 1.5))),
        ("(f) Coverage", "Coverage (%)", lambda x: 40 + 40 * (1 - np.exp(-(x - 1) / 2))),
        ("(g) Overhead", "Overhead (%)", lambda x: 5 * x),
        ("(h) Net utility", "Utility", lambda x: 70 + 20 * (1 - np.exp(-(x - 1) / 2)) - 5 * (x - 4) ** 2)]):
    ax = axs[1, i]
    ax.plot(M, [formula(m) for m in M], color="red", marker="o", lw=2)
    ax.set(xlabel="# AUVs", ylabel=yl, title=tt); ax.grid(alpha=0.3)
save(fig, "Fig_20_MultiAUV_Scaling")
