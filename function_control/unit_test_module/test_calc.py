# References https://www.youtube.com/watch?v=6tNS--WetLI
# References https://docs.python.org/3.7/library/unittest.html#test-cases

import unittest
import calc


# Separator for print output
def new_section(message):
    print(f"\n--- {message} ---\n")


new_section("Defining a test case by inheriting from base test case")


class TestCalc(unittest.TestCase):

    # Method must be named test_
    def test_add(self):  # These three steps are in one test
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)
        # Must pass arguments as last arguments in error assert check
        self.assertRaises(ValueError, calc.divide, 10, 0)
        # Can also check exception via context manager
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

# Would need to run via terminal: python -m unittest test_calc.py
# Otherwise, can run via below:
if __name__ == '__main__':
    unittest.main()