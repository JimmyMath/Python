def firstDuplicate(a):
    l = zip(a,range(len(a)))
    di = list_to_dict(l)
    ll = [(v[1],k) for k, v in di.iteritems() if len(v) > 1]
    if not ll:
        return -1
    else:
        (x,y) = min(ll)
        return y

def list_to_dict(li):
     dct = {}
     for (item,v) in li:
         if dct.has_key(item):
                 dct[item] = dct[item] + [v]
         else:
             dct[item] = [v]
     return dct
