# Create an empty list
my_list = [10, 20, 30, 40 ]

# Append elements 10, 20, 30, 40
my_list.append(50)
my_list.append(60)
my_list.append(70)
my_list.append(80)

# Insert value 15 at the second position (index 1)
my_list.insert(1, 15)

# Extend my_list with another list [50, 60, 70]
my_list.extend([90, 95, 99])

# Remove the last element
my_list.pop()

# Sort the list in ascending order
my_list.sort()

# Find and print the index of value 30
index_30 = my_list.index(30)
print("Final list:", my_list)
print("Index of 30:", index_30)
