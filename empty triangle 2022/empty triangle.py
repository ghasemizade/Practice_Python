#This project is for draw a hollow triangle

#get input
inputuser = int (input ("Enter a number for side of triangle "))
dir = str (input ("Enter a direction between (up, down, left, right)"))

import turtle
tri = turtle.Turtle ()

if dir == 'up':
    tri.forward (inputuser)
    tri.left (60)

    tri.forward (inputuser)
    tri.left (60)

    tri.forward (inputuser)
    tri.left (60)

if dir == 'down':
    tri.forward (inputuser)
    tri.right (60)

    tri.forward (inputuser)
    tri.right (60)

    tri.forward (inputuser)
    tri.right (60)

if dir == 'left':
    tri.left (90)
    tri.forward (inputuser)
    tri.left (120)

    tri.forward (inputuser)
    tri.left (120)

    tri.forward (inputuser)
    tri.left (120)

if dir == 'right':
    tri.left (90)
    tri.forward (inputuser)
    tri.right (120)

    tri.forward (inputuser)
    tri.right (120)

    tri.forward (inputuser)
    tri.right (120)