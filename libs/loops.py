from libs import utils


def positive_integer(x):
    # Vars
    number_list = []
    looping = True
    x = int(x)

    while looping:
        number_list.append(x)
        x_odd = utils.odd_or_even(x)
        if x == 1:
            looping = False
            continue
            # Breaks the loop

        if x_odd:  # If x is odd
            x = x * 3 + 1
        else:  # If x is even
            x = int(x / 2)

    return number_list


def negative_integer(x):
    # Vars
    number_list = []
    looping = True
    x = int(x)

    while looping:
        number_list.append(x)
        x_odd = utils.odd_or_even(x)
        if x == -5 or x == -1 or x == -17:
            looping = False
            continue
            # Breaks the loop

        if x_odd:  # If x is odd
            x = x * 3 + 1
        else:  # If x is even
            x = int(x / 2)

    return number_list


def get_details(x, get_y_axis):
    # Vars
    biggest_number = 0
    amount = 0

    if x[0] < 0:  # Defining if x's numbers are negative
        x_negative = True
    else:
        x_negative = False

    for numb in x:
        amount = amount + 1
        if x_negative:  # If sequence is made by negative number
            if numb < biggest_number:
                biggest_number = numb
        else:
            if numb > biggest_number:
                biggest_number = numb

    if get_y_axis:
        # Var
        x_axis = []

        for numb in range(amount):
            x_axis.append(numb+1)

        # Defining output
        output = [amount, biggest_number, x_axis]

    else:
        # Defining output
        output = [amount, biggest_number]

    return output
    # Possible outputs:

    # If get_y_axis = false:
    # [amount, biggest_number]

    # If get_y_axis = true:
    # [amount, biggest_number, x_axis]

    # amount = amount of numbers inside x
    # biggest number = biggest number inside x (ignoring negative signs)
    # x axis = just a list with growing numbers from 1 to final number (amount)
    # e.g. If amount is 6 this will be x_axis: 1, 2, 3, 4, 5, 6.
