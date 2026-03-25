from poly_llm.to_test.closest_integer import closest_integer

def test_llm_closest_integer():
    assert closest_integer('10') == 10
    assert closest_integer('14.5') == 15
    assert closest_integer('10') == 10
    assert closest_integer('10') == 10
    assert closest_integer('-10') == -10
    assert closest_integer('14.5') == 15
    assert closest_integer('-14.5') == -15
    assert closest_integer('-14.4') == -14
    assert closest_integer('14.4') == 14
    assert closest_integer('-14.3') == -14
    assert closest_integer('14.3') == 14
    assert closest_integer('-14.2') == -14
    assert closest_integer('14.2') == 14
    assert closest_integer('-14.1') == -14
    assert closest_integer('14.1') == 14
    assert closest_integer('-14.0') == -14
    assert closest_integer('14.0') == 14
    assert closest_integer('-14.9') == -15
    assert closest_integer('14.9') == 15
