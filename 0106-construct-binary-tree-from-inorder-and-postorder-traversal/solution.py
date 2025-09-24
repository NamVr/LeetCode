# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder: return
        postorder = deque(reversed(postorder)) # now first element is root again.

        # hashmap val : i for all values in the inorder array.
        mp = { val: i for i, val in enumerate(inorder)}

        def helper(l, r):
            # base case - impossible condition:
            if l > r:
                return None

            # get the first element from deque, which will always be root.
            val = postorder.popleft()
            root = TreeNode(val)

            # find the root element index in the postorder.
            m = mp[val]

            # recursion:
            root.right = helper(m+1, r)
            root.left = helper(l, m-1)

            return root
        
        return helper(0, len(inorder) - 1)
