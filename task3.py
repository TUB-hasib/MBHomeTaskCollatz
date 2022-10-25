import task1
import task2
from datetime import datetime


def find_fast_steps_of_collatz_conjecture(number, steps_count_dict):
    """input: int number, dict key= numbers upto given number-1   value= total steps for that key
        output: int. total no of steps for that number"""
    if number == 1:
        return 0

    total_steps = 0
    while number > 1:
        if number in steps_count_dict:  # found the value in previous iteration
            # print(f"previous value {number} and the current dict {steps_count_dict}")
            return total_steps + steps_count_dict.get(number)
        if task1.is_even(number):
            number = int(number / 2)
        else:
            number = 3 * number + 1

        total_steps = total_steps + 1

    return total_steps


def find_fast_collatz_conjecture_for_all(number):
    """input: int number
        output: list. total no of steps for each number from 1 to given number"""
    if number <= 0:
        print("Error, Given No have to be a positive non zero Number.")
        return False

    steps_count_dict = {}
    for i in range(1, number+1):
        total_steps = find_fast_steps_of_collatz_conjecture(i, steps_count_dict)
        steps_count_dict[i] = total_steps

    # print(steps_count_dict.keys())
    return steps_count_dict


if __name__ == '__main__':

    print(f"list: {find_fast_collatz_conjecture_for_all(20)}")

    start = datetime.now()
    find_fast_collatz_conjecture_for_all(3)
    print(f"time needed for fast algo {datetime.now()-start}")

    start = datetime.now()
    task2.find_collatz_conjecture_for_all(3)
    print(f"time needed for normal algo {datetime.now()-start}")
