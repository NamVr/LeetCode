class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def helper(num):
            s = str(num)
            if len(s) < 3: return 0

            res = 0

            for i in range(1, len(s)-1):
                if (s[i] < s[i-1] and s[i] < s[i+1]) or (s[i] > s[i-1] and s[i] > s[i+1]):
                    res += 1
            
            return res
        
        res = 0

        for i in range(num1, num2+1):
            res += helper(i)

        return res
