# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.diff = 0
        def height(root):
            if not root:
                return 0
            else :
                LH = height(root.left)
                RH = height(root.right)
                self.diff = max(self.diff, abs(LH-RH))
                return 1+max(LH,RH )
        height(root)
        return self.diff<=1

        
