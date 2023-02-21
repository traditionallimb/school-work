workingArray = [1, 3, 5, 7, 8]

# Array Traversal
print("Array Traversal")
for i in workingArray:
    print(f"Traversing the array: {i}")
print(workingArray)

# Array Insertion
print("\n\n\nArray Insertion")
print(f"Original Array: {workingArray}")
newArray = list(workingArray)  # Added this so that it doesn't just rename the variable, but creates a copy
newArray.insert(3, 10)
print(f"New Array: {newArray}")

# Array Deletion (pop)
print("\n\n\nArray Deletion (pop)")
print(f"Original Array: {workingArray}")
newArray = list(workingArray)
newArray.pop(2)
print(f"New Array: {newArray}")

# Array Deletion (remove)
print("\n\n\nArray Deletion (remove)")
print(f"Original Array: {workingArray}")
newArray = list(workingArray)
newArray.remove(5)
print(f"New Array: {newArray}")

# Array Deletion (del)
print("\n\n\nArray Deletion (del)")
print(f"Original Array: {workingArray}")
newArray = list(workingArray)
del newArray[2]
print(f"New Array: {newArray}")

# Array Search (index)
print("\n\n\nArray Search (index)\n")
print(f"Search Array: {workingArray}")
itemPos = workingArray.index(5)
print(f"The position of '5' in the array is found at position {itemPos}")

# Array Search (linear)
print("\n\n\nArray Search (linear)\n")
print(f"Search Array: {workingArray}")
for i in range(len(workingArray)):
    if workingArray[i] == 5:
        itemPos = i
    else:
        print("", end="\r")
print(f"The position of '5' in the array is found at position {itemPos}")

# Array Search (in)
print("\n\n\nArray Search (in)")
print(f"Search Array: {workingArray}")
print("Is '5' in the array?")
if 5 in workingArray:
    print("True")
elif 5 not in workingArray:
    print("False")

# Array Updating
print("\n\n\nArray Updating (list indexing)")
print(f"Original Array: {workingArray}")
newArray = list(workingArray)
newArray[2] = 10
print(f"New Array: {newArray}")
