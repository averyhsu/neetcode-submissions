# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if root is None: return 0
        queue = deque([root])
        #extract all node in the current layer
        while queue:
            nodes = []

            while queue:
                nodes.append(queue.popleft())#append to list of nodes
            
            for x in nodes:
                if x.left: 
                    queue.append(x.left)
                if x.right: 
                    queue.append(x.right)

            depth+=1

        return depth