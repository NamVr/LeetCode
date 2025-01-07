class Solution:
    def stringMatching(self, words):
        res = []

        # Iterate through each word in the input list.
        for i in range(len(words)):
            # Compare the current word with all other words.
            for j in range(len(words)):
                # Skip comparing the word with itself.
                if i == j:
                    continue
                if words[i] in words[j]:
                    # Add it to the result list if true.
                    res.append(words[i])
                    break  # No need to check further for this word.
        return res
