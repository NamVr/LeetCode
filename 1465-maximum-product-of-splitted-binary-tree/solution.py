# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
MOD = 10**9 + 7
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        res, total = float("-inf"), 0

        def dfs(root):
            nonlocal res, total

            if not root: return 0

            sm = root.val + dfs(root.left) + dfs(root.right)
            res = max(res, (total-sm) * sm)
            return sm

        total = dfs(root)
        dfs(root)

        return res % MOD
