class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # score = values[i] + values[j] + i - j
        n = len(values)

        # left score initially is value of first element
        max_left_score = values[0]

        res = 0

        for i in range(1,n):
            current_right_score = values[i] - i
            res = max(res, max_left_score + current_right_score)

            current_left_score = values[i] + i
            max_left_score = max(max_left_score, current_left_score)

        return res
