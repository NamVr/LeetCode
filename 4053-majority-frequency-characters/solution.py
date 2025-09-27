class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        c = Counter(s) # frequency map.

        grps = defaultdict(list) # group of all distinct chars of a particular frequency
        for c, k in c.items():
            grps[k].append(c) # k -> character mapping

        # return a string containing all characters in the majority frequency group.
        # sort by group size and frequency (priority group size then frequency)

        k, chars = max(
            grps.items(), key=lambda i: (len(i[1]), i[0])
        )

        # key -> sort with size of the group 1st priority len(i[1])
        # then sort with frequency i[0]

        return "".join(chars)
