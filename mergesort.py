# merge
def merge(array):
    # Initialize the temporary array
    temp = [0]*len(array)
    rightIndex = 1
    leftIndex = 0
    # [,]
    # start from the leftIndex
    while  rightIndex < len(array):
        while  leftIndex < len(array) - rightIndex:
            mergeSort(array[leftIndex:leftIndex+rightIndex], array[leftIndex + rightIndex:], temp, leftIndex, rightIndex)
            leftIndex += 2 * rightIndex
           
        for index in range(0, len(array)):
            array[index] = temp[index]
        leftIndex = 0

        rightIndex *= 2
        
    return array


# merge sort
def mergeSort(first, second, temp, tempStart, max):
    firstIndex = secondIndex = 0
    tempIndex = tempStart
  
    while firstIndex < max and secondIndex < max and (secondIndex < len(second) or firstIndex < len(first)):
        # compare two array and sort or merge
        if first[firstIndex] < second[secondIndex]:
            temp[tempIndex] = first[firstIndex]
            tempIndex += 1
            firstIndex += 1

        else:

            temp[tempIndex] = second[secondIndex]
            tempIndex += 1
            secondIndex += 1
    
    # collect left  number
    while firstIndex < max and firstIndex < len(first):
       
        temp[tempIndex] = first[firstIndex]
        tempIndex += 1
        firstIndex += 1

    # collect  right number
    while secondIndex <= max and secondIndex < len(second) :
        temp[tempIndex] = second[secondIndex] 
        tempIndex += 1
        secondIndex += 1


array=[1,5,2,9,7,3,8,3,10]
newArray=[4,3,1,67,55,8,0,4,-5,37,7,4,2,9,1,-1]
#print(array)
print(merge(array))
print(merge(newArray))


