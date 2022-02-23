#this project is for three min & max 

arrayuser = []
Inputuser = int(input("number of elements in array :"))

for counter in range(0,Inputuser):
    number = int(input())
    arrayuser.append(number)

# minimum
arrayuser.sort()
print(arrayuser[0],arrayuser[1],arrayuser[2])
# maximum
arrayuser.sort(reverse = True)
print(arrayuser[0],arrayuser[1],arrayuser[2])