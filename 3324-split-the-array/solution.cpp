class Solution {
public:
    bool isPossibleToSplit(vector<int>& nums) {
        unordered_map<int,int> mp;

        for (int& num : nums) {
            // add to the hashmap
            mp[num]++;

            if (mp[num] > 2) return false;
        }

        return true;
    }
};
