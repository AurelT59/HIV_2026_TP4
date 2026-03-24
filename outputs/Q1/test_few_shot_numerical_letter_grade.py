import unittest


class TestNumericalLetterGrade(unittest.TestCase):
    
    def test_top_grades(self):
        # Test highest grades (4.0 and near 4.0)
        self.assertEqual(numerical_letter_grade([4.0]), ['A+'], "4.0 GPA should be A+")
        self.assertEqual(numerical_letter_grade([3.8]), ['A'], "3.8 GPA should be A")
        self.assertEqual(numerical_letter_grade([3.9]), ['A'], "3.9 GPA should be A")
        # Test boundary at 3.7
        self.assertEqual(numerical_letter_grade([3.7]), ['A-'], "3.7 GPA should be A-")
        self.assertEqual(numerical_letter_grade([3.71]), ['A'], "3.71 GPA should be A")
        self.assertEqual(numerical_letter_grade([3.69]), ['A-'], "3.69 GPA should be A-")
        # Test A- range
        self.assertEqual(numerical_letter_grade([3.5]), ['A-'], "3.5 GPA should be A-")
        self.assertEqual(numerical_letter_grade([3.4]), ['A-'], "3.4 GPA should be A-")
        # Test boundary at 3.3
        self.assertEqual(numerical_letter_grade([3.3]), ['B+'], "3.3 GPA should be B+")
        self.assertEqual(numerical_letter_grade([3.31]), ['A-'], "3.31 GPA should be A-")
        self.assertEqual(numerical_letter_grade([3.29]), ['B+'], "3.29 GPA should be B+")
    
    def test_middle_grades(self):
        # Test B+ range
        self.assertEqual(numerical_letter_grade([3.1]), ['B+'], "3.1 GPA should be B+")
        self.assertEqual(numerical_letter_grade([3.01]), ['B+'], "3.01 GPA should be B+")
        # Test boundary at 3.0
        self.assertEqual(numerical_letter_grade([3.0]), ['B'], "3.0 GPA should be B")
        self.assertEqual(numerical_letter_grade([3.01]), ['B+'], "3.01 GPA should be B+")
        self.assertEqual(numerical_letter_grade([2.99]), ['B'], "2.99 GPA should be B")
        # Test B range
        self.assertEqual(numerical_letter_grade([2.8]), ['B'], "2.8 GPA should be B")
        self.assertEqual(numerical_letter_grade([2.75]), ['B'], "2.75 GPA should be B")
        # Test boundary at 2.7
        self.assertEqual(numerical_letter_grade([2.7]), ['B-'], "2.7 GPA should be B-")
        self.assertEqual(numerical_letter_grade([2.71]), ['B'], "2.71 GPA should be B")
        self.assertEqual(numerical_letter_grade([2.69]), ['B-'], "2.69 GPA should be B-")
        # Test B- range
        self.assertEqual(numerical_letter_grade([2.5]), ['B-'], "2.5 GPA should be B-")
        self.assertEqual(numerical_letter_grade([2.4]), ['B-'], "2.4 GPA should be B-")
        # Test boundary at 2.3
        self.assertEqual(numerical_letter_grade([2.3]), ['C+'], "2.3 GPA should be C+")
        self.assertEqual(numerical_letter_grade([2.31]), ['B-'], "2.31 GPA should be B-")
        self.assertEqual(numerical_letter_grade([2.29]), ['C+'], "2.29 GPA should be C+")
    
    def test_lower_grades(self):
        # Test C+ range
        self.assertEqual(numerical_letter_grade([2.1]), ['C+'], "2.1 GPA should be C+")
        self.assertEqual(numerical_letter_grade([2.01]), ['C+'], "2.01 GPA should be C+")
        # Test boundary at 2.0
        self.assertEqual(numerical_letter_grade([2.0]), ['C'], "2.0 GPA should be C")
        self.assertEqual(numerical_letter_grade([2.01]), ['C+'], "2.01 GPA should be C+")
        self.assertEqual(numerical_letter_grade([1.99]), ['C'], "1.99 GPA should be C")
        # Test C range
        self.assertEqual(numerical_letter_grade([1.8]), ['C'], "1.8 GPA should be C")
        self.assertEqual(numerical_letter_grade([1.75]), ['C'], "1.75 GPA should be C")
        # Test boundary at 1.7
        self.assertEqual(numerical_letter_grade([1.7]), ['C-'], "1.7 GPA should be C-")
        self.assertEqual(numerical_letter_grade([1.71]), ['C'], "1.71 GPA should be C")
        self.assertEqual(numerical_letter_grade([1.69]), ['C-'], "1.69 GPA should be C-")
        # Test C- range
        self.assertEqual(numerical_letter_grade([1.5]), ['C-'], "1.5 GPA should be C-")
        self.assertEqual(numerical_letter_grade([1.4]), ['C-'], "1.4 GPA should be C-")
        # Test boundary at 1.3
        self.assertEqual(numerical_letter_grade([1.3]), ['D+'], "1.3 GPA should be D+")
        self.assertEqual(numerical_letter_grade([1.31]), ['C-'], "1.31 GPA should be C-")
        self.assertEqual(numerical_letter_grade([1.29]), ['D+'], "1.29 GPA should be D+")
    
    def test_low_grades(self):
        # Test D+ range
        self.assertEqual(numerical_letter_grade([1.1]), ['D+'], "1.1 GPA should be D+")
        self.assertEqual(numerical_letter_grade([1.01]), ['D+'], "1.01 GPA should be D+")
        # Test boundary at 1.0
        self.assertEqual(numerical_letter_grade([1.0]), ['D'], "1.0 GPA should be D")
        self.assertEqual(numerical_letter_grade([1.01]), ['D+'], "1.01 GPA should be D+")
        self.assertEqual(numerical_letter_grade([0.99]), ['D'], "0.99 GPA should be D")
        # Test D range
        self.assertEqual(numerical_letter_grade([0.8]), ['D'], "0.8 GPA should be D")
        self.assertEqual(numerical_letter_grade([0.75]), ['D'], "0.75 GPA should be D")
        # Test boundary at 0.7
        self.assertEqual(numerical_letter_grade([0.7]), ['D-'], "0.7 GPA should be D-")
        self.assertEqual(numerical_letter_grade([0.71]), ['D'], "0.71 GPA should be D")
        self.assertEqual(numerical_letter_grade([0.69]), ['D-'], "0.69 GPA should be D-")
        # Test D- range
        self.assertEqual(numerical_letter_grade([0.5]), ['D-'], "0.5 GPA should be D-")
        self.assertEqual(numerical_letter_grade([0.1]), ['D-'], "0.1 GPA should be D-")
        # Test boundary at 0.0
        self.assertEqual(numerical_letter_grade([0.0]), ['E'], "0.0 GPA should be E")
        self.assertEqual(numerical_letter_grade([0.01]), ['D-'], "0.01 GPA should be D-")
    
    def test_negative_grades(self):
        # Test edge case with negative GPA (if applicable)
        self.assertEqual(numerical_letter_grade([-1.0]), ['E'], "-1.0 GPA should be E")
        self.assertEqual(numerical_letter_grade([-0.5]), ['E'], "-0.5 GPA should be E")
    
    def test_multiple_grades(self):
        # Test the example from the docstring
        self.assertEqual(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]), ['A+', 'B', 'C-', 'C', 'A-'])
        # Test a variety of grades
        self.assertEqual(numerical_letter_grade([4.0, 3.8, 3.5, 2.8, 1.5, 0.5, 0.0]), 
                        ['A+', 'A', 'A-', 'B', 'C-', 'D-', 'E'])
        # Test with duplicate grades
        self.assertEqual(numerical_letter_grade([3.0, 3.0, 3.0]), ['B', 'B', 'B'])
    
    def test_empty_list(self):
        # Test edge case with empty list
        self.assertEqual(numerical_letter_grade([]), [])


if __name__ == '__main__':
    unittest.main()