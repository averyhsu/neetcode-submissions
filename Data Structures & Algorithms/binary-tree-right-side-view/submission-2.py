# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #BFS solution: again layered bfs, at every inner list we can extract the last element
        #DFS solution: keep track of depth, sicne DFS traverse from left-->right, the last element at each depth seen is the right side view
        if not root: 
            return []
        q = deque([root])
        out = []
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if cur.left: 
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                if i ==size-1:
                    out.append(cur.val)
        
        return out
                

