class Solution {
public:
    int longestSquareStreak(vector<int>& nums) {
        int res = 0;

        unordered_set<int> s(nums.begin(), nums.end());

        for (int& num : nums) {
            int streak = 0;
            long long current = num;

            while(s.find((int)current) != s.end()) {
                streak++;

                if (current*current > 1e5) break;

                current *= current;
            }


            res = max(res, streak);
        }

        return res < 2 ? -1 : res;
    }
};
