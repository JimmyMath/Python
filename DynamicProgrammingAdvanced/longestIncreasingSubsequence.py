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