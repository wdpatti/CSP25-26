#Importing required libraries
import turtle
from PIL import Image
import random as celebrations # Renaming random library for thematic purposes

#PILLOW BONUS
def convert_to_gif(img_path):
    img = Image.open(img_path) #Open the inputted image from the path
    gif_path = "converted_image.gif" #Save image as a gif
    img.save(gif_path, format="GIF")
    return gif_path #Returns path of new file

#Defines celebration function
def display_celebration(gif_path=None):
    # Set up the Turtle screen and add title and background color
    screen = turtle.Screen()
    screen.title("Fall Celebrations")
    screen.bgcolor("black")

    #Creates new background turtle
    background_turtle = turtle.Turtle()
    # Set background GIF if a path is provided
    if gif_path:
        try:
            screen.addshape(gif_path) # Register the GIF shape
            background_turtle = turtle.Turtle()
            background_turtle.shape(gif_path) #Set the background to the gif
            background_turtle.penup()
            background_turtle.goto(0, 0) #Reset turtle at 0,0
        except turtle.TurtleGraphicsError:
            #Error handling
            print("Error: The file could not be loaded. Please ensure it's a valid .gif file.")
    
    # Create a turtle for text
    text_turtle = turtle.Turtle()
    text_turtle.hideturtle()
    text_turtle.color("white")
    # Draw "Let's Celebrate!" in large letters
    text_turtle.penup()
    text_turtle.goto(0, 200)
    text_turtle.write("Let's Celebrate!", align="center", font=("Arial", 40, "bold"))

    # Create a turtle for fireworks
    fireworks = turtle.Turtle()
    fireworks.speed(0)
    fireworks.hideturtle()
    # Draw fireworks effect
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]
    for _ in range(30): # Draw 30 fireworks
        fireworks.penup()
        x = celebrations.randint(-200, 200) #Choose a random location for the firework
        y = celebrations.randint(-200, 200)
        fireworks.goto(x, y)
        fireworks.pendown()
        # Choose a random color
        fireworks.color(celebrations.choice(colors))
        # Draw lines radiating from the point to create a firework effect
        for _ in range(12): # 12 lines per firework
            fireworks.forward(50)
            fireworks.backward(50)
            fireworks.right(30) # 360 degrees divided by 12 lines

    screen.exitonclick()

#Define all of the various holidays as functions that return lists of activities
def diwali():
    return ["Light diyas", "Prepare sweets", "Fireworks", "Family gathering"]

def thanksgiving():
    return ["Cook a turkey", "Family dinner", "Express gratitude", "Watch a parade", "Watch football"]

def day_of_the_dead():
    return ["Visit graves", "Make sugar skulls", "Create altars", "Share family stories"]

def guy_fawkes_day():
    return ["Bonfires", "Fireworks", "Burning effigies", "Sing traditional songs"]

def st_andrews_day():
    return ["Ceilidh dancing", "Traditional Scottish meal", "Attend events", "Celebrate Scottish culture"]

def rememberance_day():
    return ["Attend ceremonies", "Moment of silence", "Wear poppies", "Thank veterans"]

def mid_autumn_festival():
    return ["Family reunion", "Eat mooncakes", "Moon worship", "Lantern lighting"]

def yom_kippur():
    return ["Day of fasting", "Attend synagogue services", "Reflect on past actions", "Seek forgiveness"]

def rosh_hashanah():
    return ["Attend synagogue services", "Blow the shofar", "Eat symbolic foods like apples and honey", "Pray for a good year ahead"]

def halloween(): #BONUS FALL HOLIDAY FUNC
    return ["Buy pumpkins", "Decorate the house", "Buy candy", "Tell spooky stories"]

#Dict of holiday functions
holiday_functions = {
    "Diwali": diwali,
    "Thanksgiving": thanksgiving,
    "Day of the Dead": day_of_the_dead,
    "Guy Fawkes Day": guy_fawkes_day,
    "St. Andrew's Day": st_andrews_day,
    "Rememberance Day": rememberance_day,
    "Mid-Autumn Festival": mid_autumn_festival,
    "Yom Kippur": yom_kippur,
    "Rosh Hashanah": rosh_hashanah,
    "Halloween": halloween #BONUS FUNCTION
}

#Defines funciton to display holiday activities
def display_activities(holiday_name):
    if holiday_name in holiday_functions:
        print(f"\nActivities for {holiday_name}:")
        activities = holiday_functions[holiday_name]() #Call func to get activities
        for a in activities:
            print("-" + a) #Print each activity seperated by hyphens
    else:
        print(holiday_name + " is not in the list of holidays.")

#Gives the user holiday options
print("Do you celebrate any of the following holidays?")
for h in holiday_functions.keys():
    print("-" + h)

#Ask user for holiday input and display the activities associated with that holiday if it exists
user_holiday = input("\nIf you celebrate one of these holidays, please enter its name, or press Enter to skip: ").strip() #Strips input of unnecessary spaces
if user_holiday in holiday_functions:
    display_activities(user_holiday)
else:
    print(user_holiday + " is not recognized as one of the holidays in our list.") #Notify user if holiday does not exist

#Ask user for image input and process it if needed
img_path = input("Enter the path to an image (PNG, JPEG, JPG, GIF) for the background, or press Enter to skip: ").strip() #Strips input of unnecessary spaces
if not img_path:
    gif_path = None #Use no background if no input is given
elif img_path.lower().endswith(('.jpg', '.jpeg', '.png')):
    gif_path = convert_to_gif(img_path) #BONUS PILLOW for personal images - If the image if a jpg, jpeg, or png, convert it to a gif and set the gifpath to that 
else:
    gif_path = img_path #If the gifpath is anything else just set the gifpath to the provided path

display_celebration(gif_path) #Runs the display procedure from above
