from poly_llm.to_test.file_name_check import file_name_check

def test_llm_file_name_check():
    assert file_name_check('example.txt') == 'Yes'
    assert file_name_check('1example.dll') == 'No'
    assert file_name_check('.txt') == 'No'
    assert file_name_check('example.txt') == 'Yes'
    assert file_name_check('1example.dll') == 'No'
    assert file_name_check('.txt') == 'No'
    assert file_name_check('example.txt') == 'Yes'
    assert file_name_check('1example.dll') == 'No'
    assert file_name_check('.txt') == 'No'
