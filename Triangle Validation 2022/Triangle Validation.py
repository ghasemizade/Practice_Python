# This program takes three numbers 
# from the user and tells the user
# That these three numbers can be triangles Or not.

firstside = int(input("Enter the side"))
secondside = int(input("Enter the side"))
thirdside = int(input("Enter the side"))

if firstside < secondside + thirdside:
    print("this is a Triangle")
elif secondside < firstside + thirdside:
    print("this is a Triangle")
elif thirdside < firstside + secondside:
    print("this is a Triangle")
else:
    print("Error")
