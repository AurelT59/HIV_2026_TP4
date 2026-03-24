import unittest

class TestFileNameCheck(unittest.TestCase):
    
    def test_valid_files(self):
        """Test valid file names that should return 'Yes'"""
        # Basic valid files
        self.assertEqual(file_name_check("example.txt"), 'Yes')
        self.assertEqual(file_name_check("file.exe"), 'Yes')
        self.assertEqual(file_name_check("document.dll"), 'Yes')
        
        # Valid files with digits (up to 3)
        self.assertEqual(file_name_check("a1b2c3.txt"), 'Yes')
        self.assertEqual(file_name_check("test123.exe"), 'Yes')
        self.assertEqual(file_name_check("file1.dll"), 'Yes')
        self.assertEqual(file_name_check("abc123.txt"), 'Yes')
        
        # Valid files with uppercase letters
        self.assertEqual(file_name_check("EXAMPLE.txt"), 'Yes')
        self.assertEqual(file_name_check("File.EXE"), 'Yes')
        self.assertEqual(file_name_check("A1b2c3.dll"), 'Yes')
        
    def test_invalid_files_no_dot(self):
        """Test files without dot"""
        self.assertEqual(file_name_check("exampletxt"), 'No')
        self.assertEqual(file_name_check("example"), 'No')
        self.assertEqual(file_name_check(".txt"), 'No')
    
    def test_invalid_files_multiple_dots(self):
        """Test files with multiple dots"""
        self.assertEqual(file_name_check("file.name.txt"), 'No')
        self.assertEqual(file_name_check("a.b.c.exe"), 'No')
    
    def test_invalid_files_wrong_extension(self):
        """Test files with invalid extensions"""
        self.assertEqual(file_name_check("file.pdf"), 'No')
        self.assertEqual(file_name_check("file.doc"), 'No')
        self.assertEqual(file_name_check("file.txt.exe"), 'No')
        self.assertEqual(file_name_check("file.java"), 'No')
    
    def test_invalid_files_empty_before_dot(self):
        """Test files with empty substring before dot"""
        self.assertEqual(file_name_check(".txt"), 'No')
        self.assertEqual(file_name_check(".exe"), 'No')
        self.assertEqual(file_name_check(".dll"), 'No')
    
    def test_invalid_files_no_letter_start(self):
        """Test files that don't start with a letter"""
        self.assertEqual(file_name_check("1example.dll"), 'No')
        self.assertEqual(file_name_check("123file.txt"), 'No')
        self.assertEqual(file_name_check("_file.exe"), 'No')
        self.assertEqual(file_name_check("-file.dll"), 'No')
        self.assertEqual(file_name_check(".txt"), 'No')
    
    def test_invalid_files_too_many_digits(self):
        """Test files with more than 3 digits"""
        self.assertEqual(file_name_check("file1234.txt"), 'No')
        self.assertEqual(file_name_check("a1b2c3d4.exe"), 'No')
        self.assertEqual(file_name_check("12345.dll"), 'No')
    
    def test_edge_cases(self):
        """Test edge cases"""
        # Single character valid file name
        self.assertEqual(file_name_check("a.txt"), 'Yes')
        
        # Single character invalid (not starting with letter)
        self.assertEqual(file_name_check("1.txt"), 'No')
        
        # Mixed case extensions (should be invalid as only lowercase are accepted)
        self.assertEqual(file_name_check("file.TXT"), 'No')
        self.assertEqual(file_name_check("file.Exe"), 'No')
        
        # Spaces (invalid)
        self.assertEqual(file_name_check("file name.txt"), 'No')

if __name__ == '__main__':
    unittest.main()