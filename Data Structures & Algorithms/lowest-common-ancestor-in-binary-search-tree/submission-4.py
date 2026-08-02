# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #find larger/smaller of p q and rename to s,l
        #chck s,l in relation to current node
        #s<=cur<=l, property of BST, they have to connect thru cur --> return cur
        #if s>cur, recurse on cur->right
        #if l<cur, recurse on cur-->left
        print(root.val)
        if p.val>q.val:
            l = p
            s = q
        else: 
            l = q
            s = p
        if s.val <= root.val<=l.val:
            print("return")
            return root
        if s.val>root.val:
            print("right)")
            return  self.lowestCommonAncestor(root.right, l,s)
        if l.val<root.val:
            print("left")
            return self.lowestCommonAncestor(root.left, l,s)
        
        