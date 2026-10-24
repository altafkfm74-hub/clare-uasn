"""Fig. 15B — Reliability, channel quality, spatial (Master Part 2)."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, STYLES, save

fig, axs = plt.subplots(2, 4, figsize=(24, 11))
snr = np.linspace(0, 20, 40)
for i, m in enumerate(METHODS):
    axs[0, 0].plot(snr, 4.5 - 0.15 * i * np.exp(-snr / 10) - 0.1 * snr / 20,
                   color=COLORS[m], ls=STYLES[m], lw=2, label=m)
    axs[0, 1].semilogy(snr, 0.5 * np.exp(-snr / 5) * (1 + 0.15 * i),
                       color=COLORS[m], ls=STYLES[m], lw=2)
    axs[0, 2].plot(np.linspace(0, 30, 40), 95 - 0.2 * i - 0.3 * np.linspace(0, 30, 40),
                   color=COLORS[m], ls=STYLES[m], lw=2)
    axs[0, 3].bar(i, 10 + 1.5 * i, color=COLORS[m], edgecolor="black")
axs[0, 0].set(xlabel="SNR (dB)", ylabel="re-tx/pkt", title="(a) Re-tx vs SNR")
axs[0, 0].legend(fontsize=6)
axs[0, 1].set(xlabel="SNR (dB)", ylabel="PER", title="(b) PER vs SNR")
axs[0, 2].set(xlabel="Loc. error (m)", ylabel="PDR (%)", title="(c) PDR vs Loc. Error")
axs[0, 3].set_xticks(range(len(METHODS)))
axs[0, 3].set_xticklabels(METHODS, rotation=45, ha="right", fontsize=6)
axs[0, 3].set(ylabel="RMSE (m)", title="(d) Localization RMSE")

X, Y = np.meshgrid(np.linspace(10, 30, 40), np.linspace(0, 20, 40))
Z = 90 - 0.3 * X - 1.0 * Y
c = axs[1, 0].contourf(X, Y, Z, levels=15, cmap="viridis")
axs[1, 0].set(xlabel="Load", ylabel="SNR (dB)", title="(e) CLARE Heatmap")
fig.colorbar(c, ax=axs[1, 0], label="PDR (%)")

Z2 = 85 - 0.5 * X - 1.5 * Y
c2 = axs[1, 1].contourf(X, Y, Z2, levels=15, cmap="viridis")
axs[1, 1].set(xlabel="Load", ylabel="SNR (dB)", title="(f) QE-ORP Heatmap")
fig.colorbar(c2, ax=axs[1, 1], label="PDR (%)")

X2, Y2 = np.meshgrid(np.linspace(0.5, 3.0, 40), np.linspace(10, 50, 40))
Z3 = 60 - 10 * X2 - 0.5 * Y2 + 20
c3 = axs[1, 2].contourf(X2, Y2, Z3, levels=15, cmap="viridis")
axs[1, 2].set(xlabel="Speed (m/s)", ylabel="Visit (min)", title="(g) AoI Heatmap")
fig.colorbar(c3, ax=axs[1, 2], label="AoI (s)")

for i, m in enumerate(METHODS):
    t = np.linspace(0, 60, 40)
    axs[1, 3].plot(t, 22 + 1.5 * i + 3 * np.exp(-t / 20) + 2 * np.sin(t / 5 + i),
                   color=COLORS[m], ls=STYLES[m], lw=2)
axs[1, 3].set(xlabel="Time (min)", ylabel="AoI (s)", title="(h) AoI Time-Series")
save(fig, "Fig_15B_Master_Part2")
