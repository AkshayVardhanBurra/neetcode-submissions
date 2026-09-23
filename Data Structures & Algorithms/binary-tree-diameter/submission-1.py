# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def max_size(self, root):
        if root == None:
            return 0
        else:
            return 1 + max([self.max_size(root.left), self.max_size(root.right)])
    


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        else:
            curr = self.max_size(root.left) + self.max_size(root.right)
            

            max_val = max([curr, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)])


            return max_val