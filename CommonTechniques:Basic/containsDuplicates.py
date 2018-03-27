def containsDuplicates(a):
    D={}
    for i in range(len(a)):
        if a[i] not in D:
            D[a[i]]=[i]
        else:
            D[a[i]]=D[a[i]]+[i]
    for k in D.keys():
        if len(D[k])>1:
            return True
    return False