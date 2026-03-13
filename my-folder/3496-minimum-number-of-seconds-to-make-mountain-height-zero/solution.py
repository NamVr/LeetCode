class Solution:
    def minNumberOfSeconds(self, height: int, times: list[int]) -> int:
        l, r = 1, 10**16

        while l < r:
            m = (l + r) // 2
            total = 0

            for t in times: # calculate individual time for all workers
                # math
                # t = w * (2w + 3w + ... hw) = w * (1 + 2 + ... + h) = w * (h (h + 1) / 2) 

                # t = w * (h**2 + h) / 2
                # 2t = w * (h**2 + h)
                # 2t/w = h2 + h (add 1/4 to both sides)
                # 2t/w + 1/4 = h2 + h + 1/4 = (h + 1/2) **2
                # square root both sides
                # root((h + 1/2) ** 2) = root(2t/w + 1/4)
                # (h + 1/2) = root (2t/w + 1/4)
                # (h) = root (2t/w + 1/4) - 1/2
                # or literally, h = root(2t/w + 0.25) - 0.5
                total += int(math.sqrt(m / t * 2 + 0.25) - 0.5)
                if total >= height: # if total time is more than height, not all workers were used, 
                    break

            if total >= height: # total > height, optimize it further.
                r = m
            else: # possible solution L. Check for more.
                l = m + 1

        return l
