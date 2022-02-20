#this project about calculate divisor number

number = int(input("Enter the number :"))
counter = int(1)
print("these are number divisor of inputuser :")

for counter in range(counter , number):
    if number % counter == 0:
        print(counter)