"""CLI for a frozen MMLU-Pro evaluation set. Does not generate model answers."""
import argparse
import json
from pathlib import Path
from datasets import load_dataset
from coursework_audit import DATASET, REVISION
from coursework_score import score

def read_predictions(path):
    predictions = {}
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        record = json.loads(line)
        qid = record.get("question_id")
        if type(qid) is not int or qid in predictions:
            raise ValueError(f"Invalid or duplicate question_id on line {line_no}")
        if "prediction" not in record:
            raise ValueError(f"Missing prediction on line {line_no}")
        predictions[qid] = record["prediction"]
    return predictions

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--predictions", required=True, type=Path)
    parser.add_argument("--question-ids", type=Path,
                        help="Pre-fixed JSON array of question IDs; default: full test split")
    parser.add_argument("--output", type=Path, default=Path("results/model_scores.json"))
    args = parser.parse_args()
    rows = list(load_dataset(DATASET, revision=REVISION, split="test"))
    if args.question_ids:
        ids = json.loads(args.question_ids.read_text(encoding="utf-8"))
        if not isinstance(ids, list) or not ids or any(type(q) is not int for q in ids):
            raise ValueError("question-ids must be a nonempty JSON array of integers")
        if len(ids) != len(set(ids)):
            raise ValueError("Duplicate IDs in the frozen question list")
        if set(ids) - {r["question_id"] for r in rows}:
            raise ValueError("Frozen question list contains unknown IDs")
        selected = set(ids)
        rows = [r for r in rows if r["question_id"] in selected]
    report = {"dataset": DATASET, "revision": REVISION,
              "scope": "fixed_subset" if args.question_ids else "full_test",
              **score(rows, read_predictions(args.predictions))}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(report, ensure_ascii=False, indent=2)
    args.output.write_text(text + "\n", encoding="utf-8")
    print(text)

if __name__ == "__main__":
    main()
