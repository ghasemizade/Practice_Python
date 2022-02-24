#This project is for write a numbers on ascending & descending

Myarray = []
Inputuser = int(input("Enter number of elements : "))
user = str(input("Enter A/Ascending , D/Descending :"))

for counter in range(0,Inputuser):
    number = int(input())
    Myarray.append(number)

if user == "A" or "Ascending":
    Myarray.sort()
    print(Myarray)
if user == "D" or "Descending":
    Myarray.sort(reverse=True)
    print(Myarray)