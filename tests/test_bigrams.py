import unittest
from src.bigrams import get_bigrams


class TestBigrams(unittest.TestCase):
    def test_normal_word(self):
        self.assertEqual(get_bigrams("cat"), [' c', 'ca', 'at', 't '])

    def test_empty_string(self):
        self.assertEqual(get_bigrams(""), ['  '])

    def test_single_char(self):
        self.assertEqual(get_bigrams("a"), [' a', 'a '])


if __name__ == "__main__":
    unittest.main()