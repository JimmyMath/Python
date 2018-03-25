def decodeString(s):
    strings = list(s)
    if "]" not in strings:
        return s
    i = strings.index("]")
    front = strings[:i]
    a, n="", ""
    while front[-1]!="[":
        a+=front[-1]
        front.pop()
    a = a[::-1]
    front.pop()
    while front[-1].isdigit():
        n+=front[-1]
        if len(front)==1:
            break
        else:
            front.pop()
    n=int(n[::-1])
    
    if front[-1].isdigit():
        return a*n+decodeString(s[i+1:])
    else:
        return decodeString("".join(front)+a*n+s[i+1:])
        
