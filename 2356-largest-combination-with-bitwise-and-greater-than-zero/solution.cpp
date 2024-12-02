class Solution {
public:
    int largestCombination(vector<int>& candidates) {
        //int n = candidates.size();
        int ans = 0;

        for (int i = 0; i < 32; i++) {
            int count = 0;
            for (auto& c : candidates) {
                if (c & (1 << i)) count++;
            }
            ans = max(ans,count);
        }

        return ans;
    }
};