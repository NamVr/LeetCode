class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> n1(nums1.begin(), nums1.end());
        unordered_set<int> n2(nums2.begin(), nums2.end());
        vector<int> a,b;

        for (int i : n1) {
            if (!n2.count(i)) {
                a.push_back(i);
            }
        }

        for (int i : n2) {
            if (!n1.count(i)) {
                b.push_back(i);
            }
        }

        return {a, b};
    }
};
