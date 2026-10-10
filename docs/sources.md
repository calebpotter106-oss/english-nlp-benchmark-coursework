# 论文与官方资源

核对日期：2026-10-10。只引用作者原文和官方代码；检索引擎的候选记录不能代替原文。

## MMLU-Pro

Wang, Y. 等（2024）. *MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark*. NeurIPS 2024 Datasets and Benchmarks。

- [原始论文，arXiv v6](https://arxiv.org/abs/2406.01574v6)
- [官方数据，固定 revision](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro/tree/b189ec765aa7ed75c8acfea42df31fdae71f97be)
- [官方代码仓库](https://github.com/TIGER-AI-Lab/MMLU-Pro)
- [固定版本 README](https://github.com/TIGER-AI-Lab/MMLU-Pro/blob/f418b116db00b065c2aea046518d8fcf74d39872/README.md)
- [官方答案提取和计分程序](https://github.com/TIGER-AI-Lab/MMLU-Pro/blob/f418b116db00b065c2aea046518d8fcf74d39872/compute_accuracy.py)

适合支撑 PPT 的原文位置：§3 基准构建、Figure 1 难度/提示稳定性/推理方式比较、Table 2 作者模型实验、§7 局限。图表中的分数不是本组实验结果。

## IFEval

Zhou, J. 等（2023）. *Instruction-Following Evaluation for Large Language Models*. arXiv:2311.07911。

- [原始论文，arXiv v1](https://arxiv.org/abs/2311.07911v1)
- [官方代码与数据目录](https://github.com/google-research/google-research/tree/master/instruction_following_eval)
- [固定版本输入数据](https://github.com/google-research/google-research/blob/6e6b1ff7471be7ed884ff7ce0821c889a3a1b0c9/instruction_following_eval/data/input_data.jsonl)
- [固定版本 strict/loose 检查器](https://github.com/google-research/google-research/blob/6e6b1ff7471be7ed884ff7ce0821c889a3a1b0c9/instruction_following_eval/evaluation_lib.py)

适合支撑 PPT 的位置：Figure 1 可验证指令流程；§2.2 与 Table 3 展示 prompt/instruction 和 strict/loose 四类指标。论文概述约 500 条提示，本次官方文件计数为 541 条。规则通过不等于事实正确；宽松检查可能增加假阳性。

## LiveBench

White, C. 等（2025；预印本首发于 2024）. *LiveBench: A Challenging, Contamination-Limited LLM Benchmark*. ICLR 2025。

- [原始论文，arXiv v2](https://arxiv.org/abs/2406.19314v2)
- [官方代码仓库](https://github.com/LiveBench/LiveBench)
- [固定版本 README 与 release 参数](https://github.com/LiveBench/LiveBench/blob/24364d65076429adfcba7be18af4d44fddc43dce/README.md)
- [固定版本客观判分入口](https://github.com/LiveBench/LiveBench/blob/24364d65076429adfcba7be18af4d44fddc43dce/livebench/gen_ground_truth_judgment.py)
- [官方数据入口](https://huggingface.co/livebench)

适合支撑 PPT 的位置：§2 任务与更新；Figure 1、Table 1 作者历史实验；§5 局限；§6 复现。动态更新降低污染风险，但不保证无污染；某些开放式创作没有易定义的客观金标准。

不将 README 的旧版本说明直接称为“全站当前最新版本”，也不将历史图表中的分数称为最新排行榜。
