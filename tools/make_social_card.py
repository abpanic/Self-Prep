#!/usr/bin/env python3
"""Render assets/social-card.png, the 1200x630 image used for Open Graph / Twitter.

Regenerate with:  python tools/make_social_card.py
Committed as a PNG so the Vercel build needs nothing but Quarto.
"""
from __future__ import annotations

import pathlib

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

INK = "#2c3e50"       # navbar primary, from the cosmo theme
ACCENT = "#18bc9c"
PAPER = "#ffffff"
MUTED = "#7b8a99"

OUT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "social-card.png"

# 1200x630 is the size Open Graph and Twitter both render without cropping.
DPI = 100
fig = plt.figure(figsize=(12.0, 6.30), dpi=DPI)
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 1200)
ax.set_ylim(0, 630)
ax.axis("off")

# A single accent bar down the left, rather than a busy background.
ax.add_patch(FancyBboxPatch((0, 0), 18, 630, boxstyle="square,pad=0",
                            facecolor=ACCENT, edgecolor="none"))

ax.text(80, 522, "Self-Prep", fontsize=78, fontweight="bold", color=INK,
        va="center", ha="left")

ax.text(80, 442, "Two notebook series, zero to job-ready",
        fontsize=30, color=INK, va="center", ha="left")
ax.text(80, 398, "— and they show their working.",
        fontsize=30, color=MUTED, va="center", ha="left")

# The two series, as labelled cards.
for x, title, sub in ((80, "ML: Zero to Hero", "16 notebooks · complete"),
                      (640, "DSA: Zero to Hero", "23 notebooks · 11 built")):
    ax.add_patch(FancyBboxPatch((x, 180), 480, 132, boxstyle="round,pad=0,rounding_size=14",
                                facecolor="#f4f6f8", edgecolor="#dfe5ea", linewidth=1.5))
    ax.text(x + 32, 271, title, fontsize=30, fontweight="bold", color=INK,
            va="center", ha="left")
    ax.text(x + 32, 226, sub, fontsize=22, color=MUTED, va="center", ha="left")

ax.text(80, 96, "No claim is made that was not measured.",
        fontsize=24, color=ACCENT, fontweight="bold", va="center", ha="left")

OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT, dpi=DPI, facecolor=PAPER)
print("wrote %s (%d x %d)" % (OUT, 12.0 * DPI, 6.30 * DPI))
