# Willie Byrne
# This Program will output whether or not today is a weekday
# Running on a weekday it will print "It's a weekday"
# Running a weekend it will print "It's the weekend"

import datetime
today = datetime.datetime.now()
day = today.weekday()
#first step was to import datetime
# used docs.python.org to understand the working of datetime module

dayname = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
#give daynames numerical values to help with loop

print("Today is ", dayname[day])

if day <= 4:
     #if it is anyday between Monday - Friday, inclusive
     print("It is a Weekday")
else:
     #if not, it must be Saturday or Sunday
     print("It is the Weekend!!!")


