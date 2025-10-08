print("Welcome to the Space Mission Inventory Manager!")
print("You will check and manage the inventory for your space mission.")

f = open("files/inventory.txt", "r")
inventory = f.read()
f.close()

print("\nCurrent Inventory: ")
print(inventory)

oxygen_status_index = inventory.find("oxygen")
oxygen_status = inventory[oxygen_status_index:oxygen_status_index+11]
print("\nOxygen status:", oxygen_status)

food_status_index = inventory.find("food")
food_status = inventory[food_status_index:food_status_index+9]
print("Food status:", food_status)

reduced_inventory = ""

for i in inventory.split(", "):
    if i.split(": ")[1] == "low":
        print(f"\nWarning: {i.split(': ')[0]} are low!")
        a = "low"
    elif i.split(": ")[1] == "medium":
        a = "low" 
    elif i.split(": ")[1] == "high":
        a = "medium" 
    elif i.split(": ")[1] == "available":
        a = "unavailable"
    elif i.split(": ")[1] == "unavailable":
        a = "unavailable"

        
    reduced_inventory = reduced_inventory + i.split(": ")[0] + ": " + a + ", "

reduced_inventory = reduced_inventory[:-2]

inventory_length = len(inventory)
print("\nThe total number of characters in the inventory description is:", inventory_length)

updated_inventory = inventory.replace("food: low", "food: full")
print("\nUpdated inventory: ")
print(updated_inventory)

uppercase_inventory = updated_inventory.upper()
print("\nUppercase Inventory: ")
print(uppercase_inventory)

inventory_summary = updated_inventory[:30]
print("\nInventory Summary (First 2 Resources):")
print(inventory_summary)

# save inventory
f = open("files/inventory.txt", "w")
f.write(reduced_inventory)
f.close()