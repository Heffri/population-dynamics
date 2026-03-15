"""
main.py — Run all simulations and save plots to results/plots/.

Usage:
    python src/main.py
"""

import sys
import os
import numpy as np

# Allow imports from src/ when run from repo root
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from models    import two_species, three_species
from solvers   import forward_euler, rk45
from visualize import (time_series, phase_portrait,
                       euler_stability, three_species_panel)

OUT = os.path.join(os.path.dirname(__file__), "..", "results", "plots")
os.makedirs(OUT, exist_ok=True)

# ── Shared parameters ────────────────────────────────────────────────────────
PARAMS_2 = dict(alpha=0.3, beta=0.1, delta=0.05, gamma=0.1)
PARAMS_3 = dict(alpha=0.3, beta=0.1, delta=0.05, gamma=0.3, eta=0.1, zeta=0.5)


# ── 1. Forward Euler stability study ─────────────────────────────────────────
print("1. Euler stability study ...")

def single_species(t, y, gamma=0.1):
    return [-gamma * y[0]]

T_exp, h_values = 60, [5, 8, 11, 14, 17, 20]
t_analytical = np.linspace(0, T_exp, 300)
y_analytical = 10 * np.exp(-0.1 * t_analytical)

t_list, y_list = [], []
for h in h_values:
    t, y = forward_euler(single_species, [10.0], 0, T_exp, h)
    t_list.append(t)
    y_list.append(y[:, 0])

euler_stability(
    h_values, t_list, y_list,
    t_analytical, y_analytical,
    title="Forward Euler Stability — Aphid Decay (varying step size h)",
    save_path=os.path.join(OUT, "1_euler_stability.png"),
)


# ── 2. Two-species Lotka-Volterra ─────────────────────────────────────────────
print("2. Two-species model ...")

t, y, sol = rk45(two_species, [10.0, 10.0], 0, 60, **PARAMS_2)

time_series(
    t,
    [y[:, 0], y[:, 1]],
    labels=["Tomato plants", "Aphids"],
    colors=["#2e8b57", "#e07b39"],
    title="2-Species Lotka-Volterra: Tomato Plants vs. Aphids",
    save_path=os.path.join(OUT, "2_two_species_timeseries.png"),
)

phase_portrait(
    y[:, 0], y[:, 1],
    xlabel="Plant population", ylabel="Aphid population",
    title="Phase Portrait — Plants vs. Aphids",
    save_path=os.path.join(OUT, "3_phase_portrait.png"),
)


# ── 3. Euler vs RK45 comparison ───────────────────────────────────────────────
print("3. Euler vs RK45 ...")

t_euler, y_euler = forward_euler(two_species, [10.0, 10.0], 0, 60, h=0.05, **PARAMS_2)
t_rk, y_rk, _   = rk45(two_species, [10.0, 10.0], 0, 60, **PARAMS_2)

import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 2, figsize=(13, 4), sharey=False)
titles = ["Tomato Plants", "Aphids"]
colors_euler = ["#2e8b57", "#e07b39"]
colors_rk    = ["#145a32", "#784212"]
for i, (ax, title, ce, cr) in enumerate(zip(axes, titles, colors_euler, colors_rk)):
    ax.plot(t_euler, y_euler[:, i], color=ce, alpha=0.7, lw=1.5,
            label=f"Forward Euler (h=0.05)")
    ax.plot(t_rk,   y_rk[:, i],   color=cr, lw=2, linestyle="--",
            label="RK45 (adaptive)")
    ax.set_title(title, fontweight="bold")
    ax.set_xlabel("Time (days)")
    ax.set_ylabel("Population")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)
fig.suptitle("Forward Euler vs. RK45", fontsize=13, fontweight="bold")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "4_euler_vs_rk45.png"), dpi=150, bbox_inches="tight")
plt.close(fig)
print(f"  Saved: {os.path.join(OUT, '4_euler_vs_rk45.png')}")


# ── 4. Three-species: Plants + Aphids + Ladybugs ──────────────────────────────
print("4. Three-species model (biological control) ...")

t3, y3, sol3 = rk45(three_species, [10.0, 10.0, 10.0], 0, 60, **PARAMS_3)
t2, y2, sol2 = rk45(two_species,   [10.0, 10.0],       0, 60, **PARAMS_2)

t_dense = np.linspace(0, 60, 2000)
S_with    = np.trapz(sol3(t_dense)[0], t_dense)
S_without = np.trapz(sol2(t_dense)[0], t_dense)

three_species_panel(
    t3, y3[:, 0], y3[:, 1], y3[:, 2],
    t2, y2[:, 0], y2[:, 1],
    S_with, S_without,
    save_path=os.path.join(OUT, "5_three_species_biocontrol.png"),
)

print(f"\nResults:")
print(f"  Plant yield without ladybugs : {S_without:.1f}")
print(f"  Plant yield with ladybugs    : {S_with:.1f}")
print(f"  Improvement                  : +{((S_with - S_without) / S_without * 100):.1f}%")
print("\nAll plots saved to results/plots/")
