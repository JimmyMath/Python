def zigzag(a):
    
    s = a[:2]
    n = 1
    for i in range(2,len(a)):
        if s[-2] < s[-1]:
            if s[-1] > a[i]:
                s.append(a[i])
            else:
                if n < len(s):
                    n = len(s)
                s = [s[-1], a[i]]
        elif s[-2] > s[-1]:
            if s[-1] < a[i]:
                s.append(a[i])
            else:
                if n < len(s):
                    n = len(s)
                s = [s[-1], a[i]]
        else:
            s = [s[-1], a[i]]
    return n
    