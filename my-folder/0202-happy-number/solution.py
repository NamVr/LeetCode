class Solution:
    def isHappy(self, n: int) -> bool:
        # condition: if a number ever repeats, it is not a happy number.
        visit = set()

        while n not in visit:
            visit.add(n)
            n = sum(int(c)**2 for c in str(n))

            if n == 1:
                return True

        return False
