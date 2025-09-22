monthlyIncome = 2500
totalExpenses = 0

rent = float(input("Enter your rent for the month: $"))
groceries = float(input("Enter your groceries cost for the month: $"))
utilities = float(input("Enter your utilities cost for the month: $"))
entertainment = float(input("Enter your entertainment cost for the month: $"))

totalExpenses = rent + groceries + utilities + entertainment

if monthlyIncome == totalExpenses:
    print("\nYou're perfectly on budget!")
elif monthlyIncome > totalExpenses:
    print("\nGreat! You're under budget by $" + str(monthlyIncome - totalExpenses))
else:
    print("\nYou're over budget by: $" + str(totalExpenses - monthlyIncome))

essentialExpenses = rent + utilities + groceries
savingsRate = ((monthlyIncome - essentialExpenses) / monthlyIncome) * 100
print(f"\nYour savings rate, after essential expenses, is: {savingsRate} percent.")

savingsGoal = 10000
monthsToSave = savingsGoal // (monthlyIncome - essentialExpenses)
print(f"It will take approximately {str(monthsToSave)} months to save $10,000 with your current spending.")

if savingsGoal % (monthlyIncome - essentialExpenses) == 0:
    print(f"You will reach exactly $10,000 after {str(monthsToSave)} months.")
else:
    print("You will have a little extra savings after", monthsToSave, "months.")

print("\nFinal Summary:")
print("1. Your total monthly essential expenses are: $", essentialExpenses)
print(f"2. You're saving {str(savingsRate)} percent of your income after essential expenses.")
print("3. You can reach your $10,000 savings goal in about", monthsToSave, "months.\n")