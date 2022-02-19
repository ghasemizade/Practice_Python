# Calculate the product of multiplication between two intervals

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
product = 1

for i in range (num1 , num2):
    if i % 2 == 1:
        product *= i

print(product)

