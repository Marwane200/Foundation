class Greedy:

    #Given an american coin set find the minum amount of coins
    def minCoins(self, money :int) -> int:
        coins = [25,10,5,1]
        count = 0
        while money:
           for coin in coins:
               while (money - coin) >= 0:
                   money -= coin
                   count  += 1
               if money == 0: break
        
        return count
    
    #Leet Code 1403: Minimum Sub Sequence
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        total = sum(nums)
        subArray = []

        for num in nums:
            subArray.append(num)
            subTotal = sum(subArray)
            if subTotal > (total - subTotal):
                return subArray

        return subArray

testArray = [4,4,7,6,7]
test = Greedy()
print(test.minCoins(92))
print(test.minSubsequence(testArray))