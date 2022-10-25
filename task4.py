from matplotlib import pyplot as plt
import task2


def create_diargam_for_steps_of_collatz_conjecture(number):
    """input: int number
            output: diagram. plotting total no of steps for each number from 1 to given number"""
    steps = task2.find_collatz_conjecture_for_all(number)
    print(steps)
    x_axis = [x for x in range(1, number + 1)]
    y_axis = steps
    plt.scatter(x_axis, y_axis, label='total_steps')

    plt.xlabel('values')
    plt.ylabel('no of steps')
    plt.title('diagram for number of steps for each value')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    create_diargam_for_steps_of_collatz_conjecture(100)
