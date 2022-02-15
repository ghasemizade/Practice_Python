#   In this program, the user enter the radius 
#               then 
#   Calculate envirment, area and diameter.

from msilib.schema import Environment


pi = 3.14
radius = float(input("enter radius :"))

envirement = 2 * pi * radius
area = pi * radius * radius
diameter = 2 * radius

print("Envirement = %.2f" %envirement)
print("Area = %.2f" %area)
print("Diameter = %.2f" %diameter)


