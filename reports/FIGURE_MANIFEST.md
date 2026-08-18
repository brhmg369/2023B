# 逐问 Figure Manifest

状态约定：`planned` / `ready`。

| Figure ID | 问题 | 类型 | 该图说明 | 源数据/来源 | 绘图脚本 | 输出 | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| fig_q1_geometry | Q1 | [MECH] | 二维斜坡剖面的坐标、水深、半覆盖宽度与覆盖宽度定义 | 题面图 7 / q1 公式 | code/make_figures.py | figures/q1/fig_q1_geometry.pdf | ready |
| fig_q1_result | Q1 | [RESULT] | 水深、覆盖宽度、重叠率随测线位置的变化 | q1 公式计算 | code/make_figures.py | figures/q1/fig_q1_result.pdf | ready |
| fig_q2_heatmap | Q2 | [RESULT] | 覆盖宽度随测线方向夹角与船位距离的变化 | result2.xlsx | code/make_figures.py | figures/q2/fig_q2_heatmap.pdf | ready |
| fig_q3_layout | Q3 | [RESULT] | 34 条南北向测线在矩形海域内的布设 | result3.xlsx | code/make_figures.py | figures/q3/fig_q3_layout.pdf | ready |
| fig_q3_spacing | Q3 | [VALIDATE] | 相邻测线间距与重叠率校验 | result3.xlsx | code/make_figures.py | figures/q3/fig_q3_spacing.pdf | ready |
| fig_q4_depth | Q4 | [DATA] | 附件水深空间分布与推荐测线叠加 | 附件.xlsx / result4.xlsx | code/make_figures.py | figures/q4/fig_q4_depth.pdf | ready |
| fig_q4_comparison | Q4 | [COMPARE] | 四种分带方案的测线总长度与超 20% 重叠长度比较 | result4.xlsx | code/make_figures.py | figures/q4/fig_q4_comparison.pdf | ready |

说明：各图均生成 PDF（论文引用）、SVG（矢量源）与 PNG（QA 预览）；绘图脚本统一为 `code/make_figures.py`，源数据来自对应结果表或附件。示意图（fig_q1_geometry、fig_q3_layout）当前由 Matplotlib 程序化生成，未使用 draw.io 源文件。
