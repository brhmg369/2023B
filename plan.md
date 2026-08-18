# 方案

本文件为 2023 年高教社杯全国大学生数学建模竞赛 B 题「多波束测线问题」的建模与论文撰写方案。仓库 `2023B` 已具备四个子问题的建模程序、结果表和论文手交接材料，本次任务是在既有证据基础上完成论文初稿并同步图形证据链。

## 用户偏好

- 排版引擎：LaTeX（xelatex，MiKTeX 已安装）
- 竞赛类型：国赛（CUMCM）
- 论文语言：中文
- 子问题数量：已知 4 个

## workflow

| step | skills | 主要产物 |
| --- | --- | --- |
| 1. 赛题分析与建模设计 | `2analysis-modeling` | `reports/ANALYSIS_MODELING_REPORT.md` |
| 2. 各问增量闭环 | `4drawio` / `5writing` / `3coding-visual` | `figures/qN/`、`paper/`、`reports/*` |
| 3. 全文整合与排版 | `5writing` | `paper/main.tex` |
| 4. 验证与验收 | `6verity` | `reports/VERIFY_REPORT.md` |

## 目录结构

```text
2023B/
├── plan.md
├── todo.md
├── reports/
│   ├── ANALYSIS_MODELING_REPORT.md
│   ├── RESULTS_REPORT.md
│   ├── PAPER_WRITING_STATE.md
│   ├── FIGURE_MANIFEST.md
│   └── VERIFY_REPORT.md
├── code/
├── figures/
│   ├── q1/ q2/ q3/ q4/
│   └── style/cumcm.mplstyle
├── paper/
│   ├── main.tex
│   └── sections/
└── results/ result1-4.xlsx
```

## 说明

赛题分析、建模公式、结果和验证证据的来源为仓库内的 `docs/q1-q4_paper_writer_handoff.md`、`code/q1-q4_*.py` 与 `result1-4.xlsx`，论文写作不得脱离这些已核验产物。
