#Repeat entire script until the user requests to stop
while True:
    #Repeat until the numbers are both integers
    while True:
        #If these numbers are very large or very small nothing should change due to the nature of python's floating point variables
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        #Check validity of num1 and num2 with try: except:
        try:
            num1 = float(num1)
            num2 = float(num2)
            break
        except:
            print("Both num1 and num2 must be able to be expressed as floating point values. Please try again.")
            continue

    #Calculate and output sum, diff, product of num1 & num2
    sum = num1 + num2
    print(f"The sum of {str(num1)} and {str(num2)} is {str(sum)}.")
    diff = num1 - num2
    print(f"The difference of {str(num1)} and {str(num2)} is {str(diff)}.")
    product = num1 * num2
    print(f"The product of {str(num1)} and {str(num2)} is {str(product)}.")
    
    #Check if num2 is zero (to prevent zero division)
    if num2 == 0:
        print("Because the second number is zero, the quotient and modulo calculations are not possible.")
    else:
        #If num2 is not zero calculate and output quotient with floor division and remainder with modulo
        quotient = num1 // num2
        print(f"The quotient (floor division) of {str(num1)} and {str(num2)} is {str(quotient)}.")
        modulo = num1 % num2
        print(f"The remainder after dividing {str(num1)} by {str(num2)} is {str(modulo)}.")

    #Ask if user would like to try again - if not then break out of the while loop
    if input("Would you like to perform these calculations on another set of numbers? (y/n)").lower() in ["no", "n"]:
        break