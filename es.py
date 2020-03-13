#Willie Byrne
#This program reads in a text file (extract from Moby Dick)
#And outputs the number of e's it contains
#.txt file found online, link in code below

letters = 'e'
k = 0

with open('/Users/Willie/Desktop/moby_dick.txt', 'r') as f:
    #f= Moby Dick.txt link. 
    #Using the 'with open as f' function, enables us to use one less line of code
    for line in f:
        words = line.split()
        #splitting passage into lines, and then words
        #enables us to search for specified letters
        for i in words:
            for letter in i:
                #seaching for letter e
                if(letter == letters):
                # letters = e, stated at start
                k= k+1
#loop keeps counting e's until all are traced
print(k) 

