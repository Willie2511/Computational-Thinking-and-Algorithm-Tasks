# Willie Byrne
# Find approximate square root of a number (input) 
# Using Newton's method
# Newton's method: square root of N = 1/2 (N/A + A)
# Where N is the number to get the square root of
# and A is your educated guess
 
n = float(input("please enter a number: "))
y = float(input("please enter number of iterations: "))
a = float(input("please make an educated guess: "))
# ask for user inputs which are necessary for the 
# square root calculation

def newton_method(n, a, y):
    ans = a 
    y = y-1
    #While loop until y = 0
    while y > 0:
        ans = 0.5 * (ans + (n / ans))
        y = y - 1
    return ans # return ans when loop is finished

print (newton_method (n, a, y))
# print results to screen 