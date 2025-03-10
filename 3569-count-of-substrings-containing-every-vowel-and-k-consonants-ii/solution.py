class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # if i get this in a interview, he/she hates me

        def helper(k):
            vowel = defaultdict(int) # to store count of vowels
            non_vowel = 0 # to track non vowel count

            l,res = 0,0

            for r in range(len(word)):
                # check if the letter is vowel/non vowel and update counter
                if word[r] in "aeiou":
                    vowel[word[r]] += 1
                else:
                    non_vowel += 1

                while len(vowel) == 5 and non_vowel >= k:
                    res += len(word) - r

                    # backwards remove counter for sliding window
                    if word[l] in "aeiou":
                        vowel[word[l]] -= 1
                    else:
                        non_vowel -= 1
                    
                    # pop vowel dict key if count is zero
                    if vowel[word[l]] == 0:
                        vowel.pop(word[l])
                    
                    # lastly, l++
                    l += 1
                
            return res
        
        return helper(k) - helper(k+1)

