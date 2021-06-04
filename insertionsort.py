
key = 0
sortedIndex = 0
array = [12, 11, 13, 5, 6]
def insertionSort():
    # traversed through the unsorted array
    for unsortedIndex in range(1, len(array)):
        key = array[unsortedIndex]
        sortedIndex = unsortedIndex - 1
        # compare everything and move the larger number to the right
        # make new position for key
        while sortedIndex >= 0 and key < array[sortedIndex]:
            array[sortedIndex + 1] = array[sortedIndex]
            sortedIndex = sortedIndex - 1
        # insert the key to new position
        array[sortedIndex + 1] = key
insertionSort()
for index in range(0, len(array)):
    print("%d" %array[index])

