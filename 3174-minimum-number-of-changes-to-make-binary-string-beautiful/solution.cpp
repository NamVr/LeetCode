class Solution {
public:
    int minChanges(string s) {
        int res = 0;

        for (int i = 0; i < s.length()-1; i+=2) {
            if (s[i] != s[i+1]) res++;
        }

        return res;
    }
};
