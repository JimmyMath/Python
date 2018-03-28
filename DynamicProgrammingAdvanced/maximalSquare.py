#You have a 2D binary matrix that's filled with 0s and 1s. In the matrix, find the largest square that contains only 1s and return its area.

#Example

#For

#matrix = [
#    ['1', '0', '1', '1', '1'],
#    ['1', '0', '1', '1', '1'],
#    ['1', '1', '1', '1', '1'],
#    ['1', '0', '0', '1', '0'],
#    ['1', '0', '0', '1', '0']
#    ]
#the output should be
#maximalSquare(matrix) = 9.

#Input/Output

#[execution time limit] 4 seconds (py)

#[input] array.arra  return 1
        return 0
    else:y.char matrix

#Guaranteed constraints:
#0 ≤ matrix.length ≤ 100,
#1 ≤ matrix[i].length ≤ 100,
#0 ≤ matrix[i][j] ≤ 1.

#[output] integer

#An integer that represents the area of the largest square in the given matrix that is composed only of 1s.

def maximalSquare(matrix):
    if matrix == []:
        return 0
    r, l = len(matrix), len(matrix[0])
    if r == 1 or l == 1:
        if matrix != [['0'] * l] * r:
    S = [ [0 for j in range(l)] for i in range(r) ]
    for i in range(r):
        S[i][0] = int(matrix[i][0])
    for j in range(l):
        S[0][j] = int(matrix[0][j])
        
    for i in range(1, r):
        for j in range(1, l):
            if matrix[i][j] == '1':
                S[i][j] = min(S[i][j-1],S[i-1][j],S[i-1][j-1]) + 1
            else:
                S[i][j] = 0 
    n = S[0][0]
    for i in range(r):
        for j in range(l):
            if n < S[i][j]:
                n = S[i][j]
    return n**2
