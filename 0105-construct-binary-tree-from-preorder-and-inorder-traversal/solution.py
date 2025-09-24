# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # first node of preorder is always the root
        # root element in inorder traversal will divide array into two parts, left and right.
        # recursively run for both leaf nodes.
        preorder = deque(preorder)

        # hashmap for val : index in the inorder table
        mp = {val : i for i, val in enumerate(inorder)}

        def helper(l, r):
            # base case:
            if l > r: #impossible
                return None
            
            # get the first element in preorder, which is the root.
            val = preorder.popleft()
            root = TreeNode(val)

            # find index of root val in inorder array using map.
            m = mp[val]

            # recursion:
            root.left = helper(l, m-1)
            root.right = helper(m+1, r)

            return root

        return helper(0, len(inorder) - 1) # returns root.
