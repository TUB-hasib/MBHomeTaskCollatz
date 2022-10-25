import unittest
from task3 import find_fast_collatz_conjecture_for_all, find_fast_steps_of_collatz_conjecture

class MyTestCase(unittest.TestCase):

    def test_find_fast_collatz_conjecture_for_all_check_zero(self):
        self.assertEqual(find_fast_collatz_conjecture_for_all(0), False)  # add assertion here

    def test_find_fast_collatz_conjecture_for_all_check_negative_value(self):
        self.assertEqual(find_fast_collatz_conjecture_for_all(-12), False)  # add assertion here

    def test_find_fast_collatz_conjecture_for_all_check_positive_value(self):
        self.assertEqual(find_fast_collatz_conjecture_for_all(10), {1: 0, 2: 1, 3: 7, 4: 2, 5: 5, 6: 8, 7: 16, 8: 3, 9: 19, 10: 6})  # add assertion here


if __name__ == '__main__':
    unittest.main()
