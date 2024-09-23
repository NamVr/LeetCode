// uses sliding window approach + 2 pointers

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // create a hash set for O(1) operations
        unordered_set<char> m;
        int maxLength = 0; // to track max length
        int l = 0;

        for (int r = 0; r < s.length(); r++) {
            // traverse right pointer till end till no duplicates
            while (m.find(s[r]) != m.end()) {
                // keep deleting left
                m.erase(s[l++]);
            }

            // now insert the character in set
            m.insert(s[r]);

            // compute maximum length
            maxLength = max(maxLength, r-l+1);
        }

        return maxLength;
    }
};
