"""Fig. 17 — Recursive localization pipeline validation."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import save

fig, axs = plt.subplots(2, 4, figsize=(24, 11))
t = np.arange(100)
tr = np.abs(2 + np.sin(t / 5) + 0.5 * np.random.default_rng(0).normal(size=100))
axs[0, 0].plot(t, tr, color="red", lw=1.5)
axs[0, 0].set(xlabel="Time step", ylabel="Trace", title="(a) Covariance Trace")

eta = 1 / (1 + tr)
axs[0, 1].plot(t, eta, color="blue", lw=1.5)
axs[0, 1].set(xlabel="Time step", ylabel="eta", title="(b) Localization Confidence")

sigma = np.linspace(0, 5, 40)
axs[0, 2].plot(sigma, 5 + 2 * sigma + 0.5 * sigma ** 2, color="green", lw=2)
axs[0, 2].set(xlabel="Ranging noise (m)", ylabel="RMSE (m)", title="(c) RMSE vs Noise")

rate = np.linspace(0, 2.5, 40)
for M in [1, 2, 4]:
    axs[0, 3].plot(rate, 10 + 5 / (1 + M * rate), lw=2, label=f"{M} AUVs")
axs[0, 3].set(xlabel="Beacon rate", ylabel="RMSE (m)", title="(d) RMSE vs Beacon")
axs[0, 3].legend(fontsize=6)

for M in [1, 2, 3, 4]:
    axs[1, 0].scatter(M, 20 - 3 * M, color="blue", s=80)
axs[1, 0].set(xlabel="# AUVs", ylabel="RMSE (m)", title="(e) Fusion Gain")

X, Y = np.meshgrid(np.linspace(0, 1000, 40), np.linspace(0, 1000, 40))
Z = 1 + np.exp(-((X - 500) ** 2 + (Y - 500) ** 2) / (2 * 300 ** 2))
axs[1, 1].imshow(Z, extent=[0, 1000, 0, 1000], origin="lower", cmap="viridis")
axs[1, 1].set(xlabel="X (m)", ylabel="Y (m)", title="(f) GDOP Map")

err = np.abs(np.random.default_rng(1).normal(10, 5, 1000))
axs[1, 2].hist(err, bins=40, cumulative=True, density=True, color="blue")
axs[1, 2].set(xlabel="Error (m)", ylabel="CDF", title="(g) Position Error CDF")

tr2 = np.linspace(0.5, 5, 40)
axs[1, 3].plot(tr2, 1 / (1 + tr2), color="red", lw=2)
axs[1, 3].set(xlabel="Covariance trace", ylabel="eta", title="(h) eta vs Trace")
save(fig, "Fig_17_Localization_Pipeline")
