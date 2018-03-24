import numpy as np
from collections import Counter
import itertools
def sudoku2(grid):
    
    grid=np.array(grid)
    
    for i in range(0,9):
        c=Counter(grid[i,:])
        for z in grid[i,:]:
            if c[z]>1 and z!='.':
                    return False
    
    for j in range(0,9):
        c=Counter(grid[:,j])
        for y in grid[:,j]:
            if c[y]>1 and y!='.':
                    return False
                
    for h,k in itertools.product([1,4,7],[1,4,7]):
        sub=[]
        for a,b in itertools.product([-1,0,1],[-1,0,1]):
            sub.append(grid[h+a][k+b])
        c=Counter(sub)
        for w in sub:
            if c[w]>1 and w!='.':
                return False
    
    return True
