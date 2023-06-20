import turtle



# Set the turtle speed and shape
turtle.speed(20)
turtle.shape("turtle")
# Draw the turtleace
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.circle(100)

# Draw the eyes
turtle.penup()
turtle.goto(-40, 40)
turtle.pendown()
turtle.circle(20)
turtle.begin_fill()
turtle.color("black")
turtle.circle(20)
turtle.end_fill()

turtle.penup()
turtle.goto(40, 40)
turtle.pendown()
turtle.circle(20)
turtle.begin_fill()
turtle.color("black")
turtle.circle(20)
turtle.end_fill()

# Draw nose
turtle.penup()
turtle.goto(-35, -30)
turtle.pendown()
turtle.setheading(0)
turtle.forward(70)
turtle.left(120)
turtle.forward(70)
turtle.left(120)
turtle.forward(70)

# Draw the mouth
turtle.penup()
turtle.goto(-55, -30)
turtle.pendown()
turtle.setheading(-40)
turtle.forward(70)
turtle.left(80)
turtle.forward(70)
turtle.left(80)

# Hide the turtle
turtle.hideturtle()

turtle.done() 