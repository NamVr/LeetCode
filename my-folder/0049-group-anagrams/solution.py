class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list) # counter : strings

        for s in strs:
            count = [0] * 26 # a .. z

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            m[tuple(count)].append(s)
        
        return list(m.values())
