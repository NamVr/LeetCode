# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val # initially, the root value

        def dfs(node):
            nonlocal res # allows to use global variable

            # base case, root node is null
            if not node:
                return 0
            
            # compute the left and right sub trees
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            # avoid negative values, max with 0
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # calculate the result with and without split + root node
            # update global variable with split
            # return the value to parent function without split

            # with split (left + right + node), remember negatives are already removed
            res = max(res, node.val + leftMax + rightMax)

            # return the max of left and right without split, along with root node
            return max(leftMax, rightMax) + node.val
        
        dfs(root)
        return res
