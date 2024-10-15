class Solution {
public:
    long long minimumSteps(string s) {
        int l = 0;
        long long res = 0;

        for (int r = 0; r < s.length(); r++) {
            if (s[r] == '0') {
                res += r-l;
                l++;
            }
        }

        return res;
    }
};
