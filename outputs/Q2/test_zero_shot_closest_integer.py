from poly_llm.to_test.closest_integer import closest_integer

def test_llm_closest_integer():
    assert closest_integer('10') == 10
    assert closest_integer('14.5') == 15
    assert closest_integer("0") == 0
    assert closest_integer("1") == 1
    assert closest_integer("2") == 2
    assert closest_integer("3") == 3
    assert closest_integer("4") == 4
    assert closest_integer("5") == 5
    assert closest_integer("6") == 6
    assert closest_integer("7") == 7
    assert closest_integer("8") == 8
    assert closest_integer("9") == 9
    assert closest_integer("10") == 10
    assert closest_integer("11") == 11
    assert closest_integer("12") == 12
    assert closest_integer("13") == 13
    assert closest_integer("14") == 14
    assert closest_integer("15") == 15
    assert closest_integer("16") == 16
    assert closest_integer("17") == 17
    assert closest_integer("18") == 18
    assert closest_integer("19") == 19
