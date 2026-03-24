import unittest

class TestNumericalLetterGrade(unittest.TestCase):
    
    def test_basic_grades(self):
        """Test basic grade conversions from the example"""
        grades = [4.0, 3.0, 1.7, 2.0, 3.5]
        expected = ['A+', 'B', 'C-', 'C', 'A-']
        self.assertEqual(numerical_letter_grade(grades), expected)
    
    def test_boundary_values_exact_4_0(self):
        """Test exact 4.0 GPA"""
        self.assertEqual(numerical_letter_grade([4.0]), ['A+'])
    
    def test_boundary_values_above_3_7(self):
        """Test GPAs just above 3.7"""
        self.assertEqual(numerical_letter_grade([3.71]), ['A'])
        self.assertEqual(numerical_letter_grade([3.8]), ['A'])
        self.assertEqual(numerical_letter_grade([3.9]), ['A'])
    
    def test_boundary_values_exact_3_7(self):
        """Test exact 3.7 GPA - should be A- since condition is > 3.7"""
        self.assertEqual(numerical_letter_grade([3.7]), ['A-'])
    
    def test_boundary_values_above_3_3(self):
        """Test GPAs in A- range"""
        self.assertEqual(numerical_letter_grade([3.31]), ['A-'])
        self.assertEqual(numerical_letter_grade([3.5]), ['A-'])
    
    def test_boundary_values_above_3_0(self):
        """Test GPAs in B+ range"""
        self.assertEqual(numerical_letter_grade([3.01]), ['B+'])
        self.assertEqual(numerical_letter_grade([3.2]), ['B+'])
    
    def test_boundary_values_exact_3_0(self):
        """Test exact 3.0 GPA - should be B since condition is > 3.0"""
        self.assertEqual(numerical_letter_grade([3.0]), ['B'])
    
    def test_boundary_values_above_2_7(self):
        """Test GPAs in B range"""
        self.assertEqual(numerical_letter_grade([2.71]), ['B'])
        self.assertEqual(numerical_letter_grade([2.8]), ['B'])
    
    def test_boundary_values_above_2_3(self):
        """Test GPAs in B- range"""
        self.assertEqual(numerical_letter_grade([2.31]), ['B-'])
        self.assertEqual(numerical_letter_grade([2.5]), ['B-'])
    
    def test_boundary_values_above_2_0(self):
        """Test GPAs in C+ range"""
        self.assertEqual(numerical_letter_grade([2.01]), ['C+'])
        self.assertEqual(numerical_letter_grade([2.2]), ['C+'])
    
    def test_boundary_values_exact_2_0(self):
        """Test exact 2.0 GPA - should be C since condition is > 2.0"""
        self.assertEqual(numerical_letter_grade([2.0]), ['C'])
    
    def test_boundary_values_above_1_7(self):
        """Test GPAs in C range"""
        self.assertEqual(numerical_letter_grade([1.71]), ['C'])
        self.assertEqual(numerical_letter_grade([1.9]), ['C'])
    
    def test_boundary_values_above_1_3(self):
        """Test GPAs in C- range"""
        self.assertEqual(numerical_letter_grade([1.31]), ['C-'])
        self.assertEqual(numerical_letter_grade([1.5]), ['C-'])
    
    def test_boundary_values_above_1_0(self):
        """Test GPAs in D+ range"""
        self.assertEqual(numerical_letter_grade([1.01]), ['D+'])
        self.assertEqual(numerical_letter_grade([1.2]), ['D+'])
    
    def test_boundary_values_exact_1_0(self):
        """Test exact 1.0 GPA - should be D since condition is > 1.0"""
        self.assertEqual(numerical_letter_grade([1.0]), ['D'])
    
    def test_boundary_values_above_0_7(self):
        """Test GPAs in D range"""
        self.assertEqual(numerical_letter_grade([0.71]), ['D'])
        self.assertEqual(numerical_letter_grade([0.9]), ['D'])
    
    def test_boundary_values_exact_0_7(self):
        """Test exact 0.7 GPA - should be D- since condition is > 0.7"""
        self.assertEqual(numerical_letter_grade([0.7]), ['D-'])
    
    def test_boundary_values_above_0_0(self):
        """Test GPAs in D- range"""
        self.assertEqual(numerical_letter_grade([0.01]), ['D-'])
        self.assertEqual(numerical_letter_grade([0.5]), ['D-'])
    
    def test_boundary_values_exact_0_0(self):
        """Test exact 0.0 GPA - should be E"""
        self.assertEqual(numerical_letter_grade([0.0]), ['E'])
    
    def test_negative_gpa(self):
        """Test negative GPA values - should be E"""
        self.assertEqual(numerical_letter_grade([-1.0]), ['E'])
        self.assertEqual(numerical_letter_grade([-0.5]), ['E'])
    
    def test_multiple_grades(self):
        """Test multiple grades in one call"""
        grades = [4.0, 3.8, 3.5, 2.5, 1.5, 0.5, 0.0]
        expected = ['A+', 'A', 'A-', 'B-', 'C-', 'D-', 'E']
        self.assertEqual(numerical_letter_grade(grades), expected)
    
    def test_empty_list(self):
        """Test empty list input"""
        self.assertEqual(numerical_letter_grade([]), [])
    
    def test_all_same_grades(self):
        """Test list with all same grades"""
        grades = [3.5, 3.5, 3.5]
        expected = ['A-', 'A-', 'A-']
        self.assertEqual(numerical_letter_grade(grades), expected)

if __name__ == '__main__':
    unittest.main()