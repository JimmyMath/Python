def firstNotRepeatingCharacter(s):
    from collections import Counter
    c=Counter(s)
    last=0
    for word in list(s):
        if c[word]==1:
            return word       
        else:
            last=last+1
    if last==len(list(s)):
        return '_'
            