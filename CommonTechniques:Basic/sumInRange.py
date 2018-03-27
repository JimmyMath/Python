import numpy as np
def sumInRange(nums, queries):
    N,S = np.cumsum(nums),0
    for i in range(len(queries)):
        if queries[i][0]==0:
            S+=N[queries[i][1]]
        else:
            S+=N[queries[i][1]]-N[queries[i][0]-1]
    return S%(10**9+7)
