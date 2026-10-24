"""Fig. 19 — Buffer and energy state dynamics."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, STYLES, save

fig, axs = plt.subplots(2, 4, figsize=(24, 11))
t = np.linspace(0, 60, 40)
for i, m in enumerate(METHODS):
    axs[0, 0].plot(t, 40 - 1.5 * i + 5 * np.sin(t / 5 + i), color=COLORS[m], ls=STYLES[m], lw=2, label=m)
    axs[0, 1].plot(t, 1000 - 4 * i * t / 10, color=COLORS[m], ls=STYLES[m], lw=2)
axs[0, 0].set(xlabel="Time (min)", ylabel="Buffer", title="(a) Buffer Occupancy")
axs[0, 0].legend(fontsize=5); axs[0, 0].grid(alpha=0.3)
axs[0, 1].set(xlabel="Time (min)", ylabel="Energy (J)", title="(b) Residual Energy")
axs[0, 1].grid(alpha=0.3)

for i, m in enumerate(METHODS):
    axs[0, 2].bar(i, 5 + 0.4 * i, color=COLORS[m], edgecolor="black")
axs[0, 2].set_xticks(range(len(METHODS)))
axs[0, 2].set_xticklabels(METHODS, rotation=45, ha="right", fontsize=6)
axs[0, 2].set(ylabel="Mean hops", title="(c) Hop Count")

for i, m in enumerate(METHODS):
    axs[0, 3].plot(t, 0.1 + 0.04 * i + 0.01 * t, color=COLORS[m], ls=STYLES[m], lw=2)
axs[0, 3].set(xlabel="Time (min)", ylabel="Hot-spot idx", title="(d) Hot-Spot Index")

for i, m in enumerate(METHODS):
    axs[1, 0].plot(np.linspace(0, 10, 40), 0.6 + 0.02 * i + 0.03 * np.linspace(0, 10, 40),
                   color=COLORS[m], ls=STYLES[m], lw=2)
axs[1, 0].set(xlabel="Time (h)", ylabel="Fairness", title="(e) Jain Fairness")

load = np.linspace(5, 35, 40)
for i, m in enumerate(METHODS):
    axs[1, 1].plot(load, 0.4 + 0.08 * i + 0.02 * load, color=COLORS[m], ls=STYLES[m], lw=2)
axs[1, 1].set(xlabel="Load", ylabel="E/bit (J/pkt)", title="(f) Energy per Bit")

lt = np.linspace(100, 300, 40)
for i, m in enumerate(METHODS):
    axs[1, 2].plot(lt, 1 - np.exp(-(lt - 100) / (50 + 8 * i)), color=COLORS[m], ls=STYLES[m], lw=2)
axs[1, 2].set(xlabel="Lifetime (h)", ylabel="CDF", title="(g) Lifetime CDF")

for i, m in enumerate(METHODS):
    axs[1, 3].hist(np.random.default_rng(i).normal(800 - 40 * i, 50, 200), bins=20,
                   alpha=0.4, color=COLORS[m], label=m)
axs[1, 3].set(xlabel="Residual E (J)", ylabel="Frequency", title="(h) Energy Histogram")
axs[1, 3].legend(fontsize=4)
save(fig, "Fig_19_Buffer_Energy_Dynamics")
