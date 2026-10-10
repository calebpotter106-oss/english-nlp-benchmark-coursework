"""Synthetic fixtures test software only, NOT any model performance."""
import unittest
from coursework_score import parse, score

def rows():
    return [{"question_id": i, "answer": "A", "options": ["x", "y"]}
            for i in range(4)]

class Tests(unittest.TestCase):
    def test_letter(self): self.assertEqual(parse(" a "), "A")
    def test_explicit(self):
        self.assertEqual(parse("Reasoning. Answer: B"), "B")
    def test_last(self):
        self.assertEqual(parse("Answer: B. Answer: A"), "A")
    def test_invalid(self): self.assertIsNone(parse("unclear"))
    def test_range(self):
        self.assertEqual(score(rows(), {0: "J"})["invalid"], 1)
    def test_denominator(self):
        r = score(rows(), {0: "A", 1: "B", 2: "unclear"})
        self.assertEqual(r, {"total": 4, "correct": 1,
            "missing": 1, "invalid": 1, "accuracy": .25,
            "missing_rate": .25, "invalid_rate": .25})
    def test_unknown(self):
        with self.assertRaises(ValueError): score(rows(), {9: "A"})
    def test_duplicate(self):
        with self.assertRaises(ValueError): score(rows() * 2, {})

if __name__ == "__main__": unittest.main(verbosity=2)
