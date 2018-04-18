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

#0 ≤ sequence[i] ≤ 106. 
        else:
            s += [(i,1)]
    return max([s[i][1] for i in range(k)])
