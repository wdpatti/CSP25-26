print("Welcome to the Simple Calculator Program!")

# Assigns initial variables
num1 = 10
num2 = 5
operation = "addition"

# Prints initial values
print("Initial values:")
print("Number 1:", num1)
print("Number 2:", num2)
print("Operation 1:", operation)

# Prompts the user to enter new values
num1 = int(input("Enter a new value for Number 1: "))
num2 = int(input("Enter a new value for Number 2: "))
operation = input("Enter an operation (addition, subtraction, multiplication, division): ")

# Checks val of operation var
if operation == "addition":
    result = num1 + num2
elif operation == "subtraction":
    result = num1 - num2
elif operation == "multiplication":
    result = num1 * num2
elif operation == "division":
    result = num1 / num2
else:
    result = None
    print("Invalid operation entered.")

# Prints the result of the operation
if result != None:
    print("The restulf of the operation is:", result)

# reassigns values and prints updated result

num1 = result
num2 = num2 * 2
print("Updated values after reassignment:")
print("Number 1 (result of previous operation):", num1)
print("Number 2 (doubled):", num2)