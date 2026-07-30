# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None
        merged_list = ListNode()
        cpy = merged_list



        while True:

            min_n = lists[0]
            ind = 0

            n_c = 0
            for n in range(0, len(lists)):
                if lists[n] == None:
                    n_c += 1
                    continue
                elif min_n == None or lists[n].val < min_n.val:
                    ind = n
                    min_n = lists[n]
            
            if n_c == len(lists):
                return cpy.next

            
            lists[ind] = lists[ind].next
            min_n.next = None
            merged_list.next = min_n
            merged_list = merged_list.next
        
        return cpy.next
            

            

            # for i in range(0, len(lists)):
            #     if i != ind and lists[i] != None:
            #         lists[i] = lists[i].next
            #         if lists[i] == None:
            #             null_count -= 1
                
