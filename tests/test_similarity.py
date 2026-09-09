import unittest
from src.similarity import jaccard_similarity, dice_similarity, cosine_similarity


class TestSimilarity(unittest.TestCase):
    def test_identical_vectors(self):
        a = [1, 1, 0, 0]
        self.assertEqual(jaccard_similarity(a, a), 1.0)
        self.assertEqual(dice_similarity(a, a), 1.0)
        self.assertAlmostEqual(cosine_similarity(a, a), 1.0)

    def test_completely_different_vectors(self):
        a = [1, 1, 0, 0]
        b = [0, 0, 1, 1]
        self.assertEqual(jaccard_similarity(a, b), 0.0)
        self.assertEqual(dice_similarity(a, b), 0.0)
        self.assertEqual(cosine_similarity(a, b), 0.0)

    def test_partial_overlap(self):
        a = [1, 1, 0, 0]
        b = [1, 0, 1, 0]
        self.assertAlmostEqual(jaccard_similarity(a, b), 1/3)
        self.assertAlmostEqual(dice_similarity(a, b), 0.5)
        self.assertAlmostEqual(cosine_similarity(a, b), 0.5)

    def test_zero_vectors(self):
        a = [0, 0, 0, 0]
        b = [0, 0, 0, 0]
        self.assertEqual(jaccard_similarity(a, b), 1.0)
        self.assertEqual(dice_similarity(a, b), 1.0)
        self.assertEqual(cosine_similarity(a, b), 1.0)


if __name__ == "__main__":
    unittest.main()