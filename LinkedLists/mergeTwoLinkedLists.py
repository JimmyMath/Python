# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    if l1==None or l2==None:
        return l1 or l2
    dummy=ListNode(None)
    curr=dummy
    while True:
        if l1.value<l2.value:
            curr.next=l1
            curr=curr.next
            if l1.next==None:
                curr.next=l2
                break
            l1=l1.next
        else:
            curr.next=l2
            curr=curr.next
            if l2.next==None:
                curr.next=l1
                break
            l2=l2.next   
    return dummy.next