data = [10, 15, 12, 1, 2, 5, 7]
def quickSort(data, start, end):
    # check if the element is only one 
    # check if element is already sorted
    if start >= end:
        return

    # partition or divide  the data
    pivotIndex = partition(data, start, end)

    # sort the left side 
    quickSort(data, 0, pivotIndex - 1)
    
    # sort the right side
    quickSort(data, pivotIndex + 1, end)

def partition(data, start, end):
    pivotIndex = start
    pivotValue = data[pivotIndex]

    # traverse through the data
    while start < end:
        # find the number greater than pivot value
        while start < len(data) and pivotValue >= data[start]:
            start += 1

        # find the number less than pivot value
        while data[end] > pivotValue:
            end -= 1
        
        # if start and end index are not crossing each other then swap start and end
        if start < end:
            data[start], data[end] = data[end], data[start]
    # put the pivot in the right position or swap with the end index
    data[end], data[pivotIndex] = data[pivotIndex], data[end]
    return end
quickSort(data, 0, len(data)-1)
print(data)