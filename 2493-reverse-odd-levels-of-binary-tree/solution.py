# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(l,r, level):
            if l is None or r is None:
                return
            
            if level%2 == 0:
                t = l.val
                l.val = r.val
                r.val = t
            
            dfs(l.left, r.right, level+1)
            dfs(l.right, r.left, level+1)

        dfs(root.left, root.right, 0)
        return root
    
