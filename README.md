# Weekly-Tasks


This repository contains a number of weekly tasks completed over the past three months.

1. The first task was to write a program that calculates a users Body Mass Index. Body Mass Index is calculated using the formula kg/m*m. The inputs needed for this calculation are the person's height in meters squared and weight in kilograms. The output is their weight divided by their height in metres squared. Therefore, I labelled the user input for height(in meters) as x, and let height = x * x in order to get the users height in meters squared. This makes the program much easier for a potential user to calculate BMI, due to its user friendly height and weight units. This is a simple program which deals with basic user inputs.

2. The second weekly task was to write a program that asks a user to input a string and outputs every second letter in reverse order. I declared the variable "s" as the user input, recieved using the input("please enter a sentence: ") command. Every second letter in reverse was achieved using the print(s[::-2]) command. A short piece of code was developed to achieve the desired result for this task. 

3. The third task was to write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. This task was an introduction to inputs, loops and if statements. The program begins by asking the user to input a positive integer, and the variable 'n' is given to this input. We then start our while loop by instructing the loop, which will follow, to continue until n=1. We then move onto including the instructions set out in the task. If n / 2 is not equal to zero, it is therefore odd, and should be multiplied by 3 and have 1 added to it. We then use the Else function, which means that n is divisible by 2 and is therefore even, we then simply divide the number by 2. This loop continues until n = 1, and "Finished" is then printed on the screen.  While the code for this task was quite simple, it required careful thought and attention.

4. The fourth weekly task was to write a program that outputs whether or not today is a weekday. This task introduced me to importing, and datetime. While the resulting code was realtively simple, using datetime and a loop, it was challenging as using datetime correctly required me to learn new code.

5. The fifth weekly task was to write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

6. The sixth weekly task was to write a program that reads in a text file and outputs the number of e's it contains. The text file downloaded was a passage from Moby Dick. This task required a more complex loop and line.split functions with which i was unfamiliar. It took a few unsuccessful attempts before I eventually completed the task.

7. The seventh weekly task in the repository was to write a program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes. This task introduced matplotlib and numpy as tools to analyse and visualise a set of data. It was challenging to get comfortable using both matplotlib and numpy, especially when attempting to produce accurate graphs. However, through trial and error and simply spending time working with both programs it made me realise how powerful both tools will prove to be throughout my data career.

Overall the weekly tasks proved both challenging and rewarding in my development as a new programmer. The weekly lectures provided me with adequate information to complete the tasks, while self learning with blogs such as Real Python, A Whirlwind Tour of Python, and countless Youtube videos also provided me with numerous techniques to complete the body of work.



ACKNOWLEDGMENTS

VanderPlas, J (2016) 'A Whirlwind Tour of Python'. Available at: https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf

Various Authors (2020) 'Real Python'. Available at: https://realpython.com/

Sagar, A. (2019) '10 Python Tips and Tricks You Should Learn Today' Towards Data Science. Available at: https://towardsdatascience.com/10-python-tips-and-tricks-you-should-learn-today-a05c23a39dc5

