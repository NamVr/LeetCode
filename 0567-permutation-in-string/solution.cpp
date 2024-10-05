class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char,int> mp;

        for (auto& x: s1) mp[x]++;

        int r = 0, l = 0, n = s2.length(), req = s1.length();

        while (r < n) {
            if (mp[s2[r]] > 0) {
                req--;
            }
            mp[s2[r]]--;
            r++;

            if (!req) return true;

            if (r-l == s1.length()) {
                if (mp[s2[l]] >= 0) {
                    req++;
                } 
                mp[s2[l]]++;
                l++;
            }
        }

        return false;
    }
};
