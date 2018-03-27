import numpy as np
def findLongestSubarrayBySum(s, arr):
    N,index,m=np.cumsum([0]+arr),[],0
    for i in range(len(arr)):
        index.append(i+1)
        if N[index[-1]]-N[index[0]-1]==s and len(index)>m:
            m,longest=len(index),[index[0],index[-1]]
        if N[index[-1]]-N[index[0]-1]>s:
            while index!=[] and N[index[-1]]-N[index[0]-1]>s:
                del index[0]
            if index!=[] and N[index[-1]]-N[index[0]-1]==s and len(index)>m:
                m,longest=len(index),[index[0],index[-1]]
    if m==0:
        return [-1]
    return longest
