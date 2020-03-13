#Willie Byrne
#A program that asks the user to input any positive integer
#and outputs the successive values of the following calculation
#at each step calculate the next value by taking current value
#and if it is even, divide it by two
#if it is odd, multiply it by three and add 1
#Program ends if the current value is 1


n = int(input("Please enter a positive integer: "))
#ask user to input positive integer
while n != 1: 
    if int (n) % 2 != 0:
        #if the input number does not divide by 2 (odd) then:
        n = int(n*3)+1
    else:
        #if it does divide by 2 (even) then:
        n = int(n)/2
    print(n)
print("Finished")
#print finished when loop ends (current value = 1)