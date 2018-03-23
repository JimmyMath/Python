def containsCloseNums(nums, k):
    D={}
    for i in range(len(nums)):
        if nums[i] in D:
            D[nums[i]]=D[nums[i]]+[i]
        else:
            D[nums[i]]=[i]
 
    for v in D.values():
        if len(v)>1:
            for x in v:
                for y in v:
                    if abs(x-y)<=k and x!=y:
                        return True
                    
    return False
