import sys

array = [64, 25, 12, 22, 11]
# Traverse all the array's elements
for index in range(len(array)):
    # find minimum value from the array
    minIndex = index
    for rightIndex in range(index+1, len(array)):
        # check the min
        if array[minIndex] > array[rightIndex]:
            minIndex = rightIndex
    # swap min from the right to the left
    array[index], array[minIndex] = array[minIndex], array[index]
    
# print the sorted data
print("Sorted Array")
for index in range(len(array)):
    print("%d" %array[index])