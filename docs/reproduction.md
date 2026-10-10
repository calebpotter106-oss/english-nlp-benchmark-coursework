# 复现说明

## 1. 核验官方数据

在仓库根目录运行：

```text
python -m pip install -r requirements.txt
python src/coursework_audit.py results/audit_rerun.json
```

程序固定官方数据 revision，检查样本数、字段、学科类别、选项数量、题目 ID 唯一性，以及每题的答案索引范围/答案字母一致性。

联网仅用于下载公开数据，无需提供模型 API 密钥。`checked_at_utc` 会随复现时间变化；其他内容应与保存结果比较，不要求整份 JSON 的 SHA256 在重跑后相同。

## 2. 验证评分程序

```text
python src/test_coursework_score.py
```

测试包括：纯字母答案、显式 `Answer: X`、多个答案取最后一个、无法解析的输出、选项越界、固定分母、未知题目 ID、重复评测题目。

合成例子中有 4 题：1 题答对、1 题答错、1 题无效、1 题缺失。程序应计算 `accuracy=0.25`。这是预设案例的软件测试，**不是模型测得的 25% 准确率**。

## 3. 为未来的模型回答计分

预测文件是 JSON Lines，每行一条：

```json
{"question_id": 0, "prediction": "Answer: A"}
```

上面只说明格式，不能据此认定题目 0 的真实答案。必须使用模型实际生成的原始回答，而不是复制标准答案。重复或未知题目 ID 将报错。

评测整个测试集：

```text
python src/run_coursework_scoring.py --predictions predictions.jsonl --output results/model_scores.json
```

只评测事先冻结的子集：先保存一个题目 ID 的 JSON 数组，例如 `[0, 1, 2]`；确认 ID 真实存在，并在模型生成回答前确定该数组，然后运行：

```text
python src/run_coursework_scoring.py --predictions predictions.jsonl --question-ids question_ids.json --output results/model_scores.json
```

全量和子集评测不能使用同一个分母。程序只对所选题集评分，题集之外的预测将报错。缺失预测、空响应、非文本响应或无法识别/越界的选项均不计为正确。

## 4. 重现条件与限制

- Python 版本和依赖环境可能影响安装过程；测试代码使用标准库即可运行。
- 首次加载数据需要联网，之后可使用本地缓存。
- 本仓库没有生成真实模型输出的调用程序，也未报告真实模型准确率。
- 论文图表是作者历史实验，不能称为本组测量或当前最新排行榜。
