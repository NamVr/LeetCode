class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0 # edge case

        # create splits
        splits = [weights[i] + weights[i+1] for i in range(len(weights) - 1)]

        splits.sort() # O(nlogn)

        i = k - 1
        _max = sum(splits[-i:])
        _min = sum(splits[:i])

        return _max - _min
