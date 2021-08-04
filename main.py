# Includes
import matplotlib.pyplot as plt
from libs import utils
from libs import loops


def make_line_chart(y_list, x_list):
    plt.plot(x_list, y_list)
    plt.show()


numb = int(input('Please choose any positive integer: '))

if utils.is_positive(numb):
    numb_sequence = loops.positive_integer(numb)
else:  # If is negative or 0
    numb_sequence = loops.negative_integer(numb)

sequence_details = loops.get_details(numb_sequence, True)

x_axis = sequence_details[2]
biggest_number = sequence_details[1]
numbers_amount = sequence_details[0]

print('This is the biggest number in the sequence: '+str(biggest_number))
print('This is the total amount of numbers in your sequence: ' + str(numbers_amount))

make_line_chart(numb_sequence, x_axis)
