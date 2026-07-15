# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return None
        elif head.next == None:
            return head;
        else:
            p1 = None
            p2 = head
            p3 = head.next
            
            while p2 != None:
                
                p2.next = p1
                p1 = p2
                p2 = p3
                if p3 != None:
                    p3 = p3.next
                

 
            
            return p1
        