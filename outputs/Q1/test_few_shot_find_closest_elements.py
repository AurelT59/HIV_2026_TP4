import unittest
from poly_llm.to_test.find_closest_elements import find_closest_elements

class TestFindClosestElements(unittest.TestCase):
    def test_closest_elements_basic(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2), "Closest pair should be (2.0, 2.2)")
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0), "Closest pair should be (2.0, 2.0) (duplicates)")

    def test_closest_elements_two_elements(self):
        self.assertEqual(find_closest_elements([5.0, 1.0]), (1.0, 5.0), "With two elements, they are returned in sorted order")
        self.assertEqual(find_closest_elements([1.0, 5.0]), (1.0, 5.0), "Two elements in sorted order")

    def test_closest_elements_ordered(self):
        result = find_closest_elements([3.0, 1.0, 7.0, 4.0])
        self.assertLessEqual(result[0], result[1], "First element should be smaller than or equal to the second")
        # Note: closest in [3,1,7,4] is (3,4) with distance 1 or (1,3) with distance 2, (4,7) distance 3 → (3,4)
        self.assertEqual(find_closest_elements([3.0, 1.0, 7.0, 4.0]), (3.0, 4.0), "Closest pair in unsorted list")

    def test_closest_elements_negative_numbers(self):
        self.assertEqual(find_closest_elements([-1.0, -2.0, -3.0, -4.0, -2.1]), (-2.0, -2.1), "Negative numbers with decimal")

    def test_closest_elements_mixed_signs(self):
        self.assertEqual(find_closest_elements([-1.0, 0.0, 1.0, 0.1]), (0.0, 0.1), "Mixed signs: closest is near zero")

    def test_closest_elements_identical_values(self):
        self.assertEqual(find_closest_elements([5.0, 5.0, 10.0]), (5.0, 5.0), "Duplicate identical values should be selected")

    def test_closest_elements_float_precision(self):
        # Test with small differences that highlight float precision
        self.assertEqual(find_closest_elements([1.0, 1.0000000001, 2.0]), (1.0, 1.0000000001), "Very close floats")

    def test_closest_elements_all_same(self):
        self.assertEqual(find_closest_elements([7.0, 7.0, 7.0]), (7.0, 7.0), "All elements same: first two should be returned")

    def test_closest_elements_large_list(self):
        nums = list(range(1, 100)) + [101.5, 101.6]
        self.assertEqual(find_closest_elements(nums), (101.5, 101.6), "Large list: closest pair at end")

    def test_closest_elements_reverse_order(self):
        self.assertEqual(find_closest_elements([10.0, 9.0, 8.0, 1.5, 1.4]), (1.4, 1.5), "Reverse sorted with closest pair at end")

    def test_closest_elements_symmetry(self):
        # Order in the list shouldn't affect which pair is returned
        list1 = [1.0, 2.1, 3.0, 2.0]
        list2 = [3.0, 2.0, 1.0, 2.1]
        result1 = find_closest_elements(list1)
        result2 = find_closest_elements(list2)
        self.assertEqual(result1, result2, "Order of input should not affect result")

    def test_closest_elements_minimum_distance_zero(self):
        """Test when minimum possible distance (0) exists (duplicates)."""
        self.assertEqual(find_closest_elements([10.0, 5.0, 10.0]), (10.0, 10.0), "Duplicate values have zero distance")

    def test_closest_elements_single_pair_with_ties(self):
        # When multiple pairs have same distance, function returns first found
        # In our case, the first encountered pair with min distance wins
        # Let's calculate: [1,3] diff=2, [3,5] diff=2, [1,2] diff=1 → (1,2)
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 5.0]), (1.0, 2.0), "Tie-breaking: first smallest difference wins")

    def test_closest_elements_string_in_list_throws_error(self):
        # This test is excluded because it's not applicable; the function doesn't validate input types
        # But if needed, we could test for TypeErrors here
        pass

if __name__ == "__main__":
    unittest.main()