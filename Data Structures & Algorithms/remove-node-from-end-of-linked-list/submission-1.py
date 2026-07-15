# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head == None:
            return
        

        size = 0

        curr = head

        while curr != None:
            curr = curr.next
            size += 1
        
        nodes_to_skip = size - n

        if nodes_to_skip == 0:
            return head.next

        i = 0
        curr = head
        while curr.next != None and i < nodes_to_skip - 1:
            curr = curr.next
            i+=1

        print(curr.val)
        if curr.next != None:
            curr.next = curr.next.next
        
        return head
        