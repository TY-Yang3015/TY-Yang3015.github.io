"""Generate the four MiniAcc blog charts (single-column blog style).

Run with: python3 assets/images/miniacc/make_charts.py
Outputs PNGs at 200 dpi, ~6.2 in wide, next to this script.
"""

import matplotlib

matplotlib.use("Agg")  # non-interactive, CPU-only

from pathlib import Path

import matplotlib.pyplot as plt

OUT_DIR = Path(__file__).resolve().parent
OUT_DIR.mkdir(parents=True, exist_ok=True)
DPI = 200
FIG_W = 6.2  # inches, single-column blog width

# Consistent muted palette
TEAL = "#2A7F8E"      # above baseline / primary series
GREY = "#9AA0A6"      # below baseline
TEAL_LIGHT = "#7FB5BE"
TEAL_DARK = "#1F5F6B"
ORANGE = "#C97B4A"    # second series in grouped chart
LABEL_GREY = "#333333"

plt.rcParams.update({
    "figure.dpi": DPI,
    "savefig.dpi": DPI,
    "font.size": 9,
    "axes.edgecolor": "#BBBBBB",
    "axes.labelcolor": LABEL_GREY,
    "text.color": LABEL_GREY,
    "xtick.color": LABEL_GREY,
    "ytick.color": LABEL_GREY,
    "axes.linewidth": 0.8,
    "font.family": "DejaVu Sans",
})


def despine(ax):
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)


def save(fig, name):
    path = OUT_DIR / name
    fig.savefig(path, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {path}")


# ---------------------------------------------------------------- Chart A
def chart_individual_modules():
    data = [
        ("Kitchen INT8", 1.881),
        ("AdaLN fusion", 1.372),
        ("SageAttention", 0.998),
        ("Query token merge", 0.995),
        ("Heun solver", 0.994),
        ("FFN token merge", 0.993),
        ("Sol sparse attention", 0.990),
        ("Compiler default", 0.970),
    ]  # sorted descending
    labels = [d[0] for d in data]
    values = [d[1] for d in data]
    colors = [TEAL if v >= 1.0 else GREY for v in values]

    fig, ax = plt.subplots(figsize=(FIG_W, 3.2))
    y = range(len(labels))
    ax.barh(y, values, color=colors, height=0.62)
    ax.axvline(1.0, color=LABEL_GREY, linestyle="--", linewidth=0.9)
    ax.text(1.0, -0.45, "baseline", ha="center", va="bottom",
            fontsize=8, color=LABEL_GREY)
    ax.set_yticks(list(y), labels)
    ax.invert_yaxis()
    ax.set_xlabel("Speed-up vs baseline (×, 1.0 = unchanged)")
    ax.set_xlim(0.0, 2.05)
    ax.grid(False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    for yi, v in zip(y, values):
        ax.text(v + 0.03, yi, f"{v:.3f}", va="center", fontsize=8,
                color=LABEL_GREY)
    save(fig, "chart-individual-modules.png")


# ---------------------------------------------------------------- Chart B
def chart_integrated():
    data = [
        ("Baseline", 1.000),
        ("AdaLN + Kitchen", 2.156),
        ("AdaLN + Kitchen + Sage", 2.508),
        ("AdaLN + Kitchen + Sol", 2.187),
    ]  # sorted so fastest renders at the bottom after inversion
    labels = [d[0] for d in data]
    values = [d[1] for d in data]

    fig, ax = plt.subplots(figsize=(FIG_W, 2.4))
    y = range(len(labels))
    ax.barh(y, values, color=TEAL, height=0.6)
    ax.axvline(1.0, color=LABEL_GREY, linestyle="--", linewidth=0.9)
    ax.text(1.0, -0.45, "baseline", ha="center", va="bottom",
            fontsize=8, color=LABEL_GREY)
    ax.set_yticks(list(y), labels)
    ax.invert_yaxis()
    ax.set_xlabel("End-to-end speed-up vs baseline (×)")
    ax.set_xlim(0.0, 2.9)
    ax.yaxis.grid(False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    for yi, v in zip(y, values):
        ax.text(v + 0.05, yi, f"{v:.3f}×", va="center", fontsize=8,
                color=LABEL_GREY)
    save(fig, "chart-integrated.png")


# ---------------------------------------------------------------- Chart C
def chart_quality_deltas():
    metrics = ["Subject", "Background", "Motion", "Dynamic",
               "Aesthetic", "Imaging", "Overall"]
    sage = [0.135, -0.305, 0.905, 6.250, 1.599, -4.706, -29.823]
    sol = [0.631, -0.505, -0.028, 0.000, 1.280, -0.456, 0.202]

    x = range(len(metrics))
    width = 0.38

    fig, ax = plt.subplots(figsize=(FIG_W, 3.4))
    ax.bar([i - width / 2 for i in x], sage, width,
           label="Sage", color=TEAL)
    ax.bar([i + width / 2 for i in x], sol, width,
           label="Sol", color=ORANGE)
    ax.axhline(0.0, color=LABEL_GREY, linewidth=0.9)
    ax.set_xticks(list(x), metrics, rotation=25, ha="right")
    ax.set_ylabel("VBench change vs baseline (percentage points)")
    ax.yaxis.grid(True, color="#DDDDDD", linewidth=0.6)
    ax.set_axisbelow(True)
    despine(ax)
    ax.legend(frameon=False, loc="lower left", fontsize=8)
    save(fig, "chart-quality-deltas.png")


# ---------------------------------------------------------------- Chart D
def chart_time_breakdown():
    configs = ["Baseline", "AdaLN + Kitchen", "AdaLN + Kitchen + Sage"]
    text_encode = [48.6, 48.97, 48.79]
    denoise = [256.9, 79.49, 60.59]
    decode_save = [19.0, 18.46, 18.58]
    colors = [TEAL_LIGHT, TEAL, TEAL_DARK]
    seg_labels = ["Text encode", "Denoise", "Decode + save"]

    fig, ax = plt.subplots(figsize=(FIG_W, 2.6))
    y = range(len(configs))
    left = [0.0] * len(configs)
    for seg, color, lab in zip((text_encode, denoise, decode_save),
                               colors, seg_labels):
        ax.barh(y, seg, left=left, color=color, height=0.55, label=lab)
        left = [l + s for l, s in zip(left, seg)]

    # Annotate denoise values inside the bars
    for yi, v in zip(y, denoise):
        ax.text(text_encode[yi] + v / 2, yi, f"{v:.1f} s",
                ha="center", va="center", fontsize=8, color="white")

    ax.set_yticks(list(y), configs)
    ax.invert_yaxis()
    ax.set_xlabel("Time per request (seconds)")
    ax.yaxis.grid(False)
    despine(ax)
    ax.legend(frameon=False, loc="lower right", fontsize=8)
    ax.set_xlim(0.0, max(sum(t) for t in
                        zip(text_encode, denoise, decode_save)) * 1.02)
    save(fig, "chart-time-breakdown.png")


if __name__ == "__main__":
    chart_individual_modules()
    chart_integrated()
    chart_quality_deltas()
    chart_time_breakdown()
