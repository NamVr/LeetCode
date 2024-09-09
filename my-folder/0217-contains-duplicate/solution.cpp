#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> mySet;

        for (int i = 0; i < nums.size(); i++) {
            if (mySet.count(nums[i])) return true;
            mySet.insert(nums[i]);
        }

        return false;
    }
};

