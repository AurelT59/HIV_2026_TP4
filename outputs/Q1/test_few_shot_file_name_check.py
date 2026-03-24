import unittest

class TestFileNameCheck(unittest.TestCase):
    
    def test_valid_file_names(self):
        """Test various valid file names that meet all criteria."""
        self.assertEqual(file_name_check("example.txt"), 'Yes', "example.txt is a valid file name")
        self.assertEqual(file_name_check("myFile.exe"), 'Yes', "myFile.exe is a valid file name")
        self.assertEqual(file_name_check("abc123.dll"), 'Yes', "abc123.dll is a valid file name (3 digits allowed)")
        self.assertEqual(file_name_check("A.txt"), 'Yes', "A.txt is a valid file name (single letter)")
        self.assertEqual(file_name_check("a1b2c3.exe"), 'Yes', "a1b2c3.exe is valid (exactly 3 digits)")
        self.assertEqual(file_name_check("MyDocument.txt"), 'Yes', "MyDocument.txt is valid with mixed case")
    
    def test_invalid_starts_with_digit(self):
        """Test file names that start with a digit (invalid)."""
        self.assertEqual(file_name_check("1example.dll"), 'No', "1example.dll is invalid: starts with a digit")
        self.assertEqual(file_name_check("9test.txt"), 'No', "9test.txt is invalid: starts with a digit")
        self.assertEqual(file_name_check("0abc.exe"), 'No', "0abc.exe is invalid: starts with a digit")
        self.assertEqual(file_name_check("12345.txt"), 'No', "12345.txt is invalid: starts with a digit")
    
    def test_invalid_extension(self):
        """Test file names with unsupported extensions."""
        self.assertEqual(file_name_check("example.pdf"), 'No', "example.pdf is invalid: unsupported extension")
        self.assertEqual(file_name_check("file.mp3"), 'No', "file.mp3 is invalid: unsupported extension")
        self.assertEqual(file_name_check("document.docx"), 'No', "document.docx is invalid: unsupported extension")
        self.assertEqual(file_name_check("script.py"), 'No', "script.py is invalid: unsupported extension")
        self.assertEqual(file_name_check("binary.bin"), 'No', "binary.bin is invalid: unsupported extension")
    
    def test_empty_name_before_dot(self):
        """Test file names with empty substring before the dot."""
        self.assertEqual(file_name_check(".txt"), 'No', ".txt is invalid: empty name before dot")
        self.assertEqual(file_name_check(".exe"), 'No', ".exe is invalid: empty name before dot")
        self.assertEqual(file_name_check(".dll"), 'No', ".dll is invalid: empty name before dot")
    
    def test_no_dot_in_name(self):
        """Test file names without a dot (no extension)."""
        self.assertEqual(file_name_check("example"), 'No', "example is invalid: no dot")
        self.assertEqual(file_name_check("testdll"), 'No', "testdll is invalid: no dot")
    
    def test_multiple_dots(self):
        """Test file names with multiple dots."""
        self.assertEqual(file_name_check("example.txt.bak"), 'No', "example.txt.bak is invalid: multiple dots")
        self.assertEqual(file_name_check("my.a.exe"), 'No', "my.a.exe is invalid: multiple dots")
    
    def test_more_than_three_digits(self):
        """Test file names with more than 3 digits."""
        self.assertEqual(file_name_check("abc1234.txt"), 'No', "abc1234.txt is invalid: 4 digits (exceeds limit)")
        self.assertEqual(file_name_check("a1b2c3d4.exe"), 'No', "a1b2c3d4.exe is invalid: 4 digits")
        self.assertEqual(file_name_check("test12345.dll"), 'No', "test12345.dll is invalid: 5 digits")
    
    def test_digits_in_extension(self):
        """Test that digits in the extension are handled correctly."""
        # Note: The function only checks if the extension is in ['txt', 'exe', 'dll']
        # So 'txt1' would fail because it's not exactly 'txt'
        self.assertEqual(file_name_check("example.txt1"), 'No', "example.txt1 is invalid: extension not exact match")
        self.assertEqual(file_name_check("file.t1xt"), 'No', "file.t1xt is invalid: extension not exact match")
    
    def test_uppercase_extensions(self):
        """Test that uppercase extensions are invalid (case-sensitive check)."""
        self.assertEqual(file_name_check("example.TXT"), 'No', "example.TXT is invalid: extension must be lowercase")
        self.assertEqual(file_name_check("file.EXE"), 'No', "file.EXE is invalid: extension must be lowercase")
        self.assertEqual(file_name_check("doc.DLL"), 'No', "doc.DLL is invalid: extension must be lowercase")
    
    def test_edge_cases(self):
        """Test edge cases."""
        self.assertEqual(file_name_check("a.txt"), 'Yes', "a.txt is valid: minimal valid name")
        self.assertEqual(file_name_check("Z123.exe"), 'Yes', "Z123.exe is valid: starts with letter, 3 digits")
        self.assertEqual(file_name_check(""), 'No', "empty string is invalid: no dot")
        self.assertEqual(file_name_check("file"), 'No', "file without extension is invalid")
        self.assertEqual(file_name_check("..txt"), 'No', "..txt is invalid: empty name before dot")
        self.assertEqual(file_name_check("file."), 'No', "file. is invalid: empty extension")