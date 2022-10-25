import task1


def find_collatz_conjecture_for_all(number):
    """input: int number
        output: list. total no of steps for each number from 1 to given number"""
    if number <= 0:
        print("Error, Given No have to be a positive non zero Number.")
        return False

    steps = []
    for i in range(1, number + 1):
        steps.append(task1.find_steps_of_collatz_conjecture(i))

    return steps


if __name__ == '__main__':
    print(find_collatz_conjecture_for_all(100))
