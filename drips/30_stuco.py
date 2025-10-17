print("Welcome to the Student Club Event Manager!\nYou will manage items and activities for the event.")

#Initial setup & prints
inventory = "snacks: available, water: low, projector: available, chairs: unavailable"
print("Initial event setup:", inventory)

#Print index of the word 'water'
print("The word 'water' starts at index:", inventory.find("water"))

#Print first two items using slice
print("First two items for the event:", inventory[:29])

#Replaced water low with water available
inventory = inventory.replace("water: low", "water: available")
print("Updated event setup after replacing 'water':", inventory)

#Prints uppercase inventory
print("Event setup in UPPERCASE:", inventory.upper())

#Prints len of inventory
print("The total number of characters in the event setup:", len(inventory))

#Final event setup after adding mics
final_inventory = inventory + ", microphones: available"
print("Final event setup after adding 'microphones':", final_inventory)