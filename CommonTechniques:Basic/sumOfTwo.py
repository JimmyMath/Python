def sumOfTwo(a, b, v):
    S=set(a)
    b=list(set(b))
    for x in b:
        if v-x in S:
            return True
    return False
