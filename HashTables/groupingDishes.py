def groupingDishes(dishes):
    keys=[]
    hash={}
    for row in dishes:
        for i in range(1,len(row)):
            keys=keys+[row[i]]
    keys=sorted([x for i, x in enumerate(keys) if x not in keys[:i]])
    for k in keys:
        values=[]
        for row in dishes:
            if k in row[1:]:
                values=values+[row[0]]
        hash[k]=sorted(values)

    return [[k]+hash[k] for k in keys if len(hash[k]) > 1]
    