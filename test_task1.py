import unittest
from task1 import is_even, find_steps_of_collatz_conjecture


class MyTestCase(unittest.TestCase):

    def test_is_even_check_even_no(self):
        self.assertEqual(is_even(8), True)  # add assertion here

    def test_is_even_check_odd_no(self):
        self.assertEqual(is_even(9), False)  # add assertion here

    def test_find_steps_of_collatz_conjecture_check_zero(self):
        self.assertEqual(find_steps_of_collatz_conjecture(0), False)  # add assertion here

    def test_find_steps_of_collatz_conjecture_check_negative_value(self):
        self.assertEqual(find_steps_of_collatz_conjecture(-15), False)  # add assertion here

    def test_find_steps_of_collatz_conjecture_check_one(self):
        self.assertEqual(find_steps_of_collatz_conjecture(1), 0)  # add assertion here

    def test_find_steps_of_collatz_conjecture_check_even(self):
        self.assertEqual(find_steps_of_collatz_conjecture(20), 7)  # add assertion here

    def test_find_steps_of_collatz_conjecture_check_odd(self):
        self.assertEqual(find_steps_of_collatz_conjecture(29), 18)  # add assertion here

    def test_find_steps_of_collatz_conjecture_check_large_value(self):
        self.assertEqual(find_steps_of_collatz_conjecture(10000), 29)  # add assertion here


if __name__ == '__main__':
    unittest.main()
