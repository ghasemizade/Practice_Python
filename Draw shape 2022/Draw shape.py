#This project is for draw a 4 shape


#input
Inputlength = int (input ("Enter a size of square side "))
Inputwidth = int (input ("Enter a number for width "))


#square
import turtle
shape = turtle.Turtle ()

shape.forward (Inputlength)
shape.left (90)

shape.forward (Inputlength)
shape.left (90)

shape.forward (Inputlength)
shape.left (90)

shape.forward (Inputlength)
shape.left (90)

#rectangle
shape.forward (Inputlength)
shape. left (90)

shape.forward (Inputwidth)
shape. left (90)

shape.forward (Inputlength)
shape. left (90)

shape.forward (Inputwidth)
shape. left (90)


#triangle
shape.forward (Inputlength)
shape.left (120)

shape.forward (Inputlength)
shape.left (120)

shape.forward (Inputlength)
shape.left (120)


#circle
shape.circle (Inputlength)