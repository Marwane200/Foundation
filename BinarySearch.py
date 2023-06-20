def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    i = -1

    while left <= right:
        mid = (left + right )//2
        if arr[mid] >= target:
            i = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
    return i

def upperBinarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    i = -1

    while left <= right:
        mid = (left + right )//2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] <= target:
            left = mid + 1
            i = mid
    return i

def trueFalseSearch(arr):
    left = 0
    right = len(arr) - 1
    i = -1
    while left <= right:
        mid = (left + right )//2
        if arr[mid]:
            i = mid
            left = mid + 1
        else:
            right = mid - 1
    return i

test1 = [1,2,3,4,5,6]
test2 = [1,2,3,3,3]
test3 = [True,True,True,True,False,False]

ans1 = binarySearch(test1,4)
lower = binarySearch(test2,3)
upper =  upperBinarySearch(test2,3)
binary = trueFalseSearch(test3)
print(ans1)
print(lower,upper)
print(binary)