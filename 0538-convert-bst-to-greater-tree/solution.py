# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # create a variable to track the maximum sum that will be assigned to the last node
        sum = 0

        # we will start with the root
        def helper(root):
            nonlocal sum

            # if root is not null, run the loop at the greater side (right)
            # now sum will be updated with right's sum
            # append the value to the root.

            # after that get the current sum and traverse to the left
            if root:
                helper(root.right)
                root.val += sum

                sum = root.val
                helper(root.left)
            
            return root

        return helper(root)
