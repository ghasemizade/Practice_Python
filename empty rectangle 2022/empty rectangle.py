#this project about draw hollow rectangle

from turtle import width


length = int(input("Enter length of rectangle size :"))
width = int(input("Enter width of rectangle size"))

import turtle
rec = turtle.Turtle()

rec.forward (length)
rec.left(90)

rec.forward (width)
rec.left(90)

rec.forward (length)
rec.left(90)

rec.forward (width)
rec.left(90)