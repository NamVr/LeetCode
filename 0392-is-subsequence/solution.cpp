class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0, j = 0;
        while (i < s.length() && j < t.length()) {
            // check condition
            if (s[i] == t[j]) 
                i++;
            j++;
        }

        return i == s.length();
    }
};
