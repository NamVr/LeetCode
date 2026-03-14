class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # only contains a,b,c no same letter consecutive.

        # n -> all strings of length n
        # k -> return the kth string in lexicographical order.
        # no of strings: 3 * 2^(n-1)
        total = 3 * 2**(n-1)

        # given edge case
        if k > total:
            return ""

        q = deque([""])

        while k :
            temp = q.popleft() # get the sequence from queue

            for ch in ['a','b','c']:
                if not temp or temp[-1] != ch:
                    q.append(temp + ch)

                    if len(temp) + 1 == n:
                        k -= 1
            
                if k == 0: # when kth element is generated break the loop
                    break

        return q[-1] # the last element
