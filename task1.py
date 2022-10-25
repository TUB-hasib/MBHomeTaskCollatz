def is_even(number):
    """input: int number
    output: bool. true for even. false for odd num"""
    if number % 2 == 0:
        return True
    else:
        return False


def find_steps_of_collatz_conjecture(number):
    """input: int number
        output: int. no of steps need to reach 1 for the given number"""
    if number <= 0:
        print("Error, Given Number have to be a positive non zero Number.")
        return False
    if number == 1:
        return 0

    total_steps = 0
    while number > 1:
        if is_even(number):
            number = int(number / 2)
        else:
            number = 3 * number + 1

        total_steps = total_steps + 1
    return total_steps


if __name__ == '__main__':
    print(find_steps_of_collatz_conjecture(10000))
