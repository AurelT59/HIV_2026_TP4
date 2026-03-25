from poly_llm.to_test.closest_integer import closest_integer

def test_llm_closest_integer():
    assert closest_integer('10') == 10
    assert closest_integer('14.5') == 15
    assert closest_integer('10') == 10
    assert closest_integer('14.5') == 15
    assert closest_integer('10') == 10
    assert closest_integer('14.5') == 15
    assert closest_integer('-14.5') == -15
    assert closest_integer('-10.5') == -10
    assert closest_integer('-14.4') == -14
    assert closest_integer('-14.5') == -14
    assert closest_integer('-14.6') == -14
    assert closest_integer('-14.7') == -14
    assert closest_integer('-14.8') == -14
    assert closest_integer('-14.9') == -14
    assert closest_integer('-14.99') == -14
    assert closest_integer('-14.999') == -14
    assert closest_integer('-14.9999') == -14
    assert closest_integer('-14.999999') == -14
    assert closest_integer('-14.9999999') == -14
