# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #First look, seems only DFS would work as size generalized from layers can't help with individual branches
        #DFS, pass max down specifc 
            #if val>largest, count+
            #largest = max(val, max)
            #dfs(left, largest)
        count = 0

        def dfs(node,largest):
            nonlocal count
            if not node: 
                return None
            val = node.val
            if val>=largest:
                count+=1
            dfs(node.left, max(val,largest))
            dfs(node.right,max(val,largest))
            return None
        dfs(root,-math.inf)

        return count