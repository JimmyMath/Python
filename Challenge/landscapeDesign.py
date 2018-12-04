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