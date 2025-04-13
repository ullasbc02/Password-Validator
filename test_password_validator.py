import unittest
from password_validator2 import validate_password

class TestPasswordValidator(unittest.TestCase):
    def test_valid_passwords(self):
        self.assertTrue(validate_password("StrongPass1!"))
        self.assertTrue(validate_password("Aa1!aaba"))  # no repetition

    def test_length_constraints(self):
        self.assertFalse(validate_password("A1b!"))  # too short
        self.assertFalse(validate_password("A1b!ccccccccccccccccc!"))  # too long

    def test_missing_requirements(self):
        self.assertFalse(validate_password("abcdefg1!"))  # no uppercase
        self.assertFalse(validate_password("ABCDEFG1!"))  # no lowercase
        self.assertFalse(validate_password("Abcdefgh!"))  # no digit
        self.assertFalse(validate_password("Abcdefg1"))   # no special char

    def test_invalid_characters(self):
        self.assertFalse(validate_password("Abc1234<"))
        self.assertFalse(validate_password("Abc1234{"))
        self.assertFalse(validate_password("Abc 1234!"))

    def test_repeating_characters(self):
        self.assertFalse(validate_password("AAAabc123!"))
        self.assertFalse(validate_password("abc!!!123A"))  
        self.assertFalse(validate_password("Aa1!aaaa"))   
        self.assertFalse(validate_password("Aa1!aaaaaaaaaaaaaaaa"))

    def test_edge_lengths(self):
        self.assertFalse(validate_password("Aa1!aaab"))    
        self.assertFalse(validate_password("Aa1!" + "a" * 15)) 

    def test_non_string_inputs(self):
        self.assertFalse(validate_password(12345678))
        self.assertFalse(validate_password(None))
        self.assertFalse(validate_password(["Abc123!"]))

if __name__ == '__main__':
    unittest.main()
