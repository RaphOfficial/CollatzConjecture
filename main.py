# Includes
import matplotlib.pyplot as plt
from libs import utils
from libs import loops


def make_line_chart(x_list, y_list):
    plt.plot(x_list, y_list)
    plt.show()


def calculate_collatz_conjecture(seed):
    if utils.is_positive(seed):  # If is positive
        numb_sequence = loops.positive_integer(seed)
    else:  # If is negative or 0
        numb_sequence = loops.negative_integer(seed)

    # Vars
    sequence_details = loops.get_details(numb_sequence, True)
    y_axis = sequence_details[2]  # Just a list with growing numbers from 1 to final number (amount) e.g. If amount
    # is 6 this will be x_axis: 1, 2, 3, 4, 5, 6.
    biggest_number = sequence_details[1]  # Biggest number inside x (ignoring negative signs)
    numbers_amount = sequence_details[0]  # amount of numbers inside x
    # X is the numb sequence
    chart_details = [numb_sequence, y_axis]

    output = [numbers_amount, biggest_number, chart_details]
    return output


if __name__ == "__main__":
    numb = int(input('Please choose any integer: '))
    result = calculate_collatz_conjecture(numb)

    # Vars
    chart_details_result = result[2]
    x = chart_details_result[0]
    y = chart_details_result[1]
    biggest_result_number = result[1]
    numbers_result_amount = result[0]

    print('This is the biggest number in the sequence: ' + str(biggest_result_number))
    print('This is the total amount of numbers in your sequence: ' + str(numbers_result_amount))

    make_line_chart(y, x)

