# assignment dyslexia occurs when the variable and value are written in reverse order, like 1500 = totalCalories

dailyCalories = 2500
totalCalories = 0

breakfast = float(input("Enter your breakfast calories: "))
lunch = float(input("Enter your lunch calories: "))
dinner = float(input("Enter your dinner calories: "))
snacks = float(input("Enter your snacks calories: "))

totalCalories = breakfast + lunch + dinner + snacks
calorieDeficit = dailyCalories - totalCalories

if calorieDeficit > 0:
    print("\nYou're in a calorie deficit! Deficit: " + str(calorieDeficit) + " calories.")
elif calorieDeficit == 0:
    print("\nYou're maintaining your weight.")
else:
    print(f"\nYou're in a calorie surplus! Surplus: {str(abs(calorieDeficit))} calories.")

weightLossGoal = 5
caloriesToLose1Pound = 3500
totalCaloriesToLose = weightLossGoal * caloriesToLose1Pound

daysToLoseWeight = totalCaloriesToLose // calorieDeficit

if totalCaloriesToLose % calorieDeficit == 0:
    print(f"It will take exactly {str(daysToLoseWeight)} days to lose {str(weightLossGoal)} pounds.")
else:
    print(f"It will take approximately {str(daysToLoseWeight)} days to lose {str(weightLossGoal)} pounds, with some extra deficit left.")

print("\nFinal Summary:")
print("1. Your total daily calorie intake is: ", totalCalories)
print("2. You're in a deficit of ", calorieDeficit, " calories per day.")
print("3. It will take you around", daysToLoseWeight, "days to lose", weightLossGoal, "pounds.\n")