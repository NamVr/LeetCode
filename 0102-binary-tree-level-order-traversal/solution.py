# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] # final array

        # let's do BFS for level order traversal
        # create a exploratory queue and add the root node

        q = deque()
        q.append(root)

        # explore the q level wise
        while q:
            # get the number of nodes in this level
            n = len(q)
            level = [] # level order array to store node values

            # run level wise loop
            for _ in range(n):
                # get the node.
                node = q.popleft()

                # check if the node exists
                if node:
                    # add the node's value to the level array
                    level.append(node.val)

                    # check for node's left and right trees
                    q.append(node.left)
                    q.append(node.right)
            
            # finally update this level in the final result
            if level:
                res.append(level)

        return res
