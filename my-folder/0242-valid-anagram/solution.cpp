class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        int fs[26] = {0};
        
        for (int i = 0; i < s.length(); i++) {
            fs[s[i] - 'a']++;
        }
        for (int i = 0; i < t.length(); i++) {
            fs[t[i] - 'a']--;
        }

        for (int i = 0; i < 26; i++) {
            if (fs[i] != 0) return false;
        }
        return true;
    }
};
