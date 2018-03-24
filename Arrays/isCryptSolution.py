import itertools
def isCryptSolution(crypt, solution):
    nums=[]
    for x in crypt:
        string=''
        for i,y in itertools.product(range(len(x)),solution):
            if x[i]==y[0]:
                string+=y[1]
        nums.append(string)  
    for i in range(3):
        if len(nums[i])>1 and nums[i][0]=='0':
            return False
    if int(nums[0])+int(nums[1])==int(nums[2]):
        return True
    return False