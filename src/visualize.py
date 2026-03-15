"""
Plotting helpers for the population dynamics simulations.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

COLORS = {
    "plants":   "#2e8b57",   # sea green
    "aphids":   "#e07b39",   # burnt orange
    "ladybugs": "#c0392b",   # crimson
    "euler":    "#e74c3c",
    "rk45":     "#2980b9",
    "analytical": "#2c3e50",
}


def time_series(t, populations, labels, colors, title, xlabel="Time (days)",
                ylabel="Population", save_path=None):
    """Plot one or more population time series on a single axes."""
    fig, ax = plt.subplots(figsize=(12, 5))
    for pop, label, color in zip(populations, labels, colors):
        ax.plot(t, pop, label=label, color=color, linewidth=2)
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend(framealpha=0.9)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")
        print(f"  Saved: {save_path}")
    plt.close(fig)


def phase_portrait(x, y, xlabel, ylabel, title, save_path=None):
    """Plot a 2D phase portrait (x vs y) with a direction arrow."""
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(x, y, color=COLORS["plants"], linewidth=1.5, alpha=0.85)
    ax.plot(x[0], y[0], "o", color="black", markersize=7, label="Start", zorder=5)
    ax.plot(x[-1], y[-1], "s", color="grey", markersize=7, label="End", zorder=5)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.legend(framealpha=0.9)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")
        print(f"  Saved: {save_path}")
    plt.close(fig)


def euler_stability(h_values, t_euler_list, y_euler_list, t_analytical, y_analytical,
                    title, save_path=None):
    """Show Forward Euler solutions for several step sizes vs. the analytical solution."""
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(t_analytical, y_analytical, color=COLORS["analytical"],
            linestyle="--", linewidth=2, label="Analytical solution")
    cmap = plt.cm.plasma
    for i, (h, t, y) in enumerate(zip(h_values, t_euler_list, y_euler_list)):
        c = cmap(i / max(len(h_values) - 1, 1))
        ax.plot(t, y, color=c, marker="o", markersize=3, label=f"Euler h={h}")
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_xlabel("Time (days)")
    ax.set_ylabel("Population")
    ax.legend(framealpha=0.9, fontsize=9)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")
        print(f"  Saved: {save_path}")
    plt.close(fig)


def three_species_panel(t, plants, aphids, ladybugs,
                        t_no_bug, plants_no_bug, aphids_no_bug,
                        S_with, S_without, save_path=None):
    """
    Two-panel figure:
      Left  — 3-species trajectories (plants / aphids / ladybugs)
      Right — plant yield comparison (with vs. without ladybugs)
    """
    fig = plt.figure(figsize=(14, 5))
    gs  = gridspec.GridSpec(1, 2, width_ratios=[3, 2])

    # Left: time series
    ax1 = fig.add_subplot(gs[0])
    ax1.plot(t, plants,   color=COLORS["plants"],   linewidth=2, label="Plants")
    ax1.plot(t, aphids,   color=COLORS["aphids"],   linewidth=2, label="Aphids")
    ax1.plot(t, ladybugs, color=COLORS["ladybugs"], linewidth=2, label="Ladybugs")
    ax1.set_title("3-Species Dynamics: Plants, Aphids & Ladybugs",
                  fontsize=13, fontweight="bold")
    ax1.set_xlabel("Time (days)")
    ax1.set_ylabel("Population")
    ax1.legend(framealpha=0.9)
    ax1.grid(alpha=0.3)

    # Right: bar chart of plant yield (integral)
    ax2 = fig.add_subplot(gs[1])
    bars = ax2.bar(["Without\nLadybugs", "With\nLadybugs"],
                   [S_without, S_with],
                   color=[COLORS["aphids"], COLORS["plants"]],
                   width=0.5, edgecolor="white", linewidth=1.2)
    ax2.set_title("Total Plant Yield (S)", fontsize=13, fontweight="bold")
    ax2.set_ylabel("∫ Plants dt  (population·days)")
    for bar, val in zip(bars, [S_without, S_with]):
        ax2.text(bar.get_x() + bar.get_width() / 2, val + 5,
                 f"{val:.0f}", ha="center", va="bottom", fontsize=11)
    improvement = ((S_with - S_without) / S_without) * 100
    ax2.set_ylim(0, max(S_with, S_without) * 1.2)
    ax2.annotate(f"+{improvement:.1f}%", xy=(1, S_with),
                 xytext=(0.5, (S_with + S_without) / 2),
                 fontsize=11, color=COLORS["plants"],
                 arrowprops=dict(arrowstyle="-", color="grey"))
    ax2.grid(axis="y", alpha=0.3)

    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")
        print(f"  Saved: {save_path}")
    plt.close(fig)
