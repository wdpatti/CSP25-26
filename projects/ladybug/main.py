import turtle

#setup python turtle libaries
screen = turtle.Screen()
screen.bgcolor("lightgreen")
turtle.setup(width=600, height=600)

t = turtle.Turtle()
t.pensize(2)

for x_off, y_off, color in [(-50, -50, ("red", "black")), (250, -50, ("yellow", "blue")), (-50, -335, ("orange", "red")), (250, -335, ("purple", "green"))]: # iterate through the four different ladybugs with coordinates and colors
    t.setheading(0)
    t.penup()
    t.goto(x_off + -100, y_off + 50) # add offsets to main circle coordinates - this will be used throughout to make four ladybugs accurately
    t.pendown()
    t.fillcolor(color[0])
    t.begin_fill()
    t.circle(100) # Draw a larger body as a circle
    t.end_fill()

    t.penup()
    t.goto(x_off + -100, y_off + 225) # Position for the head
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(40) # Draw the head
    t.end_fill()

    t.penup()
    t.goto(x_off + -100, y_off + 225)
    t.setheading(-90)
    t.pendown()
    t.pensize(3)
    t.forward(175) # Line separating the body

    t.color(color[1])

    spots_positions = [(-50, 50), (50, 50), (-75, 0), (75, 0), (-50, -50), (50, -50)] # list of different spot positions
    for spot_x, spot_y in spots_positions:
        t.penup()
        t.goto(x_off + -115 + spot_x, y_off + 150 + spot_y)
        t.pendown()
        t.fillcolor(color[1]) # choose the color based on list from initial for loop
        t.begin_fill()
        t.circle(15) # Draw the spots
        t.end_fill()

    t.color("black") #set color to black after making spots

    legs_positions = [(-85, 50), (-100, 0), (-85, -50), (85, 50), (100, 0), (85, -50)]
    for leg_x, leg_y in legs_positions:
        t.penup()
        t.goto(x_off + -100 + leg_x, y_off + 150 + leg_y)
        t.pendown()
        t.setheading(leg_x/100*30-90) # Adjust leg direction
        t.forward(50) # Draw the legs

    t.penup()
    t.goto(x_off + -95, y_off + 275) # LeY antenna position with offsets
    t.setheading(60)
    t.pendown()
    t.forward(60)
    t.penup()
    t.goto(x_off + -105, y_off + 275) # LeY antenna position with offsets
    t.setheading(120)
    t.pendown()
    t.forward(60)


#ending function calls to make sure that the window stays open after the turtle is done drawing
t.hideturtle()

screen.exitonclick()