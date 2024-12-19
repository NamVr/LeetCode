"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        m = { None : None } # OG Node : Copy Node
        # edge case, if null is called, null is linked
        
        # pass 1 : create nodes and map them
        curr = head
        while curr:
            copy = Node(curr.val)
            m[curr] = copy

            curr = curr.next

        # pass 2 : link nodes together
        curr = head
        while curr:
            copy = m[curr] # get the copy node
            copy.next = m[curr.next]
            copy.random = m[curr.random]
            curr = curr.next
        
        return m[head]
