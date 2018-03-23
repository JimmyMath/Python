# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):
    if l==None:
        return None
    if n==0:
        return l
    if l.next==None:
        return l
    
    r,s=l.next,l.next
    i,D=1,{}
    
    while r:
        D[0]=l
        D[i]=r
        r=r.next
        i=i+1
    
    if i==n:
        return l
        
    
    D[i-n-1].next=None
    D[i-1].next=l
    
    return D[i-n]
        
    
    