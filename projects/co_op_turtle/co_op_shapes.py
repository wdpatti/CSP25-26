import turtle

screen = turtle.Screen()
screen.title("Traffic Light")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("black")

startX = -50
startY = -40
width = 100
height = 200

pen.penup()
pen.goto(startX, startY)
pen.pendown()
pen.begin_fill()

pen.goto(startX, startY + height)
pen.goto(startX + width, startY + height)
pen.goto(startX + width, startY)
pen.goto(startX, startY)
pen.end_fill()
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