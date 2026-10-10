"""Pinned official-data audit; no model inference or training."""
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from datasets import load_dataset

DATASET = "TIGER-Lab/MMLU-Pro"
REVISION = "b189ec765aa7ed75c8acfea42df31fdae71f97be"

def audit():
    ds = load_dataset(DATASET, revision=REVISION)
    rows = list(ds["test"])
    ids = [r["question_id"] for r in rows]
    bad = [r["question_id"] for r in rows if not (
        isinstance(r["answer_index"], int)
        and 0 <= r["answer_index"] < len(r["options"]) <= 10
        and r["answer"] == "ABCDEFGHIJ"[r["answer_index"]])]
    return {
        "dataset": DATASET, "revision": REVISION,
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "splits": {k: len(v) for k, v in ds.items()},
        "fields": ds["test"].column_names,
        "categories": dict(sorted(Counter(
            r["category"] for r in rows).items())),
        "options": dict(sorted(Counter(
            len(r["options"]) for r in rows).items())),
        "unique_question_ids": len(set(ids)) == len(ids),
        "label_mismatch_count": len(bad),
        "first_bad_ids": bad[:20], "model_inference": False}

if __name__ == "__main__":
    report = audit()
    path = Path(sys.argv[1] if len(sys.argv) > 1 else
                "outputs/submission/audit.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(report, ensure_ascii=False, indent=2)
    path.write_text(text + "\n", encoding="utf-8")
    print(text)
