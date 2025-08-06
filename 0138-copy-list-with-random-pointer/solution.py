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
        m = { None : None } # edge case, null -> null

        curr = head

        # PASS 1: Hashmap.
        while curr:
            copy = Node(curr.val)
            m[curr] = copy
            curr = curr.next
        
        curr = head

        # PASS 2: Create new linked list.
        while curr:
            copy = m[curr]
            copy.next = m[curr.next]
            copy.random = m[curr.random]
            curr = curr.next
        
        return m[head]
