class Solution {
public:
    int maximumSum(vector<int>& nums) {
        int res = -1;
        int dp[82] = {}; // hashmap storage

        for (int n : nums) {
            int d = 0;
            for (int i = n; i; i /= 10)
                d += i % 10; // sum of digits
            
            if (dp[d])
                res = max(res, dp[d] + n);

            dp[d] = max(dp[d], n);
        }

        return res;
    }
};
