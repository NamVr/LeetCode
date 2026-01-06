# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # apply bfs.
        i = 0 # start from level 1 and so on.
        res = float("-inf")
        res_level = 0

        q = deque([root])

        while q:
            i += 1

            curr = 0
            for _ in range(len(q)):
                node = q.popleft()

                curr += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # check sum max
            if res < curr:
                res, res_level = curr, i
    
        return res_level
