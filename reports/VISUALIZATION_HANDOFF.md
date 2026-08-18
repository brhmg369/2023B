# 给论文手的高端图件交接

本轮已由画图手重做 `code/make_figures.py`，并重新生成正文图件与新增三维图。所有图均输出为 `pdf/svg/png` 三种格式，论文优先引用 `pdf`。

## 已替换的正文图

- `figures/q1/fig_q1_geometry.*`：替换原坐标轴式草图，改为几何投影示意图，突出 `W` 是水平投影宽度。
- `figures/q1/fig_q1_result.*`：改为三联趋势图，分别展示水深、覆盖宽度、重叠率。
- `figures/q2/fig_q2_heatmap.*`：改为等值热力图，保留作为 `W(r,beta)` 的二维投影。
- `figures/q3/fig_q3_layout.*`：改为覆盖条带叠加图，不再只是竖线。
- `figures/q3/fig_q3_spacing.*`：改为“间距递推 + 重叠率约束区间”校验图。
- `figures/q4/fig_q4_depth.*`：改为真实水深等深线与推荐测线叠加图。
- `figures/q4/fig_q4_comparison.*`：改为长度-冗余-线段数权衡图，用于解释 `0.25 NM` 与 `0.50 NM` 的取舍。

## 新增图及建议插入位置

| 图件 | 建议位置 | 建议图注 |
| --- | --- | --- |
| `figures/q2/fig_q2_3d_geometry.pdf` | 问题二 6.1，式 `alpha_eff` 前后 | 任意航向下海平面、坡面与扫描平面的三维几何关系 |
| `figures/q2/fig_q2_width_surface.pdf` | 问题二 6.2，热力图旁边或之后 | 覆盖宽度 `W(r,beta)` 的三维曲面 |
| `figures/q4/fig_q4_bathymetry_surface.pdf` | 问题四 8.1，介绍附件数据时 | 附件真实海域三维海底地形 |
| `figures/q4/fig_q4_contour_route_overlay.pdf` | 问题四 8.2 或 8.4 | 等深线、分带边界与推荐测线叠加 |

## 论文写作提醒

- Q1 几何图旁必须继续强调：`W` 是水平投影宽度，不是坡面长度，可直接与水平测线间距比较。
- Q2 不要只放热力图。三维几何图负责解释公式来源，三维曲面负责展示结果形态，热力图只是补充。
- Q3 图中的半透明覆盖条带可支撑“无漏测”的论证，正文应点明覆盖条带跨过东西边界。
- Q4 对比图已经刻意标出 `0.25 NM` 指标最优和 `0.50 NM` 工程折中。正文必须同步修改推荐口径，否则图会反向暴露逻辑矛盾。

## 复现方式

在项目根目录运行：

```bash
python code/make_figures.py
```

依赖：

- `numpy`
- `openpyxl`
- `matplotlib`

运行后会覆盖 `figures/q1`、`figures/q2`、`figures/q3`、`figures/q4` 下的同名图件，并生成新增三维图。
