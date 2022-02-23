# this project about revers number then check with firstnumber

inputuser = int(input("Enter the number :"))

reversnumber = 0

while inputuser != 0:
    digit = inputuser % 10
    reversnumber = reversnumber * 10 + digit
    inputuser //= 10


if inputuser == reversnumber:
    print("Yes")
else:
    print("No")        