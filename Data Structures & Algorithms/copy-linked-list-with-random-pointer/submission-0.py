"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        node_dict = { }

        curr = head

        while curr != None:
            node_dict[curr] = Node(curr.val, curr.next, curr.random)
            curr = curr.next
        

        curr = head

        while curr != None:

            copy_node = node_dict[curr]
            if copy_node.next != None:
                copy_node.next = node_dict[copy_node.next]
            if copy_node.random != None:
                copy_node.random = node_dict[copy_node.random]
            curr = curr.next
        

        return node_dict[head]