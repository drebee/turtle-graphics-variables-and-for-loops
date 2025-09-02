from turtle import *

speed(10)

number_of_sides = 100
angle = 360 / number_of_sides
for i in range(number_of_sides):
    forward(2)
    right(angle)

exitonclick()