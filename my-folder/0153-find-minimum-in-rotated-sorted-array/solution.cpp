#include <algorithm>
using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0, r = nums.size()-1;

        while (l < r) {
            // check if array is already sorted
            if (nums[l] < nums[r]) {
                return nums[l];
            }

            int m = l+(r-l)/2;

            if (nums[m] >= nums[l]) {
                // left side is sorted, search right.
                l = m+1;
            } else {
                r = m;
            }
        }

        return nums[l];
    }
};
