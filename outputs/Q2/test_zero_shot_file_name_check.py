from poly_llm.to_test.file_name_check import file_name_check

def test_llm_file_name_check():
    assert file_name_check('example.txt') == 'Yes'
    assert file_name_check('1example.dll') == 'No'
    assert file_name_check('.txt') == 'No'
    assert file_name_check('test.txt') == 'Yes'
    assert file_name_check('test.exe') == 'No'
    assert file_name_check('test.dll') == 'No'
    assert file_name_check('test.1') == 'No'
    assert file_name_check('test.2') == 'No'
    assert file_name_check('test.3') == 'No'
    assert file_name_check('test.4') == 'No'
    assert file_name_check('test.5') == 'No'
    assert file_name_check('test.6') == 'No'
    assert file_name_check('test.7') == 'No'
    assert file_name_check('test.8') == 'No'
    assert file_name_check('test.9') == 'No'
    assert file_name_check('test.10') == 'No'
