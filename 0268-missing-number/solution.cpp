class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int sum = accumulate(nums.begin(),nums.end(), 0);
        for (int i = 1; i <= nums.size(); i++) {
            sum -= i;
        }

        return -sum;
    }
};
