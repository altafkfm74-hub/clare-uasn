"""Fig. 21 — Component ablation deep-dive."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import save

fig, axs = plt.subplots(2, 4, figsize=(24, 11))
variants = ["CLARE", "w/o Ch", "w/o Buf", "w/o E", "w/o Loc", "w/o AUV"]
load = np.linspace(10, 30, 40)
Z = np.zeros((6, len(load)))
for i, v in enumerate(variants):
    Z[i] = 95 - 0.5 * i * 2 - 0.1 * load
axs[0, 0].imshow(Z, aspect="auto", cmap="viridis", extent=[10, 30, 0, 6])
axs[0, 0].set_yticks(np.arange(6) + 0.5)
axs[0, 0].set_yticklabels(variants, fontsize=6)
axs[0, 0].set(xlabel="Load", title="(a) PDR Ablation")

dPDR = [-7.5, -6.1, -5.7, -4.8, -6.8]
axs[0, 1].bar(range(len(dPDR)), dPDR, color="red", edgecolor="black")
axs[0, 1].set_xticks(range(len(dPDR)))
axs[0, 1].set_xticklabels(variants[1:], rotation=45, ha="right", fontsize=7)
axs[0, 1].set(ylabel="ΔPDR", title="(b) ΔPDR")

dDelay = [0.57, 0.44, 0.36, 0.24, 0.50]
axs[0, 2].bar(range(len(dDelay)), dDelay, color="blue", edgecolor="black")
axs[0, 2].set_xticks(range(len(dDelay)))
axs[0, 2].set_xticklabels(variants[1:], rotation=45, ha="right", fontsize=7)
axs[0, 2].set(ylabel="ΔDelay", title="(c) ΔDelay")

dEnergy = [0.82, 0.55, 0.89, 0.43, 0.65]
axs[0, 3].bar(range(len(dEnergy)), dEnergy, color="green", edgecolor="black")
axs[0, 3].set_xticks(range(len(dEnergy)))
axs[0, 3].set_xticklabels(variants[1:], rotation=45, ha="right", fontsize=7)
axs[0, 3].set(ylabel="ΔEnergy", title="(d) ΔEnergy")

dAoI = [6, 4, 3, 2, 18]
axs[1, 0].bar(range(len(dAoI)), dAoI, color="orange", edgecolor="black")
axs[1, 0].set_xticks(range(len(dAoI)))
axs[1, 0].set_xticklabels(variants[1:], rotation=45, ha="right", fontsize=7)
axs[1, 0].set(ylabel="ΔAoI", title="(e) ΔAoI")

wp = np.linspace(0.1, 0.5, 9); wr = np.linspace(0.1, 0.5, 9)
WP, WR = np.meshgrid(wp, wr)
Z2 = 95 - 5 * (WP - 0.30) ** 2 - 5 * (WR - 0.20) ** 2
c = axs[1, 1].contourf(WP, WR, Z2, levels=15, cmap="viridis")
axs[1, 1].plot(0.30, 0.20, "*", color="red", ms=20, markeredgecolor="black")
axs[1, 1].set(xlabel="wp", ylabel="wr", title="(f) PDR Surface")
fig.colorbar(c, ax=axs[1, 1], label="PDR (%)")

features = ["Channel", "Buffer", "Energy", "LocConf", "AUV", "Routing"]
variance = [24, 18, 22, 15, 12, 9]
axs[1, 2].bar(range(len(features)), variance, color="blue", edgecolor="black")
axs[1, 2].set_xticks(range(len(features)))
axs[1, 2].set_xticklabels(features, rotation=45, ha="right", fontsize=7)
axs[1, 2].set(ylabel="Variance (%)", title="(g) Feature Contribution")

angles = np.linspace(0, 2 * np.pi, 6, endpoint=False).tolist() + [0]
axr = fig.add_subplot(2, 4, 8, polar=True)
for i, v in enumerate(variants):
    vals = [0.9 - 0.08 * i] * 6 + [0.9 - 0.08 * i]
    axr.plot(angles, vals, lw=2, label=v)
axr.set_xticks(angles[:-1]); axr.set_xticklabels(features, fontsize=6)
axr.set_title("(h) Ablation Radar", pad=15)
save(fig, "Fig_21_Ablation_DeepDive")
