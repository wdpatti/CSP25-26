while True:
    while True:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        try:
            num1 = float(num1)
            num2 = float(num2)
            break
        except:
            print("Both num1 and num2 must be able to be expressed as floating point values. Please try again.")
            continue

    sum = num1 + num2
    print(f"The sum of {str(num1)} and {str(num2)} is {str(sum)}.")
    diff = num1 - num2
    print(f"The difference of {str(num1)} and {str(num2)} is {str(diff)}.")
    product = num1 * num2
    print(f"The sum of {str(num1)} and {str(num2)} is {str(product)}.")
    if num2 == 0:
        print("Because the second number is zero, the quotient and modulo calculations are not possible.")
    else:
        quotient = num1 // num2
        print(f"The quotient (floor division) of {str(num1)} and {str(num2)} is {str(quotient)}.")
        modulo = num1 % num2
        print(f"The remainder after dividing {str(num1)} and {str(num2)} is {str(modulo)}.")

    if input("Would you like to perform these calculations on another set of numbers? (y/n)").lower() in ["no", "n"]:
        break