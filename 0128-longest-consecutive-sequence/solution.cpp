class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s(nums.begin(),nums.end());
        int longest = 0;

        for (auto& n : s) {
            // assume start of sequence
            // n is start of sequence, so there is no value for n-1
            // count returns 0 when n-1 is not found in hashset.

            if (!s.count(n-1)) {
                int length = 1;
                // till there's no next subsequence, keep incrementing length.
                while (s.count(n+length)) length++;

                // calc max length
                longest = max(length, longest);
            }
        }

        return longest;
    }
};
