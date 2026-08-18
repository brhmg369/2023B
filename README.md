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
