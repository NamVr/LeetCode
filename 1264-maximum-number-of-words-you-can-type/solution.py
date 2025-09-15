class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        s = set(brokenLetters)
        words = text.split(" ")
        res = 0

        for word in words:
            for c in word:
                if c in s:
                    res += 1
                    break

        return len(words) - res
