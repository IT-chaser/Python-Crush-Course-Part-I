import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self):
        """Creat first name, last name and annual salary"""
        self.my_employee = Employee('John', 'Alex', 0)

    def test_give_default_raise(self):
        """Test that giving default raise works properly?"""
        self.assertEqual(self.my_employee.give_raise(), '$5,000')

    def test_give_custom_raise(self):
        """Test for giving custom raise works properly?"""
        self.assertEqual('$10,000', self.my_employee.give_raise('$10,000'))
if __name__ == '__main__':
    unittest.main()
