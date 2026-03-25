from poly_llm.to_test.separate_paren_groups import separate_paren_groups

def test_llm_separate_paren_groups():
    assert separate_paren_groups('(()()) ((())) () ((())()())') == ['(()())', '((()))', '()', '((())()())']
    assert separate_paren_groups('() (()) ((())) (((())))') == ['()', '(())', '((()))', '(((())))']
    assert separate_paren_groups('(()()) ((())) () ((())()())') == ['(()())', '((()))', '()', '((())()())']
    assert separate_paren_groups('() (()) ((())) (((())))') == ['()', '(())', '((()))', '(((())))']
    assert separate_paren_groups('(()()) ((())) () ((())()())') == ['(()())', '((()))', '()', '((())()())']
    assert separate_paren_groups('() (()) ((())) (((())))') == ['()', '(())', '((()))', '(((())))']
    assert separate_paren_groups('((()))') == ['((()))']
    assert separate_paren_groups('()') == ['()']
    assert separate_paren_groups('((()))') == ['((()))']
    assert separate_paren_groups('((()))') == ['((()))']
    assert separate_paren_groups('((()))') == ['((()))']
    assert separate_paren_groups('((()))') == ['((()))']
    assert separate_paren_groups('((()))') == ['((()))']
    assert separate_paren_groups('((()))')
