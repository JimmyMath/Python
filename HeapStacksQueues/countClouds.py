'''
Created on Mar 23, 2018

@author: Jim
'''
def countClouds(skyMap):
    n=0
    for i in range(len(skyMap)):
        for j in range(len(skyMap[0])):
            if skyMap[i][j] == '1':
                modifyClouds(skyMap,i,j)
                n+=1
    return n
                
def modifyClouds(M,k,l):
    if 0<=k<len(M) and 0<=l<len(M[0]) and M[k][l]=='1':
        M[k][l]='0'
        modifyClouds(M,k-1,l)
        modifyClouds(M,k+1,l)
        modifyClouds(M,k,l-1)
        modifyClouds(M,k,l+1)
    else: 
        return
    
    