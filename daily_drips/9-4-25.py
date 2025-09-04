age = 16
first_name = "John"
last_name = "Doe"

full_name = f"{first_name} {last_name}"

greeting = "Hellow my name is " + full_name + " and I am " + str(age) + " years old."

print(greeting)

user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
user_age = input("Enter your age: ")

user_full_name = user_first_name + " " + user_last_name
user_greeting = "Nice to meet you, " + user_full_name + "! You are " + user_age + " years old."

print(user_greeting)