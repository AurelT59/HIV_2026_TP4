import unittest


class TestFindClosestElements(unittest.TestCase):
    def test_basic_cases_from_docstring(self):
        # Test case from docstring
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))
        
        # Test case with duplicate numbers from docstring
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))

    def test_simple_positive_numbers(self):
        # Adjacent numbers are closest
        self.assertEqual(find_closest_elements([1.0, 2.0, 5.0, 10.0]), (1.0, 2.0))
        
        # Numbers with different spacing
        self.assertEqual(find_closest_elements([1.0, 3.0, 6.0, 10.0, 15.0]), (1.0, 3.0))

    def test_negative_numbers(self):
        # All negative numbers
        self.assertEqual(find_closest_elements([-5.0, -3.0, -10.0, -2.0]), (-3.0, -2.0))
        
        # Mixed positive and negative
        self.assertEqual(find_closest_elements([-2.0, -1.0, 1.0, 2.0]), (-1.0, 1.0))

    def test_decimal_numbers(self):
        # With decimal precision
        self.assertEqual(find_closest_elements([1.11, 1.12, 5.5, 10.0]), (1.11, 1.12))
        
        # Small differences
        self.assertEqual(find_closest_elements([1.0001, 1.0002, 1.0003]), (1.0002, 1.0003))

    def test_duplicate_values(self):
        # Multiple duplicates
        self.assertEqual(find_closest_elements([3.0, 3.0, 5.0, 7.0]), (3.0, 3.0))
        
        # All same values
        self.assertEqual(find_closest_elements([2.0, 2.0, 2.0, 2.0]), (2.0, 2.0))

    def test_large_numbers(self):
        # Large values
        self.assertEqual(find_closest_elements([1000000.0, 1000001.0, 2000000.0]), (1000000.0, 1000001.0))

    def test_only_two_elements(self):
        # Minimal input
        self.assertEqual(find_closest_elements([1.5, 2.5]), (1.5, 2.5))

    def test_unsorted_input(self):
        # Random order input
        self.assertEqual(find_closest_elements([10.0, 1.0, 5.0, 2.1, 3.0]), (2.1, 3.0))

    def test_float_precision(self):
        # Test with very small differences
        result = find_closest_elements([1.0, 1.0 + 1e-10, 2.0])
        self.assertEqual(result, (1.0, 1.0 + 1e-10))

if __name__ == '__main__':
    unittest.main()