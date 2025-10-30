import turtle

screen = turtle.Screen()
screen.bgcolor("lightpink")

t = turtle.Turtle()
t.pensize(3)
t.color("black")

#create rect
t.pencolor("blue")
t.penup()
t.goto(-200, -50)
t.pendown()
t.forward(400)
t.left(90)
t.forward(20)
t.left(90)
t.forward(400)
t.left(90)
t.forward(20)
t.left(90)
t.penup()
#left circle
t.pencolor("red")
t.goto(-150, -125)
t.pendown()
t.circle(40)
#right circle
t.penup()
t.goto(150, -125)
t.pendown()
t.circle(40)
t.pencolor("black")
#vert line thru left circle
t.penup()
t.goto(-190, -50)
t.pendown()
t.goto(-190, -90)
#vert line thru right circle
t.penup()
t.goto(110, -50)
t.pendown()
t.goto(110, -90)
#vert line left
t.penup()
t.goto(-175, -45)
t.pendown()
t.goto(-175, -30)
#vert line right
t.penup()
t.goto(175, -45)
t.pendown()
t.goto(175, -30)
#vert line left
t.penup()
t.goto(-50, -45)
t.pendown()
t.goto(-50, -30)
#vert line right
t.penup()
t.goto(50, -45)
t.pendown()
t.goto(50, -30)

t.hideturtle()

screen.exitonclick()
