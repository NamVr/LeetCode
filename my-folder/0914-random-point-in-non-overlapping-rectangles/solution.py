class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects

        # prefix array
        self.prefix = [0] * len(rects)
        for i, (x1, y1, x2, y2) in enumerate(rects):
            points = (x2-x1+1) * (y2-y1+1)

            if i == 0:
                self.prefix[i] = points
            else:
                self.prefix[i] = self.prefix[i-1] + points

    def pick(self) -> List[int]:
        rnd = random.randint(1, self.prefix[-1]) # inclusive of 1 .. n

        # find the rectangle it belongs to
        rect = bisect.bisect_left(self.prefix, rnd)

        # get all the rectangle indexes to return
        x1, y1, x2, y2 = self.rects[rect]

        # return random point
        return [random.randint(x1, x2), random.randint(y1, y2)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
