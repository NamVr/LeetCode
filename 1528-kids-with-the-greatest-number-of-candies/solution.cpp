class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> ans(candies.size(), false);
        int m = *max_element(candies.begin(), candies.end());
        for (int i = 0; i < candies.size(); i++) {
            if (candies[i]+extraCandies >= m) ans[i] = true;
        }

        return ans;
    }
};
