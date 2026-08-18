"""Generate the Figure Pack for CUMCM 2023B.

Figures are generated from the same formulas and result workbooks used by
``q1_*`` through ``q4_*``, so every figure is traceable to a source file.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import openpyxl


ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"
STYLE = FIG / "style" / "cumcm.mplstyle"
plt.style.use(STYLE)

NM = 1852.0
THETA_DEG = 120.0
ALPHA_DEG = 1.5


def depth_at(x_m: float, center_depth_m: float, alpha_rad: float) -> float:
    return center_depth_m - x_m * math.tan(alpha_rad)


def half_widths(depth_m: float, theta_rad: float, alpha_rad: float) -> tuple[float, float]:
    half_angle = theta_rad / 2.0
    common = depth_m * math.sin(half_angle) * math.cos(alpha_rad)
    left = common / math.cos(half_angle + alpha_rad)
    right = common / math.cos(half_angle - alpha_rad)
    return left, right


def q2_coverage(r_nm: float, beta_deg: float, center_depth_m: float = 120.0) -> float:
    alpha_rad = math.radians(ALPHA_DEG)
    theta_rad = math.radians(THETA_DEG)
    beta_rad = math.radians(beta_deg)
    s = r_nm * NM
    depth = center_depth_m + s * math.tan(alpha_rad) * math.cos(beta_rad)
    alpha_eff = math.atan(math.tan(alpha_rad) * math.sin(beta_rad))
    half_angle = theta_rad / 2.0
    width = (
        depth
        * math.sin(half_angle)
        * math.cos(alpha_eff)
        * (1.0 / math.cos(half_angle + alpha_eff) + 1.0 / math.cos(half_angle - alpha_eff))
    )
    return width


def read_result3() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    wb = openpyxl.load_workbook(ROOT / "result3.xlsx", data_only=True)
    ws = wb["测线坐标与覆盖"]
    x, spacing, eta = [], [], []
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row[1] is None:
            continue
        x.append(float(row[1]))
        spacing.append(float(row[14]) if row[14] is not None else 0.0)
        eta.append(float(row[16]) if row[16] is not None else 0.0)
    return np.array(x), np.array(spacing), np.array(eta)


def read_result4_comparison() -> tuple[list[str], np.ndarray, np.ndarray]:
    wb = openpyxl.load_workbook(ROOT / "result4.xlsx", data_only=True)
    ws = wb["候选方案比较"]
    names, length, over20 = [], [], []
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row[0] is None:
            continue
        names.append(str(row[0]))
        length.append(float(row[4]))
        over20.append(float(row[8]))
    return names, np.array(length), np.array(over20)


def read_result4_segments() -> np.ndarray:
    wb = openpyxl.load_workbook(ROOT / "result4.xlsx", data_only=True)
    ws = wb["推荐测线坐标"]
    segs = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row[3] is None:
            continue
        segs.append((float(row[3]), float(row[5]), float(row[6])))
    return np.array(segs)


def read_bathymetry() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    wb = openpyxl.load_workbook(ROOT / "附件.xlsx", data_only=True)
    ws = wb[wb.sheetnames[0]]
    x = np.array([float(ws.cell(2, c).value) for c in range(3, ws.max_column + 1)])
    y = np.array([float(ws.cell(r, 2).value) for r in range(3, ws.max_row + 1)])
    z = np.array(
        [[float(ws.cell(r, c).value) for c in range(3, ws.max_column + 1)] for r in range(3, ws.max_row + 1)]
    )
    return x, y, z


def save(fig, q: str, name: str) -> None:
    out = FIG / q
    out.mkdir(parents=True, exist_ok=True)
    fig.savefig(out / f"{name}.pdf")
    fig.savefig(out / f"{name}.svg")
    fig.savefig(out / f"{name}.png", dpi=150)
    plt.close(fig)
    print(f"Wrote {out / name}.pdf / .svg / .png")


def fig_q1_geometry() -> None:
    alpha = math.radians(ALPHA_DEG)
    phi = math.radians(THETA_DEG / 2.0)
    D0 = 70.0
    x0 = 120.0
    Dx = depth_at(x0, D0, alpha)
    bl, br = half_widths(Dx, math.radians(THETA_DEG), alpha)
    xl = x0 - bl
    xr = x0 + br

    x_sea = np.linspace(xl - 90, xr + 90, 200)
    y_sea = depth_at(x_sea, D0, alpha)

    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    ax.plot(x_sea, y_sea, color="#4D4D4D", lw=2.0, label="海底坡面")
    ax.axhline(0, color="#0072B2", lw=1.6, label="海面")
    ax.plot([x0, xl], [0, depth_at(xl, D0, alpha)], color="#D55E00", lw=1.2)
    ax.plot([x0, xr], [0, depth_at(xr, D0, alpha)], color="#D55E00", lw=1.2)
    ax.plot([x0], [0], marker="o", color="#0072B2")
    ax.plot([xl, xr], [depth_at(xl, D0, alpha), depth_at(xr, D0, alpha)], marker="o", ls="none", color="#D55E00")
    ax.plot([x0, x0], [0, Dx], ls="--", color="#4D4D4D", lw=1.0)

    # Project footprints up to the sea surface to mark the horizontal projections.
    ax.plot([xl, xl], [0, depth_at(xl, D0, alpha)], ls=":", color="#888888", lw=1.0)
    ax.plot([xr, xr], [0, depth_at(xr, D0, alpha)], ls=":", color="#888888", lw=1.0)

    def harr(xa, xb, y, text, color):
        ax.annotate("", xy=(xb, y), xytext=(xa, y), arrowprops=dict(arrowstyle="<->", color=color, lw=1.0))
        ax.text((xa + xb) / 2, y + 1.2, text, ha="center", va="bottom", color=color, fontsize=10)

    harr(xl, x0, 0.5, r"$B_L$", "#009E73")
    harr(x0, xr, 0.5, r"$B_R$", "#009E73")
    harr(xl, xr, -6.0, r"$W=B_L+B_R$", "#0072B2")
    ax.text(x0 + 2, Dx / 2, r"$D$", color="#4D4D4D", va="center")
    ax.text(x0 + 22, 2.2, r"$\phi$", color="#D55E00")
    ax.text(x0 + 30, depth_at(x0 + 30, D0, alpha) - 5, r"$\alpha$", color="#4D4D4D")

    ax.set_xlabel("水平距离 $x$ / m")
    ax.set_ylabel("海水深度 $D$ / m")
    ax.set_ylim(-16, None)
    ax.legend(loc="upper right")
    save(fig, "q1", "fig_q1_geometry")


def fig_q1_result() -> None:
    theta = math.radians(THETA_DEG)
    alpha = math.radians(ALPHA_DEG)
    D0 = 70.0
    xs = np.linspace(-800, 800, 321)
    D = np.array([depth_at(x, D0, alpha) for x in xs])
    W = np.empty_like(D)
    bl = np.empty_like(D)
    br = np.empty_like(D)
    for i, d in enumerate(D):
        bl[i], br[i] = half_widths(d, theta, alpha)
        W[i] = bl[i] + br[i]

    table_x = np.arange(-800, 801, 200)
    eta = []
    for i in range(1, len(table_x)):
        prev_d = depth_at(table_x[i - 1], D0, alpha)
        cur_d = depth_at(table_x[i], D0, alpha)
        _, prev_br = half_widths(prev_d, theta, alpha)
        cur_bl, cur_br = half_widths(cur_d, theta, alpha)
        spacing = table_x[i] - table_x[i - 1]
        eta.append((prev_br + cur_bl - spacing) / (cur_bl + cur_br) * 100.0)

    fig, axes = plt.subplots(1, 3, figsize=(11.2, 3.1))
    axes[0].plot(xs, D, color="#0072B2")
    axes[0].set_xlabel("测线位置 $x$ / m")
    axes[0].set_ylabel("海水深度 $D$ / m")

    axes[1].plot(xs, W, color="#E69F00")
    axes[1].set_xlabel("测线位置 $x$ / m")
    axes[1].set_ylabel("覆盖宽度 $W$ / m")

    axes[2].plot(table_x[1:], eta, marker="o", color="#009E73")
    axes[2].axhline(10, color="#D55E00", ls="--", lw=1.0)
    axes[2].axhline(20, color="#D55E00", ls="--", lw=1.0)
    axes[2].axhline(0, color="#4D4D4D", ls=":", lw=1.0)
    axes[2].set_xlabel("测线位置 $x$ / m")
    axes[2].set_ylabel("重叠率 $\\eta$ / %")
    axes[2].text(620, 12, "10%–20%", color="#D55E00", fontsize=8)

    for ax in axes:
        ax.grid(alpha=0.25)
    save(fig, "q1", "fig_q1_result")


def fig_q2_heatmap() -> None:
    betas = np.arange(0, 316, 15)
    rs = np.linspace(0, 2.1, 43)
    W = np.array([[q2_coverage(r, b) for r in rs] for b in betas])

    fig, ax = plt.subplots(figsize=(7.0, 4.0))
    im = ax.imshow(W, aspect="auto", origin="lower", cmap="viridis",
                   extent=[rs[0], rs[-1], betas[0], betas[-1]])
    cb = fig.colorbar(im, ax=ax)
    cb.set_label("覆盖宽度 $W$ / m")
    ax.set_xlabel("测量船距中心点距离 $r$ / 海里")
    ax.set_ylabel("测线方向夹角 $\\beta$ / °")
    save(fig, "q2", "fig_q2_heatmap")


def fig_q3_layout() -> None:
    x, _, _ = read_result3()
    x_min, x_max = -3704.0, 3704.0
    y_min, y_max = -1852.0, 1852.0
    colors = plt.cm.viridis(np.linspace(0.0, 0.85, len(x)))

    fig, ax = plt.subplots(figsize=(8.0, 3.6))
    ax.add_patch(plt.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min,
                               fill=False, edgecolor="#4D4D4D", lw=1.4))
    for xi, c in zip(x, colors):
        ax.axvline(xi, color=c, lw=0.8)
    ax.scatter([], [], c=[], cmap="viridis", vmin=0, vmax=1)
    ax.set_xlim(x_min - 300, x_max + 300)
    ax.set_ylim(y_min - 260, y_max + 260)
    ax.set_xlabel("东西向坐标 $x$ / m")
    ax.set_ylabel("南北向坐标 $y$ / m")
    ax.set_title("34 条南北向测线（西深东浅）")
    ax.text(x_min + 120, y_max + 80, "西（深）", ha="center", color="#4D4D4D")
    ax.text(x_max - 120, y_max + 80, "东（浅）", ha="center", color="#4D4D4D")
    save(fig, "q3", "fig_q3_layout")


def fig_q3_spacing() -> None:
    x, spacing, eta = read_result3()
    pair = np.arange(2, len(x) + 1)
    spacing = spacing[1:]
    eta = eta[1:]

    fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.2))
    axes[0].plot(pair, spacing, marker="o", color="#0072B2")
    axes[0].set_xlabel("相邻测线对编号")
    axes[0].set_ylabel("测线间距 $d$ / m")

    axes[1].plot(pair, eta, marker="o", color="#009E73")
    axes[1].axhline(10, color="#D55E00", ls="--", lw=1.0)
    axes[1].axhline(20, color="#D55E00", ls="--", lw=1.0)
    axes[1].set_xlabel("相邻测线对编号")
    axes[1].set_ylabel("重叠率 $\\eta$ / %")
    for ax in axes:
        ax.grid(alpha=0.25)
    save(fig, "q3", "fig_q3_spacing")


def fig_q4_depth() -> None:
    x, y, z = read_bathymetry()
    segs = read_result4_segments()

    fig, ax = plt.subplots(figsize=(7.4, 5.4))
    im = ax.imshow(z, aspect="auto", origin="lower", cmap="viridis",
                   extent=[x[0], x[-1], y[0], y[-1]])
    cb = fig.colorbar(im, ax=ax)
    cb.set_label("海水深度 / m")
    for seg in segs:
        ax.plot([seg[0], seg[0]], [seg[1], seg[2]], color="white", lw=0.35, alpha=0.65)
    ax.set_xlabel("横向坐标 $x$ / 海里")
    ax.set_ylabel("纵向坐标 $y$ / 海里")
    save(fig, "q4", "fig_q4_depth")


def fig_q4_comparison() -> None:
    names, length, over20 = read_result4_comparison()
    short = ["全域\n5.0 NM", "1.0 NM", "0.5 NM\n推荐", "0.25 NM"]
    xpos = np.arange(len(names))
    selected = 2
    colors = ["#B8B8B8", "#B8B8B8", "#0072B2", "#B8B8B8"]

    fig, axes = plt.subplots(1, 2, figsize=(10.0, 3.4))
    axes[0].bar(xpos, length, color=colors)
    axes[0].set_xticks(xpos, short, fontsize=8)
    axes[0].set_ylabel("测线总长度 / m")
    axes[0].set_ylim(0, 620000)

    axes[1].bar(xpos, over20, color=colors)
    axes[1].set_xticks(xpos, short, fontsize=8)
    axes[1].set_ylabel("超 20% 重叠长度 / m")
    axes[1].set_ylim(0, 320000)
    for ax in axes:
        ax.grid(axis="y", alpha=0.25)
        ax.spines.top.set_visible(False)
        ax.spines.right.set_visible(False)
    save(fig, "q4", "fig_q4_comparison")


def main() -> None:
    fig_q1_geometry()
    fig_q1_result()
    fig_q2_heatmap()
    fig_q3_layout()
    fig_q3_spacing()
    fig_q4_depth()
    fig_q4_comparison()


if __name__ == "__main__":
    main()
