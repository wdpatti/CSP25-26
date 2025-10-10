import turtle
screen = turtle.Screen()
screen.title("Traffic Lights")

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color("red")
pen.goto(0, 100)
pen.pendown()
pen.begin_fill()
pen.circle(25)
pen.end_fill()
pen.penup()

pen.goto(0,35)
pen.color("yellow")
pen.pendown()
pen.begin_fill()
pen.circle(25)
pen.end_fill()
pen.penup()

pen.goto(0,-30)
pen.color("green")
pen.pendown()
pen.begin_fill()
pen.circle(25)
pen.end_fill()
pen.penup()

pen.hideturtle()


screen.mainloop()