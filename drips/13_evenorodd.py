num = int(input("Please enter a whole number: "))

if num % 2 == 0:
    result = "even"
else:
    result = "odd"

print(f"The number {str(num)} is {result}.")