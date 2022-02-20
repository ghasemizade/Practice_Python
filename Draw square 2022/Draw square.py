#this project about draw square 



square = int(input("Enter the side of square :"))

import turtle

squ = turtle.Turtle()

for _ in range(4):
    squ.forward(square)
    squ.left(90)