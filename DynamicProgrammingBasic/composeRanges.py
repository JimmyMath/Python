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