'''
HASH MAPS:

Hash Maps are a very integral data structure that provide very quick look up time
This Class shows algorithms which implement hash maps unique ways
'''

class HashMaps:

    #Leet Code: Two Sum - https://leetcode.com/problems/two-sum/
    #Given an array of integers and an integer, return indices of the two numbers such that they add up to target.
    def twoSum(self, numsList, target):

        HashMap = {}

        for i in numsList:
            HashMap[i] = i
        
        for n in numsList:
            lookup = target - n
            if HashMap.get(lookup):
                return [n,lookup]

        return None

#Test Cases
test = HashMaps()

#Two Sum Example
exampleList = [2,7,11,15]
target = 9
result = test.twoSum(exampleList, target)
print(result)