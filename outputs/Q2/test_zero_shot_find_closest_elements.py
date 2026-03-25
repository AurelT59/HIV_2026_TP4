from poly_llm.to_test.find_closest_elements import find_closest_elements

def test_llm_find_closest_elements():
    assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
    assert find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)
    assert find_closest_elements([1, 2, 3, 4, 5]) == (4, 5)
    assert find_closest_elements([1, 2, 3, 4, 5, 6]) == (4, 5)
    assert find_closest_elements([1, 2, 3, 4, 5, 6, 7]) == (5, 6)
    assert find_closest_elements([1, 2, 3, 4, 5, 6, 7, 8]) == (6, 7)
    assert find_closest_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]) == (7, 8)
    assert find_closest_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == (8, 9)
    assert find_closest_elements([1, 2, 3, 4, 5, 6
