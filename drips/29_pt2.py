print("Welcome to the Coding Competition Tracker!")
# ...

tasks = "complete Python tutorial, submit project proposal, debug code"
print("\nInitial tasks to complete:", tasks)

# Task 1

tasks = tasks + ", "+ input("New task: ")
print("Updated tasks:", tasks)

# Task 2

print("Tasks in uppercase:", tasks.upper())

# Task 3

print("Index of debug code:", tasks.find("debug code"))

# Task 4

print("First two tasks:", tasks[:49])

# Task 5

tasks = tasks.replace("debug code", "optimize code")
print("Tasks list after replacing debug code with optimize code:", tasks)

# Task 6
print("Final task list:", tasks)

# Task 7
print("Length of tasks:", len(tasks))

# Task 8

print("Attempting to change the first task...")
tasks.replace("complete", "delete")
print("Tasks after attempted modification:", tasks)
print("First task:", tasks[:7])

#Task 9
new_tasks = tasks.capitalize()
print("Updated first task:", new_tasks)