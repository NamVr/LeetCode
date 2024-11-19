class Solution {
public:
    long long maximumSubarraySum(vector<int>& nums, int k) {
        long long res = 0, sum = 0;
        unordered_map<int,int> mp;

        int i = 0;

        while (i < k && i < nums.size()) {
            mp[nums[i]]++;
            sum += nums[i];
            i++;
        }

        if (mp.size() == k) res = sum;

        // first iteration completed

        while (i < nums.size()) {
            mp[nums[i]]++;
            mp[nums[i-k]]--;
            // sliding window approach.

            // if last element has 0 elements, then reset the set (cleanup)
            if (mp[nums[i-k]] == 0) mp.erase(nums[i-k]);

            sum += nums[i];
            sum -= nums[i-k];

            if (mp.size() == k) res = max(res, sum);
            i++;
        }

        return res;
    }
};
