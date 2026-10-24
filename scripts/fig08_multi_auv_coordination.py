"""Fig. 16 — Multi-AUV coordination validation."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import save

fig, axs = plt.subplots(2, 4, figsize=(24, 11))
rng = np.random.default_rng(0)
axs[0, 0].scatter(rng.uniform(100, 900, 50), rng.uniform(100, 900, 50),
                  s=20, c="k", alpha=0.4, label="Sensors")
axs[0, 0].plot(200 + 600 * np.linspace(0, 1, 60),
               500 + 250 * np.sin(8 * np.pi * np.linspace(0, 1, 60)),
               color="red", lw=2, label="AUV1")
a = 2 * np.pi * np.linspace(0, 1, 60)
axs[0, 0].plot(500 + 300 * np.cos(a), 500 + 300 * np.sin(a), color="blue", lw=2, label="AUV2")
a = 4 * np.pi * np.linspace(0, 1, 60)
r = 100 + 250 * np.linspace(0, 1, 60)
axs[0, 0].plot(300 + r * np.cos(a), 500 + r * 0.6 * np.sin(a), color="green", lw=2, label="AUV3")
a = 2 * np.pi * np.linspace(0, 1, 60)
axs[0, 0].plot(500 + 400 * np.cos(a), 500 + 400 * np.sin(a), color="orange", lw=2, label="AUV4")
axs[0, 0].set(xlabel="X (m)", ylabel="Y (m)", title="(a) Trajectories")
axs[0, 0].legend(fontsize=5)

d = np.abs(rng.normal(120, 40, 1000))
axs[0, 1].hist(d, bins=30, cumulative=True, density=True, color="blue", alpha=0.6, label="Coordinated")
axs[0, 1].hist(np.abs(rng.normal(30, 10, 1000)), bins=30, cumulative=True, density=True,
               color="red", alpha=0.6, label="Uncoordinated")
axs[0, 1].set(xlabel="Inter-AUV distance (m)", ylabel="CDF", title="(b) Inter-AUV Distance CDF")
axs[0, 1].legend(fontsize=6)

for lo, hi, c, lab in [(200, 300, "red", "AUV1"), (100, 200, "blue", "AUV2"),
                        (150, 350, "green", "AUV3"), (200, 250, "orange", "AUV4")]:
    axs[0, 2].plot([0, 100], [lo, lo], color=c, lw=6, label=lab)
    axs[0, 2].plot([0, 100], [hi, hi], color=c, lw=6)
axs[0, 2].set(xlabel="Time", ylabel="Depth (m)", title="(c) Depth Zoning")
axs[0, 2].legend(fontsize=6)

for w in [1, 2, 3, 4, 5]:
    axs[0, 3].bar(w, 10 ** (-w), color="blue", edgecolor="black")
axs[0, 3].set_yscale("log")
axs[0, 3].set(xlabel="Slot width ΔT (s)", ylabel="P_coll", title="(d) Beacon Collision")

axs[1, 0].bar([0, 1, 2, 3, 4], [0.05, 0.30, 0.45, 0.18, 0.02], color="blue", edgecolor="black")
axs[1, 0].set(xlabel="# AUVs covering node", ylabel="Frequency (%)", title="(e) Coverage Distribution")

for M in range(1, 9):
    axs[1, 1].scatter(M, min(2.5, 0.8 + 0.4 * np.log(M)), color="blue", s=50)
axs[1, 1].set(xlabel="# AUVs", ylabel="Mean coverage", title="(f) Mean Coverage")

events = np.arange(0, 20)
axs[1, 2].semilogy(events, 1e-5 * (1 + events), color="blue", lw=2)
axs[1, 2].set(xlabel="# handshake events", ylabel="Risk", title="(g) Collision Risk")

axs[1, 3].bar(["Uncoord", "Coord"], [42, 78], color=["red", "blue"], edgecolor="black", alpha=0.7)
axs[1, 3].bar(["Uncoord", "Coord"], [35, 9], bottom=[42, 78], color=["pink", "lightblue"], edgecolor="black")
axs[1, 3].set(ylabel="Fraction", title="(h) Coverage vs Overlap")
save(fig, "Fig_16_MultiAUV_Coordination")
