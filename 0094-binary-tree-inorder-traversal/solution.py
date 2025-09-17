# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # LEFT -> ROOT -> RIGHT
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

        stack = []
        res = []

        while root or stack:
            while root:
                stack.append(root) # keep adding root in stack.
                root = root.left # traverse LEFT nodes at the end
            
            root = stack.pop()
            res.append(root.val) # add ROOT to result.

            root = root.right # traverse RIGHT nodes at the end

        return res
