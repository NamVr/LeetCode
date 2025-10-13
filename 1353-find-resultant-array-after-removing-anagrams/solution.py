class Solution:
    def removeAnagrams(self, w: List[str]) -> List[str]:
        return [w[i] for i in range(0, len(w)) if i == 0 or sorted(w[i]) != sorted(w[i - 1])]
