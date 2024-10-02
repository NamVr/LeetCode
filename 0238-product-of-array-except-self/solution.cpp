class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int prefix = 1, suffix = 1, n = nums.size();
        //vector<int> res(n,1);
        int res[n]; // using raw array

        for (int i = 0; i < n; i++) {
            res[i] = prefix;
            prefix *= nums[i];
        }

        for (int i = n-1; i >= 0; i--) {
            res[i] = res[i] * suffix;
            suffix *= nums[i];
        }

        // convert back to vector
        return vector<int>(res, res+n);
    }
};
