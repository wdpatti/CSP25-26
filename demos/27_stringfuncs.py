print("Welcome to the Space Mission Inventory Manager!")
print("You will check and manage the inventory for your space mission.")

inventory = "oxygen: full, water: full, food: low, fuel: medium, tools: available, medkits: high, spare parts: low"

print("\nCurrent Inventory: ")
print(inventory)

oxygen_status_index = inventory.find("oxygen")
oxygen_status = inventory[oxygen_status_index:oxygen_status_index+11]
print("\nOxygen status:", oxygen_status)

food_status_index = inventory.find("food")
food_status = inventory[food_status_index:food_status_index+9]
print("Food status:", food_status)

for i in inventory.split(", "):
    if i.split(": ")[1] == "low":
        print(f"\nWarning: {i.split(': ')[0]} are low!")

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