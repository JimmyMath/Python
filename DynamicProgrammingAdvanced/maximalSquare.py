def maximalSquare(matrix):
    if matrix==[]:
        return 0
    r=len(matrix)
    l=len(matrix[0])
    
    if r==1 or l==1:
        if matrix!=[['0']*l]*r:
            return 1
        return 0
    else:
        S=[[0 for j in range(l)] for i in range(r)]
        for i in range(r):
            S[i][0]=int(matrix[i][0])
        for j in range(l):
            S[0][j]=int(matrix[0][j])
        
        for i in range(1,r):
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
