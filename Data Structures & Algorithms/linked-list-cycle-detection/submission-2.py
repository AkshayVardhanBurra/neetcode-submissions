# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        if head.next == head:
            return True
        slow = head
        fast = head.next

        while slow != None and fast != None and slow != fast:
            slow = slow.next
            if fast.next != None:
                fast = fast.next.next
            else:
                fast = None
        
        if slow == None or fast == None:
            return False
        return slow == fast
            