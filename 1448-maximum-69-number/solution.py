class Solution:
    def maximum69Number (self, num: int) -> int:
        # only applicable to change the first occuring 6 into 9.
        res = [int(x) for x in str(num)]

        for i in range(len(res)):
            if res[i] == 6:
                res[i] = 9
                break

        return int(''.join(map(str, res)))
