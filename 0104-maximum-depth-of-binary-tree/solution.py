# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive DFS method
        # find the max depth of left and right trees
        # add it with the root node's final result + 1

        # base case: if node is undefined
        if not root:
            return 0
        
        # now return the max depth
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
