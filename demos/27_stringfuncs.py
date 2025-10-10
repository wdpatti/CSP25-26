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
    elif i.split(": ")[1] == "high" or i.split(": ")[1] == "full":
        a = "medium" 
    elif i.split(": ")[1] == "available":
        a = "unavailable"
    elif i.split(": ")[1] == "unavailable":
        a = "unavailable"

        
    reduced_inventory = reduced_inventory + i.split(": ")[0] + ": " + a + ", "

reduced_inventory = reduced_inventory[:-2]
print("\nReduced Inventory: ")
print(reduced_inventory)

update = input("\nPrint the resource you want to update: ")
new_status = input("Print the new status (low, medium, high, full, available, unavailable): ")

for i in reduced_inventory.split(", "):
    if i.split(": ")[0] == update:
        reduced_inventory = reduced_inventory.replace(i, update + ": " + new_status)

inventory_length = len(inventory)
print("\nThe total number of characters in the inventory description is:", inventory_length)

updated_inventory = reduced_inventory.replace("food: low", "food: full")
print("\nUpdated inventory: ")
print(updated_inventory)

uppercase_inventory = updated_inventory.upper()
print("\nUppercase Inventory: ")
print(uppercase_inventory)

inventory_summary = updated_inventory[:30]
print("\nInventory Summary (First 2 Resources):")
print(inventory_summary)

print("\nInventory report:")
for i in updated_inventory.split(", "):
    print(i)

# save inventory
f = open("files/inventory.txt", "w")
f.write(updated_inventory)
f.close()