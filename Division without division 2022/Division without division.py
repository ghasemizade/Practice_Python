#this project Divison without divison

firstnum = int(input("Enter first number :"))
secondnum = int(input("Enter second number :"))

Divison = 0
mod = firstnum
i = 0
for counter in range (secondnum):
    if mod >= secondnum:
        i += 1
        mod -= secondnum
    else:
        break    

print(i)
    