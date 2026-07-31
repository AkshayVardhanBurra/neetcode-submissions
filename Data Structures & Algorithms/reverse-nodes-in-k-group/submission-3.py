# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:\

    def reverseKNodes(self, head, k):
        prev = None
        curr = head
        nex = curr.next
        end = head
        
        while k > 0:
            curr.next = prev
            prev = curr
            curr = nex
            if nex:
                nex = nex.next
            k -= 1
        return (prev, end)
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #mark what nodes will be part of the reversal

        reverse_starters = []

        curr = head
        start = head
        count = 1
        while curr != None: # (O (n))
            
            if count % k == 0:
                reverse_starters.append(start)
                start = None
                if curr.next != None:
                    start = curr.next
            count += 1
            curr = curr.next
        
        

        
        final_list = ListNode()
        add_from = final_list
        for n in reverse_starters:
            starts, end = self.reverseKNodes(n, k)
            add_from.next = starts
            add_from = end
        add_from.next = start
        return final_list.next

        

        # for every node in reverse starter, reverse the nodes O(n)

        
        