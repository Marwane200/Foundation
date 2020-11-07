class Sort:
    def mergeSort(self, array):

        if len(array) == 1: return array

        middle = len(array)//2
        LeftArray = array[:middle]
        RightArray = array[middle:]


        Left = self.mergeSort(LeftArray)
        Right = self.mergeSort(RightArray)

        result = self.mergeArray(Left, Right)
        return list(result)

    def mergeArray(self, LeftArray, RightArray):
        resultArray = []

        while LeftArray and RightArray:
            if LeftArray[0] <= RightArray[0]:
                resultArray.append(LeftArray.pop(0))
            elif LeftArray[0] > RightArray[0]:
                resultArray.append(RightArray.pop(0))

        if not RightArray: resultArray += LeftArray
        else: resultArray += RightArray
        
        return resultArray

testArray = [1,3,2,8,4,7,6]
test = Sort()
result = test.mergeSort(testArray)
print(result)