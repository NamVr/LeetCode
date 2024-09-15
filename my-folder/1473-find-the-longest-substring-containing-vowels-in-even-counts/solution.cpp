class Solution {
public:
    int findTheLongestSubstring(string s) {
        // bitmask
        unordered_map<char,int> vowelMap = {{'a', 0},{'e', 1},{'i', 2},{'o', 3},{'u',4}};

        // hashmap
        unordered_map<int,int> firOcc;
        firOcc[0] = -1; // initial state

        int state = 0;
        int maxLength = 0;

        for (int i = 0; i < s.size(); i++) {
            if (vowelMap.find(s[i]) != vowelMap.end()) {
                state ^= (1 << vowelMap[s[i]]);
            }

            if (firOcc.find(state) != firOcc.end()) {
                maxLength = max(maxLength, i-firOcc[state]);
            } else {
                firOcc[state] = i;
            }
        }

        return maxLength;
    }
};
