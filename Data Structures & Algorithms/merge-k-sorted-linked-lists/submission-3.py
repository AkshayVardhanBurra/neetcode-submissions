# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None
        
        merged = ListNode()
        cpy = merged
        

        heap = []
        n_count = 0
        while n_count != len(lists):
            n_count = 0
            for i in range(0, len(lists)):
                if lists[i] != None:
                    heapq.heappush(heap, NodeWrapper(lists[i]))
                    temp = lists[i].next
                    lists[i].next = None
                    lists[i] = temp
                else:
                    n_count += 1
            
        while len(heap) > 0:
            node = heapq.heappop(heap)
            merged.next = node.node
            merged = merged.next

        return cpy.next
        
        
                


            

            

            # for i in range(0, len(lists)):
            #     if i != ind and lists[i] != None:
            #         lists[i] = lists[i].next
            #         if lists[i] == None:
            #             null_count -= 1
                
