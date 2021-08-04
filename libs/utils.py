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


def is_positive(int_value):
    # This function returns True if a number is positive
    # Vars
    x = int(int_value)
    output = False
    if x > 0:
        output = True
    return output

    # Possible outputs:
    # False = Number is negative or 0
    # True = Number is positive
