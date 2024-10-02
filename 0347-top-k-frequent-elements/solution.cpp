class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // edge case, no element
        if (!nums.size()) return {};

        // create a hashmap to store count of each element
        unordered_map<int,int> mp;

        for (int& key: nums) {
            if (mp.find(key) == mp.end()) {
                mp[key] = 0;
            } else {
                mp[key]++;
            }
        }

        // return top count elements k
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> minHeap;

        for (auto& entry: mp) {
            minHeap.push({entry.second, entry.first});

            if (minHeap.size() > k) {
                minHeap.pop(); // keeps only k element in heap
            }
        }

        vector<int> res;
        while (!minHeap.empty()) {
            res.push_back(minHeap.top().second);
            minHeap.pop();
        }

        return res;
    }
};
