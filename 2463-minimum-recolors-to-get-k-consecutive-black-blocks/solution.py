class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        check = 0
        res = float("inf")

        # Move r pointer (starts from 0 to n)
        for r in range(len(blocks)):
            # Increment check if block at r pointer is white
            if blocks[r] == "W":
                check += 1

            # k consecutive elements are found
            if r - l + 1 == k:
                # Update minimum
                res = min(res, check)
                # Decrement check if block at l pointer is white
                if blocks[l] == "W":
                    check -= 1
                # Move l pointer
                l += 1

        return res
