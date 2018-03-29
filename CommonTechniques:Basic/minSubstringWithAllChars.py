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
    S = list(s)
    T, index, m, i = set(list(t)), [], len(S)+1, 0
    for x in range(len(S)):
        if S[x] in T:
            index.append(x)      
    while i < len(index):
        for j in range(i, len(index)):
            if T <= set(S[index[i]:index[j]+1]):
                for k in range(j-i+1):
                    if T <= set(S[index[j-k]:index[j]+1]):
                        break
                if m > index[j]-index[j-k]+1:
                    m = index[j]-index[j-k]+1
                    a = "".join(S[index[j-k]:index[j]+1])
                    i = j - k + 1
                    break
        i = j + 1
    return a if t else ""
