#Your friend John decided to do landscape design. Now his garden can be represented as n vertical columns, the ith of which begins on the y coordinate of a[i], and goes infinitely down. John can do one operation - change the height of any column by 1 (note that the heights can become negative). Your friend wants to change the height of the columns from ai to bi, so that for each 1 ≤ i ≤ n - 2, bi = bi + 2, and any two adjacent columns differ in height exactly on diff.
#Help your friend understand, what is the minimum amount of operations he should perform to obtain desired heights.

#Example

#For a = [1, 2, 3, -1, 2] and diff = 1, the output should be
#landscapeDesign(a, diff) = 5.
#John can obtain the following b = [2, 1, 2, 1, 2].

     _
   _| |  _             _   _   _ 
 _| | | | |           | |_| |_| |
| | | | | |  -------> | | | | | |
| | | |_| |           | | | | | |
| | | | | |           | | | | | |

#Input/Output

#[execution time limit] 4 seconds (py)

#[input] array.integer a

#Initial heights of the columns.

#Guaranteed constraints:
#2 ≤ a.length ≤ 10**5,
#-109 ≤ a[i] ≤ 10**9.

#[input] integer diff

#The height on which two neighboring columns should differ.

#Guaranteed constraints:
#0 ≤ diff ≤ 10**9.

#[output] integer64

#The minimum number of operations John should perform to obtain the desired heights.
#[Python2] Syntax Tips


def landscapeDesign(a, diff):
    k, even, odd1, odd2 = len(a), [], [], []
    for i in range(0,k-1,2):
        even.append(a[i])
        odd1.append(a[i+1]+diff)
        odd2.append(a[i+1]-diff)
    if k % 2 == 1: even.append(a[-1])
    b, c = sorted(even + odd1), sorted(even + odd2)
    bx, cx, S, T = b[(k-1)/2], c[(k-1)/2], 0 , 0
    for y in b:
        S += abs(bx-y)
    for z in c:
        T += abs(cx-z)
    return min(S,T)
