# Python Built-in Functions Programming Assignment
# Name: [Your Name]
# Task Chosen: [Task Number and Name]

# INSTRUCTIONS:
# 1. Choose ONE task from the task options document
# 2. Write your program below using at least one built-in function
# 3. Add comments explaining your code and why you chose each built-in function
# 4. Test your program to ensure it works correctly

# ============================================
# YOUR CODE STARTS HERE
# ============================================

def get_input(): # Function to get input
    user_input = "" # Starting with empty input
    while True: # Repeat until broken
        try:
            user_input = float(input("Please enter your grade: ")) # Get input in float form to handle decimals
            if user_input < 0 or user_input > 100: # checking the the grade is valid even further
                print("Please enter a grade from 0-100.")
                continue
            return user_input
        except: # If float() fails then ask the user to input a different number
            print("Please enter a number.")

def calculate(grade): # Function to calculate the grade
    scale = {90: "A", 80: "B", 70: "C", 60: "D", 0: "F"} # Grade scale dict
    for i in scale.keys(): # looping through the grade scale
        if grade >= i: # if the grade is greater than this number
            return scale[i] # return that number


print("Your letter grade is", calculate(get_input())) # Call both functions with the input as the calculate func's argument
    


# ============================================
# YOUR CODE ENDS HERE
# ============================================