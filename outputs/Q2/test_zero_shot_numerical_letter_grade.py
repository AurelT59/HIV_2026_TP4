from poly_llm.to_test.numerical_letter_grade import numerical_letter_grade

def test_llm_numerical_letter_grade():
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
    assert numerical_letter_grade([1.2]) == ['D+']
    assert numerical_letter_grade([4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0]) == ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+']
    assert numerical_letter_grade([3.0, 2.0, 1.0]) == ['C', 'B', 'A']
    assert numerical_letter_grade([0.0, -1.0]) == ['D', 'F']
    assert numerical_letter_grade([]) == []
