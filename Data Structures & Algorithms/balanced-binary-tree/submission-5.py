# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            else :
             
                LH = height(root.left)
                RH = height(root.right)
                if (LH==-1) or (RH==-1):
                  return -1
                diff = abs(LH-RH)
                if diff>1:
                    return -1
                return 1+max(LH,RH )
      
        return   height(root)!=-1

        
