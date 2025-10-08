print("Welcome to the program!")
length = 5
width = 10
height = 15

length = int(input("Enter a new value for length: "))
width = int(input("Enter a new value for width: "))
height = int(input("Enter a new value for height: "))
volume = length * width * height

print("The volume is", volume)

length = volume
width *= 2
height -= 5

print("The new length is ", length)
print("The new width is ", width)
print("The new height is ", height)