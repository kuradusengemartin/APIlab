# Initialize an empty list to store names
names = []

# Get names from the user until an empty input is given
while True:
    name = input("Enter a name (or press Enter to finish): ")
    if not name:
        break
    names.append(name)

# Capitalize the first letter of each name
capitalized_names = [name.title() for name in names]

# Sort the names alphabetically
sorted_names = sorted(capitalized_names)

# Display the sorted names
print("Sorted Names:")
for name in sorted_names:
    print(name)