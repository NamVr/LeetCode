class Solution {
public:
    unordered_map<int, int> memo;
    unordered_set<string> dict;
    int minExtraChar(string s, vector<string>& dictionary) {
        dict = unordered_set<string>(dictionary.begin(), dictionary.end());
        return dp(0,s);
    }

    int dp(int i, const string& s) {
        // memoization
        if (memo.find(i) != memo.end()) return memo[i];

        // base case 0
        if (i == s.length()) return 0;

        int res = s.length() - i; // int max/ worse case
        for (int j = i+1; j <= s.length(); j++) {
            string sub = s.substr(i, j-i);

            if (dict.find(sub) != dict.end()) {
                res = min(res, dp(j,s));
            } else {
                res = min(res, (j-i) + dp(j,s));
            }
        }

        memo[i] = res;
        return res;
    }
};
