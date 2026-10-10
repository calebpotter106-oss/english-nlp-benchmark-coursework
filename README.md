# 英文 NLP 评测数据集调研：代码与支撑材料

课程方向：英文评测数据集、任务与指标、论文创新以及工程适用性。以 **MMLU-Pro** 为本地数据核验案例，以 **IFEval** 和 **LiveBench** 为对照。

> 本仓库已经完成数据结构/标签检查及评分程序测试；**没有完成真实模型推理或跨模型性能实验**。合成测试的准确率不能当作模型成绩。

## 教师查验入口

| 内容 | 直接入口 |
|---|---|
| 固定官方版本的数据核验代码 | [src/coursework_audit.py](src/coursework_audit.py) |
| 固定分母的评分实现 | [src/coursework_score.py](src/coursework_score.py) |
| 预测文件评分命令入口 | [src/run_coursework_scoring.py](src/run_coursework_scoring.py) |
| 8 项合成案例单元测试 | [src/test_coursework_score.py](src/test_coursework_score.py) |
| 本组真实数据核验结果 | [results/audit.json](results/audit.json) |
| 真实程序测试日志 | [results/score_tests.txt](results/score_tests.txt) |
| 论文、官方数据与评分代码 | [docs/sources.md](docs/sources.md) |
| 详细复现和预测格式 | [docs/reproduction.md](docs/reproduction.md) |
| 已完成与未完成的范围 | [docs/status.md](docs/status.md) |

## 快速复现

建议使用 Python 3.11 或更新的兼容版本。数据检查需要联网访问 Hugging Face；评分单元测试不需要联网、GPU 或 API 密钥。

```text
python -m pip install -r requirements.txt
python src/coursework_audit.py results/audit_rerun.json
python src/test_coursework_score.py
```

在 Windows 上如终端中文乱码，可以先设置 `PYTHONUTF8=1`。仓库内保存的原始结果不会被上述命令覆盖。

## 已得到的核验结果

官方数据集：`TIGER-Lab/MMLU-Pro`，固定 revision：`b189ec765aa7ed75c8acfea42df31fdae71f97be`。

- 测试集 12,032 条，验证示例 70 条，14 个学科类别。
- 题目 ID 唯一；答案字母、索引和选项范围冲突 0 条。
- 10 个选项的题目 9,981 条，约占 83%；其余 2,051 条为 3—9 个选项。
- 评分程序的 8 项合成测试通过。这仅检验软件逻辑，不测量任何真实模型能力。

标签表示一致不等于每道题的事实答案已被人工确认。这里也没有将验证示例称为训练集。

## 数据用途与评分边界

准确率使用**事先确定的题目数量**作分母，缺失和无效回答按错计入；答案超出该题实际选项数时视为无效。最终测试题及答案不应同时用于训练或选择提示方案。

若以后只测试某个子集，须先固定题目 ID，再生成预测；不能评测后挑选答对的题目。模型版本、提示、生成参数、原始输出和运行日期应另行记录。

## 发布范围

只公开课程相关原创检查/评分代码、说明和不含个人信息的统计结果。论文 PDF、官方完整数据集、模型答案、账号凭据和本地电脑路径不在本仓库中重新发布。官方资料通过超链接访问，其许可由相应来源决定。

文件校验清单：[SHA256SUMS.json](SHA256SUMS.json)。原始结果核验日期为 2026-10-10。
