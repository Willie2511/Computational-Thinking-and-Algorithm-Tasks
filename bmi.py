#Willie Byrne
#BMI Calculator
#Weight in kg
#Height in meters squared

weight = float(input("weight in KG: "))
x = float(input("height in Meters: "))
# Ask for user inputs
# Could have asked for height in meters squared
#but it is easier for users to input height in meters
height = x*x
#asked user for height in meters, then converted it to meters squared
#in order to successfully calculate BMI
bmi = weight/ height 
# Simple BMI calculation formula
print("BMI = ", bmi)