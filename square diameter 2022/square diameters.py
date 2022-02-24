from cmath import sqrt
#This project is for diameter of square

#get input
inputuser = int (input ("Enter a number for side of square :"))


num = int (inputuser)

temp = 1.4 * num

import turtle
dia = turtle.Turtle ()

dia.forward (inputuser)
dia.left (90)

dia.forward (inputuser)
dia.left (90)

dia.forward (inputuser)
dia.left (90)

dia.forward (inputuser)

dia.left (135)
dia.forward (temp)

dia.left (135)
dia.forward (inputuser)

dia.left (135)
dia.forward (temp)