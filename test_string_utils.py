import unittest
from string_utils import is_palindrome

class TestStringUtils(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("Python"))

if __name__ == "__main__":
    unittest.main()
