#this project about product without product operotor


from itertools import product


firstnum = int(input("Enter the first number :"))
secondnum = int(input("Enter the second number :"))
product = 0
for i in range (0 , secondnum):
    product += firstnum

print(product)