class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # to preserve the order of characters make it easy;
        # we can keep hashmapping from s -> t
        # once a hashmap already exists, check if it's the same mapping
        # otherwise, return false.

        # No two characters may map to the same character.

        m = {} # to map characters
        col = set() # to check for collision
        
        # length of both strings is same.
        for i in range(len(s)):

            # if it already exists in hashmap
            if s[i] in m:
                # check if the mapping is same.
                if m[s[i]] != t[i]:
                    return False
            
            # if its not in map; check for collisions
            else:
                if t[i] in col:
                    return False

                # create mapping for both ends.
                m[s[i]] = t[i]
                col.add(t[i])
        
        return True
