#include <algorithm>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() <= 1) return 0;
        int l = 0, r = 1;
        int res = 0;

        while(r < prices.size()) {
            if (prices[l] >= prices[r]) {
                l = r;
                r++;
            } else {
                res = max(res,(prices[r]-prices[l]));
                r++;
            }
        }

        return res;
    }
};
