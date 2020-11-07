class HashMaps:

    #Leet Code: Two Sum 
    def twoSum(self, numsList, target):

        HashMap = {}

        for i in numsList:
            HashMap[i] = i
        
        for n in numsList:
            lookup = target - n
            if HashMap.get(lookup):
                return [n,lookup]

        return None

test = HashMaps()

exampleList = [2,7,11,15]
target = 9
result = test.twoSum(exampleList, target)
print(result)