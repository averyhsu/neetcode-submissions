# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #Observation: usual dfs left to right traversal. However, for each node, if I wait till  left  recursion is completed then label it's order then do the right recursion, the order labeling will happen in BST size order.
        order = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            order.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return order[k-1]