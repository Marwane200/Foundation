import heapq

'''
SORTING ALGORITHMS

    -Sorting Algorithms are a common class of problems with many implementation
    -This class highlights some of the foundational implmentations of sorting

    -SORT FUNCTIONS-
        selectionSort: finds the minimum number and pops it into the result array
        mergeSort: uses divide and conqure to to sort elements in n log(n) time
        heapSort: uses heap data structure and heap pop to sort array
'''
class Sort:

    def selectionSort(self, array):
        result = []
        size = len(array)
        for n in range(size):
            #Take minimum of the subarray and pop it into the result array
            result.append(array.pop(array.index(min(array))))
        
        return result
    

    def mergeSort(self, array):
        if not array:
            return None

        #base case
        if len(array) == 1: return array

        #divide array in two
        middle = len(array)//2
        LeftArray = array[:middle]
        RightArray = array[middle:]

        # call merge sort on both halfs
        Left = self.mergeSort(LeftArray)
        Right = self.mergeSort(RightArray)

        # bring sorted halfs together
        result = self.mergeArray(Left, Right)
        return list(result)

    def mergeArray(self, LeftArray, RightArray):
        resultArray = []

        #append smallest value to the result array
        while LeftArray and RightArray:
            if LeftArray[0] <= RightArray[0]:
                resultArray.append(LeftArray.pop(0))
            elif LeftArray[0] > RightArray[0]:
                resultArray.append(RightArray.pop(0))

        if not RightArray: resultArray += LeftArray
        else: resultArray += RightArray
    
        return resultArray
    
    #Heap Sorting
    def heapSort(self, array):
        heapq.heapify(array)
        result = []
        while array:
            result.append(heapq.heappop(array))
        
        print(result)
        return result
    


testArray = [2,6,9,8,4,7]
sort = Sort()

# Merge Sort
test1 = sort.mergeSort(testArray)

# Heap Sort
test2 = sort.heapSort(testArray)

#Selection Sort
test3 = sort.selectionSort(testArray)