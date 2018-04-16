def paintHouses(cost):
    k = len(cost)
    a ,b, c = 0, 0, 0 
    for i in range(k-1,-1,-1):
        a, b ,c = min(b,c)+cost[i][0], min(a,c)+cost[i][1], min(a,b)+cost[i][2]
    return min(a,b,c)
    