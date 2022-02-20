# this project about draw left bottom triangle

side = int(input("Enter the side of triangle :"))
chord = int(input("Enter the chord of triangle :"))
import turtle
tri = turtle.Turtle()

 
tri.forward(side) # draw base
 
tri.left(90)
tri.forward(side)
 
tri.left(130)
tri.forward(chord)
 
turtle.done()