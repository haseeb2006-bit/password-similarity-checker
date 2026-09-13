import unittest
from src.dataset import load_passwords, precompute_fingerprints, find_closest_match
from src.bloom_filter import get_fingerprint


class TestDataset(unittest.TestCase):
    def test_load_passwords_returns_list(self):
        passwords = load_passwords("data/passlist.txt")
        self.assertIsInstance(passwords, list)
        self.assertGreater(len(passwords), 0)

    def test_load_passwords_no_whitespace(self):
        passwords = load_passwords("data/passlist.txt")
        for password in passwords[:10]:
            self.assertEqual(password, password.strip())

    def test_precompute_fingerprints_matches_length(self):
        passwords = ["cat", "dog", "bird"]
        fingerprints = precompute_fingerprints(passwords, L=1000, K=20)
        self.assertEqual(len(fingerprints), 3)
        for fp in fingerprints:
            self.assertEqual(len(fp), 1000)

    def test_find_closest_match_identical_password(self):
        passwords = ["password1", "letmein", "qwerty"]
        fingerprints = precompute_fingerprints(passwords, L=1000, K=20)
        candidate = get_fingerprint("password1", L=1000, K=20)
        result = find_closest_match(candidate, passwords, fingerprints)
        self.assertEqual(result["closest_password"], "password1")
        self.assertAlmostEqual(result["max_score"], 1.0)


if __name__ == "__main__":
    unittest.main()