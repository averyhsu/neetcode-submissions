# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #At every node the lognest diameter is basically max of left +max of right
        # We can have global max var and use recursion to update that as we recurse down each node
        self.diam = 0

        self.max_depth(root)
        return self.diam
        
    
    def max_depth(self, root):
        if root:
            left = self.max_depth(root.left)
            right = self.max_depth(root.right)
            self.diam = max(self.diam, left+right)
            return 1+max(self.max_depth(root.left), self.max_depth(root.right))
        else:
            return 0