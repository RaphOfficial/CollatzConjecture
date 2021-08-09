# Collatz Conjecture
### Main Script
This is a python project to calculate the Collatz Conjecture of a given positive or negative integer. The main script gives a line graph as output, and some useful data like the biggest number in the number sequence, and the amount of number in the sequence before reaching one of the ending numbers *(1, -1, -5, -17).*

![CollatzGraph](https://user-images.githubusercontent.com/45014622/128683082-0d3088b5-1a20-443e-9532-136290f420d2.jpg =350x) 
This is an example of a line graph generated by the script starting with the seed *9663*.
This is the input of the script:

```` 
py main.py
Please choose any positive integer: 9663
```` 
And this is the output given by the script in the terminal:
```` 
This is the biggest number in the sequence: 27114424
This is the total amount of numbers in your sequence: 185
```` 
The line graph is made with matplotlib and is given with the text output in the terminal.
<br>

### Making scripts
This python project can also be used to make others scripts without having to code everything from scratch, *script_example.py*  is an example of a script made with the main core of this project.
To make scripts with this projects, firstly you have to download the *main.py*  file and the *libs*  folders and put them in the same directory of your project. Secondly, you have to import the main file in to the script, like in the following example: `import main`.
Once you have done it you can get the Collatz Conjecture very easily, in this way:
<br>
Input
```` 
    output = main.calculate_collatz_conjecture(seed)
```` 

Output
````
[numbers_amount, biggest_number, chart_details]
```` 
<br>
In the output, the variable *numbers_amount*  represents the amount of numbers in the sequence before arriving to one of the ending loops. The variable *biggest_number*  represents the biggest number in the sequence (or lowest if a negative integer has given). The variable *char_details*  represents an array with X and Y values to make a chart with sequence. 

### Script Example
In this Python project is also included a script example *(script_example.py)* made with the project's main file *(main)*.
*script_example.py* Scans all the seeds within a range of numbers, and then when the script scanned all the seeds or it gets interrupted by the user with the `Control+C` hotkey it prints out the seed with the highest biggest number in the sequence and the seed with the highest amount of numbers in the Collatz Conjecture's sequence. 
<br>
Input
````
py script_example.py
Please select the starting seed: 1
Please select an ending seed or use 0 to loop infinitely: 10
````
Output
````
Calculated seed N1. Amo: 1 - Bgst: 1
Calculated seed N2. Amo: 2 - Bgst: 2
Calculated seed N3. Amo: 8 - Bgst: 16
Calculated seed N4. Amo: 3 - Bgst: 4
Calculated seed N5. Amo: 6 - Bgst: 16
Calculated seed N6. Amo: 9 - Bgst: 16
Calculated seed N7. Amo: 17 - Bgst: 52
Calculated seed N8. Amo: 4 - Bgst: 8
Calculated seed N9. Amo: 20 - Bgst: 52
Calculated seed N10. Amo: 7 - Bgst: 16

The seed with biggest number is seed N7. With a value of: 52
The seed with more numbers in the sequence is the seed N9. With a value of: 20
We reached seed N10 starting from seed N1

Done!
````
This script can also be looped infinitely by choosing 0 as an ending loop, this will continue calculating Collatz Conjecture's sequence until the user terminates the process by using `Control+C` hotkey.
In case the starting seed is a negative integer, the *biggest_number* variable will return the lowest number in the sequence.
