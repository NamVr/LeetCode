#include <set>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        set<int> mySet;

        for (int i = 0; i < nums.size(); i++) {
            if (mySet.count(nums[i])) {
                // already exists
                mySet.erase(nums[i]);
            } else {
                // doesn't exists
                mySet.insert(nums[i]);
            }
        }

        return *mySet.begin();
    }
};
