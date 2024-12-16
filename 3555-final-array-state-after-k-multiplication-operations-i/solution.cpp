class Solution {
public:
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {
        int n = nums.size();

        while (k--) {
            int minidx = 0;
            for (int i = 0; i < n; i++) {
                if (nums[i] < nums[minidx]) {
                    minidx = i;
                }
            }

            nums[minidx] *= multiplier;
        }

        return nums;
    }
};
