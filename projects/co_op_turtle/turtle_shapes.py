import turtle

screen = turtle.Screen()
screen.title("Traffic Light")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("black")

startX = 0
startY = -100
width = 100
height = 200

pen.penup()
pen.goto(0, startY)
pen.pendown()
pen.begin_fill()

pen.goto(startX, startY + height)
pen.goto(startX + width, startY + height)
pen.goto(startX + width, startY)
pen.goto(0, startY)
pen.end_fill()

screen.mainloop()