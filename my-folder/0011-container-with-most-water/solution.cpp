#include <algorithm>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        long int res = 0;
        int l = 0, r = height.size() - 1;

        while (l < r) {
            long int temp = (long)(r-l) * min(height[l], height[r]);
            res = max(res,temp);

            (height[l] > height[r]) ? r-- : l++; 
        }

        return res;
    }
};
