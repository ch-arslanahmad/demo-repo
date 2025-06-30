import unittest
from list_manager import add_to_list  # Import the function to be tested

class TestListManager(unittest.TestCase):
    # Test if the add_to_list function works correctly
    def test_add_to_list(self):
        my_list = []  # Start with an empty list
        
        # Test if adding a value works
        self.assertEqual(add_to_list(my_list, 5), [5])  # Add 5 to the list
        self.assertEqual(add_to_list(my_list, 10), [5, 10])  # Add 10 to the list
        self.assertEqual(add_to_list(my_list, -3), [5, 10, -3])  # Add -3 to the list

if __name__ == "__main__":
    unittest.main()
