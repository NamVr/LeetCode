class Fancy:

    def __init__(self):
        self.mod = 10**9 + 7
        self.arr = [] # list
        self.a = 1 # global multiplication constant
        self.b = 0 # global addition constant

    def append(self, val: int) -> None:
        x = (val - self.b + self.mod) % self.mod
        self.arr.append(x * pow(self.a, self.mod-2, self.mod) % self.mod)

    def addAll(self, inc: int) -> None:
        self.b = (self.b + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.a = (self.a * m) % self.mod
        self.b = (self.b * m) % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr): return -1

        return (self.a * self.arr[idx] + self.b) % self.mod


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
