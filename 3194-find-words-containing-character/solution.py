class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []

        for i, s in enumerate(words):
            if x in s:
                res.append(i)
    
        return res
