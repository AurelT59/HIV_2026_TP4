from poly_llm.to_test.find_closest_elements import find_closest_elements

def test_llm_find_closest_elements():
    assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
    assert find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)
    assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
    assert find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)
    assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
    assert find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)
    assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2, 3.9]) == (3.9, 3.9)
    assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2, 3.9, 4.0]) == (3.9, 4.0)
    assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5
