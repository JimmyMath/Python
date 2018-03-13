import heapq
def simplifyPath(path):
    ps=path.split("/")
    array=[]
    for x in ps:
        if x!='' and x!='.':
            array.append(x)
    h=[]
    for i in range(len(array)):
        if array[i]!="..":
            heapq.heappush(h,(len(array)-1-i,array[i]))
        else:
            heapq.heappushpop(h,(len(array),array[i]))
    array1=[]
    for x in h:
        if x[1]!="..":
            array1.append(x)
    if array1==[]:
        return "/"
    s=""
    for y in sorted(array1)[::-1]:
        s+="/"+y[1]
    return s
