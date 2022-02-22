# this project about calculate count, cum, min, max, variance


Myarray = []
Inputuser = int(input("Number of elements in array :"))
sum = 0

for i in range(0,Inputuser):
   number = int(input())
   sum += number
   Myarray.append(number)

#count of number
print("count of numbr : %i" %Inputuser)
#max number in array
print("max number in array : %i" %max(Myarray))
#min number in array
print("min number in array : %i" %min(Myarray))
#sum of number in array
print("sum of number : %i" %sum)
#average of number in array
average = float(sum / Inputuser)
print("average number in array : %.2f" %average)













