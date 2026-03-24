import unittest
from poly_llm.to_test.closest_integer import closest_integer

class TestClosestInteger(unittest.TestCase):
    def test_round_away_from_zero_positive(self):
        self.assertEqual(closest_integer("14.5"), 15, "14.5 should round up to 15")
        self.assertEqual(closest_integer("2.5"), 3, "2.5 should round up to 3")
        self.assertEqual(closest_integer("0.5"), 1, "0.5 should round up to 1")
        self.assertEqual(closest_integer("99.5"), 100, "99.5 should round up to 100")
    
    def test_round_away_from_zero_negative(self):
        self.assertEqual(closest_integer("-14.5"), -15, "-14.5 should round down to -15")
        self.assertEqual(closest_integer("-2.5"), -3, "-2.5 should round down to -3")
        self.assertEqual(closest_integer("-0.5"), -1, "-0.5 should round down to -1")
        self.assertEqual(closest_integer("-99.5"), -100, "-99.5 should round down to -100")
    
    def test_round_normal(self):
        self.assertEqual(closest_integer("10"), 10, "10 should return 10")
        self.assertEqual(closest_integer("15.3"), 15, "15.3 should round to 15")
        self.assertEqual(closest_integer("15.7"), 16, "15.7 should round to 16")
        self.assertEqual(closest_integer("0"), 0, "0 should return 0")
    
    def test_round_normal_negative(self):
        self.assertEqual(closest_integer("-10"), -10, "-10 should return -10")
        self.assertEqual(closest_integer("-15.3"), -15, "-15.3 should round to -15")
        self.assertEqual(closest_integer("-15.7"), -16, "-15.7 should round to -16")
    
    def test_trailing_zeros(self):
        self.assertEqual(closest_integer("14.50"), 15, "14.50 should round to 15")
        self.assertEqual(closest_integer("14.500"), 15, "14.500 should round to 15")
        self.assertEqual(closest_integer("-14.50"), -15, "-14.50 should round to -15")
    
    def test_edge_cases(self):
        self.assertEqual(closest_integer("0.1"), 0, "0.1 should round to 0")
        self.assertEqual(closest_integer("0.4"), 0, "0.4 should round to 0")
        self.assertEqual(closest_integer("0.6"), 1, "0.6 should round to 1")
        self.assertEqual(closest_integer("-0.1"), 0, "-0.1 should round to 0")
        self.assertEqual(closest_integer("-0.4"), 0, "-0.4 should round to 0")
        self.assertEqual(closest_integer("-0.6"), -1, "-0.6 should round to -1")
    
    def test_large_numbers(self):
        self.assertEqual(closest_integer("123456.5"), 123457, "123456.5 should round to 123457")
        self.assertEqual(closest_integer("-123456.5"), -123457, "-123456.5 should round to -123457")
        self.assertEqual(closest_integer("999999.9"), 1000000, "999999.9 should round to 1000000")
        self.assertEqual(closest_integer("-999999.9"), -1000000, "-999999.9 should round to -1000000")

if __name__ == '__main__':
    unittest.main()