class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # 0100 -> 101001
        # 1 operation: 2 steps
        # 1: convert all 1 ______ 1 into 00000000000
        # 2: convert all 0 ______ 0 into 1 1111111 1
        # 1111 -> 4 answer
        ones = s.count('1')

        s = '1' + s + '1' # augmentation

        runs = []
        cnt = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
            else:
                runs.append((s[i - 1], cnt))
                cnt = 1

        runs.append((s[-1], cnt))

        best_gain = 0

        for i in range(1, len(runs) - 1):
            if runs[i][0] == '1':
                if runs[i - 1][0] == '0' and runs[i + 1][0] == '0':
                    best_gain = max(
                        best_gain,
                        runs[i - 1][1] + runs[i + 1][1]
                    )

        return ones + best_gain
