class Solution {
public:
    string makeFancyString(string s) {
        int n = s.size();
        if (n < 3) return s;
        int j = 2;
        
        for (int i = 2; i < n; i++) {
            if (s[i] != s[j-1] || s[i] != s[j-2]) {
                // not equal to last 2 chars
                s[j++] = s[i];
            }
        }

        s.resize(j);
        return s;
        
    }
};
