import unittest
from unittest.mock import patch
from employee import Employee

# References https://www.youtube.com/watch?v=6tNS--WetLI
# Best practices:
# Tests should be isolated. Should run independed of other tests
# Adding tests to existing code
# Test-driven development
# Write test before you write the code
# What do you want code to do?
# Then write the code that gets the test to pass
# Any testing is better than no testing
# Also there is the pytest module


# Class tester
class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  # Needs to have this name
        print('setupClass')

    @classmethod
    def tearDownClass(cls):  # camelCased, needs to have this name
        print('teardownClass')

    # Runs this code before every single test
    def setUp(self):  # camelCased
        print('setUp')
        # Creates these before every single test
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    # Runs this code after every single test
    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        # Pass what should be mocked into patch
        # Just mocking the requests.get function in employee.py
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            # Checking that mocked function is called with correct arg
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()