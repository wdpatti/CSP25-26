import turtle

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
favorite_animal = input("Enter your favorite animal: ")

full_name = first_name + " " + last_name

message = f"Hi {full_name}! I heard that your favorite animal is {favorite_animal}."

print(message)

screen = turtle.Screen()

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 0)

pen.write(message, align="center", font=("Arial", 16, "normal"))

screen.mainloop()