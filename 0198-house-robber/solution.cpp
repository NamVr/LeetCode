class Solution {
public:
    int rob(vector<int>& nums) {
        int prev = 0, curr = 0, next = 0;
        // prev and curr are DP memoization

        for (auto& i : nums) {
            next = max(prev+i, curr);
            prev = curr;
            curr = next;
        }

        return curr;
    }
};
