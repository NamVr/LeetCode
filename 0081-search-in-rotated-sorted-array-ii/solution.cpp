class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int l = 0, r = nums.size()-1, pivot;

        while (l <= r) {
            int m = l + (r-l)/2;
            if (nums[m] == target) return true;

            if (nums[l] == nums[m] && nums[m] == nums[r]) {
                l++; r--;
            }

            else if (nums[l] <= nums[m]) {
                // left side is sorted
                if (nums[l] <= target && target < nums[m]) {
                    r = m-1;
                } else {
                    l = m+1;
                }
            } else {
                // right side is sorted
                if (nums[m] < target && target <= nums[r]) {
                    l = m+1;
                } else {
                    r = m-1;
                }
            }
        }

        return false;
    }
};
