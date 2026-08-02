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
        out = []
        def dfs(node, depth):
            #go thru tree left to right updating last seen node at each depth --> returns nothing
            if not node:
                return True
            if len(out)==depth:#first time at this depth
                out.append(node.val)
            #been at this depth before
            out[depth]=node.val
            depth+=1
            return dfs(node.left,depth) and dfs(node.right,depth) 

        dfs(root,0)
        return out  

            











        # if not root: 
        #     return []
        # q = deque([root])
        # out = []
        # while q:
        #     size = len(q)
        #     for i in range(size):
        #         cur = q.popleft()
        #         if cur.left: 
        #             q.append(cur.left)
        #         if cur.right:
        #             q.append(cur.right)
        #         if i ==size-1:
        #             out.append(cur.val)
        
        # return out

                

