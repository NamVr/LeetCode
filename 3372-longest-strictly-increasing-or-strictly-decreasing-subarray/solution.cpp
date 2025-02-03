class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int inc = 1, dec = 1, res = 1;

        // run a single pass iteration
        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums[i+1] > nums[i]) {
                // check for strictly increasing sequence
                inc++;
                dec = 1; // reset dec
            } else if (nums[i+1] < nums[i]) {
                // check for strictly decreasing sequence
                dec++;
                inc = 1; // reset inc
            } else {
                // reset counters if none SI or SD
                inc = dec = 1;
            }

            // finally get the max out of the 3 counters
            res = max({res, inc, dec});
        }

        return res;
    }
};
