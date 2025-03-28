class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we will create a hashmap of Counter : anagrams list []
        # create a counter for each word, and group together the anagrams in that specific list/tuple
        res = defaultdict(list)

        # iterate for every word in the list
        for s in strs:
            # for this specific string, create a counter object
            count = [0] * 26

            # now calculate the character count
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            # map the current string to the count tuple
            res[tuple(count)].append(s)
        
        # now we have a res hashmap of values of multiple lists
        # which are anagrams, we dont need keys (counter) anymore

        return list(res.values())
