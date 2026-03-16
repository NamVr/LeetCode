# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        # DFS Solution.
        def dfs(node, level=0):
            if not node: return # base case.

            # create level list if already does not exists.
            if level == len(res): res.append([])

            res[level].append(node.val) # add the value

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root)
        return res
