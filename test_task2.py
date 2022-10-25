import unittest
from task2 import find_collatz_conjecture_for_all


class MyTestCase(unittest.TestCase):

    def test_find_collatz_conjecture_for_all_check_zero(self):
        self.assertEqual(find_collatz_conjecture_for_all(0), False)  # add assertion here

    def test_find_collatz_conjecture_for_all_check_negative_value(self):
        self.assertEqual(find_collatz_conjecture_for_all(-12), False)  # add assertion here

    def test_find_collatz_conjecture_for_all_check_positive_value(self):
        self.assertEqual(find_collatz_conjecture_for_all(10), [0, 1, 7, 2, 5, 8, 16, 3, 19, 6])  # add assertion here


if __name__ == '__main__':
    unittest.main()
