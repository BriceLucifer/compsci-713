#!/usr/bin/env python3
"""
COMPSCI 713 AI Fundamentals — Exam Visualization Suite
Run from repo root: uv run python exam/visualize_713.py
Outputs:  exam/src/chapters/figures/*.png  (11 figures)
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

# ── Output directory ────────────────────────────────────────
FIGURES_DIR = os.path.join(os.path.dirname(__file__), "src", "chapters", "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)

# matplotlib FancyBboxPatch expects ((x,y), w, h, ...) — this helper normalises the call
def fbp(x, y, w, h, **kw):
    return FancyBboxPatch((x, y), w, h, **kw)


plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "figure.facecolor": "white",
    "axes.spines.top": False,
    "axes.spines.right": False,
})


def save(name: str) -> None:
    path = os.path.join(FIGURES_DIR, f"{name}.png")
    plt.savefig(path, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close()
    print(f"  ✓  {name}.png")


# ═══════════════════════════════════════════════════════════
# Figure 01 — Exam Topic Weight Distribution
# ═══════════════════════════════════════════════════════════
def fig_topic_weights():
    topics = [
        "E — MYCIN (unlisted)",
        "C — Knowledge Rep. (unlisted)",
        "H — Multi-Agent Systems",
        "D — Knowledge Graphs",
        "F — Decision Trees & Ensembles",
        "G — Soft Computing\n(Fuzzy + Bayesian)",
        "B — Logic Neural Networks",
        "A — Symbolic Logic\n(Propositional + FOL)",
    ]
    weights   = [0, 0, 10, 10, 15, 20, 20, 25]
    colors    = ["#f1c40f", "#f1c40f", "#e67e22", "#e67e22",
                 "#e74c3c", "#e74c3c", "#e74c3c", "#e74c3c"]
    hatches   = ["///", "///", "", "", "", "", "", ""]

    fig, ax = plt.subplots(figsize=(12, 6))

    bars = ax.barh(topics, weights, color=colors, edgecolor="white",
                   height=0.6, linewidth=1.5)
    for bar, hatch in zip(bars, hatches):
        bar.set_hatch(hatch)

    for bar, w, topic in zip(bars, weights, topics):
        if w > 0:
            ax.text(bar.get_width() + 0.4, bar.get_y() + bar.get_height() / 2,
                    f"{w}%", va="center", fontsize=12, fontweight="bold",
                    color="#2c3e50")
        else:
            ax.text(0.5, bar.get_y() + bar.get_height() / 2,
                    "Not in sample — but full lecture devoted → likely testable!",
                    va="center", fontsize=8.5, color="#e67e22", style="italic")

    legend_elements = [
        mpatches.Patch(color="#e74c3c", label="[RED] Must-Know (≥15%)"),
        mpatches.Patch(color="#e67e22", label="[ORG] High Freq (10–14%)"),
        mpatches.Patch(color="#f1c40f", label="[YEL] Medium (unlisted in sample)"),
    ]
    ax.legend(handles=legend_elements, loc="lower right", fontsize=10,
              framealpha=0.9)

    ax.set_xlabel("Mark Weight in Sample Test (%)", fontsize=12)
    ax.set_title(
        "COMPSCI 713 — Exam Topic Priority Map\n"
        "(Sample Test S1 2026 · 20 marks total · 6 questions)",
        fontsize=13, fontweight="bold", pad=12)
    ax.set_xlim(0, 32)
    ax.axvline(15, color="gray", linestyle="--", alpha=0.35, linewidth=1)
    ax.grid(axis="x", alpha=0.25)

    save("01_topic_weights")


# ═══════════════════════════════════════════════════════════
# Figure 02 — Propositional Logic Truth Tables
# ═══════════════════════════════════════════════════════════
def fig_truth_table():
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

    # ── Left: full connectives table ──
    ax = axes[0]
    ax.axis("off")

    P = [0, 0, 1, 1]
    Q = [0, 1, 0, 1]
    data = [
        [p, q, 1 - p, p & q, p | q, (1 - p) | q, 1 - (p ^ q)]
        for p, q in zip(P, Q)
    ]
    headers = ["P", "Q", "¬P", "P∧Q", "P∨Q", "P→Q", "P↔Q"]

    cell_colors = []
    for row in data:
        cell_colors.append(
            ["#d5e8d4" if v == 1 else "#f8cecc" for v in row])

    tbl = ax.table(cellText=data, colLabels=headers,
                   cellLoc="center", loc="center",
                   cellColours=cell_colors)
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(13)
    tbl.scale(1.15, 2.2)
    ax.set_title(
        "All Propositional Connectives\n(Green = TRUE  |  Red = FALSE)",
        fontsize=12, fontweight="bold", pad=20)

    # ── Right: implication trap ──
    ax2 = axes[1]
    ax2.axis("off")

    trap_headers = ["P", "Q", "P→Q", "Interpretation"]
    trap_data = [
        ["T", "T", "T", "✓  Rule holds normally"],
        ["T", "F", "F", "✗  Rule BROKEN — only false row!"],
        ["F", "T", "T", "✓  Vacuously true (premise false)"],
        ["F", "F", "T", "✓  Vacuously true (premise false)"],
    ]
    trap_colors = [
        ["#d5e8d4"] * 3 + ["#d5e8d4"],
        ["#f8cecc"] * 3 + ["#f8cecc"],
        ["#fff2cc"] * 3 + ["#fff2cc"],
        ["#fff2cc"] * 3 + ["#fff2cc"],
    ]

    tbl2 = ax2.table(cellText=trap_data, colLabels=trap_headers,
                     cellLoc="center", loc="center",
                     cellColours=trap_colors)
    tbl2.auto_set_font_size(False)
    tbl2.set_fontsize(11)
    tbl2.scale(1.15, 2.4)
    ax2.set_title(
        "⚠️  Implication Exam Trap (P → Q)\n"
        "The ONLY false row is: P=T, Q=F",
        fontsize=12, fontweight="bold", color="#c0392b", pad=20)

    plt.suptitle("Module A — Symbolic Logic: Truth Tables",
                 fontsize=14, fontweight="bold")
    plt.tight_layout()
    save("02_truth_table")


# ═══════════════════════════════════════════════════════════
# Figure 03 — LNN T-norms Comparison
# ═══════════════════════════════════════════════════════════
def fig_lnn_tnorms():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    a = np.linspace(0, 1, 300)
    b = 0.7          # fix b, vary a
    # exam example from Q2(b)
    a_ex, b_ex = 0.4, 0.9

    specs = [
        ("Product",      "a ⊗ b = a × b",              a * b,
         "#3498db",  a_ex * b_ex,        "#3498db"),
        ("Lukasiewicz",  "a ⊗ b = max(0, a+b−1)",       np.maximum(0, a + b - 1),
         "#27ae60",  max(0, a_ex + b_ex - 1), "#27ae60"),
        ("Gödel (min)",  "a ⊗ b = min(a, b)",            np.minimum(a, b),
         "#9b59b6",  min(a_ex, b_ex),    "#9b59b6"),
    ]

    for ax, (name, formula, values, color, ex_val, ec) in zip(axes, specs):
        ax.plot(a, values, color=color, linewidth=2.5)
        ax.fill_between(a, values, alpha=0.12, color=color)

        # mark exam example
        ax.scatter([a_ex], [ex_val], color="red", s=100, zorder=6)
        ax.annotate(
            f"Q2 example:\nCold={b_ex}, AtHome={a_ex}\n→ {ex_val:.2f}",
            xy=(a_ex, ex_val), xytext=(0.55, ex_val + 0.25),
            arrowprops=dict(arrowstyle="->", color="red"),
            color="red", fontsize=8.5)

        # Boolean AND for reference
        bool_val = 1 if (a_ex >= 0.5 and b_ex >= 0.5) else 0
        ax.scatter([a_ex], [bool_val], color="gray", s=80, zorder=5,
                   marker="D", label=f"Boolean AND = {bool_val}")
        ax.legend(fontsize=8)

        ax.set_title(f"{name}\n{formula}", fontweight="bold", fontsize=11)
        ax.set_xlabel("a (truth value)")
        ax.set_ylabel(f"AND(a, b={b})")
        ax.set_xlim(0, 1); ax.set_ylim(-0.05, 1.05)
        ax.grid(alpha=0.3)

    plt.suptitle(
        "Module B — LNN: Three T-norms for Soft Conjunction\n"
        "(All equal Boolean AND at {0, 1} endpoints — gradients enable learning)",
        fontsize=12, fontweight="bold")
    plt.tight_layout()
    save("03_lnn_tnorms")


# ═══════════════════════════════════════════════════════════
# Figure 04 — Fuzzy Logic: Membership Functions & Operations
# ═══════════════════════════════════════════════════════════
def fig_fuzzy():
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    heights = np.linspace(140, 220, 400)

    def trapezoid(x, a, b, c, d):
        mu = np.zeros_like(x, dtype=float)
        mask1 = (x >= a) & (x < b)
        mask2 = (x >= b) & (x <= c)
        mask3 = (x > c) & (x <= d)
        mu[mask1] = (x[mask1] - a) / (b - a)
        mu[mask2] = 1.0
        mu[mask3] = (d - x[mask3]) / (d - c)
        return mu

    mu_short  = trapezoid(heights, 140, 140, 155, 168)
    mu_medium = trapezoid(heights, 155, 165, 175, 185)
    mu_tall   = trapezoid(heights, 170, 185, 210, 220)

    # ── Left: three fuzzy sets ──
    ax1 = axes[0]
    ax1.plot(heights, mu_short,  "b-", lw=2, label="Short")
    ax1.plot(heights, mu_medium, "g-", lw=2, label="Medium")
    ax1.plot(heights, mu_tall,   "r-", lw=2, label="Tall")

    x_pt = np.array([183.0])
    mu_pt = trapezoid(x_pt, 170, 185, 210, 220)[0]
    ax1.axvline(183, color="gray", linestyle="--", alpha=0.7)
    ax1.scatter([183], [mu_pt], color="red", s=100, zorder=6)
    ax1.annotate(
        f"μ_Tall(183cm) ≈ {mu_pt:.2f}\n≠ 'probability' — it's\na degree of membership!",
        xy=(183, mu_pt), xytext=(195, 0.55),
        arrowprops=dict(arrowstyle="->", color="darkred"),
        color="darkred", fontsize=8.5)

    ax1.set_xlabel("Height (cm)"); ax1.set_ylabel("Membership degree μ")
    ax1.set_title("Fuzzy Sets: Height Linguistic Variables", fontweight="bold")
    ax1.legend(); ax1.grid(alpha=0.3); ax1.set_ylim(-0.05, 1.15)

    # ── Middle: fuzzy operations ──
    ax2 = axes[1]
    mu_A, mu_B = 0.8, 0.7   # high_temp, high_humidity
    labels = ["μ_A\n(temp=0.8)", "μ_B\n(humidity=0.7)",
              "A AND B\nmin(A,B)", "A OR B\nmax(A,B)", "NOT A\n1−A"]
    values = [mu_A, mu_B, min(mu_A, mu_B), max(mu_A, mu_B), 1 - mu_A]
    bar_colors = ["#3498db", "#27ae60", "#e74c3c", "#9b59b6", "#f39c12"]

    bars = ax2.bar(labels, values, color=bar_colors, edgecolor="white", width=0.6)
    for bar, val in zip(bars, values):
        ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02,
                 f"{val:.1f}", ha="center", fontsize=13, fontweight="bold")
    ax2.axhline(0.5, color="gray", linestyle="--", alpha=0.5, label="0.5 threshold")
    ax2.set_ylim(0, 1.2); ax2.set_ylabel("Truth degree")
    ax2.set_title("Fuzzy Operations\n(μ_A=0.8 high temp, μ_B=0.7 high humidity)",
                  fontweight="bold")
    ax2.legend(fontsize=9); ax2.grid(axis="y", alpha=0.3)

    # ── Right: crisp vs fuzzy comparison ──
    ax3 = axes[2]
    h_pts = [165, 175, 183, 195, 205]
    crisp = [0, 1, 1, 1, 1]          # hard cutoff at 175
    fuzzy_t = [trapezoid(np.array([float(h)]), 170, 185, 210, 220)[0] for h in h_pts]

    x = np.arange(len(h_pts))
    w = 0.35
    ax3.bar(x - w/2, crisp,   w, label="Crisp (≥175 → 'tall')", color="#e74c3c", alpha=0.8)
    ax3.bar(x + w/2, fuzzy_t, w, label='Fuzzy degree "Tall"',    color="#3498db", alpha=0.8)
    ax3.set_xticks(x); ax3.set_xticklabels([f"{h}cm" for h in h_pts])
    ax3.set_ylabel("Value"); ax3.set_ylim(0, 1.25)
    ax3.set_title("Crisp vs Fuzzy Classification\n(Same data, richer representation)",
                  fontweight="bold")
    ax3.legend(fontsize=9); ax3.grid(axis="y", alpha=0.3)

    plt.suptitle("Module G — Fuzzy Logic: Membership Functions & Operations",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    save("04_fuzzy_logic")


# ═══════════════════════════════════════════════════════════
# Figure 05 — Vagueness vs Uncertainty (Q6 exam pattern)
# ═══════════════════════════════════════════════════════════
def fig_vagueness_uncertainty():
    fig, ax = plt.subplots(figsize=(15, 7.5))
    ax.set_xlim(0, 15); ax.set_ylim(0, 7.5)
    ax.axis("off")

    ax.text(7.5, 7.15,
            "Vagueness vs Uncertainty — The Core Distinction (Q6 type: 4 marks)",
            ha="center", fontsize=14, fontweight="bold", color="#2c3e50")

    # ── Vagueness column ──
    ax.add_patch(fbp(0.25, 0.3, 6.0, 6.4,
                               boxstyle="round,pad=0.1",
                               facecolor="#ffeaa7", edgecolor="#f39c12", linewidth=2.5))
    ax.text(3.25, 6.45, "VAGUENESS  ((Vagueness))",
            ha="center", fontsize=14, fontweight="bold", color="#e67e22")

    vague_rows = [
        ("Question →",   "To what DEGREE is this true?"),
        ("Source →",     "The CONCEPT has blurry edges"),
        ("Tool →",       "Fuzzy Logic — μ ∈ [0, 1]"),
        ("Output →",     "Degree of membership (not prob.)"),
        ("Cue words →",  '"high risk"  "warm"  "tall"  "almost"'),
        ("Q6 Example 1 →", '"High risk" — blurry concept → Vagueness'),
        ("Q6 Example 3 →", '"Almost excellent" — graded concept → Vagueness'),
    ]
    for i, (label, text) in enumerate(vague_rows):
        y = 5.7 - i * 0.75
        ax.text(0.55, y, label, fontsize=9, fontweight="bold", color="#7d6608")
        ax.text(0.55, y - 0.32, text, fontsize=9, color="#333")

    # ── Uncertainty column ──
    ax.add_patch(fbp(8.75, 0.3, 6.0, 6.4,
                               boxstyle="round,pad=0.1",
                               facecolor="#dfe6e9", edgecolor="#636e72", linewidth=2.5))
    ax.text(11.75, 6.45, "UNCERTAINTY  ((Uncertainty))",
            ha="center", fontsize=14, fontweight="bold", color="#2c3e50")

    uncertain_rows = [
        ("Question →",   "How LIKELY is this true?"),
        ("Source →",     "Our KNOWLEDGE is incomplete"),
        ("Tool →",       "Bayesian Reasoning — P ∈ [0, 1]"),
        ("Output →",     "Probability (there is a fact we don't know)"),
        ("Cue words →",  '"classifying"  "inferring"  "predicting class"'),
        ("Q6 Example 2 →", '"Did a burglary happen?" — unknown fact → Uncertainty'),
        ("Q6 Example 4 →", '"Inferring class from evidence" → Uncertainty'),
    ]
    for i, (label, text) in enumerate(uncertain_rows):
        y = 5.7 - i * 0.75
        ax.text(9.05, y, label, fontsize=9, fontweight="bold", color="#2c3e50")
        ax.text(9.05, y - 0.32, text, fontsize=9, color="#333")

    # ── Middle VS badge ──
    circle = plt.Circle((7.5, 3.5), 0.85, color="white", ec="#bdc3c7", lw=2, zorder=3)
    ax.add_patch(circle)
    ax.text(7.5, 3.5, "VS", ha="center", va="center",
            fontsize=20, fontweight="bold", color="#7f8c8d", zorder=4)

    # ── Common trap ──
    ax.text(7.5, 0.6,
            "⚠️  Both use [0, 1] scale — but meaning differs:\n"
            "Fuzzy 0.6 = '60% of the concept applies'   |   "
            "Bayesian 0.6 = '60% probability the fact is true'",
            ha="center", fontsize=9.5, color="#c0392b", fontweight="bold",
            bbox=dict(boxstyle="round", facecolor="white", edgecolor="#c0392b", alpha=0.9))

    save("05_vagueness_uncertainty")


# ═══════════════════════════════════════════════════════════
# Figure 06 — Entropy & Information Gain
# ═══════════════════════════════════════════════════════════
def fig_entropy():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

    # ── Left: binary entropy curve ──
    ax1 = axes[0]
    p = np.linspace(0.001, 0.999, 500)
    H = -p * np.log2(p) - (1 - p) * np.log2(1 - p)

    ax1.plot(p, H, color="#2980b9", linewidth=2.5)
    ax1.fill_between(p, H, alpha=0.12, color="#2980b9")

    ax1.scatter([0.5], [1.0], color="red", s=100, zorder=6)
    ax1.annotate(
        "H(0.5) = 1.0 bit\n(maximum uncertainty\n= 50/50 split)",
        xy=(0.5, 1.0), xytext=(0.63, 0.82),
        arrowprops=dict(arrowstyle="->", color="red"), color="red", fontsize=9)

    ax1.scatter([0.0, 1.0], [0.0, 0.0], color="#27ae60", s=100, zorder=6)
    ax1.annotate(
        "H(0) = H(1) = 0\n(pure class\n= no uncertainty)",
        xy=(0.05, 0.0), xytext=(0.15, 0.3),
        arrowprops=dict(arrowstyle="->", color="#27ae60"),
        color="#27ae60", fontsize=9)

    ax1.set_xlabel("p  (proportion of positive class)", fontsize=11)
    ax1.set_ylabel("H(p)  —  Entropy (bits)", fontsize=11)
    ax1.set_title(
        "Binary Entropy Function\nH(p) = −p·log₂(p) − (1−p)·log₂(1−p)",
        fontweight="bold")
    ax1.grid(alpha=0.3); ax1.set_xlim(0, 1); ax1.set_ylim(0, 1.15)

    # ── Right: IG worked example ──
    ax2 = axes[1]
    ax2.axis("off"); ax2.set_xlim(0, 10); ax2.set_ylim(0, 10)

    ax2.text(5, 9.6, "Information Gain — Step-by-Step",
             ha="center", fontsize=12, fontweight="bold")

    # Parent: 5 pos, 5 neg
    H_parent = 1.0
    # After split: left=4pos/0neg, right=1pos/5neg
    H_left  = 0.0
    H_right = -(1/6)*np.log2(1/6) - (5/6)*np.log2(5/6)
    H_after = (4/10)*H_left + (6/10)*H_right
    IG      = H_parent - H_after

    rows = [
        ("#dae8fc", "Parent node",
         f"10 samples: 5⊕  5⊖  →  H = {H_parent:.3f} bits"),
        ("white",   "━━ split on Feature X ━━", ""),
        ("#d5e8d4", "Left branch  (4 samples)",
         f"4⊕  0⊖  →  H = {H_left:.3f}  (perfectly pure!)"),
        ("#ffe6cc", "Right branch (6 samples)",
         f"1⊕  5⊖  →  H = {H_right:.3f}"),
        ("white",   "", ""),
        ("#fef9e7", "Weighted H after split",
         f"4/10 × 0 + 6/10 × {H_right:.3f} = {H_after:.3f}"),
        ("#e1d5e7", "Information Gain  IG",
         f"H_parent − H_after = {H_parent:.3f} − {H_after:.3f} = {IG:.3f} bits"),
        ("white",   "", ""),
        ("#d5e8d4", "Decision",
         "Pick the feature with the HIGHEST IG at each node!"),
    ]

    y = 8.9
    for fc, label, val in rows:
        if label:
            ax2.add_patch(fbp(0.05, y - 0.5, 9.9, 0.65,
                                        boxstyle="round,pad=0.05",
                                        facecolor=fc, edgecolor="#ccc", linewidth=0.5))
            ax2.text(0.3, y - 0.12, label, fontsize=9.5, fontweight="bold", va="center")
            ax2.text(3.5, y - 0.12, val,   fontsize=9,   va="center", color="#1a5276")
        y -= 0.9

    plt.suptitle("Module F — Decision Trees: Entropy & Information Gain",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    save("06_entropy_infogain")


# ═══════════════════════════════════════════════════════════
# Figure 07 — Bagging vs Boosting
# ═══════════════════════════════════════════════════════════
def fig_bagging_boosting():
    fig, axes = plt.subplots(1, 2, figsize=(16, 8))

    for ax in axes:
        ax.set_xlim(0, 10); ax.set_ylim(0, 10)
        ax.axis("off")

    def box(ax, x, y, w, h, fc, ec, text, fontsize=9, bold=False):
        ax.add_patch(fbp(x, y, w, h,
                                   boxstyle="round,pad=0.1",
                                   facecolor=fc, edgecolor=ec, linewidth=2))
        ax.text(x + w/2, y + h/2, text,
                ha="center", va="center", fontsize=fontsize,
                fontweight="bold" if bold else "normal",
                multialignment="center")

    def arrow(ax, x1, y1, x2, y2, label="", color="gray"):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", color=color, lw=1.8))
        if label:
            mx, my = (x1 + x2)/2, (y1 + y2)/2
            ax.text(mx + 0.15, my, label, fontsize=8, color=color)

    # ── BAGGING ──
    ax1 = axes[0]
    ax1.text(5, 9.7, "BAGGING  (Bootstrap Aggregating)",
             ha="center", fontsize=13, fontweight="bold", color="#2980b9")
    ax1.text(5, 9.25, "e.g., Random Forest  |  PARALLEL  |  reduces VARIANCE",
             ha="center", fontsize=9.5, color="#7f8c8d")

    box(ax1, 3.0, 8.0, 4.0, 0.9, "#d6eaf8", "#2980b9",
        "Original Dataset (n samples)", 9.5, True)

    for i, (x, lbl) in enumerate([(0.5, "Bootstrap\nSample 1"),
                                   (3.8, "Bootstrap\nSample 2"),
                                   (7.1, "Bootstrap\nSample 3")]):
        arrow(ax1, 5, 8.0, x + 0.8, 6.9, color="#2980b9")
        box(ax1, x, 6.1, 1.6, 0.85, "#aed6f1", "#2980b9", lbl, 8)
        arrow(ax1, x + 0.8, 6.1, x + 0.8, 5.25, color="#27ae60")
        box(ax1, x, 4.4, 1.6, 0.85, "#a9dfbf", "#27ae60",
            f"Tree {i+1}\n(full depth)", 8)

    ax1.text(5, 3.9, "↓  all independent  ↓", ha="center", fontsize=9, color="#7f8c8d")
    box(ax1, 2.5, 2.9, 5.0, 0.85, "#d5f5e3", "#27ae60",
        "VOTE / AVERAGE  →  Final Prediction", 10, True)

    ax1.text(5, 2.2,
             "✅  Lower VARIANCE  |  No sequential dependency\n"
             "✅  Feature bagging (√p features/split) decorrelates trees",
             ha="center", fontsize=9, color="#1a5276",
             bbox=dict(boxstyle="round", facecolor="#d6eaf8", alpha=0.85))

    # ── BOOSTING ──
    ax2 = axes[1]
    ax2.text(5, 9.7, "BOOSTING  (AdaBoost)",
             ha="center", fontsize=13, fontweight="bold", color="#c0392b")
    ax2.text(5, 9.25, "SEQUENTIAL  |  each round corrects the last  |  reduces BIAS",
             ha="center", fontsize=9.5, color="#7f8c8d")

    rounds = [
        (8.0, "#fadbd8", "#e74c3c",   "Round 1  Weak Learner\n(equal sample weights)"),
        (6.1, "#fad7a0", "#e67e22",   "Round 2  Weak Learner\n(upweight R1 errors)"),
        (4.2, "#a9dfbf", "#27ae60",   "Round 3  Weak Learner\n(upweight R2 errors)"),
    ]
    for y, fc, ec, lbl in rounds:
        box(ax2, 2.0, y - 0.65, 6.0, 1.05, fc, ec, lbl, 9)

    arrow(ax2, 5, 7.35, 5, 6.75, "reweight errors →", "#c0392b")
    arrow(ax2, 5, 5.45, 5, 4.85, "reweight errors →", "#c0392b")

    box(ax2, 2.0, 3.0, 6.0, 1.0, "#fadbd8", "#c0392b",
        "Weighted sum:  α₁h₁ + α₂h₂ + α₃h₃\n(α = learner confidence)", 9)
    arrow(ax2, 5, 3.0, 5, 2.3, color="gray")
    box(ax2, 2.5, 1.4, 5.0, 0.9, "#c0392b", "#922b21",
        "Final Prediction  (sign of weighted sum)", 10, True)

    ax2.text(5, 0.75,
             "✅  Lower BIAS  |  Focuses on hard examples\n"
             "⚠️  Sequential → cannot parallelise",
             ha="center", fontsize=9, color="#78281f",
             bbox=dict(boxstyle="round", facecolor="#fadbd8", alpha=0.85))

    plt.suptitle("Module F — Ensemble: Bagging vs Boosting",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    save("07_bagging_boosting")


# ═══════════════════════════════════════════════════════════
# Figure 08 — Bayes Theorem & Naïve Bayes
# ═══════════════════════════════════════════════════════════
def fig_bayes():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6.5))

    # ── Left: Bayes formula + base-rate example ──
    ax1 = axes[0]
    ax1.axis("off"); ax1.set_xlim(0, 10); ax1.set_ylim(0, 10)

    ax1.text(5, 9.6, "Bayes' Theorem — Formula Breakdown",
             ha="center", fontsize=12, fontweight="bold")

    # formula box
    ax1.add_patch(fbp(0.4, 7.8, 9.2, 1.5,
                                boxstyle="round,pad=0.1",
                                facecolor="#dae8fc", edgecolor="#2980b9", linewidth=2))
    ax1.text(5, 8.85, "P(H | e)  =  P(e | H) × P(H)  ÷  P(e)",
             ha="center", fontsize=13, fontweight="bold", color="#1a5276")
    ax1.text(5, 8.2, "Posterior  =  Likelihood  ×  Prior  ÷  Marginal",
             ha="center", fontsize=10, color="#555")

    parts = [
        (1.5, 6.2, "#e8f8f5", "#1e8449",  "P(H)",    "PRIOR",       "Before evidence\n= 0.001"),
        (4.5, 6.2, "#fef9e7", "#f39c12",  "P(e|H)",  "LIKELIHOOD",  "Evidence if H true\n= 0.95"),
        (7.5, 6.2, "#fdedec", "#c0392b",  "P(e)",    "MARGINAL",    "Total evidence\n= 0.0594"),
        (5.0, 4.0, "#e8daef", "#6c3483",  "P(H|e)",  "POSTERIOR",   "Updated belief\n≈ 0.016"),
    ]
    for x, y, fc, ec, sym, name, val in parts:
        ax1.add_patch(fbp(x-1.2, y-0.65, 2.4, 1.45,
                                   boxstyle="round,pad=0.1",
                                   facecolor=fc, edgecolor=ec, linewidth=2))
        ax1.text(x, y + 0.52, sym,  ha="center", fontsize=13, fontweight="bold", color=ec)
        ax1.text(x, y + 0.08, name, ha="center", fontsize=8,  color="#555")
        ax1.text(x, y - 0.38, val,  ha="center", fontsize=8.5, color=ec, fontweight="bold")

    ax1.annotate("", xy=(5, 4.8), xytext=(5, 5.65),
                arrowprops=dict(arrowstyle="->", color="purple", lw=2))

    ax1.text(5, 2.6,
             "Medical test example (disease prevalence 0.1%)\n"
             "Sensitivity 95%  ·  False positive 5%\n"
             "Even with a positive test, P(disease | +) ≈ 1.6%\n"
             "→ Base Rate Fallacy: low prior dominates!",
             ha="center", fontsize=9, color="#333",
             bbox=dict(boxstyle="round", facecolor="#fdfefe", edgecolor="#bdc3c7"))

    # ── Right: Naïve Bayes spam example ──
    ax2 = axes[1]
    ax2.axis("off"); ax2.set_xlim(0, 10); ax2.set_ylim(0, 10)

    ax2.text(5, 9.6, "Naïve Bayes — Email Spam Example",
             ha="center", fontsize=12, fontweight="bold")

    ax2.add_patch(fbp(0.3, 8.3, 9.4, 0.9,
                                boxstyle="round,pad=0.1",
                                facecolor="#fef9e7", edgecolor="#f39c12", linewidth=2))
    ax2.text(5, 8.75, 'Email contains: "Free"  "Win"  "Click" — Spam or Ham?',
             ha="center", fontsize=10.5, fontweight="bold")

    features = [
        ('Word: "Free"',  "P(free | spam)=0.90", "P(free | ham)=0.10"),
        ('Word: "Win"',   "P(win  | spam)=0.80", "P(win  | ham)=0.05"),
        ('Word: "Click"', "P(click| spam)=0.70", "P(click| ham)=0.20"),
    ]
    for i, (feat, spam_p, ham_p) in enumerate(features):
        y = 7.4 - i * 0.85
        ax2.add_patch(fbp(0.3, y - 0.35, 9.4, 0.7,
                                    boxstyle="round,pad=0.05",
                                    facecolor="#fdfefe", edgecolor="#bdc3c7", linewidth=1))
        ax2.text(0.7, y, feat,   fontsize=9,  fontweight="bold", va="center")
        ax2.text(4.5, y, spam_p, fontsize=9,  color="#c0392b",   va="center")
        ax2.text(7.2, y, ham_p,  fontsize=9,  color="#27ae60",   va="center")

    ax2.text(5, 4.55,
             "P(spam)·0.90·0.80·0.70 = 0.5 × 0.504 = 0.252",
             ha="center", fontsize=9.5, color="#c0392b",
             bbox=dict(boxstyle="round", facecolor="#fdedec", alpha=0.85))
    ax2.text(5, 3.8,
             "P(ham) ·0.10·0.05·0.20 = 0.5 × 0.001 = 0.0005",
             ha="center", fontsize=9.5, color="#27ae60",
             bbox=dict(boxstyle="round", facecolor="#e8f8f5", alpha=0.85))
    ax2.text(5, 3.1, "→  spam score >> ham score  →  CLASSIFY as SPAM ✉️",
             ha="center", fontsize=11, fontweight="bold", color="#c0392b")

    ax2.add_patch(fbp(0.4, 1.4, 9.2, 1.35,
                                boxstyle="round,pad=0.1",
                                facecolor="#fff2cc", edgecolor="#f39c12", linewidth=2))
    ax2.text(5, 2.4, "⚠️  'Naïve' assumption: all features are INDEPENDENT",
             ha="center", fontsize=10, fontweight="bold", color="#e67e22")
    ax2.text(5, 1.85,
             "P(free, win, click | C) ≈ P(free|C) × P(win|C) × P(click|C)",
             ha="center", fontsize=9, color="#555")

    plt.suptitle("Module G — Bayesian Reasoning: Bayes Theorem & Naïve Bayes",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    save("08_bayes_naive_bayes")


# ═══════════════════════════════════════════════════════════
# Figure 09 — TransE Knowledge Graph Embedding
# ═══════════════════════════════════════════════════════════
def fig_transe():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # ── Left: 2D vector space ──
    ax1 = axes[0]
    ax1.set_xlim(-0.5, 5); ax1.set_ylim(-0.5, 5)
    ax1.grid(alpha=0.3); ax1.set_facecolor("#f8f9fa")

    entities = {
        "Einstein":   np.array([0.5, 0.8]),
        "Germany":    np.array([3.2, 2.1]),
        "Berlin":     np.array([3.5, 0.6]),
        "Relativity": np.array([1.0, 3.5]),
    }
    for name, pos in entities.items():
        ax1.scatter(*pos, s=220, zorder=5, color="#3498db", edgecolors="white", lw=2)
        ax1.annotate(name, pos, textcoords="offset points",
                    xytext=(8, 6), fontsize=11, fontweight="bold", color="#1a5276")

    # bornIn: Einstein → Germany
    h = entities["Einstein"]; t = entities["Germany"]
    ax1.annotate("", xy=t, xytext=h,
                arrowprops=dict(arrowstyle="-|>", color="#e74c3c", lw=2.5))
    mid = (h + t) / 2
    ax1.text(mid[0] - 0.2, mid[1] + 0.2, "bornIn",
             fontsize=11, color="#e74c3c", fontweight="bold")

    # capitalOf: Germany → Berlin (dotted, example)
    h2 = entities["Berlin"]
    ax1.annotate("", xy=entities["Germany"], xytext=h2,
                arrowprops=dict(arrowstyle="-|>", color="#9b59b6", lw=1.5,
                                linestyle="dashed"))
    ax1.text(3.55, 1.4, "capitalOf?", fontsize=9, color="#9b59b6")

    ax1.text(0.0, 4.7, "TransE:  h + r ≈ t",
             fontsize=13, fontweight="bold", color="#c0392b",
             bbox=dict(boxstyle="round", facecolor="#fadbd8", alpha=0.85))
    ax1.text(0.0, 4.2, "Einstein + bornIn ≈ Germany",
             fontsize=10, color="#555")
    ax1.set_title("KG Embeddings — Entities & Relations as Vectors",
                  fontweight="bold")
    ax1.set_xlabel("Embedding dim 1"); ax1.set_ylabel("Embedding dim 2")

    # ── Right: inference tasks table ──
    ax2 = axes[1]
    ax2.axis("off"); ax2.set_xlim(0, 10); ax2.set_ylim(0, 10)

    ax2.text(5, 9.6, "KGE Inference Tasks & TransE Limitation",
             ha="center", fontsize=12, fontweight="bold")

    tasks = [
        (8.0, "#dae8fc", "#2980b9",
         "Link Prediction  (h, r, ?)  ←— Most tested!",
         "Find the TAIL entity.\n(Einstein, bornIn, ?)  →  Germany\n"
         "Compute: t* = argmin_t  |h + r − t|"),
        (5.5, "#d5e8d4", "#27ae60",
         "Relation Prediction  (h, ?, t)",
         "Find the RELATION type.\n(Einstein, ?, Germany)  →  bornIn"),
        (3.0, "#fff2cc", "#f39c12",
         "TransE Limitation — 1-to-N relations",
         "If Einstein bornIn many places → model fails.\n"
         "Fix: TransH projects onto relation hyperplane."),
        (0.7, "#fdedec", "#c0392b",
         "Scoring function (L1 distance)",
         "score(h, r, t) = ||h + r − t||₁\n"
         "Lower score = more likely triple"),
    ]
    for y, fc, ec, title, content in tasks:
        ax2.add_patch(fbp(0.2, y - 0.2, 9.6, 2.05,
                                   boxstyle="round,pad=0.1",
                                   facecolor=fc, edgecolor=ec, linewidth=1.8))
        ax2.text(0.55, y + 1.65, title, fontsize=10, fontweight="bold", color=ec)
        ax2.text(0.55, y + 0.6, content, fontsize=8.5, color="#333",
                multialignment="left")

    plt.suptitle("Module D — Knowledge Graph Embeddings: TransE & Link Prediction",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    save("09_transe_kge")


# ═══════════════════════════════════════════════════════════
# Figure 10 — MYCIN: CF Chain & Forward/Backward Chaining
# ═══════════════════════════════════════════════════════════
def fig_mycin():
    fig, axes = plt.subplots(1, 2, figsize=(15, 6.5))

    # ── Left: CF chain computation ──
    ax1 = axes[0]
    ax1.axis("off"); ax1.set_xlim(0, 10); ax1.set_ylim(0, 10)

    ax1.text(5, 9.6, "MYCIN — Confidence Factor Calculation",
             ha="center", fontsize=13, fontweight="bold")

    steps = [
        (8.1, "#dae8fc", "#2980b9",
         "Step 1 — Combine premise evidence",
         "CF(Fever AND Chills) = min(CF_Fever, CF_Chills)\n"
         "= min(0.8, 0.6) = 0.6"),
        (6.0, "#fef9e7", "#f39c12",
         "Step 2 — Apply rule certainty",
         "CF_rule = 0.7  (how confident the expert is in the rule)\n"
         "CF(conclusion) = CF_premise × CF_rule = 0.6 × 0.7 = 0.42"),
        (3.9, "#d5e8d4", "#27ae60",
         "Step 3 — Combine two independent rules (→ same conclusion)",
         "Rule A: CF_A = 0.42   Rule B: CF_B = 0.6\n"
         "Combined = CF_A + CF_B × (1 − CF_A) = 0.42 + 0.6×0.58 = 0.768"),
        (1.7, "#e8daef", "#6c3483",
         "Step 4 — Threshold & explanation facility",
         "CF > 0.5 → recommend treatment\n"
         "MYCIN explains: 'Rule A (0.42) + Rule B (0.6) → combined 0.768'"),
    ]

    for y, fc, ec, title, content in steps:
        ax1.add_patch(fbp(0.15, y - 0.75, 9.7, 1.85,
                                   boxstyle="round,pad=0.1",
                                   facecolor=fc, edgecolor=ec, linewidth=2))
        ax1.text(0.5, y + 0.85, title,   fontsize=9.5, fontweight="bold", color=ec)
        ax1.text(0.5, y + 0.05, content, fontsize=8.5, color="#333")
        if y > 2:
            ax1.annotate("", xy=(5, y - 0.75), xytext=(5, y - 1.25),
                        arrowprops=dict(arrowstyle="->", color="#bdc3c7", lw=1.5))

    # ── Right: backward vs forward chaining ──
    ax2 = axes[1]
    ax2.axis("off"); ax2.set_xlim(0, 10); ax2.set_ylim(0, 10)

    ax2.text(5, 9.6, "Chaining Strategies",
             ha="center", fontsize=13, fontweight="bold")

    # forward
    ax2.add_patch(fbp(0.2, 6.0, 4.3, 3.3,
                               boxstyle="round,pad=0.1",
                               facecolor="#d5e8d4", edgecolor="#27ae60", linewidth=2))
    ax2.text(2.35, 9.05, "FORWARD CHAINING",
             ha="center", fontsize=11, fontweight="bold", color="#1e8449")
    ax2.text(2.35, 8.6, "Data-driven",
             ha="center", fontsize=9, color="#555", style="italic")
    fwd = ["Known facts (given)", "→ Apply matching rules",
           "→ Derive new facts", "→ Repeat until goal met"]
    for i, s in enumerate(fwd):
        ax2.text(0.5, 8.1 - i * 0.52, s, fontsize=9,
                fontweight="bold" if i == 0 else "normal", color="#1e8449")
    ax2.text(0.5, 6.25, '"I have facts → what can I conclude?"',
             fontsize=8, color="#555", style="italic")

    # backward (MYCIN)
    ax2.add_patch(fbp(5.5, 6.0, 4.3, 3.3,
                               boxstyle="round,pad=0.1",
                               facecolor="#dae8fc", edgecolor="#2980b9", linewidth=2))
    ax2.text(7.65, 9.05, "BACKWARD CHAINING",
             ha="center", fontsize=11, fontweight="bold", color="#1a5276")
    ax2.text(7.65, 8.6, "Goal-driven  ← MYCIN uses this",
             ha="center", fontsize=9, color="#555", style="italic")
    bwd = ["Start from a hypothesis goal", "← Find rules that prove it",
           "← Ask for needed evidence", "← Confirm or reject goal"]
    for i, s in enumerate(bwd):
        ax2.text(5.7, 8.1 - i * 0.52, s, fontsize=9,
                fontweight="bold" if i == 0 else "normal", color="#1a5276")
    ax2.text(5.7, 6.25, '"I suspect X → what evidence to ask for?"',
             fontsize=8, color="#555", style="italic")

    # MYCIN summary
    ax2.add_patch(fbp(0.2, 0.3, 9.6, 5.4,
                               boxstyle="round,pad=0.1",
                               facecolor="#fdfefe", edgecolor="#bdc3c7", linewidth=1))
    ax2.text(5, 5.5, "MYCIN Key Properties", ha="center", fontsize=11, fontweight="bold")

    props = [
        ("CF range",         "−1 (certainly false) to +1 (certainly true); 0 = unknown"),
        ("Premise CF",       "AND → min  |  OR → max  |  NOT → 1 − CF"),
        ("Rule application", "CF_conclusion = CF_premise × CF_rule"),
        ("Combining rules",  "CF_combined = CF_a + CF_b × (1 − CF_a)"),
        ("Threshold",        'CF > 0.5 typically triggers recommendation'),
        ("Explanation",      '"How" = trace rule chain  |  "Why" = show current goal'),
    ]
    for i, (k, v) in enumerate(props):
        y = 5.0 - i * 0.77
        ax2.text(0.5, y, f"• {k}:", fontsize=9, fontweight="bold", color="#2c3e50")
        ax2.text(0.5, y - 0.38, f"  {v}", fontsize=8.5, color="#555")

    plt.suptitle("Module E — MYCIN Expert System: CF Calculation & Reasoning Chains",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    save("10_mycin_cf")


# ═══════════════════════════════════════════════════════════
# Figure 11 — FOL Quantifiers (Q1b pattern)
# ═══════════════════════════════════════════════════════════
def fig_fol_quantifiers():
    fig, ax = plt.subplots(figsize=(15, 7))
    ax.set_xlim(0, 15); ax.set_ylim(0, 7)
    ax.axis("off")

    ax.text(7.5, 6.75,
            "FOL Quantifiers — The Most Common Exam Trap (Q1b type)",
            ha="center", fontsize=14, fontweight="bold", color="#c0392b")

    cols = [
        (2.5,  "#d5e8d4", "#27ae60",
         "∀x P(x)",
         "Universal  (Universal quantifier)",
         "For ALL x in the domain\nP(x) is true",
         '"All birds can fly"',
         "Disproved by ONE\ncounterexample"),
        (7.5,  "#dae8fc", "#2980b9",
         "∃x P(x)",
         "Existential  (Existential quantifier)",
         "There EXISTS at least\none x where P(x) is true",
         '"Some birds can fly"',
         "Proved by ONE example"),
        (12.5, "#f8cecc", "#c0392b",
         "¬∀x P(x)",
         "Negated Universal — KEY EXAM",
         "Equivalent: ∃x ¬P(x)\n'NOT all → some do not'\nQ1b answer: ¬∀x Fly(x)",
         '"Not all birds can fly"',
         "⚠️  ≠ ∀x ¬P(x)\n('NO bird can fly' — wrong!)"),
    ]

    for cx, fc, ec, sym, name, meaning, example, trap in cols:
        ax.add_patch(fbp(cx - 2.2, 0.25, 4.4, 6.1,
                                   boxstyle="round,pad=0.1",
                                   facecolor=fc, edgecolor=ec, linewidth=2.5))
        ax.text(cx, 6.1,  sym,     ha="center", fontsize=20, fontweight="bold", color=ec)
        ax.text(cx, 5.55, name,    ha="center", fontsize=9, fontweight="bold", color="#333")
        ax.text(cx, 4.75, meaning, ha="center", fontsize=9, color="#333",
                multialignment="center")
        ax.text(cx, 3.7, "Example:", ha="center", fontsize=9, fontweight="bold", color=ec)
        ax.text(cx, 3.3, example,  ha="center", fontsize=9, style="italic", color="#555")

        ax.add_patch(fbp(cx - 1.9, 0.4, 3.8, 2.5,
                                   boxstyle="round,pad=0.05",
                                   facecolor="white", edgecolor="#ffcc00", linewidth=2))
        ax.text(cx, 2.65, "Exam note:",
                ha="center", fontsize=8, fontweight="bold", color="#d35400")
        ax.text(cx, 2.1, trap, ha="center", fontsize=8.5, color="#d35400",
                multialignment="center")

    ax.text(7.5, 0.1,
            "De Morgan's Laws:  ¬∀x P(x) ≡ ∃x ¬P(x)   |   ¬∃x P(x) ≡ ∀x ¬P(x)",
            ha="center", fontsize=10.5, fontweight="bold", color="#6c3483",
            bbox=dict(boxstyle="round", facecolor="#e8daef", alpha=0.9))

    save("11_fol_quantifiers")


# ═══════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════
def main():
    print("COMPSCI 713 — Generating exam visualizations...\n")
    fig_topic_weights()
    fig_truth_table()
    fig_lnn_tnorms()
    fig_fuzzy()
    fig_vagueness_uncertainty()
    fig_entropy()
    fig_bagging_boosting()
    fig_bayes()
    fig_transe()
    fig_mycin()
    fig_fol_quantifiers()
    print(f"\n✅  All 11 figures saved to:\n   {FIGURES_DIR}")
    print("   Reference in markdown:  ![Title](./figures/XX_name.png)")


if __name__ == "__main__":
    main()
