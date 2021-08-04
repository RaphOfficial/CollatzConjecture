# Includes
import matplotlib.pyplot as plt


def odd_or_even(int_value):
    # This function defines if a number is odd or even
    # Var
    int_value = int(int_value)

    if (int_value % 2) == 0:
        output = False
    else:
        output = True
    return output

    # Possible outputs:
    # False = Number is even
    # True = Number is odd


def make_line_chart(y_list, auto_assignment):
    if auto_assignment:
        # Vars
        x_axis = []
        y_count = 0

        for numbs in y_list:
            y_count += 1
            x_axis.append(y_count)
    else:
        print("Not supported in this version of the file.")
        return -1
    # Vars
    y_axis = y_list
    plt.plot(x_axis, y_axis)
    plt.show()


# Vars
looping = True
numb = int(input('Please choose any positive integer: '))
x = numb
number_list = []

while looping:
    number_list.append(x)
    x_odd = odd_or_even(x)
    if x == 1:
        looping = False
        continue
        # Breaks the loop

    if x_odd:  # If x is odd
        x = x * 3 + 1
    else:  # If x is even
        x = int(x/2)

make_line_chart(number_list, True)
