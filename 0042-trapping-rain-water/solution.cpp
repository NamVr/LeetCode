class Solution {
public:
    int trap(vector<int>& height) {
        if (!height.size()) return 0;

        int res = 0;
        int l = 0, r = height.size()-1;
        int maxl = height[l], maxr = height[r];

        while (l < r) {
            if (maxl <= maxr) {
                //shift left pointer
                l++;
                maxl = max(height[l], maxl);
                res += maxl - height[l];
            } else {
                //shift right pointer
                r--;
                maxr = max(height[r], maxr);
                res += maxr - height[r];
            }
        }
        return res;
    }
};
