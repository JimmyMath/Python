def minSubstringWithAllChars(s, t):
    if t == "":return ""
    S = list(s)
    T, m, i = set(list(t)), len(S)+1, 0
    while i < len(S):
        for j in range(i+1, len(S)+1):
            if T <= set(S[i:j]):
                for k in range(1, j-i+1):
                    if T <= set(S[j-k:j]):
                        break
                if m > k:
                    m = k
                    a = "".join(S[j-k:j])
                    i = j-k+1
                    break
        i = j
    return a
