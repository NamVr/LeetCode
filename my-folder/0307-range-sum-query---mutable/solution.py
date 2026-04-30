class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.bit = [0] * (self.n + 1)
        self.nums = nums[:]

        for i in range(self.n):
            self._add(i, nums[i])

    def _add(self, i, val):
        i += 1
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self._add(index, diff)

    def _sum(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def sumRange(self, l: int, r: int) -> int:
        return self._sum(r) - self._sum(l - 1)
