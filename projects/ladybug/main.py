import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")
turtle.setup(width=600, height=600)

t = turtle.Turtle()
t.pensize(2)

t.penup()
t.goto(-100, 50)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(100) # Draw a larger body as a circle
t.end_fill()

t.penup()
t.goto(-100, 150) # Position for the head
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(40) # Draw the head
t.end_fill()

t.penup()
t.goto(-100, 150)
t.setheading(-90)
t.pendown()
t.pensize(3)
t.forward(200) # Line separating the body

spots_positions = [(-50, 50), (50, 50), (-75, 0), (75, 0), (-50, -50), (50, -50)]
for spot_x, spot_y in spots_positions:
    t.penup()
    t.goto(-100 + spot_x, 50 + spot_y)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(15) # Draw the spots
    t.end_fill()

legs_positions = [(-100, 50), (-100, 0), (-100, -50), (100, 50), (100, 0), (100, -50)]
for leg_x, leg_y in legs_positions:
    t.penup()
    t.goto(-100 + leg_x, 50 + leg_y)
    t.pendown()
    t.setheading(leg_x) # Adjust leg direction
    t.forward(50) # Draw the legs

t.penup()
t.goto(-115, 180) # LeY antenna position
t.setheading(60)
t.pendown()
t.setheading(120)
t.pendown()
t.forward(60)

t.hideturtle()

screen.exitonclick()