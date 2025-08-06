# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n = 0 # count of respective lists

        # PASS 1: Get the length of both linked lists.
        curr = headA
        while curr:
            n += 1
            curr = curr.next
        
        curr = headB
        while curr:
            n -= 1
            curr = curr.next

        # PASS 2: Get the difference, if n is pos, A has more elements, otherwise B has more elements
        pA, pB = headA, headB
        if n > 0:
            # skip n times in the A list
            while n > 0:
                pA = pA.next
                n -= 1
        else:
            # skip n times in the B list
            while n < 0:
                pB = pB.next
                n += 1
            
        # find the intersection, starting from curr and another head.
        # Finally start the second pass
        while pA != pB:
            pA = pA.next
            pB = pB.next
        
        return pA
