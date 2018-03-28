#Given a 2D grid skyMap composed of '1's (clouds) and '0's (clear sky), count the number of clouds. A cloud is surrounded by clear sky, and is formed by connecting adjacent clouds horizontally or vertically. You can assume that all four edges of the skyMap are surrounded by clear sky.

#Example

#For

#skyMap = [['0', '1', '1', '0', '1'],
#          ['0', '1', '1', '1', '1'],
#          ['0', '0', '0', '0', '1'],
#          ['1', '0', '0', '1', '1']]
#the output should be 
#countClouds(skyMap) = 2;

#For

#skyMap = [['0', '1', '0', '0', '1'],
#          ['1', '1', '0', '0', '0'],
#          ['0', '0', '1', '0', '1'],
#          ['0', '0', '1', '1', '0'],
#          ['1', '0', '1', '1', '0']]
#the output should be
#countClouds(skyMap) = 5.

#Input/Output

#[execution time limit] 4 seconds (py)

#[input] array.array.char skyMap

#A 2D grid that represents a map of the sky, as described above.

#Guaranteed constraints:

#0 ≤ skyMap.length ≤ 300,
#0 ≤ skyMap[i].length ≤ 300.

#[output] integer

#The number of clouds in the given skyMap, as described above.

def countClouds(skyMap):
    n = 0
    for i in range(len(skyMap)):
        for j in range(len(skyMap[0])):
            if skyMap[i][j] == '1':
                n += 1
                modifyClouds(skyMap, i, j)
    return n
                
def modifyClouds(M, k, l):
    if 0 <= k < len(M) and 0 <= l < len(M[0]) and M[k][l] == '1':
        M[k][l] = '0'
        modifyClouds(M, k-1, l)
        modifyClouds(M, k+1, l)
        modifyClouds(M, k, l-1)
        modifyClouds(M, k, l+1)
    else: 
        return
    
    
