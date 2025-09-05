import turtle

fonts = ["Arial", "Courier", "Comic Sans MS", "Times New Roman", "Verdana", "Wingdings"]

screen = turtle.Screen()
screen.title("Test Fonts with Turtle Graphics")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("blue")

pen.penup()
pen.goto(0, 100)

for font in fonts:
    pen.write(f"This is {font}", align="center", font=(font, 24, "normal"))
    pen.sety(pen.ycor() - 50)

screen.mainloop()