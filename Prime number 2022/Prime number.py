# this project about calculate prime number

Inputuser = int(input("Enter the number :"))
sum = int(0)
result = int()
for counter in range (2 , Inputuser):
    if Inputuser % counter == 0:
        result = int(sum + 1)

if result == Inputuser:
    print("Yes")
else:
    print("No")            
