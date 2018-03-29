 #You have two strings, s and t. The string t contains only unique elements. Find and return the minimum consecutive substring of s that contains all of the elements from t.

#It's guaranteed that the answer exists. If there are several answers, return the one which starts from the smallest index.

#Example

#For s = "adobecodebanc" and t = "abc", the output should be
#minSubstringWithAllChars(s, t) = "banc".

#Input/Output

#[execution time limit] 4 seconds (py)

#[input] string s

#A string consisting only of lowercase English letters.

#Guaranteed constraints:
#0 ≤ s.length ≤ 100.

#[input] string t

#A string consisting only of unique lowercase English letters.

#Guaranteed constraints:
#0 ≤ t.length ≤ min(26, s.length).

#[output] string

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
