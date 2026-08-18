# 2023B 多波束测线问题

本仓库保存 2023 年高教社杯数学建模 B 题的建模程序、结果表和论文写作交接材料。

## 问题一

已完成内容：

- `code/q1_multibeam_model.py`：二维斜坡多波束覆盖宽度与重叠率计算程序；
- `result1.xlsx`：问题一表 1 计算结果；
- `docs/q1_paper_writer_handoff.md`：写给论文手的问题一建模交接；
- `docs/q1_result_table.csv`：表 1 结果的 CSV 版本。

运行方式：

```powershell
python code/q1_multibeam_model.py
```

程序参数来自题面：换能器开角 `120 deg`，坡度 `1.5 deg`，中心水深 `70 m`，测线位置为 `-800` 到 `800 m`。

## 问题二

已完成内容：

- `code/q2_multibeam_model.py`：三维坡面方向角下的多波束覆盖宽度计算程序；
- `result2.xlsx`：问题二表 2 计算结果；
- `docs/q2_paper_writer_handoff.md`：写给论文手的问题二建模交接。

运行方式：

```powershell
python code/q2_multibeam_model.py
```

程序参数来自题面：换能器开角 `120 deg`，坡度 `1.5 deg`，中心水深 `120 m`，距离为 `0` 到 `2.1 NM`，测线方向夹角为 `0` 到 `315 deg`。

## 问题三

已完成内容：

- `code/q3_survey_line_design.py`：规则单坡面矩形海域的测线布设递推优化程序；
- `result3.xlsx`：问题三推荐测线方案、坐标与约束校验；
- `docs/q3_paper_writer_handoff.md`：写给论文手的问题三建模交接。

运行方式：

```powershell
python code/q3_survey_line_design.py
```

程序参数来自题面：矩形海域南北长 `2 NM`、东西宽 `4 NM`，中心水深 `110 m`，西深东浅，坡度 `1.5 deg`，换能器开角 `120 deg`。推荐方案为沿等深线南北向布设 `34` 条测线，总长度 `125936 m`。

## 问题四

已完成内容：

- `code/q4_real_bathymetry_design.py`：基于附件真实水深网格的分带测线布设程序；
- `result4.xlsx`：问题四候选方案、推荐测线坐标、覆盖与重叠校验；
- `docs/q4_paper_writer_handoff.md`：写给论文手的问题四建模交接。

运行方式：

```powershell
python code/q4_real_bathymetry_design.py
```

程序读取 `附件.xlsx`，主推荐 `0.5 NM` 分带布线方案：测线线段数 `461`，总长度 `426886 m`，漏测率 `0.0000%`，重叠率超过 `20%` 部分总长度 `5481.92 m`。
