#Given a sorted integer array that does not contain any duplicates, return a summary of the number ranges it contains.

#Example

#For nums = [-1, 0, 1, 2, 6, 7, 9], the output should be
#composeRanges(nums) = ["-1->2", "6->7", "9"].

#Input/Output

#[execution time limit] 4 seconds (py)

#[input] array.integer nums

#A sorted array of unique integers.

#Guaranteed constraints:
#0 ≤ nums.length ≤ 15,
#-(231 - 1) ≤ nums[i] ≤ 231 - 1.

#[output] array.string

def composeRanges(nums):
    if len(nums)==0:
        return []
    elif len(nums)==1:
        return [str(nums[0])]
    else:
        for i in range(0,len(nums)-1):
            if nums[i]+1<nums[i+1]:
                if i==0:
                    array=[str(nums[0])]
                else:
                    array=[str(nums[0])+"->"+str(nums[i])]
                return array+composeRanges(nums[i+1:])
            else:
                if i==len(nums)-2:
                    return [str(nums[0])+"->"+str(nums[-1])]
