#Given a sequence of numbers in an array, find the length of its longest increasing subsequence (LIS).
#The longest increasing subsequence is a subsequence of a given sequence in which the subsequence's elements are in strictly increasing order, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous or unique.

#Example

#For sequence = [1, 231, 2, 4, 89, 32, 12, 234, 33, 90, 34, 100], the output should be

#longestIncreasingSubsequence(sequence) = 7.

#The LIS itself is [1, 2, 4, 32, 33, 34, 100].

#Input/Output

#[execution time limit] 4 seconds (py)

#[input] array.integer sequence

#An array describing a sequence.

#Guaranteed constraints:

#1 ≤ sequence.length ≤ 1000,

#0 ≤ sequence[i] ≤ 10**6. 

#[output] integer

#The length of the longest increasing subsequence of a given sequence.

def longestIncreasingSubsequence(sequence):
    k = len(sequence)
    s = [(0,1)]
    for i in range(1,k):
        m = 1
        for j in range(i-1,-1,-1):
            if sequence[j] < sequence[i]:
                if m < s[j][1]+1:
                    m = s[j][1]+1
        if m > 1:
            s += [(i,m)]
        else:
            s += [(i,1)]
    return max([s[i][1] for i in range(k)])
