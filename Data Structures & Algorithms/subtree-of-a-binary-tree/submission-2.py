# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #traverse through every node for root. At each node, check if its equal to subroot
        #both None, true
        #root none, subroot not none, false
        #root not none, subroot none, move on
        #root not none, subroot not none, compare
        if not root and not subRoot:
            return True
        elif  not root and subRoot:
            return False
        elif root and not subRoot:
            pass
        else: #both exist
            #call equal check
            if  self.equal (root,subRoot):
                return True
        #recursively walk through tree, only one has to be true
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)

    def equal(self, root, subRoot):
        if not root and not subRoot:
            return True
        elif  (not root) ^ (not subRoot):
            return False
        if  root.val!=subRoot.val:
            return False

        left = self.equal(root.left, subRoot.left)
        right =  self.equal(root.right,  subRoot.right)
        return  left and right