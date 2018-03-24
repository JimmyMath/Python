def nextLarger(a):
    a=a[::-1]
    Larger=[-1]
    
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            Larger.append(a[i]) 
        else:
            b=a[:i]
            while b!=[]:
                if b[-1]>a[i+1]:
                    Larger.append(b[-1])
                    break
                b.pop()
            if b==[]:
                Larger.append(-1)
    return Larger[::-1]
