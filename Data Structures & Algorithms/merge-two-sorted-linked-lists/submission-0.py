# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = list1
        p2 = list2
        start = None
        p3 = None
        if p1 == None:
            return p2
        elif p2 == None:
            return p1
        
        if p1.val <= p2.val:
            p3 = ListNode(p1.val)
            p1 = p1.next
            start = p3
        else:
            p3 = ListNode(p2.val)
            p2 = p2.next
            start = p3
        
        while p1 != None and p2 != None:

            if p1.val <= p2.val:
                p3.next = ListNode(p1.val)
                p3 = p3.next
                p1 = p1.next
            else:
                p3.next = ListNode(p2.val)
                p3 = p3.next
                p2 = p2.next
        
        if p2 != None:
            p3.next = p2
        else:
            p3.next = p1

        return start

 

        
