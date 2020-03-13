# Willie Byrne
# This program will take a positive floating 
# point number as input and outputs an approx
# square root.

import math

#define newtons square root calculation
def newton(n, x):
    x1 = x - (x*x-n)/(2*x*x)
    return x1

def main():
    while True:
        #ask user to input number to get the approx square root of
        x = float(input("Please enter a number: "))
        if x == '':
            break 
        x = float(x)
        print ("The square root of ",x,"is", math.sqrt(x))
        #Use the .sqrt function to find square root of input number
main()



