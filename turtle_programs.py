# 1- Python program to draw star


import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle named star
star = turtle.Turtle()
star.color("black")
star.pensize(2)

# Draw a star
for _ in range(5):
    star.forward(100)
    star.right(144)

# End the drawing
turtle.done()


# 2-Python program to draw square

import turtle

skk = turtle.Turtle()

for i in range(4):
    skk.forward(50)
    skk.right(90)

turtle.done()

# 3-Python program to draw hexagon

import turtle

polygon = turtle.Turtle()

num_sides = 6
side_length = 70
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()

# 4-Draw the parallelogram
import turtle

# Initialize the turtle
t = turtle.Turtle()

# Set the turtle's speed
t.speed(1)

# Draw the parallelogram
for i in range(2):
	t.forward(100)
	t.left(60)
	t.forward(50)
	t.left(120)

# 5-  python program to draw circle
import turtle

# Set up the turtle screen and set the background color to white
screen = turtle.Screen()
screen.bgcolor("white")

# Create a new turtle and set its speed to the fastest possible
pen = turtle.Turtle()
pen.speed(0)

# Set the fill color to red
pen.fillcolor("red")
pen.begin_fill()

# Draw the circle with a radius of 100 pixels
pen.circle(100)

# End the fill and stop drawing
pen.end_fill()
pen.hideturtle()

# Keep the turtle window open until it is manually closed
turtle.done()

