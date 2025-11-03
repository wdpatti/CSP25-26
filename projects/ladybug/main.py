import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")
turtle.setup(width=600, height=800)

t = turtle.Turtle()
t.pensize(2)

x_off = -50
for i in range(2):
    t.setheading(0)
    t.penup()
    t.goto(x_off + -100, 50)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    t.circle(100) # Draw a larger body as a circle
    t.end_fill()

    t.penup()
    t.goto(x_off + -100, 225) # Position for the head
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(40) # Draw the head
    t.end_fill()

    t.penup()
    t.goto(x_off + -100, 225)
    t.setheading(-90)
    t.pendown()
    t.pensize(3)
    t.forward(175) # Line separating the body

    spots_positions = [(-50, 50), (50, 50), (-75, 0), (75, 0), (-50, -50), (50, -50)]
    for spot_x, spot_y in spots_positions:
        t.penup()
        t.goto(x_off + -115 + spot_x, 150 + spot_y)
        t.pendown()
        t.fillcolor("black")
        t.begin_fill()
        t.circle(15) # Draw the spots
        t.end_fill()

    legs_positions = [(-85, 50), (-100, 0), (-85, -50), (85, 50), (100, 0), (85, -50)]
    for leg_x, leg_y in legs_positions:
        t.penup()
        t.goto(x_off + -100 + leg_x, 150 + leg_y)
        t.pendown()
        t.setheading(leg_x/100*30-90) # Adjust leg direction
        t.forward(50) # Draw the legs

    t.penup()
    t.goto(x_off + -115, 275) # LeY antenna position
    t.setheading(60)
    t.pendown()
    t.forward(60)
    t.penup()
    t.goto(x_off + -90, 275) # LeY antenna position
    t.setheading(120)
    t.pendown()
    t.forward(60)
    x_off = 250



t.hideturtle()

screen.exitonclick()