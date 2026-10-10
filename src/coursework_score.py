"""Score a pre-fixed row set. Missing/invalid predictions count as wrong."""
import re

def parse(value):
    if not isinstance(value, str):
        return None
    value = value.strip()
    if re.fullmatch(r"[A-J]", value, re.I):
        return value.upper()
    hits = re.findall(r"\bAnswer\s*[:：]\s*([A-J])\b", value, re.I)
    return hits[-1].upper() if hits else None

def score(rows, predictions):
    rows = list(rows)
    ids = [r["question_id"] for r in rows]
    if len(ids) != len(set(ids)) or not rows:
        raise ValueError("Empty or duplicate evaluation questions")
    if set(predictions) - set(ids):
        raise ValueError("Predictions contain unknown question IDs")
    correct = missing = invalid = 0
    for row in rows:
        qid = row["question_id"]
        if qid not in predictions:
            missing += 1
            continue
        answer = parse(predictions[qid])
        if answer is None or ord(answer) - 65 >= len(row["options"]):
            invalid += 1
            continue
        correct += answer == row["answer"]
    total = len(rows)
    return {"total": total, "correct": correct,
            "missing": missing, "invalid": invalid,
            "accuracy": correct / total,
            "missing_rate": missing / total,
            "invalid_rate": invalid / total}
