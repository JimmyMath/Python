'''
Created on Mar 14, 2018

@author: Jim
'''
# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseNodesInKGroups(l, k):
    
    if k == 1:
        return l
    
    r,i = l.next,1
    
    while r:
        r = r.next
        i = i+1
    
    if i < k:
        return l
    
    dummy, n = ListNode(None), None
    
    for j in range(k):
        m = l.next
        l.next = n
        n = l
        dummy.next = l
        l = m
    
    if i==k:
        return dummy.next
    
    s=dummy.next.next
    
    for a in range(k-2):
        s=s.next
    
    s.next=reverseNodesInKGroups(l, k)
    
    return dummy.next
        
        
    