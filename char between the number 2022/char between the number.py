#this project about char between the number


from ctypes.wintypes import CHAR
from email import charset


#take input from user
inputuser = int (input ("Enter a number "))
char = input ("Enter a character for add between numbers")

#define variable
num = inputuser
stash = 0
num2 = num


#define for
for counter in range (num % 100):
    stash = int (num2 % 10)
    
    if stash % 10 == 0:
        break

    num2 = num2 / 10
    print (stash, char)