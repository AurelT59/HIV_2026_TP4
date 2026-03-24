import unittest


class TestSeparateParenGroups(unittest.TestCase):
    def test_separate_simple_groups(self):
        """Should separate three groups correctly ignoring spaces"""
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])
    
    def test_separate_consecutive_simple_groups(self):
        """Should separate three consecutive simple groups"""
        self.assertEqual(separate_paren_groups('()()()'), ['()', '()', '()'])
    
    def test_separate_single_nested_group(self):
        """A single deeply nested group should be returned as one element"""
        self.assertEqual(separate_paren_groups('((()))'), ['((()))'])
    
    def test_separate_two_nested_groups(self):
        """Should separate two groups each with one level of nesting"""
        self.assertEqual(separate_paren_groups('(())(())'), ['(())', '(())'])
    
    def test_separate_single_simple_group(self):
        """A single simple group should return a list with one element"""
        self.assertEqual(separate_paren_groups('()'), ['()'])
    
    def test_empty_input(self):
        """Empty string should return empty list"""
        self.assertEqual(separate_paren_groups(''), [])
    
    def test_only_spaces(self):
        """String with only spaces should return empty list"""
        self.assertEqual(separate_paren_groups('     '), [])
    
    def test_separate_mixed_depth_groups(self):
        """Should handle groups with different nesting depths"""
        self.assertEqual(separate_paren_groups('()((()))(())'), ['()', '((()))', '(())'])
    
    def test_severe_nesting(self):
        """Should handle highly nested groups"""
        self.assertEqual(separate_paren_groups('((((()))))'), ['((((()))))'])
    
    def test_complex_mixed_case(self):
        """Should handle a complex mix of groups"""
        self.assertEqual(separate_paren_groups('() (()) ((())) (((())))'), ['()', '(())', '((()))', '(((())))'])
    
    def test_adjacent_groups_no_spaces(self):
        """Should separate adjacent groups without spaces"""
        self.assertEqual(separate_paren_groups('()(())(()())'), ['()', '(())', '(()())'])
    
    def test_one_balanced_group(self):
        """Single balanced pair"""
        self.assertEqual(separate_paren_groups('()'), ['()'])
    
    def test_multiple_same_nesting(self):
        """Multiple groups with same nesting level"""
        self.assertEqual(separate_paren_groups('(())(())(())'), ['(())', '(())', '(())'])
    
    def test_alternating_depths(self):
        """Alternating depth groups"""
        self.assertEqual(separate_paren_groups('()((()))()'), ['()', '((()))', '()'])


if __name__ == '__main__':
    unittest.main()