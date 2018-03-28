#Given an array of integers nums and an integer k, determine whether there are two distinct indices i and j in the array where nums[i] = nums[j] and the absolute difference between i and j is less than or equal to k.

#Example

#For nums = [0, 1, 2, 3, 5, 2] and k = 3, the output should be
#containsCloseNums(nums, k) = true.

#There are two 2s in nums, and the absolute difference between their positions is exactly 3.

#For nums = [0, 1, 2, 3, 5, 2] and k = 2, the output should be

#containsCloseNums(nums, k) = false.

#The absolute difference between the positions of the two 2s is 3, which is more than k.

#Input/Output

#[execution time limit] 4 seconds (py)

#[input] array.integer nums

#Guaranteed constraints:
#0 ≤ nums.length ≤ 55000,
#-2**31 - 1 ≤ nums[i] ≤ 2**31 - 1.

#[input] integer k
 
#Guaranteed constraints:
#0 ≤ k ≤ 35000.

#[output] boolean

def containsCloseNums(nums, k):
    D = {}
    for i in range(len(nums)):
        if nums[i] in D:
            D[nums[i]] = D[nums[i]] + [i]
        else:
            D[nums[i]] = [i] 
    for v in D.values():
        if len(v) > 1:
            for x in v:
                for y in v:
                    if abs(x-y) <= k and x != y:
                        return True
    return False
