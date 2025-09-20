# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return "#"

        q = deque() # exploratory queue.
        res = []

        q.append(root)

        while q:
            node = q.popleft()

            if node:
                res.append(str(node.val))
                q.append(node.left) if node.left else q.append(None)
                q.append(node.right) if node.right else q.append(None)
            else:
                res.append("#")

        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "#": return None
        nodes = data.split(",") # array of all nodes.
        root = TreeNode(int(nodes[0])) # i = 0
        
        i = 1 # index to traverse the ndoes list, 0th (root) is already added.
        q = deque([root]) # build the tree AT root.

        while q and i < len(nodes):
            node = q.popleft() 

            # keep checking if data is available for both childs.
            if i < len(nodes): # LEFT child.
                left = nodes[i]
                if left != "#": # its not null, it can be explored further.
                    node.left = TreeNode(int(left))
                    q.append(node.left)
                
                i += 1
            else:
                break
            
            if i < len(nodes): # RIGHT child.
                right = nodes[i]

                if right != "#":
                    node.right = TreeNode(int(right))
                    q.append(node.right)

                i += 1
            else:
                break

        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
