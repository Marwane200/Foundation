'''
RECURSION
Recusive algorithms are partical set of algorithms in which a function calls upon its self.
This class contains many classic examples of recursion

-Recursive-
    fibbonacce: given a number find the fibonnace number
    dynamicFib: finds the fibonnace number using dynamic programming and memoization
    bottomupFib: finds the fibonnace number using the bottoms up approach

    climbingStairs: given a certain integers of steps, how many possible ways is it to get to the top by taking only 1 or 2 steps
'''
class Recusive:

    # Using regular recursion
    def fibbonacce(self, num):

        #Base Cases
        if num == 0: return 0
        if num <= 2: return 1

        #Creates 2 branches that call on its self
        return self.fibbonacce(num-1) + self.fibbonacce(num-2)
    
    # finds Fibbonnace
    def dynamicFib(self, num):
        #Creates memo and initalizes the base case
        memo = [None] * (num+1)
        memo[1]=1
        memo[0]=1

        return self.memoFib(num,memo)

    #Calls in the memoization for dynamicFib
    def memoFib(self, num, memo):
        if memo[num]:
            return memo[num]
        
        memo[num] = self.memoFib(num-1,memo) + self.memoFib(num-2, memo)
        return memo[num]
    
    #Bottoms Up Approach
    def bottomUpFib(self, num):
        memo = [None] * num
        memo[0]=1
        memo[1]=1

        for n in range(2,num):
            memo[n] = memo[n-1] + memo[n-2]

        return memo[num-1]
    

    #Leet Code: Climbing Stairs - Brute Force
    def climbStairs(self, num: int) -> int:
        #Base Cases
        if num == 0: return 1
        elif num < 0: return 0

        #Possible Decisions
        step1 = self.climbStairs(num-1)
        step2 = self.climbStairs(num-2)

        return step1 + step2
    
    #Climbing Stairs with Dynamic Programming
    def climbStairs2(self, num: int) -> int:
        memo = [None] * (num+1)
        memo[1]=1
        memo[2]=2
        return self.climb(num, memo)
    
    def climb(self, num, memo):

        #Base Case which checks cache
        if memo[num]: return memo[num]

        #Decision Tree
        step1 = self.climb(num-1,memo)
        step2 = self.climb(num-2,memo)

        #Cache and return results
        memo[num] = step1 + step2
        return memo[num]


#Test Cases
test = Recusive()

fib1 = test.fibbonacce(10)
fib2 = test.dynamicFib(23)
fib3 = test.bottomUpFib(13)
print(fib1)
print(fib2)
print(fib3)

#Climbing Stairs
climb1 = test.climbStairs(28)
climb2 = test.climbStairs2(28)
print(climb1)
print(climb2)
        