import math # Import math lib to use its funcitons for rounding

# Renaming Python builtin funcs for use in program
absolute_difference = abs
conservative_estimate = math.floor #Func to round down to nearest int
liberal_estimate = math.ceil # Func to round up to nearest int

#Welcome msg
print("Welcome to the Wildlife Population Analyzer!")
print("Analyzing population estimates for bald eagles and snow leaopards from January to July.")

# Func to get valid fpn from user input
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt)) # Try to convert input to floating point num
        except ValueError:
            print("Invalid input! Please enter a number.") # Handle non-numberic input

# Collect January pop estimates for both species
print("\n--- January Population Estimates ---")
bald_eagle_jan = get_float_input("Enter the estimated January population for Bald Eagles (e.g., 316000.7): ")
snow_leopard_jan = get_float_input("Enter the estimated January population for Snow Leopard (e.g., 4000.9): ")

# Collect July pop estimates for both species
print("\n--- July Population Estimates ---")
bald_eagle_jul = get_float_input("Enter the estimated July population for Bald Eagles (e.g., 316000.7): ")
snow_leopard_jul = get_float_input("Enter the estimated July population for Snow Leopard (e.g., 4000.9): ")

# Display for easy reference
print("\nBald Eagle estimated population in January:", bald_eagle_jan)
print("\nSnow Leopardestimated population in January:", snow_leopard_jan)
print("\nBald Eagle estimated population in July:", bald_eagle_jul)
print("\nSnow Leopardestimated population in July:", snow_leopard_jul)

# Calculate and display the change in bald eagle population from Jan to Jul
bald_eagle_change = bald_eagle_jul - bald_eagle_jan # Calculate the difference
if bald_eagle_change > 0:
    print("\nBald eagle population increased by:", bald_eagle_change) # Positive Change
elif bald_eagle_change < 0:
    print("\nBald eagle population decreased by:", absolute_difference(bald_eagle_change))
else:
    print("\nBald eagle population remained the same.") # No change

#Calculate and display the change in Snow Leopard population from January to July
snow_leopard_change = snow_leopard_jul - snow_leopard_jan # Calculate the difference
if snow_leopard_change > 0:
    print("\nSnow Leopard population increased by:", snow_leopard_change) # Positive Change
elif snow_leopard_change < 0:
    print("\nSnow Leopard population decreased by:", absolute_difference(snow_leopard_change))
else:
    print("\nSnow Leopard population remained the same.") # No change

bald_eagle_conservative_jul = conservative_estimate(bald_eagle_jul)
snow_leopard_conservative_jul = conservative_estimate(snow_leopard_jul)
print("\nConservative July Population Estimate (using conservative_estimate):")
print("Bald Eagle:", bald_eagle_conservative_jul)
print("Snow Leopard:", snow_leopard_conservative_jul)

bald_eagle_liberal_jul = liberal_estimate(bald_eagle_jul)
snow_leopard_liberal_jul = liberal_estimate(snow_leopard_jul)
print("\Liberal July Population Estimate (using conservative_estimate):")
print("Bald Eagle:", bald_eagle_liberal_jul)
print("Snow Leopard:", snow_leopard_liberal_jul)

simple_bald_eagle_population = int(bald_eagle_jul)
simple_snow_leopard_population = int(snow_leopard_jul)
print("Simplified Bald Eagle Population for Reporting (using int):", simple_bald_eagle_population)
print("Simplified Snow Leopard Population for Reporting (using int):", simple_snow_leopard_population)