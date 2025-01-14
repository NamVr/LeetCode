class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        res = [0] * n

        a,b = set(), set()

        # for each iteration
        for i in range(n):
            # add current element to set
            a.add(A[i])
            b.add(B[i])

            count = 0

            # get common elements between sets
            # subloop elements in "a" set O(n) * O(1) set lookup
            for element in a:
                if element in b:
                    # if common is found add it
                    count += 1

            res[i] = count

        return res 

