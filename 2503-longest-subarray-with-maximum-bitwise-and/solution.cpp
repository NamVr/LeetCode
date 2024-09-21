class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int ans = 1;
        int curr = 0;
        int m = *max_element(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == m) {
                curr++;
                ans = max(ans,curr);
            } else {
                curr = 0;
            }
        }

        return ans;
    }
};
