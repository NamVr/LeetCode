class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {
        vector<int> s;
        for (int i = 0; i < prices.size(); ++i) {
            while (s.size() && prices[s.back()] >= prices[i]) {
                prices[s.back()] -= prices[i];
                s.pop_back();
            }
            s.push_back(i);
        }

        return prices;
    }
};
