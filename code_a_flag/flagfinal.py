# The below function draws a filled rectangle using the specified color.
# It sets the turtle's color and fill color to the given color,
# then draws a rectangle with a width of 450 units and a height of 100 units
def draw_rectangle(color):
    t.color(color)
    t.begin_fill()
    t.fillcolor(color)
    for i in range(2):
        t.forward(450)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()

import turtle 

t = turtle.Turtle()

#drawing bottom green colored strip
t.penup()
t.goto(-225,-150)
t.pendown()
draw_rectangle('green')

#middle white colored strip
t.penup()
t.goto(-225,-50)
t.pendown()
draw_rectangle('white')

#top saffron colored strip
t.penup()
t.goto(-225,50)
t.pendown()
draw_rectangle('orange')

#the below part draws the inner circle of ashoka chakra and fill it with blue color
t.color('blue')
t.penup()
t.goto(0,0)
t.right(90)
t.forward(10)
t.left(90)
t.pendown()
t.begin_fill()
t.fillcolor('blue')
t.circle(10)
t.end_fill()

#the below part draws the 24 spokes of asoka chakra
for i in range(24):
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.forward(40)
    t.right(15)



#the below part draw the outer circle of ashoka chakra
t.pensize(5)
t.color('blue')
t.penup()
t.goto(0,0)
t.right(90)
t.forward(40)
t.left(90)
t.pendown()
t.circle(40)



t.hideturtle()
turtle.done()

