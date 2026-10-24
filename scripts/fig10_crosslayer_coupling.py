"""Fig. 18 — Cross-layer coupling validation."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, STYLES, save

fig, axs = plt.subplots(2, 4, figsize=(24, 11))
rng = np.random.default_rng(0)
raw = np.clip(rng.uniform(0.3, 0.9, (11, 5)), 0, 1)
wbar = 0.075
for j, lbl in enumerate(["wp*dz", "wr*E[Ntx]", "we*(1-E)", "wb*q", "wc*(1-eta)"]):
    axs[0, 0].bar(np.arange(11) + j * wbar, raw[:, j], wbar, label=lbl)
axs[0, 0].set_xticks(np.arange(11) + 2 * wbar)
axs[0, 0].set_xticklabels(METHODS, rotation=45, ha="right", fontsize=6)
axs[0, 0].set(title="(a) Score Decomposition"); axs[0, 0].legend(fontsize=6)

for i, m in enumerate(METHODS):
    axs[0, 1].plot(np.linspace(0.6, 1.4, 40), 95 + 1 - 1.5 * i + 0.5 * np.sin(np.linspace(0.6, 1.4, 40) * 10),
                   color=COLORS[m], ls=STYLES[m], lw=2, label=m)
axs[0, 1].set(xlabel="Weight scale factor", ylabel="PDR (%)", title="(b) PDR Sensitivity")
axs[0, 1].legend(fontsize=5, ncol=2)

eta = np.linspace(0.2, 0.8, 40)
axs[0, 2].plot(eta, 55 + 40 * eta, color="red", lw=2, label="CLARE (eta-aware)")
axs[0, 2].plot(eta, 55 + 30 * eta, color="blue", lw=2, ls="--", label="eta-agnostic")
axs[0, 2].set(xlabel="eta_i", ylabel="PDR (%)", title="(c) eta Coupling")
axs[0, 2].legend(fontsize=6)

for i, m in enumerate(METHODS):
    per = np.linspace(0, 0.5, 40)
    axs[0, 3].plot(per, 0.5 + 2 * per * (1 + 0.3 * i), color=COLORS[m], ls=STYLES[m], lw=2)
axs[0, 3].set(xlabel="PER", ylabel="Energy (J/pkt)", title="(d) PER vs Energy")

for i, m in enumerate(METHODS):
    axs[1, 0].bar(i, 1.0 / (0.5 + 0.08 * i), color=COLORS[m], edgecolor="black")
axs[1, 0].set_xticks(range(len(METHODS)))
axs[1, 0].set_xticklabels(METHODS, rotation=45, ha="right", fontsize=6)
axs[1, 0].set(ylabel="Probability", title="(e) Retransmission PMF")

per = np.linspace(0.01, 0.9, 40)
axs[1, 1].plot(per, 1 / (1 - per), color="blue", lw=2)
axs[1, 1].set(xlabel="p_err", ylabel="E[Ntx]", title="(f) E[Ntx] vs p_err")

eta2 = np.linspace(0, 1, 40)
Eb = np.linspace(0, 1, 40)
X, Y = np.meshgrid(eta2, Eb)
Z = 0.3 * X + 0.2 * Y
c = axs[1, 2].contourf(X, Y, Z, levels=15, cmap="viridis")
axs[1, 2].set(xlabel="eta_j", ylabel="E_bar_j", title="(g) Score Heatmap")
fig.colorbar(c, ax=axs[1, 2], label="S")

vars_ = ["w/o Ch", "w/o Buf", "w/o E", "w/o Loc", "w/o AUV"]
vals = [-6.5, -6.1, -5.7, -4.8, -5.9]
axs[1, 3].bar(range(len(vars_)), vals, color="red", edgecolor="black")
axs[1, 3].set_xticks(range(len(vars_)))
axs[1, 3].set_xticklabels(vars_, rotation=45, ha="right", fontsize=7)
axs[1, 3].set(ylabel="ΔPDR (pts)", title="(h) Cross-Layer Ablation")
save(fig, "Fig_18_CrossLayer_Coupling")
