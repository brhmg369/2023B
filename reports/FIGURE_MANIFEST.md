# 高端可视化 Figure Manifest

状态约定：`planned` / `ready`。

| Figure ID | 问题 | 类型 | 该图说明 | 源数据/来源 | 绘图脚本 | 输出 | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| fig_q1_geometry | Q1 | [MECH] | 二维斜坡剖面、左右声束、半覆盖宽度与水平投影宽度 `W` 的几何示意 | q1 公式 | code/make_figures.py | figures/q1/fig_q1_geometry.pdf/svg/png | ready |
| fig_q1_result | Q1 | [RESULT] | 水深、水平覆盖宽度、重叠率随测线位置的三联趋势图 | q1 公式计算 | code/make_figures.py | figures/q1/fig_q1_result.pdf/svg/png | ready |
| fig_q2_3d_geometry | Q2 | [MECH] | 海平面、斜坡面、航向、坡面法向水平投影与垂直测线扫描平面的三维关系图 | q2 空间几何 | code/make_figures.py | figures/q2/fig_q2_3d_geometry.pdf/svg/png | ready |
| fig_q2_heatmap | Q2 | [RESULT] | `W(r,beta)` 的方向-距离二维等值热力图 | q2 公式计算 | code/make_figures.py | figures/q2/fig_q2_heatmap.pdf/svg/png | ready |
| fig_q2_width_surface | Q2 | [RESULT] | `W(r,beta)` 三维曲面，展示覆盖宽度随距离与航向变化的空间形态 | q2 公式计算 | code/make_figures.py | figures/q2/fig_q2_width_surface.pdf/svg/png | ready |
| fig_q3_layout | Q3 | [RESULT] | 规则坡面海域 34 条南北向测线与半透明覆盖条带叠加图 | result3.xlsx | code/make_figures.py | figures/q3/fig_q3_layout.pdf/svg/png | ready |
| fig_q3_spacing | Q3 | [VALIDATE] | 相邻测线间距递推与重叠率约束校验图 | result3.xlsx | code/make_figures.py | figures/q3/fig_q3_spacing.pdf/svg/png | ready |
| fig_q4_depth | Q4 | [DATA+RESULT] | 真实水深等深线、深度色带与 0.50 NM 推荐测线叠加 | 附件.xlsx / result4.xlsx | code/make_figures.py | figures/q4/fig_q4_depth.pdf/svg/png | ready |
| fig_q4_contour_route_overlay | Q4 | [RESULT] | 等深线、分带边界与测线方案叠加图，用于解释分带布线逻辑 | 附件.xlsx / result4.xlsx | code/make_figures.py | figures/q4/fig_q4_contour_route_overlay.pdf/svg/png | ready |
| fig_q4_bathymetry_surface | Q4 | [DATA] | 附件真实海域三维海底地形图 | 附件.xlsx | code/make_figures.py | figures/q4/fig_q4_bathymetry_surface.pdf/svg/png | ready |
| fig_q4_comparison | Q4 | [COMPARE] | 分带方案长度-冗余-线段数权衡图，标出 0.25 NM 指标最优与 0.50 NM 工程折中 | result4.xlsx | code/make_figures.py | figures/q4/fig_q4_comparison.pdf/svg/png | ready |

说明：

- 各图均生成 PDF（论文引用）、SVG（矢量源）与 PNG（QA 预览）。
- 绘图脚本统一为 `code/make_figures.py`，源数据来自 `result1-4.xlsx`、`附件.xlsx` 或正文公式。
- 当前版本已替换原始 Matplotlib 默认风格，统一采用低饱和竞赛论文风格，并补齐 Q2/Q4 三维表达。
- 正文图 1~图 11 均已嵌入 `paper/`，图号由 LaTeX 自动编号（2026-08-18 论文手整合）。
