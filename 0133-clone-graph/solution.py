"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # create a dictionary / hashmap
        # old : new node mapping
        m = {}

        def clone(node):
            if node in m:
                # node already exists, return that copy
                return m[node] # returns node: *copy*

            # if the node does not exists,
            copy = Node(node.val) # new copy node created, now create neighbors

            # add this copy to our hashmap
            m[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            
            return copy

        return clone(node) if node else None # check null node case edge case
