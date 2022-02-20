#this project about draw rectangle

firstside = int(input("Enter the side of square :"))
secondside = int(input("Enter the side of square :"))


import turtle
rec = turtle.Turtle()
#drawing first side
rec.forward(firstside)
rec.left(90)
#drawing second side
rec.forward(secondside)
rec.left(90)
#drawing third side
rec.forward(firstside)
rec.left(90)
#drawing forth side
rec.forward(secondside)
rec.left(90)