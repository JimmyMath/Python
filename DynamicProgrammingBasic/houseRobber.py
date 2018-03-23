from collections import Counter
dict = Counter()
def houseRobber(nums):
    if dict[len(nums)] != 0:
        return dict[len(nums)]
    if len(nums)==0:
        return 0
    elif len(nums)==1:
        return nums[0]
    else:
        dict[len(nums[1:])]= houseRobber(nums[1:])
        return max(dict[len(nums[1:])], nums[0]+dict[len(nums[2:])])