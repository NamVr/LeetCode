class Solution {
public:
    int minSubarray(vector<int>& nums, int p) {
        int remainder = 0;

        // calculate sum mod p
        for (int& num : nums) {
            remainder = (remainder+num) % p;
        }

        if (!remainder) return 0;

        // hashmap to store prefix sum
        unordered_map<int,int> mp;
        mp[0] = -1;

        int n = nums.size();
        int currentSum = 0;
        int minLength = n;

        for (int i = 0; i < n; i++) {
            currentSum = (currentSum + nums[i]) % p;

            int target = (currentSum - remainder + p) % p; // for negative check

            if (mp.count(target)) {
                minLength = min(minLength, i-mp[target]);
            }

            mp[currentSum] = i;
        }

        return minLength == n ? -1 : minLength;
    }
};
