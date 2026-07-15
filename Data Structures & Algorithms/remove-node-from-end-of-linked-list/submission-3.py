# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        left = head
        right = head

        i = 0
        while right != None and i < n:
            right = right.next
            i+=1




        if right == None:
            return head.next
        
        while right.next != None:
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return head

        

        