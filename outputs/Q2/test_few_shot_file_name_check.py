from poly_llm.to_test.file_name_check import file_name_check

def test_llm_file_name_check():
    assert file_name_check('example.txt') == 'Yes'
    assert file_name_check('1example.dll') == 'No'
    assert file_name_check('.txt') == 'No'
    assert file_name_check('example.txt') == 'Yes'
    assert file_name_check('example.txt') == 'Yes'
    assert file_name_check('example.exe') == 'No'
    assert file_name_check('example.dll') == 'No'
    assert file_name_check('example') == 'No'
    assert file_name_check('example.1.txt') == 'No'
    assert file_name_check('example.1.2.txt') == 'No'
    assert file_name_check('example.1.2.3.txt') == 'No'
    assert file_name_check('example.1.2.3.4.txt') == 'No'
    assert file_name_check('example.1.2.3.4.5.txt') == 'No'
    assert file_name_check('example.1.2.3.4.5.6.txt') == 'No'
    assert file_name_check('example.
