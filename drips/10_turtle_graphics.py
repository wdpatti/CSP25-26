import turtle

first_name = input("Please enter your first name: ")

screen = turtle.Screen()
screen.title("Daily Drip 10")

t = turtle.Turtle()

t.hideturtle()
t.color("red")
t.penup()
t.goto(0, 150)

t.write(f"Hi, {first_name}!", align="center", font=("Arial", 50, "normal"))

screen.mainloop()