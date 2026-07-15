# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseList(self, head):
        prev = None
        start = head
        after = head

        while after != None:
            after = after.next
            start.next = prev
            prev = start
            start = after

        return prev
            

    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None:
            return

        #find the mid point
        #reverse the second half
        #then change next pointers in order

        mid = head
        fast = head

        while fast != None and fast.next != None:
            mid = mid.next
            fast = fast.next.next

        #now mid is at the mid point
        print(mid.val)
        print(mid.next.val)
        end_of_list = self.reverseList(mid)
        
        start = head
        startNext = head.next
        endNext = end_of_list.next
 
        while endNext != None:
            start.next = end_of_list
            end_of_list.next = startNext
            end_of_list = endNext
            start = startNext
            print(start.val)
            endNext = endNext.next
            startNext = startNext.next
   

        # print(i)
        
        # start.next = end_of_list
        # end_of_list.next = mid
        # mid.next = None

        
        
        