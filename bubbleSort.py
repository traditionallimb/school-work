array = [9, 2, 8, 4, 7, 1, 5, 6]
lengthOfArray = len(array)
for i in range(lengthOfArray-1):
    for x in range(lengthOfArray - i - 1):
        if array[x] > array[x+1]:
            temp = array[j]
            array.pop(x)
            array.insert(x+1, temp)

print(array)