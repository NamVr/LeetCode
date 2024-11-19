class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int,int> mp;
        unordered_set<int> s;

        for (int i : arr) {
            mp[i]++;
        }

        for (auto& pair: mp) {
            if (!s.count(pair.second)) {
                s.insert(pair.second);
            } else return false;
        }

        return true;
    }
};
