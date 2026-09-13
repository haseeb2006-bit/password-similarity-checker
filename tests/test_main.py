import unittest
from src.main import validate_password, make_decision, explain_decision
from src.bloom_filter import get_fingerprint
from src.dataset import find_closest_match


class TestMainPipeline(unittest.TestCase):
    def test_validate_password_rejects_short(self):
        self.assertFalse(validate_password("abc"))
        self.assertTrue(validate_password("abcd"))

    def test_make_decision_threshold(self):
        self.assertEqual(make_decision(0.9, 0.7), "REJECTED")
        self.assertEqual(make_decision(0.5, 0.7), "ACCEPTED")

    def test_full_pipeline_rejects_known_weak_password(self):
        passwords = ["password1", "letmein", "qwerty"]
        fingerprints = [get_fingerprint(p, L=1000, K=20) for p in passwords]

        candidate = get_fingerprint("password1", L=1000, K=20)
        result = find_closest_match(candidate, passwords, fingerprints)
        decision = make_decision(result["max_score"], threshold=0.7)

        self.assertEqual(decision, "REJECTED")

    def test_full_pipeline_accepts_dissimilar_password(self):
        passwords = ["password1", "letmein", "qwerty"]
        fingerprints = [get_fingerprint(p, L=1000, K=20) for p in passwords]

        candidate = get_fingerprint("Xk7#mQ9zLp2!", L=1000, K=20)
        result = find_closest_match(candidate, passwords, fingerprints)
        decision = make_decision(result["max_score"], threshold=0.7)

        self.assertEqual(decision, "ACCEPTED")


if __name__ == "__main__":
    unittest.main()