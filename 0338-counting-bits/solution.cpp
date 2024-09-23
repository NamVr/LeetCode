class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> dp(n+1, 0); // has n+1 size
        int offset = 1; // base case offset

        for (int i = 1; i <= n; i++) {
            if (offset*2 == i) offset = i;
            dp[i] = 1 + dp[i-offset];
        }

        return dp;
    }
};
