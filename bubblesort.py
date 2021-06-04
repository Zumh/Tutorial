def bubbleSort(array):
    dataLength = len(array) - 1
    sorted = False 

    while not sorted:
        sorted = True

        for index in range(0, dataLength):
            
            if array[index] > array[index+1]:
                sorted = False
                array[index], array[index+1] = array[index+1], array[index]
    
    return array

data = [5,1,4,2,8]
bubbleSort(data)

print(data)