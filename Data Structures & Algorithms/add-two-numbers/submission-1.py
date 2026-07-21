# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def isLastNode(self, l1, l2):
        return (l1 == None and l2 != None and l2.next == None) or (l2 == None and l1 != None and l1.next == None) or (l1 != None and l2 != None and l1.next == None and l2.next == None)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        s = ListNode(0)
        c = s
        carry = 0

        while l1 != None or l2 != None:
            a = carry

            if l1 != None:
                a += l1.val
            
            if l2 != None:
                a += l2.val

            carry = int(a / 10)
            s.val = a % 10

            if self.isLastNode(l1, l2):
                if carry != 0:
                    s.next = ListNode(carry)
            else:
                s.next = ListNode()
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if s:
                s = s.next
        return c


