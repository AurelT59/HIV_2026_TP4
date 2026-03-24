import unittest


class TestSeparateParenGroups(unittest.TestCase):
    def test_basic_example(self):
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])

    def test_single_group(self):
        self.assertEqual(separate_paren_groups('((()))'), ['((()))'])

    def test_multiple_simple_groups(self):
        self.assertEqual(separate_paren_groups('()()()'), ['()', '()', '()'])

    def test_nested_groups(self):
        self.assertEqual(separate_paren_groups('(()())(()(()))'), ['(()())', '(()(()))'])

    def test_with_spaces(self):
        self.assertEqual(separate_paren_groups('( ) ( ( ) )'), ['()', '(())'])

    def test_empty_string(self):
        self.assertEqual(separate_paren_groups(''), [])

    def test_only_spaces(self):
        self.assertEqual(separate_paren_groups('   '), [])

    def test_complex_mixed(self):
        self.assertEqual(
            separate_paren_groups('() (()) (())() ((()))'), 
            ['()', '(())', '(())()', '((()))']
        )

    def test_unbalanced_should_not_affect(self):
        # Note: The function assumes balanced input as per specification
        # This test verifies behavior for balanced inputs
        self.assertEqual(separate_paren_groups('( ( ) ( ) )'), ['(())'])

if __name__ == '__main__':
    unittest.main()