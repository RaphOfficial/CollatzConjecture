# This is a script example for main.py (Collatz Conjecture Calculator).
# This script will calculate the Collatz Conjecture's sequence of every number starting from 0.
# Obviously, the only limit will be the time we let the script run.

# Imports``
import main  # Firstly, we have to import main.py
from time import sleep  # This will only needed to add a delay between calculations.

# Setting
delay = 0.05

starting_seed = int(input("Please select the starting seed: "))
ending_seed = int(input("Please select an ending seed or use 0 to loop infinitely: "))
valid_selection = False  # If valid selection is not true the loop will not start

if starting_seed == 0:  # 0 is not a valid seed, so we will have to change it.
    print("Zero is not a valid starting seed, the seed will be changed to the default starting seed (1)")
    starting_seed = 1
    current_seed = starting_seed

if ending_seed == 0:  # If ending_seed is 0 infinite will be True
    infinite = True
    positive = main.utils.is_positive(starting_seed)  # utils.is_positive(integer) simply returns True if a number is
    # positive or false if a number is negative
    valid_selection = True

else:  # If ending_seed isn't 0, the script has to run thru a range of numbers
    infinite = False  # infinite variable is True if the script has to run until someone stops it, and it's false if
    # it has to run between a range of seeds
    if main.utils.is_positive(starting_seed) and main.utils.is_positive(ending_seed):
        # If starting and ending seeds are both positive
        valid_selection = True
        positive = True
    elif not main.utils.is_positive(starting_seed) and not main.utils.is_positive(ending_seed):
        # If starting and ending seeds are both negative
        valid_selection = True
        positive = False
    else:
        # If starting and ending seeds are of different signs
        # (e.g. Starting seed is positive and ending seed is negative)
        print(
            'Error: if you have a selected a positive starting seed the ending seed has to be positive too. And if '
            'you have selected a negative starting seed the ending seed has to be negative too')

bgst = (0, 0)
amo = (0, 0)
current_seed = starting_seed

try:  # Run the loop, in case of keyboard interrupt (Ctrl+C) stop the loop
    while valid_selection:
        # Let's use calculate_collatz_conjecture from main.py! Result will be stored in 'result' variable
        result = main.calculate_collatz_conjecture(current_seed)
        # This is output format: [numbers_amount, biggest_number, chart_details] see main.py for details!
        numbers_amount = result[0]
        biggest_number = result[1]
        print("Calculated seed N" + str(current_seed) + ". Amo: " + str(numbers_amount) + " - Bgst: " +
              str(biggest_number))
        if numbers_amount > amo[1]:
            # If in the sequence there are a higher number amount then in the best amount score
            amo = (current_seed, numbers_amount)  # New amount score = this sequence
        if positive:  # If range of numbers is positive +
            if biggest_number > bgst[1]:
                bgst = (current_seed, biggest_number)
            if infinite:
                current_seed = current_seed + 1
            else:  # If not infinite
                if current_seed < ending_seed:
                    current_seed = current_seed + 1
                else:
                    valid_selection = False
                    break
        if not positive:
            if biggest_number < bgst[1]:
                bgst = (current_seed, biggest_number)
            if infinite:
                current_seed = current_seed - 1
            else:  # If not infinite
                if current_seed > ending_seed:
                    current_seed = current_seed - 1
                else:
                    valid_selection = False
                    break

        if delay >= 0:
            sleep(delay)

except KeyboardInterrupt:
    pass


print()
print('The seed with biggest number is seed N'+str(bgst[0])+'. With a value of: '+str(bgst[1]))
print('The seed with more numbers in the sequence is the seed N'+str(amo[0])+". With a value of: "+str(amo[1]))
print('We reached seed N'+str(current_seed)+' starting from seed N'+str(starting_seed))
print()
print('Done!')
