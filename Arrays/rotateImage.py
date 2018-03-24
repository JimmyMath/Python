'''
Created on Mar 14, 2018

@author: Jim
'''
def rotateImage(a):
    k=len(a)
    Matrix = [[0 for x in range(0,k)] for y in range(0,k)]
    for i in range(0,k):
        for j in range(0,k):
            Matrix[i][j]=a[k-1-j][i]
    return Matrix