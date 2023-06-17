
nums = [1,2,3]
letters =['a','b','c']

#list every permutation
def permutations(nums: list[int]) -> list[int]:

    if len(nums) == 0: return [[]]

    num = nums[0]
    perm_list = []
    next_perm = permutations(nums[1:])

    for perm in next_perm:
        for i in range(len(perm)):
            new_perm = perm[:i] + [num] + perm[i:]
            perm_list.append(new_perm)
        last_perm = perm + [num]
        perm_list.append(last_perm)
        
    return perm_list

print(permutations(nums))




# list every combination
def combinations(items: list) -> list:
    if len(items) == 0: return [[]]

    item = items[0]
    next_combos = combinations(items[1:])

    new_combos = []

    for combo in next_combos:
        curr_combo = [item] + combo 
        new_combos.append(curr_combo)
    
    return next_combos + new_combos


print(combinations(letters))