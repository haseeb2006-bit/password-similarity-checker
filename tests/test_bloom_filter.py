import unittest
from src.bloom_filter import get_hash_positions, insert_bigram, get_fingerprint


class TestBloomFilter(unittest.TestCase):
    def test_hash_positions_deterministic(self):
        positions1 = get_hash_positions("ca", L=1000, K=20)
        positions2 = get_hash_positions("ca", L=1000, K=20)
        self.assertEqual(positions1, positions2)

    def test_hash_positions_count(self):
        positions = get_hash_positions("ca", L=1000, K=20)
        self.assertEqual(len(positions), 20)

    def test_hash_positions_in_range(self):
        positions = get_hash_positions("ca", L=1000, K=20)
        for position in positions:
            self.assertTrue(0 <= position < 1000)

    def test_insert_bigram_sets_bits(self):
        bit_array = [0] * 1000
        insert_bigram(bit_array, "ca", L=1000, K=20)
        self.assertGreater(sum(bit_array), 0)

    def test_fingerprint_length(self):
        fingerprint = get_fingerprint("cat", L=1000, K=20)
        self.assertEqual(len(fingerprint), 1000)


if __name__ == "__main__":
    unittest.main()