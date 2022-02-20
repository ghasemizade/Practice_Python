#this project about calculate Average numbers to any number

from audioop import avg
from itertools import count


counter = int(input("Enter the count :"))
sum = 0
for i in range(counter):
    num = int(input("enter the number :"))
    sum += num

avg = sum / counter
print(avg)