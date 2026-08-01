# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #utilize depth recursion again. If at anypoint left height -right height>1
        self.balance = True
        self.max_depth(root)
        return self.balance
    
    def max_depth(self, root):
        if root:
            left = self.max_depth(root.left)
            right = self.max_depth(root.right)
            self.balance = self.balance and (abs(left-right)<=1)
            return 1+max(left, right)
        else:
            return 0

      