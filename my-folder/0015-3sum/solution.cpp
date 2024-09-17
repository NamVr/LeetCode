class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;

        for (int i = 0; i < nums.size(); i++) {
            if (i && nums[i] == nums[i-1]) continue; // duplicate check
            int l = i+1, r = nums.size()-1;

            while (l < r) {
                int threeSum = nums[i] + nums[l] + nums[r];
                if (!threeSum) {
                    ans.push_back({nums[i],nums[l],nums[r]});
                    ++l;
                    while ((l < r) && nums[l] == nums[l-1]) { ++l; }
                } else if (threeSum > 0) {
                    --r;
                } else { ++l; }
            }
        }

        return ans;
    }
};
