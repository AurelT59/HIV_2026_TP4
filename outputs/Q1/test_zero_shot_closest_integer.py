import unittest

class TestClosestInteger(unittest.TestCase):
    
    def test_normal_integers(self):
        """Test with actual integers (no decimal point)"""
        self.assertEqual(closest_integer("10"), 10)
        self.assertEqual(closest_integer("0"), 0)
        self.assertEqual(closest_integer("-5"), -5)
        self.assertEqual(closest_integer("100"), 100)
    
    def test_normal_decimals_below_half(self):
        """Test with decimals less than .5"""
        self.assertEqual(closest_integer("14.4"), 14)
        self.assertEqual(closest_integer("10.1"), 10)
        self.assertEqual(closest_integer("-14.4"), -14)
        self.assertEqual(closest_integer("-10.1"), -10)
    
    def test_normal_decimals_above_half(self):
        """Test with decimals greater than .5"""
        self.assertEqual(closest_integer("14.6"), 15)
        self.assertEqual(closest_integer("10.9"), 11)
        self.assertEqual(closest_integer("-14.6"), -15)
        self.assertEqual(closest_integer("-10.9"), -11)
    
    def test_exact_half_positive(self):
        """Test .5 case for positive numbers - should round away from zero"""
        self.assertEqual(closest_integer("14.5"), 15)
        self.assertEqual(closest_integer("0.5"), 1)
        self.assertEqual(closest_integer("100.5"), 101)
    
    def test_exact_half_negative(self):
        """Test .5 case for negative numbers - should round away from zero"""
        self.assertEqual(closest_integer("-14.5"), -15)
        self.assertEqual(closest_integer("-0.5"), -1)
        self.assertEqual(closest_integer("-100.5"), -101)
    
    def test_trailing_zeros(self):
        """Test that trailing zeros are handled correctly"""
        self.assertEqual(closest_integer("14.50"), 15)
        self.assertEqual(closest_integer("14.500"), 15)
        self.assertEqual(closest_integer("-14.50"), -15)
    
    def test_very_small_numbers(self):
        """Test with very small numbers"""
        self.assertEqual(closest_integer("0.1"), 0)
        self.assertEqual(closest_integer("0.4"), 0)
        self.assertEqual(closest_integer("0.6"), 1)
        self.assertEqual(closest_integer("0.9"), 1)
    
    def test_negative_rounding(self):
        """Test rounding behavior with negative numbers"""
        self.assertEqual(closest_integer("-0.1"), 0)
        self.assertEqual(closest_integer("-0.4"), 0)
        self.assertEqual(closest_integer("-0.6"), -1)
        self.assertEqual(closest_integer("-0.9"), -1)
    
    def test_special_cases(self):
        """Test special edge cases"""
        self.assertEqual(closest_integer("0.0"), 0)
        self.assertEqual(closest_integer("-0.0"), 0)

if __name__ == '__main__':
    unittest.main()