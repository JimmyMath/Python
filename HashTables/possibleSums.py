def possibleSums(coins, quantity):
    D={0}
    
    for i,j in zip(coins,quantity):
        E=set()
        for partial in range(0,i*(j+1),i):
            for x in D:
                E.add(partial+x)
        D=E
            
    return len(D)-1